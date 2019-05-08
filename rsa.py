
def rsa_crypt(p, q, mot):
    blocks = [] # les blocks resultats
    #on calcule en nombre issue du produit de deux nombres premier
    n=p*q
    f=(p-1)*(q-1)
    #on trouve un nombre e tel que e et f sont premiers entre eux
    global e
    e=0
    i=1
    r=0
    while (r == 0):
        if((p<e)and(q<e)and(e<f)and(e/i!=f/i)):
            r=1
        i=i+1
        e=e+1
    #print("la clé publique est {},{}".format(e,n))
    #on trouve un nombre d tel que d est l'inverse modulaire de f, on peut retouver d mathématiquement par l'algorithme d'euclide étendu
    global d
    d=0
    i=1
    r=0
    #################################################
    #ATTENTION ici on peut boucler sans fin, si p et q sont petits. Il faudrait pouvoir le detecter et l'empecher
    #################################################
    while (r ==0):
        if(e*d%f==1):
            r=1
        i=i+1
        d=d+1
    d=d-1
    #print("la clé privée est {},{}".format(d,n))
    taille_du_mot = len(mot)

    i = 0

    # Tant que i inférieur aux nombres de caractères
    while i < taille_du_mot :
        # Comme i s'incrémente jusqu'à egalité avec la taille du mot, à chaque passage dans la fonction chaque lettre sera converti.
        ascii = ord(mot[i])
    # On crypte la lettre ou plutot son code ASCII
        lettre_crypt = pow(ascii,e)%n
    # Si le code ASCII est supérieur à n
        if ascii > n :
            return "Les nombres p et q sont trop petits veulliez recommencer" # il faut tester le type du retour de rsa_crypt
        # Si le bloc crypté est supérieur à phi(n)
        if lettre_crypt > f :
            return "Erreur de calcul" # il faut tester le type du retour de rsa_crypt
    # On affiche chaque blocs cryptés
        #print ("\n Block : ",lettre_crypt,)
        blocks.append(lettre_crypt)
    # On incrémente i
        i = i + 1

    # il faut tester le type du retour de rsa_crypt. Si c'est une chaine, c'est une erreur
    return { "cle_publique": (e,n), "cle_privee": (d,n), "blocks": blocks }

def rsa_decrypt(d, n, blocks):
    result = ""

    for lettre_crypt in blocks:

        #lettre_crypt = input("\nEntrez le bloc a déchiffrer :")

        # On trouve le ASCII de chaque lettre par le calcul de décodage
        lettre_crypt=int(lettre_crypt)
        ascii = (pow(lettre_crypt,d)%n)

        # Avec la fonction chr(ASCII), on trouve le caractère correspondant.

        lettre_decrypt = chr(ascii)
        #print(lettre_decrypt)
        result = result + lettre_decrypt

    return result

if __name__ == '__main__':
    # ca marche bien avec 701,661,bonjour
    p=int(input('saisir un nombre premier p:'))
    q=int(input('saisir un nombre premier q:'))
    mot=input("saisir la phrase à crypter: ")

    crypt_result = rsa_crypt(p, q, mot)
    print("rsa_crypt: {}".format(crypt_result))

    d = crypt_result["cle_privee"][0]
    n = crypt_result["cle_privee"][1]
    blocks = crypt_result["blocks"]

    decrypt_result = rsa_decrypt(d, n, blocks)
    print("rsa_decrypt: {}".format(decrypt_result))
