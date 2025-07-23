from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def Form():
    return render_template("form.html")

@app.route('/submit', methodsm = ['POST'])
def Submit():
    name = request.form.get('name')
    return "Hallo {}, Data anda telah disimpan.".format(name)

if __name__ == '__main__':
    app.run(debug = True)