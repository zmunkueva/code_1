arr = []
n = 10 ** 7
for i in range(n):
    arr.append(i)
arr[1] = 0
i = 2
while i < n:
    if arr[i] != 0:
        j = 2 * i
        while j < n:
            arr[j] = 0
            j = j + i
    i += 1
l = []
for i in arr:
    if arr[i] != 0:
        l.append(arr[i])
print(l)
with open("file.txt", 'w', encoding = 'cp1252') as f:
    f.write(str(l))
