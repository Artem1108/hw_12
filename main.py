from flask import Flask, render_template
from utils import *

app = Flask(__name__)

@app.route("/")
def main_page():
    a = load_candidates()
    return render_template('list.html', candidates = a)

@app.route('/search/<candidate_name>')
def searchcandidate(candidate_name):
    a = get_by_name(candidate_name)
    return render_template('search.html', candidates = a)

@app.route('/skill/<skill_name>')
def skillcandidate(skill_name):
    a = get_by_skill(skill_name)
    return render_template('skill.html', candidates = a)

@app.route('/candidate/<int:id>')
def id_candidate(id):
    a = get_by_id(id)
    return render_template('single.html', candidates = a)


app.run() 