import wolframalpha
import wikipedia

while True:
    input = input("q: ")

    try:
        #wolframalpha
        app_id="2YYW3A-A7J59G3PU6"
        client= wolframalpha.Client(app_id)

        res=client.query(input)
        answer= next(res.results).text

        print(answer)
    except:

        print (wikipedia.summary(input,sentences=2))