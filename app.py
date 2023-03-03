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

    # url = "https://api.openai.com/v1/completions" //Da-Vinci-003 endpoint

    url = "https://api.openai.com/v1/chat/completions" ##chatGPT endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }
    ## Da-vinci-003 body template
    # data = {
    #     "model": "gpt-3.5-turbo",
    #     "prompt": prompt,
    #     "temperature": 0,
    #     "max_tokens": 50
    # }

    #chatGPT body template
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    ## return response.json()["choices"][0]["text"] ## da-vinci parse return object
    return response.json()["choices"][0]["message"]["content"]