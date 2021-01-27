from PrestoSQL.PrestoSQLVisitor import PrestoSQLVisitor

from graphviz import Digraph


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


class Node:
    def __init__(self, id, text):
        self._id = id
        self._text = text
        self._children = []
        self._from = None

    def add_child(self, child_id, child_label):
        child = {"id": child_id, "label": child_label}
        if child not in self._children:
            self._children.append(child)

    def remove_child(self, child_label):
        self._children = [
            child for child in self._children if child["label"] != child_label]

    def get_child_id(self, child_label):
        child_ids = [child["id"]
                     for child in self._children if child["label"] == child_label]
        if len(child_ids) > 0:
            return child_ids

    def is_all_children(self, child_label):
        has_label = self.get_child_id(child_label)
        return has_label and len(has_label) == len(self.children)

    def get_first_child_id(self):
        if len(self._children) > 0:
            return self._children[0]["id"]

    @property
    def id(self):
        return self._id

    @property
    def text(self):
        return self._text

    @property
    def children(self):
        return self._children


class PrestoSQLVisitor(PrestoSQLVisitor):
    def __init__(self, rule_names):
        super().__init__()
        self._rule_names = rule_names
        self._nodes = {}  # {id: Node object,...}
        self._root_id = None
        self._syntax_graph = Digraph(format="png")
        self._lineage_graph = Digraph(format="png")
        self._dependency = {}  # {"db.table": {db,table},{table}...}
        self._alias = {}  # {alias_identifier: reffered node key,...}
        self._field = []

    @property
    def nodes(self):
        return self._nodes

    @property
    def syntax_graph(self):
        return self._syntax_graph

    @property
    def lineage_graph(self):
        return self._lineage_graph

    @property
    def dependency(self):
        return list(self._dependency.values())

    @property
    def alias(self):
        return self._alias

    @property
    def field(self):
        return self._field

    def node_id(self, ctx):
        id = hex(hash(ctx))
        rule_name = self._rule_names[ctx.getRuleIndex()]
        return "{1}@{0}".format(id, rule_name)

    def add_node(self, ctx, suffix=""):
        id = self.node_id(ctx)
        text = suffix
        if id not in self._nodes:
            self._syntax_graph.node(id, text)
            self._nodes[id] = Node(id, text)
        return id

    def add_edge(self, parent_id, children_id, label=None):

        def add(pid, cid, l):
            self._syntax_graph.edge(pid, cid, l)
            self._nodes[pid].add_child(cid, l)
            # self._nodes[cid].parent = pid

        if isinstance(children_id, list):
            if len(children_id) == 0:
                return
            children_id = flatten(children_id)
            for child_id in children_id:
                if child_id is not None:
                    add(parent_id, child_id, label)

        else:
            if not children_id:
                return
            child_id = children_id
            add(parent_id, child_id, label)

    def add_dependency(self, qualified_name_node):
        qualified_name = self._nodes[qualified_name_node].text
        db_table = qualified_name.split(".")
        if len(db_table) == 0 or len(db_table) > 2:
            raise Exception(
                "Unresolvable name: {}".format(qualified_name))
        elif len(db_table) == 2:
            if qualified_name not in self._dependency:
                self._dependency[qualified_name] = {
                    "Database": db_table[0], "Table": db_table[1]}
        elif len(db_table) == 1:
            # an alias or invalid
            table = db_table[0]
            if table not in self._alias:
                raise Exception(
                    "Database is not specified in {}".format(qualified_name))

    def add_alias(self, alias_identifier, node_id):
        if alias_identifier not in self._alias:
            self._alias[alias_identifier] = node_id

    def add_field(self, field):
        f = {"Name": field}
        if f not in self._field:
            self._field.append(f)

    def visit(self, ctx):
        """
        Call visit(tree) will traverse all tree nodes
        and call custom visit functions right away.
        When done,
        - a simple syntax tree graph is generated in _syntax_graph;
        - corresponding nodes and edges are collected in _nodes and _edges;
        - root node id is _root;
        - _alias stores alias text -> referred node id;
        - _dependency collects all related db and tables mentioned in the query.

        Args:
            ctx ([type]): [description]

        Returns:
            [type]: [description]
        """
        # skip None ctx
        if ctx is None:
            return None

        # add root node
        if self._root_id is None:
            self._root_id = self.node_id(ctx)

        return super().visit(ctx)

    #
    #  CUSTOM VISIT FUNCTION
    #

    # Here defines custom visit function that collect nodes, edges, alias
    # and build syntax_graph when first visit the entire tree.
    #
    # The basic parsing path is:
    #
    # querySpecification -> (selectItem=selectSingle, selectAll),relation
    #   selectSingle -> expression, identifier
    #       expression -> booleanExpression -> valueExpression
    #           valueExpression -> primaryExpression and others
    #               primaryExpression --> ...
    #       identifier -> unquoted, quoted, backquoted,digit
    #   selectAll ->写死
    #   relation -> sampledRelation -> aliasedRelation -> relationPrimary

    # 127 query
    def visitQuery(self, ctx):
        this = self.add_node(ctx, "QUERY")
        if ctx.r_with():
            r_with_node = self.visit(ctx.r_with())
            self.add_edge(this, r_with_node, "WITH")

        query_no_with_node = self.visit(ctx.queryNoWith())
        self.add_edge(this, query_no_with_node)

        return this

    # 131 r_with
    def visitR_with(self, ctx):
        this = self.add_node(ctx, "WITH")
        named_query_node = [self.visit(i) for i in ctx.namedQuery()]
        self.add_edge(this, named_query_node, "WITH")
        return this

    # 256 namedQuery
    def visitNamedQuery(self, ctx):
        identifier_node = self.visit(ctx.identifier())
        query_node = self.visit(ctx.query())
        self.add_edge(identifier_node, query_node, "NAMED_QUERY")

        # add alias
        self.add_alias(self._nodes[identifier_node].text, query_node)

        if ctx.columnAliases():
            column_aliases_node = self.visit(ctx.columnAliases())
            self.add_edge(identifier_node, column_aliases_node,
                          "COLUMN_ALIASES")
        return identifier_node

    # 209 queryNoWith
    def visitQueryNoWith(self, ctx):
        query_term_node = self.visit(ctx.queryTerm())
        if ctx.sortItem():
            sort_item_node = [self.visit(i) for i in ctx.sortItem()]
            self.add_edge(query_term_node, sort_item_node, "ORDER_BY")
        return query_term_node

    # 215 queryTerm
    def visitQueryTermDefault(self, ctx):
        return self.visit(ctx.queryPrimary())

    def visitSetOperation(self, ctx):
        this = self.add_node(ctx, ctx.operator.text)
        self.add_edge(this, [self.visit(i) for i in ctx.queryTerm()])
        return this

    # 228 sortItem
    def visitSortItem(self, ctx):
        return self.visit(ctx.expression())

    # 221 queryPrimary
    def visitQueryPrimaryDefault(self, ctx):
        return self.visit(ctx.querySpecification())

    def visitTable(self, ctx):
        raise NotImplementedError  # unclear of its usage

    def visitInlineTable(self, ctx):
        return self.add_node(ctx, "INLINE_TABLE")

    def visitSubquery(self, ctx):
        return self.visit(ctx.queryNoWith())

    # 232 querySpecification
    def visitQuerySpecification(self, ctx):
        this = self.add_node(ctx, "QUERY_SPECIFICATION")
        # select
        select_item_nodes = [self.visit(i) for i in ctx.selectItem()]
        self.add_edge(this, select_item_nodes, "SELECT")

        # relation
        if ctx.relation():
            relation_node = [self.visit(i) for i in ctx.relation()]
            self.add_edge(this, relation_node, "FROM")

        # where
        if ctx.where:
            where_node = self.visit(ctx.where)
            self.add_edge(this, where_node, "WHERE")

        # group by
        if ctx.groupBy():
            group_by_node = self.visit(ctx.groupBy())
            self.add_edge(this, group_by_node, "GROUP_BY")

        # having
        if ctx.having:
            having_node = self.visit(ctx.having)
            self.add_edge(this, having_node, "HAVING")

        return this

    # 240 groupBy
    def visitGroupBy(self, ctx):
        return [self.visit(i) for i in ctx.groupingElement()]

    # 265 selectItem

    def visitSelectSingle(self, ctx):
        expression_node = self.visit(ctx.expression())

        if ctx.identifier():
            identifier_node = self.visit(ctx.identifier())
            self.add_edge(identifier_node, expression_node)
            return identifier_node
        else:
            return expression_node

    # 265 selectItem
    def visitSelectAll(self, ctx):
        if ctx.qualifiedName():
            qualified_name_node = self.visit(ctx.qualifiedName())
            this = self.add_node(
                ctx, self._nodes[qualified_name_node].text + ".*")
            self.add_edge(this, qualified_name_node)
        else:
            this = self.add_node(ctx, "*")
        return this

    # 271 relation
    def visitJoinRelation(self, ctx):
        this = self.add_node(ctx, "JOIN")
        self.add_edge(this, [self.visit(ctx.left), self.visit(
            ctx.right), self.visit(ctx.rightRelation)])
        return this

    def visitRelationDefault(self, ctx):
        return self.visit(ctx.sampledRelation())

    # 292 sampledRelation
    def visitSampledRelation(self, ctx):
        return self.visit(ctx.aliasedRelation())

    # 303 aliasedRelation
    def visitAliasedRelation(self, ctx):
        relation_primary_node = self.visit(ctx.relationPrimary())
        if ctx.identifier():
            identifier_node = self.visit(ctx.identifier())
            self.add_edge(identifier_node, relation_primary_node,
                          "RELATION_ALIAS")

            # add alias
            # self.add_alias(
            #     self._nodes[identifier_node].text, relation_primary_node)

            # TODO column alias
            if ctx.columnAliases():
                column_aliases_node = self.visit(ctx.columnAliases())
                self.add_edge(identifier_node,
                              column_aliases_node, "COLUMN_ALIASES")
            return identifier_node
        return relation_primary_node

    # 307 columnAliases
    def visitColumnAliases(self, ctx):
        return [self.visit(i) for i in ctx.identifier()]

    # 311 relationPrimary
    def visitTableName(self, ctx):
        qualified_name_node = self.visit(ctx.qualifiedName())

        self.add_dependency(qualified_name_node)
        return qualified_name_node

    def visitSubqueryRelation(self, ctx):
        return self.visit(ctx.query())

    def visitUnnest(self, ctx):
        this = self.add_node(ctx, "UNNEST")
        expression_node = [self.visit(i) for i in ctx.expression()]
        self.add_edge(this, expression_node)
        return this

    def visitLateral(self, ctx):
        this = self.add_node(ctx, "LATERAL")
        query_node = self.visit(ctx.query())
        self.add_edge(this, query_node)
        return this

    def visitParenthesizedRelation(self, ctx):
        return self.visit(ctx.relation())

    # 323 booleanExpression
    def visitPredicated(self, ctx):
        this = [self.visit(ctx.valueExpression())]
        if ctx.predicate():
            this.append(self.visit(ctx.predicate()))
        return this

    def visitLogicalNot(self, ctx):
        return self.visit(ctx.booleanExpression())

    def visitLogicalBinary(self, ctx):
        return [self.visit(i) for i in ctx.booleanExpression()]

    # 331 predicate
    def visitComparison(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitQuantifiedComparison(self, ctx):
        return self.visit(ctx.query())

    def visitBetween(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitInList(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    def visitInSubquery(self, ctx):
        return self.visit(ctx.query())

    def visitLike(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitDistinctFrom(self, ctx):
        return self.visit(ctx.valueExpression())

    # 342 valueExpression
    def visitValueExpressionDefault(self, ctx):
        return self.visit(ctx.primaryExpression())

    def visitAtTimeZone(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitArithmeticUnary(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitArithmeticBinary(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitConcatenation(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 351 primaryExpression
    # def visitNullLiteral(self, ctx):
    #     return self.add_node(ctx, "NULL_LITERAL")

    # def visitIntegerLiteral(self, ctx):
    #     return self.add_node(ctx, "INTEGER_LITERAL")

    # def visitTypeConstructor(self, ctx):
    #     pass

    # def visitNumericLiteral(self, ctx):
    #     return self.add_node(ctx, "NUMERIC_LITERAL")

    # def visitBooleanLiteral(self, ctx):
    #     return self.add_node(ctx, "BOOLEAN_LITERAL")

    # def visitStringLiteral(self, ctx):
    #     return self.add_node(ctx, "STRING_LITERAL")

    # def visitBinaryLiteral(self, ctx):
    #     return self.add_node(ctx, "BINARY_LITERAL")

    def visitPosition(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitRowConstructor(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    def visitFunctionCall(self, ctx):
        this = self.add_node(ctx, "FUNCTION_CALL")
        if ctx.expression():
            expression_node = [self.visit(i) for i in ctx.expression()]
            self.add_edge(this, expression_node)

        return this

    def visitLambda(self, ctx):
        return [self.visit(i) for i in ctx.identifier()] + \
            [self.visit(i) for i in ctx.expression()]

    def visitSubqueryExpression(self, ctx):
        return self.visit(ctx.query())

    def visitExits(self, ctx):
        return self.visit(ctx.query())

    def visitSimpleCase(self, ctx):
        return [self.visit(ctx.valueExpression())] \
            + [self.visit(i) for i in ctx.whenClause()] \
            + [self.visit(ctx.expression())]

    def visitSearchedCase(self, ctx):
        return [self.visit(i) for i in ctx.whenClause()] \
            + [self.visit(ctx.expression())]

    def visitCast(self, ctx):
        return self.visit(ctx.expression())

    def visitArrayConstructor(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    def visitSubscript(self, ctx):
        return [self.visit(ctx.primaryExpression())] \
            + [self.visit(ctx.valueExpression())]

    def visitColumnReference(self, ctx):
        return self.visit(ctx.identifier())

    def visitDereference(self, ctx):
        primary_expression_node = self.visit(ctx.primaryExpression())
        identifier_node = self.visit(ctx.identifier())
        this = self.add_node(
            ctx, self._nodes[primary_expression_node].text +
            "." + self._nodes[identifier_node].text)
        self.add_edge(this, [primary_expression_node,
                             identifier_node], "DEREFERENCE")
        return this

    def visitSubstring(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitNormalize(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitExtract(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitParenthesizedExpression(self, ctx):
        return self.visit(ctx.expression())

    def visitGroupingOperation(self, ctx):
        return [self.visit(i) for i in ctx.qualifiedName()]

    # L456 whenClause
    def visitWhenClause(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    # L513 qualifiedName
    def visitQualifiedName(self, ctx):
        identifier_node = [self.visit(i) for i in ctx.identifier()]
        qualified_name = ".".join(
            [self._nodes[n].text for n in identifier_node])
        this = self.add_node(ctx, qualified_name)
        self.add_edge(this, identifier_node, "QUALIFIED_NAME")
        return this

    # L533 identifier
    def visitUnquotedIdentifier(self, ctx):
        return self.add_node(ctx, ctx.getText())

    def visitQuotedIdentifier(self, ctx):
        return self.add_node(ctx, ctx.getText()[1:-1])

    def visitBackQuotedIdentifier(self, ctx):
        return self.add_node(ctx, ctx.getText()[1:-1])

    def visitDigitIdentifier(self, ctx):
        return self.add_node(ctx, ctx.getText())

    # lineage
    def compute_lineage(self):

        # copy nodes from _syntax_graph
        nodes = self._nodes.copy()

        # remove irrelevant edges
        def recursive_remove(node, removed_labels):
            if len(node.children) > 0:
                for child in node.children:
                    recursive_remove(nodes[child["id"]], removed_labels)
            for label in removed_labels:
                node.remove_child(label)

        recursive_remove(nodes[self._root_id], ["WHERE", "GROUP_BY",
                                                "HAVING", "ORDER_BY", "QUALIFIED_NAME"])

        # move WITH and FROM to where it is referred
        def find_leaf(node):
            if len(node.children) > 0:
                # all children is DEREFERENCE
                if node.is_all_children("DEREFERENCE"):
                    yield node
                    # last = node.get_first_child_id()
                    # if last:
                    #     yield from find_leaf(nodes[last])
                else:
                    for child in node.children:
                        yield from find_leaf(nodes[child["id"]])
            else:
                yield node

        def recursive_from_with(node):
            if node.text == "QUERY_SPECIFICATION":
                if node.get_child_id("FROM"):
                    from_node_id = node.get_child_id("FROM")[0]

                    # link alias WITH to its NAMED_QUERY node
                    for from_leaf_node in find_leaf(nodes[from_node_id]):
                        if from_leaf_node.text in self._alias:
                            from_leaf_node.add_child(
                                self._alias[from_leaf_node.text], "_WITH")

                    # link SELECT leaf node to FROM relation node
                    for select_node_id in node.get_child_id("SELECT"):
                        for select_leaf_node in find_leaf(nodes[select_node_id]):
                            select_leaf_node.add_child(from_node_id, "_FROM")

            # Use elif so that only QUERY_SPECIFICATION node directly
            # reached from root is processed, ignore any QUERY_SPECIFICATION
            # in its leaf nodes.This is critial after WITH and FROM are reconnected.
            elif len(node.children) > 0:
                for child in node.children:
                    recursive_from_with(nodes[child["id"]])
        recursive_from_with(nodes[self._root_id])

        # remove WITH and FROM edges
        recursive_remove(nodes[self._root_id], [
                         "WITH", "FROM", "NAMED_QUERY"])

        # get visible fields
        def recursive_field(node):
            if node.text == "QUERY_SPECIFICATION":
                column_number = 0
                for select_node_id in node.get_child_id("SELECT"):
                    select_node = nodes[select_node_id]
                    dereference_node_ids = select_node.get_child_id(
                        "DEREFERENCE")

                    if dereference_node_ids:
                        dereference_node = nodes[dereference_node_ids[-1]]
                        self.add_field(dereference_node.text)

                    elif select_node.text == "FUNCTION_CALL":
                        self.add_field("_col" + str(column_number))
                        column_number += 1
                    else:

                        self.add_field(select_node.text)

            elif len(node.children) > 0:
                for child in node.children:
                    recursive_field(nodes[child["id"]])

        recursive_field(nodes[self._root_id])

        # remove DEREFERENCE edge
        recursive_remove(nodes[self._root_id], ["DEREFERENCE"])

        # Build linage graph by traverssing from root. Nodes that are
        # not reachable from root node must be in isolation.Therefore
        # they are not plotted to _lineage_graph

        SYNTAX_NODE_TEXT = ["QUERY", "WITH", "INLINE_TABLE", "QUERY_SPECIFICATION",
                            "UNNEST", "LATERAL", "FUNCTION_CALL", "JOIN", "UNION",
                            "INTERSECT", "EXCEPT"]
        visited = {}

        def recursive_build_graph(node):
            if node.id in visited:
                return

            # add node
            if node.text in SYNTAX_NODE_TEXT:
                self._lineage_graph.attr("node", shape="plaintext")
            elif node.text in self._dependency:
                self._lineage_graph.attr("node", shape="ellipse")
            else:
                self._lineage_graph.attr("node", shape="box")

            self._lineage_graph.node(node.id, node.text)

            # visit child
            if len(node.children) > 0:
                for child in node.children:
                    recursive_build_graph(nodes[child['id']])
            # add edge
                    if child["label"] in ["_FROM", "_WITH"]:
                        self._lineage_graph.attr("edge", style="dashed")
                        self._lineage_graph.edge(
                            node.id, child["id"])
                    else:
                        self._lineage_graph.attr("edge", style="solid")
                        self._lineage_graph.edge(
                            node.id, child["id"], child["label"])

            visited[node.id] = 1

        recursive_build_graph(nodes[self._root_id])

        return
