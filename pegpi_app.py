
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for, request #url_for : genere les bonnes adresses en fonction du nom du serveur

from vigenere import vigenere_crypt, vigenere_decrypt, vigenere_clean

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cesar')
def cesar():
    return render_template('cesar.html')

#on associe une URL a la fonction qui suit. L'URL vigenere peut être appelé en GET pour un affichage simple
#peut être appelé en POST dans le cas de l'envoi du formulaire
@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    try: #traite des erreurs lors de l'éxecution du block(tj av except)
#request est fourni par le module request et donne les infos sur la requête en cours
        message = vigenere_clean(request.form['message']) #nettoie tout ce qui n'est pas maj
    except:
        message = ''

    try:
        key = vigenere_clean(request.form['key'])
    except:
        key = ''
#on cherche à transmettre toutes les données nécessaire au template
    error = ''
    result = ''
    if message != '' and key != '': #le formulaire est rempli donc on peut (dé)chiffrer
        # savoir si une valeur est dans un dictionnaire python
        # https://www.journaldunet.fr/web-tech/developpement/1202879-python-comment-verifier-si-une-cle-key-existe-dans-un-dictionnaire/
        if 'chiffrer' in request.form:
            result = vigenere_crypt(message, key) # on rentre dans result le résultat du cryptage
        else:
            result = vigenere_decrypt(message, key) # on rentre dans result le résultat du décryptage
    elif request.method == 'POST':  #on test que la méthode est POST pour être sur que le formulaire a été rempli
        error = 'Merci de remplir correctement le formulaire'

    return render_template('vigenere.html', params={'message': message, 'key': key, 'error': error, 'result': result}) #on donne au template les données dont il a besoin
    #params=toutes les données accumulées


@app.route('/rsa')
def rsa():
    return render_template('rsa.html')


if __name__ == '__main__':
    app.run(debug=True)
