from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    data = {
        "nama": "Arkaan",
        "umur": 15
    }
    return render_template('bio.html', **data)

if __name__ == '__main__':
    app.run(debug=True)