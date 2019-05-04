import unidecode


def vigenere_clean(text):
    tmp = unidecode.unidecode(text)
    tmp = tmp.upper()
    letters = [c for c in tmp if ord(c) >= ord('A') and ord(c) <= ord('Z')]
    clean_text = "".join(letters)
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


def vigenere_crypt(message_, key_):
    message = vigenere_clean(message_)
    key = vigenere_clean(key_)

    codingString = ""
    count = 0

    for c in message :

            codingString += TableVigenere[key[count%len(key)]][ord(c) - ord('A')]
            count += 1

    return codingString


def vigenere_decrypt(message_, key_) :
    message = vigenere_clean(message_)
    key = vigenere_clean(key_)

    decodingString = ""
    count = 0

    for c in message :
        pos = TableVigenere[key[count%len(key)]].find(c)
        pos += ord('A')
        decodingString += chr(pos)
        count += 1

    return decodingString
