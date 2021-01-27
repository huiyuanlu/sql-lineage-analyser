"""Flask App for SQL Lineage Analysis."""

from flask import Flask,  request,  jsonify
from flask_cors import CORS
import json
import os

import wtforms_json

from wtforms import Form, StringField, validators

from SparkSQL.lineage import format_sparksql, capitalize_sparksql, \
    parse_sparksql, analyse_sparksql
from PrestoSQL.lineage import format_prestosql, capitalize_prestosql,\
    parse_prestosql, analyse_prestosql

app = Flask(__name__)
CORS(app)

wtforms_json.init()


class ReqeustForm(Form):
    """Request form from json body."""

    dialect = StringField(u'dialect',
                          validators=[validators.input_required(),
                                      validators.AnyOf(["SparkSQL", "PrestoSQL"],
                                                       "Only SparkSQL and PrestoSQL are supported")])
    sql = StringField(u'sql',
                      validators=[validators.input_required()])


@app.route('/', methods=['POST'])
def analysis():
    """Analysis api."""
    # validate ip
    allowed_host = os.environ["WHITELIST"].split(",")
    # host = request.headers.get('Host')
    # ip = request.headers.get('X-Real-IP')
    # if host not in allowed_host and ip not in allowed_host:
    #     return jsonify({
    #         "code": 0,
    #         "data": None,
    #         "msg": "No permission."})

    # valid request
    form = ReqeustForm.from_json(request.get_json(silent=True))
    if not form.validate():
        return jsonify({
            "code": 0,
            "data": None,
            "msg": "Invalid Request." + json.dumps(form.errors)})

    # analysis
    try:
        if form.dialect.data == "SparkSQL":
            q_formated = format_sparksql(form.sql.data)
            q_cap = capitalize_sparksql(q_formated)
            tree, rule_names = parse_sparksql(q_cap)
            v = analyse_sparksql(tree, rule_names)

        elif form.dialect.data == "PrestoSQL":
            q_formated = format_prestosql(form.sql.data)
            q_cap = capitalize_prestosql(q_formated)
            tree, rule_names = parse_prestosql(q_cap)
            v = analyse_prestosql(tree, rule_names)

        return jsonify({
                "code": 1,
                "data": {
                    "Dependencies": v.dependency,
                    "Fields": v.field
                },
                "msg": "Success."
            })
    except Exception as e:
        return jsonify({"code": 0,
                        "data": None,
                        "msg": "Analyse error. " + str(e)})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
