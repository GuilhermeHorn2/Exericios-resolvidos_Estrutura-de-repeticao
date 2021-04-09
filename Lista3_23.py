n = int(input(':'))

div = 0

r = []
for i in range(n +1):
    if i % 2 == 1 and i != 2 and i !=1:
        r.append(i)
        div += 1
    if i == 2:
        r.append(i)
    else:
        div += 1
print(r)
print(div)

