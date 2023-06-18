meme_dictionary = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dictionary.keys():
    degisken = meme_dictionary[word]
    print(degisken)
else:
   print("Bu kelimeyi henüz eklemedik.")
