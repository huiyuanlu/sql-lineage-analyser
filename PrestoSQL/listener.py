from PrestoSQL.PrestoSQLListener import PrestoSQLListener
from graphviz import Digraph


class PrestoSQLGraphListener(PrestoSQLListener):

    def __init__(self, rule_names):
        super().__init__()
        self._nodes = {}
        self._rule_names = rule_names
        self._graph = Digraph(format="png")

    @property
    def graph(self):
        return self._graph

    def add_node(self, ctx):
        id = hex(hash(ctx))
        rule_name = self._rule_names[ctx.getRuleIndex()]

        if rule_name == "identifier" or rule_name == "string":
            r = ""
            t = ctx.getText()
            self._graph.attr("node", shape="box")
        else:
            r = rule_name
            r = r.replace("r_", "")
            t = ""
            self._graph.attr("node", shape="ellipse")

        if id not in self._nodes:
            self._graph.node(id, r + t)
            self._nodes[id] = 1

        return id

    def enterEveryRule(self, ctx):
        if ctx.parentCtx:
            n1 = self.add_node(ctx.parentCtx)
            n2 = self.add_node(ctx)
            self._graph.edge(n1, n2)

    def exitEveryRule(self, ctx):
        pass

    def visitTerminal(self, ctx):
        pass
