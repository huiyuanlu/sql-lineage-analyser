from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

import re
from typing import *

from graphviz import Digraph

import PrestoSQL
from PrestoSQL.PrestoSQLLexer import PrestoSQLLexer
from PrestoSQL.PrestoSQLParser import PrestoSQLParser
from PrestoSQL.listener import PrestoSQLGraphListener
from PrestoSQL.visitor import PrestoSQLVisitor
# https://prestodb.io/docs/current/language/reserved.html
RESERVED = ["ALTER", "AND", "AS", "BETWEEN", "BY", "CASE", "CAST", "CONSTRAINT", "CREATE", "CROSS", "CUBE", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "DEALLOCATE", "DELETE", "DESCRIBE", "DISTINCT", "DROP", "ELSE", "END", "ESCAPE", "EXCEPT", "EXECUTE", "EXISTS", "EXTRACT", "FALSE", "FOR", "FROM", "FULL", "GROUP",
            "GROUPING", "HAVING", "IN", "INNER", "INSERT", "INTERSECT", "INTO", "IS", "JOIN", "LEFT", "LIKE", "LOCALTIME", "LOCALTIMESTAMP", "NATURAL", "NORMALIZE", "NOT", "NULL", "ON", "OR", "ORDER", "OUTER", "PREPARE", "RECURSIVE", "RIGHT", "ROLLUP", "SELECT", "TABLE", "THEN", "TRUE", "UESCAPE", "UNION", "UNNEST", "USING", "VALUES", "WHEN", "WHERE", "WITH"]

# Some token in the full NONRESERVED list might appear as identifiers
# in a query. For example, "ADMIN" is only need in createRole,
# grantRoles, revokeRoles statements so in a query it can be used as for
# instance a column name. The NONRESERVED list is modified.

# NONRESERVED = ["ADD", "ADMIN", "ALL", "ALTER", "ANALYZE", "AND", "ANY", "ARRAY", "AS", "ASC", "AT", "BERNOULLI", "BETWEEN", "BY", "CALL", "CALLED", "CASCADE", "CASE", "CAST", "CATALOGS", "COLUMN", "COLUMNS", "COMMENT", "COMMIT", "COMMITTED", "CONSTRAINT", "CREATE", "CROSS", "CUBE", "CURRENT", "CURRENT_DATE", "CURRENT_ROLE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "DATA", "DATE", "DAY", "DEALLOCATE", "DEFINER", "DELETE", "DESC", "DESCRIBE", "DETERMINISTIC", "DISTINCT", "DISTRIBUTED", "DROP", "ELSE", "END", "ESCAPE", "EXCEPT", "EXCLUDING", "EXECUTE", "EXISTS", "EXPLAIN", "EXTRACT", "EXTERNAL", "FALSE", "FILTER", "FIRST", "FOLLOWING", "FOR", "FORMAT", "FROM", "FULL", "FUNCTION", "FUNCTIONS", "GRANT", "GRANTED", "GRANTS", "GRAPHVIZ", "GROUP", "GROUPING", "HAVING", "HOUR", "IF", "IGNORE", "IN", "INCLUDING", "INNER", "INPUT", "INSERT", "INTERSECT", "INTERVAL", "INTO", "INVOKER", "IO", "IS", "ISOLATION", "JSON", "JOIN", "LANGUAGE", "LAST", "LATERAL", "LEFT", "LEVEL", "LIKE", "LIMIT",
#                "LOCALTIME", "LOCALTIMESTAMP", "LOGICAL", "MAP", "MINUTE", "MONTH", "NAME", "NATURAL", "NFC", "NFD", "NFKC", "NFKD", "NO", "NONE", "NORMALIZE", "NOT", "NULL", "NULLIF", "NULLS", "ON", "ONLY", "OPTION", "OR", "ORDER", "ORDINALITY", "OUTER", "OUTPUT", "OVER", "PARTITION", "PARTITIONS", "POSITION", "PRECEDING", "PREPARE", "PRIVILEGES", "PROPERTIES", "RANGE", "READ", "RECURSIVE", "RENAME", "REPEATABLE", "REPLACE", "RESET", "RESPECT", "RESTRICT", "RETURN", "RETURNS", "REVOKE", "RIGHT", "ROLE", "ROLES", "ROLLBACK", "ROLLUP", "ROW", "ROWS", "SCHEMA", "SCHEMAS", "SECOND", "SECURITY", "SELECT", "SERIALIZABLE", "SESSION", "SET", "SETS", "SHOW", "SOME", "SQL", "START", "STATS", "SUBSTRING", "SYSTEM", "TABLE", "TABLES", "TABLESAMPLE", "TEXT", "THEN", "TIME", "TIMESTAMP", "TO", "TRANSACTION", "TRUE", "TRY_CAST", "TYPE", "UESCAPE", "UNBOUNDED", "UNCOMMITTED", "UNION", "UNNEST", "USE", "USER", "USING", "VALIDATE", "VALUES", "VERBOSE", "VIEW", "WHEN", "WHERE", "WITH", "WORK", "WRITE", "YEAR", "ZONE"]
NONRESERVED = ["ALL", "AND", "ANY", "ARRAY", "AS", "ASC", "AT", "BERNOULLI", "BETWEEN", "BY", "CASE", "CAST", "CROSS", "CUBE", "CURRENT", "CURRENT_DATE", "CURRENT_ROLE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "DATE", "DAY",  "DESC",  "DISTINCT",  "ELSE", "END", "ESCAPE", "EXCEPT", "EXCLUDING", "EXECUTE", "EXISTS",    "FALSE", "FILTER", "FIRST", "FOLLOWING", "FOR",  "FROM", "FULL",       "GROUP", "GROUPING", "HAVING", "HOUR", "IF", "IGNORE", "IN", "INCLUDING", "INNER",   "INTERSECT", "INTERVAL",    "IS",  "JSON", "JOIN",  "LAST", "LATERAL", "LEFT",  "LIKE", "LIMIT",
               "LOCALTIME", "LOCALTIMESTAMP", "MAP", "MINUTE", "MONTH", "NATURAL", "NFC", "NFD", "NFKC", "NFKD", "NORMALIZE", "NOT", "NULL", "NULLS", "ON", "OR", "ORDER", "ORDINALITY", "OUTER", "OVER", "PARTITION", "POSITION", "PRECEDING", "PROPERTIES", "RANGE", "RECURSIVE", "RESPECT", "RETURN", "RIGHT", "ROLLUP", "ROW", "ROWS", "SECOND", "SELECT", "SETS", "SOME", "SUBSTRING", "SYSTEM", "TABLE", "TABLESAMPLE", "THEN", "TIME", "TIMESTAMP", "TO", "TRUE", "TRY_CAST", "TYPE", "UESCAPE", "UNBOUNDED", "UNION", "UNNEST", "USING", "VALUES", "WHEN", "WHERE", "WITH", "WRITE", "YEAR", "ZONE"]
