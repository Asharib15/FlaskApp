from flask import Flask, render_template, jsonify 

app = Flask(__name__)

# Sample data for the chart (replace this with your actual data retrieval logic)
sample_data = [
    {"date": "2018-04-01", "open": 7000, "high": 7500, "low": 6800, "close": 7200},
    {"date": "2018-04-02", "open": 7200, "high": 7400, "low": 6900, "close": 7100},
    # Add more data here...
]


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/https://canvasjs.com/data/docs/btcusd2018.json')
def get_chart_data():
    return jsonify("index.html")


if __name__ == '__main__':
    app.run(debug=True , port=5001)

from flask import Flask , render_template

