from flask import Flask, render_template

app = Flask(__name__, static_folder = "static/dist", template_folder = "static")


@app.route('/')
def index():
    sensors =  { 
        'temperature': 80,
        'distance': 10
    }

    return render_template('index.html', sensors = sensors)

@app.route('/hello')
def hello():
    return "Hello Wordl!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)