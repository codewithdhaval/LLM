import os
import requests
import openai
import json
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        chat = request.form["chat"]
        response = openaiRest(chat)
        print(f'Response after parsing ::{response}')
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def openaiRest(prompt: str):
    # print(f'{prompt} from the user')
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0,
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
    return response.json()["choices"][0]["text"]