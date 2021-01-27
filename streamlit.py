"""Demo app."""
import streamlit as st
import json
import pandas as pd

from SparkSQL.lineage import format_sparksql, capitalize_sparksql, \
    parse_sparksql, analyse_sparksql

st.title("SQL Lineage Analyser")

queries = json.loads(open("./data/SparkSQL.json").read())
query_id = st.selectbox(label="Select a query or write one. ", options=sorted(
    [int(i) for i in queries.keys()]))
if query_id:
    q = queries[str(query_id)]

query = st.text_area(label="", value=q, height=400)

go = st.button(label="Analysis")

if go:
    try:
        q_formated = format_sparksql(query)
        q_cap = capitalize_sparksql(q_formated)

        st.header("Formatted Query")
        st.code(q_cap, language="sql")

        tree, rule_names = parse_sparksql(q_cap)

        v = analyse_sparksql(tree, rule_names)

        st.header("Upstream Databases & Tables")
        st.table(pd.DataFrame(v.dependency))

        st.header("Visible Fields")
        st.table(pd.DataFrame(v.field))

        st.header("Alias")
        st.write(v.alias)

        st.header("Syntax Graph")
        st.graphviz_chart(v.syntax_graph)

        st.header("Lineage Graph")
        st.graphviz_chart(v.lineage_graph)

    except Exception as e:
        st.write(e)
