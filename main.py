from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def video_feed():
    return render_template('dynamicIndex.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
