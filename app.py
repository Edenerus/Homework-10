from flask import Flask
from functions import *

app = Flask(__name__)


@app.route("/")
def page_index():
    return f"<pre>{get_all()}</pre>"


@app.route("/candidates/<id>")
def page_candidate(id):
    picture, candidate_info = get_by_pk(id)
    return f"""<img src = "{picture}"><pre>{candidate_info}</pre>"""


@app.route("/skills/<skill>")
def page_skills(skill):
    return f"<pre>{get_by_skill(skill)}</pre>"


app.run()