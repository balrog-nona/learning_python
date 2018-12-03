def censor(text, word):
    znak = "*"
    Word = word.capitalize()
    if word in text or Word in text:
        znak *= len(word)
        text = text.replace(word, znak)
        text = text.replace(Word, znak)
        print(text)

veta = input("Zadej sprostou vetu: ")
slovo = input("Zadej slovo, ktere chces vymazat: ")

censor(veta, slovo)

