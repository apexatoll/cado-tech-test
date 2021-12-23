from app import app
from flask import request, render_template
from .query_form import QueryForm
import whois

@app.route("/")

def query():
    form = QueryForm(request.args, meta={'csrf': False})

    search = request.args.get("search")

    results = get_whois_data(search) if form.validate() else None

    return render_template(
        "query.html",
        form = form,
        search = search,
        results = results
    )

def get_whois_data(search):
    return str(whois.whois(search))
