from flask import Flask, request, redirect
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template('first.html')


@app.get('/next/')
def next_page():
    return render_template('next.html')


@app.post('/next/')
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
    return 'Файл отправлен'


@app.route('/user/', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        user_name = request.form.get('login')
        user_pass = request.form.get('pass')
        if user_name == 'admin' and user_pass == 'qaz':
            return 'Hi admin'
        else:
            return 'what ar fack?'
    return render_template('user.html')


@app.route('/text/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        txt = request.form.get('text')
        num = len(txt.split())
        return f'Количество слов: {num}'
    return render_template('text.html')


@app.route('/suming', methods=['GET', 'POST'])
def suming():
    if request.method == 'POST':
        n1 = int(request.form.get('num1'))
        n2 = int(request.form.get('num'))
        sm = n1 + n2
        return f'{sm}'
    return f'{0}'



if __name__ == '__main__':
    app.run(debug=True)
