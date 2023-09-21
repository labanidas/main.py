from flask import Flask, render_template, request, jsonify
import os
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# Set your OpenAI API key
# openai.api_key = os.getenv("API_KEY")
@app.route("/api", methods = ['GET', 'POST'])
def fetch_data():
    # access prompt question
    prompt = request.form.get("prompt")
    # response = openai.Completion.create(
    #     engine="davinci",  # Choose the engine, e.g., "davinci" or "curie"
    #     prompt="Translate the following English text to French: 'Hello, how are you?'",
    #     max_tokens=50,  
    # )

    # generated_text = response.choices[0].text
    # print(generated_text)

    # Return the data as a JSON response
    # return jsonify({"data": data})
    data = "This is the response from the server."

    # return data
    # using jsonify({"data": data}) instead of return data since my cient side is expecting a json data instead of a single string
    return jsonify({"data": data})
    # return f"Server reponsed with 200 and promt is"




app.run(debug = True)




