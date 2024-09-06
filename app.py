from flask import Flask, request # type: ignore
import scrape
import question as q

app = Flask(__name__)

@app.route("/", methods=["GET"])
def landing():
    return "testing Ollama scrapping"

@app.route("/scrape", methods=["POST"])
def scrapeUrl():
    json_content = request.json
    url = json_content.get("text")
    messages = scrape.fetch_and_presist_article(url)
    return {"urls": url, "messages": messages}

@app.route("/ask_bot", methods=["POST"])
def askBot():
    json_content = request.json
    question = json_content.get("text")
    response = q.answer_question(question)

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)