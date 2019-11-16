l = []
for i in range(2, 10 ** 7):
    for j in range(2, i):
        if i % j == 0: break
    else: l.append(i)
print(f'{l}')
with  open("file.txt",'w',encoding = 'cp1252') as f:
    f.write(str(l))
