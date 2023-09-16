from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods = ['GET', 'POST'])
def qa():
    data = {
            "request" : "thank you"
        }
    # if request.method == 'POST':       
    #     return jsonify(data)
    # return render_template('index.html')
    return jsonify(data)

app.run(debug = True)