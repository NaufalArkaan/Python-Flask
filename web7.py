from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home(): 
    is_logged_in = True
    name = "falll"
    items = ['bola', 'sepatu', 'buku']
    return render_template('index2.html', is_logged_in=is_logged_in, name=name, items=items)

if __name__ == '__main__':
    app.run(debug=True)
