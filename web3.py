from flask import Flask #type: ignore

app = Flask(__name__)

@app.route('/profile/<username>/<universitas>')
def Profile(username, universitas):
    return "<h1 style = 'color: yellow'>Halaman Profile {}, kuliah di {}</h1>".format(username, universitas)
@app.route('/about')
def About():
    return "Ini halaman about"
@app.route('/Contact')
def Contact():
    return "Ini halaman contact"

if __name__ == '__main__':
    app.run(debug = True)
