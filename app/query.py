from app import app
from flask import request, render_template
import whois

@app.route("/")

def query():
    search = request.args.get("search")
    results = get_whois_data(search)

    return render_template("query.html", search = search, results = results)

def get_whois_data(search):
    if search: return str(whois.whois(search))
