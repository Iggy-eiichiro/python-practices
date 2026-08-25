words = {'apple':10,'orange':5,'banana':12}
results = dict(sorted(words.items(), key=lambda x: x[1]))#words.items() is a list of tuples, for example: [('apple', 10), ('orange', 5), ('banana', 12)]. key=lambda x: x[1] of x is the tuple(apple), x[1] is the value of the tuple(10).
print(results)