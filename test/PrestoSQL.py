import unittest
from PrestoSQL.lineage import format_prestosql, capitalize_prestosql, parse_prestosql, analyse_prestosql


class TestPrestoSQL(unittest.TestCase):
    def test_format_prestosql(self):
        self.assertEqual(format_prestosql("select a, --note \n b from c"),
                         "select a, b from c")

    def test_capitalize_prestosql(self):
        self.assertEqual(capitalize_prestosql("select a from b"),
                         "SELECT a FROM b")

    def test_analyse_prestosql(self):
        tests = [
            {
                "query": "select a, b from c.d",
                "field": [{"Name": "a"}, {"Name": "b"}],
                "dependency": [{"Database": "c", "Table": "d"}]
            },
            {
                "query": "select a, b from (select c, d from e.f)",
                "field": [{"Name": "a"}, {"Name": "b"}],
                "dependency": [{"Database": "e", "Table": "f"}]
            },
        ]
        for test in tests:
            q = test["query"]
            q_formated = format_prestosql(q)
            q_cap = capitalize_prestosql(q_formated)
            tree, rule_names = parse_prestosql(q_cap)
            v = analyse_prestosql(tree, rule_names)
            self.assertEqual(v.field, test["field"])
            self.assertEqual(v.dependency, test["dependency"])


if __name__ == '__main__':
     unittest.main()