KEYWORDS = dict.fromkeys(set(RESERVED+NONRESERVED), 1)


def format_prestosql(query: str) -> str:
    """Reformat PrestoSQL query.
    Args:
        query: original query.

    Returns:
        An one-line statement from the original query
        with all reversed words uppercased.
    """

    # remove inline comment --
    q = re.sub(r"\-\-.*", "", query)

    # remove embedded or multi-line comment /* */ in a non-greedy fashion
    q = re.sub(r"\/\*[\s\S]*?\*\/", "", q)

    # remove \n
    q = re.sub(r"\n", " ", q)

    # replace multiple whitespace with one whitespace
    q = re.sub(r"\s+", " ", q.strip())
    return q


def capitalize_prestosql(query: str) -> str:
    # uppcase all reserved words
    tokens = re.split(r"([^A-Za-z0-9\+\-\"'`_@:%])", query)
    for i in range(len(tokens)):
        # ignre identifers after as
        if i > 2 and tokens[i-1] == " " and tokens[i - 2] == "AS":
            continue
        token_upper = tokens[i].upper()
        if token_upper in KEYWORDS:
            tokens[i] = token_upper

    return "".join(tokens)


class PrestoSQLErrorListner(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("syntaxError", line, column, msg)


def parse_prestosql(query: str):
    """Parse query and generate ast.

    Args:
        input (str): query string

    Returns:
        [type]: [description]
    """
    input_stream = InputStream(query)
    lexer = PrestoSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PrestoSQLParser(stream)
    parser.addErrorListener(PrestoSQLErrorListner())
    tree = parser.query()
    rule_names = parser.ruleNames
    return tree, rule_names


def print_prestosql_tree_string(node, rule_names, indent, string):
    """Traverse all nodes in tree and return a cascading-style string that presents the tree.

    Args:
        tree ([type]): [description]
        rule_names ([type]): [description]
        indent (int, optional): [description]. Defaults to 0.
    """

    if isinstance(node, TerminalNodeImpl) or isinstance(node, ErrorNodeImpl):
        string += "\n{0}TOKEN='{1}'".format("  " * indent, node.getText())
    else:
        id = str(node)[1:-1].split(" ")[0]
        string += "\n{0}{1} {2}".format("  " * indent,
                                        rule_names[node.getRuleIndex()], id)

        if node.children:
            for child in node.children:
                if child:
                    string = print_prestosql_tree_string(
                        child, rule_names, indent + 1, string)
    return string


def print_prestosql_full_graph(tree, rule_names):

    walker = ParseTreeWalker()
    listener = PrestoSQLGraphListener(rule_names)
    walker.walk(listener, tree)

    return listener.graph


def analyse_prestosql(tree, rule_names):
    visitor = PrestoSQLVisitor(rule_names)
    visitor.visit(tree)
    visitor.compute_lineage()

    return visitor
