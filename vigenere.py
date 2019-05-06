#enlever les accents dans une chaine python
#https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
import unidecode


def vigenere_clean(text): # on remplace les accents par leurs propres lettres, tout mettre en majuscule, enlever ce qui n'est pas une lettre
    tmp = unidecode.unidecode(text) #on supprime les accents
    tmp = tmp.upper() #mise en maj
    letters = [c for c in tmp if ord(c) >= ord('A') and ord(c) <= ord('Z')] #compréhension liste python :https://miamondo.org/2017/02/27/python-les-comprehensions-de-liste/
    # on ne garde que les lettres dans une liste
    clean_text = "".join(letters) # on transforme les lettres de la liste en un mot
    return clean_text


TableVigenere = {'A': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  'B': "BCDEFGHIJKLMNOPQRSTUVWXYZA",
                  'C': "CDEFGHIJKLMNOPQRSTUVWXYZAB",
                  'D': "DEFGHIJKLMNOPQRSTUVWXYZABC",
                  'E': "EFGHIJKLMNOPQRSTUVWXYZABCD",
                  'F': "FGHIJKLMNOPQRSTUVWXYZABCDE",
                  'G': "GHIJKLMNOPQRSTUVWXYZABCDEF",
                  'H': "HIJKLMNOPQRSTUVWXYZABCDEFG",
                  'I': "IJKLMNOPQRSTUVWXYZABCDEFGH",
                  'J': "JKLMNOPQRSTUVWXYZABCDEFGHI",
                  'K': "KLMNOPQRSTUVWXYZABCDEFGHIJ",
                  'L': "LMNOPQRSTUVWXYZABCDEFGHIJK",
                  'M': "MNOPQRSTUVWXYZABCDEFGHIJKL",
                  'N': "NOPQRSTUVWXYZABCDEFGHIJKLM",
                  'O': "OPQRSTUVWXYZABCDEFGHIJKLMN",
                  'P': "PQRSTUVWXYZABCDEFGHIJKLMNO",
                  'Q': "QRSTUVWXYZABCDEFGHIJKLMNOP",
                  'R': "RSTUVWXYZABCDEFGHIJKLMNOPQ",
                  'S': "STUVWXYZABCDEFGHIJKLMNOPQR",
                  'T': "TUVWXYZABCDEFGHIJKLMNOPQRS",
                  'U': "UVWXYZABCDEFGHIJKLMNOPQRST",
                  'V': "VWXYZABCDEFGHIJKLMNOPQRSTU",
                  'W': "WXYZABCDEFGHIJKLMNOPQRSTUV",
                  'X': "XYZABCDEFGHIJKLMNOPQRSTUVW",
                  'Y': "YZABCDEFGHIJKLMNOPQRSTUVWX",
                  'Z': "ZABCDEFGHIJKLMNOPQRSTUVWXY",
                }


def vigenere_crypt(message, key):
    message = vigenere_clean(message)
    key = vigenere_clean(key)

    crypt_string = ""
    count = 0

    for c in message :

        ligne_crypt = TableVigenere[key[count%len(key)]] # on cherche la ligne de tabvig en question
        pos_c = ord(c) - ord('A') # on cherche la pos de la lettre dans la ligne
        crypt_c = ligne_crypt[pos_c] # on récupère le cryptage de c
        crypt_string += crypt_c
        count += 1 # on éxécute le programme pour chaques lettres du message

    return crypt_string


def vigenere_decrypt(message, key) :
    message = vigenere_clean(message)
    key = vigenere_clean(key)

    decoding_string = ""
    count = 0

    for c in message :
        ligne_decrypt = TableVigenere[key[count%len(key)]] # on cherche la ligne de tabvig en question
        pos_decrypt = ligne_decrypt.find(c) # on cherche la pos de c dans la variable
        pos_decrypt += ord('A') # devient le code ascii de la lettre correspondante
        decoding_string += chr(pos_decrypt)#donne le caractère correspondant au code ascii
        count += 1

    return decoding_string
