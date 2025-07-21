from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Halaman Utama Saya</h1>"

@app.route('/about')
def about():
    return "<h1 style = 'color: blue'>Halaman About</h1>"

@app.route('/contact')
def contact():
    return "<h1 style = 'color: green'>Halaman Contact</h1>"

if __name__ == '__main__':
    app.run(debug = True) #debug = True supaya perubahan tersimpan secara langsung
