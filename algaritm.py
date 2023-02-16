



def addNums(a,b):
    summa = a + b
    return summa



def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
print(getLargest(698654312695431,5458786854158,654898469879))
                


def faktorial(N):
    i=1
    fakt=1
    while i!=N+1:
        fakt = fakt*i        
        i += 1
    return fakt
 
print(faktorial(5))