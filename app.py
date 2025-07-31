from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/search/', methods=['GET'])
def search_endpoint():
    query = request.args.get('q')
    if query:
        return redirect(f"https://www.google.com/search?q={query}", code=302)
    else:
        return redirect("https://www.google.com/", code=302)