import wolframalpha

input = (input("question: "))
app_id="2YYW3A-A7J59G3PU6"
client= wolframalpha.Client(app_id)

res=client.query(input)
answer= next(res.results).text

print(answer)