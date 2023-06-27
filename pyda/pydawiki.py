import wikipedia

while True:

    input = (input("question: "))

    wikipedia.set_lang("es")

    print (wikipedia.summary(input,sentences=2))

