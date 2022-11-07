

import time
start = time.time() ## точка отсчета времени

from math import sqrt

n = int(input("n="))
lst=[]
for i in range(2, n):
    if (i > 10) :
        if (i % 2 == 0) or (i % 10 == 5) :
            continue
    for j in lst :
        if j > int ( (sqrt ( i ))+1 ) :
            lst.append ( i )
            break
        if (i % j == 0) :
            break
    else :
        lst.append ( i )
print(lst)
end = time.time() - start ## собственно время работы программы



