from flask import Flask, redirect, url_for, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main_page():
    # TODO: create a welcome page
    if request.method == "GET":
        return render_template('dictionary.html')
    else: # Post method
        return redirect(url_for('dictionary'))

@app.route('/dictionary')
def dictionary():
    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{request.args.get('word')}")
    if r.status_code != 200:
        return "Error"


    word = r.json()[0]['word'] 
    phonetics = r.json()[0]['phonetics']    
    meanings = r.json()[0]['meanings']
    return render_template('dictionary.html', word=word, phonetics=phonetics, meanings=meanings)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
