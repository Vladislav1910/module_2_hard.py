end = 21
for n in range(3, end):
    result = str()
    for i in range(1, end):
        for j in range(i+1, end):
           if n % (i + j) == 0:
               result += f"{i}{j}"
    print(f'{n} - {result}')

