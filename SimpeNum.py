

import time
start = time.time() ## точка отсчета времени

n = int(input("n="))
lst=[]
for i in range(2, n):
    # пробегаем по списку (lst) простых чисел
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print (lst)
end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени