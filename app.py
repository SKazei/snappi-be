import os
from flask import Flask, redirect, request, send_from_directory

app = Flask(__name__)

SEARCH_ENGINES = {
    'google': 'https://www.google.com/search?q={query}',
    'bing': 'https://www.bing.com/search?q={query}',
    'yahoo': 'https://search.yahoo.com/search?p={query}',
    'ask': 'https://www.ask.com/web?q={query}',
    'duckduckgo': 'https://duckduckgo.com/?q={query}',
    'startpage': 'https://www.startpage.com/do/search?query={query}'
}

@app.route('/googlef416689ddc8de593.html')
def google_verification():
    return send_from_directory(
        directory=os.path.abspath(os.path.dirname(__file__)),
        filename='googlef416689ddc8de593.html'
    )

@app.route('/search/', methods=['GET'])
def search_endpoint():
    query = request.args.get('q')
    if query:
        return redirect(f"https://www.google.com/search?q={query}", code=302)
    else:
        return redirect("https://www.google.com/", code=302)

@app.route('/search/<engine>/', methods=['GET'])
def dynamic_search_endpoint(engine):
    query = request.args.get('q')

    if not query:
        return redirect(SEARCH_ENGINES['google'].format(query=''), code=302)

    if engine in SEARCH_ENGINES:
        redirect_url = SEARCH_ENGINES[engine].format(query=query)
        return redirect(redirect_url, code=302)
    else:
        redirect_url = SEARCH_ENGINES['google'].format(query=query)
        return redirect(redirect_url, code=302)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/x-icon')