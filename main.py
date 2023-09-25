import os
import openai
import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# OpenAI API key
openai.api_key = os.getenv("API_KEY")

# cluster_url = "your_cluster_url"
# username = "your_username"
# password = "your_password"


@app.route('/')
def home():
    return render_template('index.html')



@app.route("/api", methods = ['POST'])
def fetch_data():
    # access prompt question
    prompt = request.form.get("prompt")
    response = openai.Completion.create(
        engine="davinci",  # Choose the engine, e.g., "davinci" or "curie"
        prompt=prompt,
        max_tokens=50,  
    )

    generated_text = response.choices[0].text
    print(generated_text)

    # Return the data as a JSON response
    # return jsonify({"data": data})
    # data = "Today's date is September 25, 2023."

    # return data
    # using jsonify({"data": data}) instead of return data since my cient side is expecting a json data instead of a single string
    return jsonify({"data": generated_text})
    # return f"Server reponsed with 200 and promt is"




app.run(debug = True)




