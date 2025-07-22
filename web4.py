from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def Search():
    keywords = request.args.get('keywords')
    # haha = request.args.get('hihi')
    page = request.args.get('page')
    return "<h1 style = 'color: gray'>Hasil Pencarian: {}, di halaman {}</h1>".format(keywords, page)

if __name__ == '__main__':
    app.run(debug = True)