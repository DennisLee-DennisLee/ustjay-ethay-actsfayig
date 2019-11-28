import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    fact = soup.find("div", id="content")
    return fact.getText()

def get_piglatin(input):
    request_url = "http://hidden-journey-62459.herokuapp.com/piglatinize/"
    param_data = {"input_text": input}
    response = requests.post(request_url, param_data)
    # result = response.headers['Location']
    result = "<ul>"
    result += "<p>"+param_data["input_text"]+"</p>"
    for i in response.headers:
        result += "<li>" + i + " | " + response.headers[i] + "</li>"
    result += "<ul>"
    result += "<p>" + response.text + "</p>"
    result += "<p>Is redirect: " + str(response.is_redirect) + "</p>"
    return result

@app.route('/')
def home():
    return get_piglatin(get_fact())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
