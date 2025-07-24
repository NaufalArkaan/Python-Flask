from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    data = [
        {
            'nama': 'fal',
            'email': 'admin123@gmail.com',
            'alamat': 'Jalan Merpati'
        },
        {
            'nama': 'admin',
            'email': 'admin123@gmail.com',
            'alamat': 'Jalan Admin'
        },
        {
            'nama': 'user',
            'email': 'user123@gmail.com',
            'alamat': 'Jalan Bandung'
        }
    ]
    return render_template('user.html', users = data)

if __name__ == '__main__':
    app.run(debug=True)