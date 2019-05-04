
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for, request

from vigenere import vigenere_crypt, vigenere_decrypt, vigenere_clean

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cesar')
def cesar():
    return render_template('cesar.html')


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    try:
        message = vigenere_clean(request.form['message'])
    except:
        message = ''

    try:
        key = vigenere_clean(request.form['key'])
    except:
        key = ''

    error = ''
    result = ''
    if message != '' and key != '':
        # python test dictionary key
        # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
        if 'chiffrer' in request.form:
            result = vigenere_crypt(message, key)
        else:
            result = vigenere_decrypt(message, key)
    elif request.method == 'POST':
        error = 'Merci de remplir correctement le formulaire'

    return render_template('vigenere.html', params={'message': message, 'key': key, 'error': error, 'result': result})


@app.route('/rsa')
def rsa():
    return render_template('rsa.html')


if __name__ == '__main__':
    app.run(debug=True)
