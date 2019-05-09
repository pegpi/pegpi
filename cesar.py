def encrypt(message, decalage):
  message_decale_lettres=[]
  for c in message.upper(): #je met en majuscule
      if ord(c)==32: #espace dans tableau ASCII
          message_decale_lettres.append(c)
      elif 48<=ord(c)<=57:   #pour les chiffres
          message_decale_lettres.append(c)
      elif 65<=ord(c)<=90:  #alphabet en majuscule
          i = 65 + ((ord(c) - 65 + decalage) %26) #je transorme en lettres en nombres et fait modulo de 26 après avoir ajouter le décalage
          message_decale_lettres.append(chr(i)) # je retransforme en lettres
      else:
         message_decale_lettres.append(chr(32)) #au cas où il y a des caractères spéciaux, met un espace
  return''.join(message_decale_lettres) #colle les mot pour former une phrase

if __name__ == '__main__':
    message = input("Entrez votre message sans accents: ")
    decalage = int(input("Entrez votre décalage (négatif pour décoder et positif pour coder): "))

    print(encrypt(message, decalage))