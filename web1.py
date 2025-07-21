from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def Hello():
    return "<h5> Hello Flask Cihuyy </h5>"

@app.route('/about')
def About():
    return "<p>lorem</p>"

if __name__ == '__main__':
    app.run()