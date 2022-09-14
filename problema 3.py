a,b=int(input('Introdu prima fractie: ')),int(input())
c,d=int(input('Introdu a doua fractie: ')),int(input())
def adunare(a,b,c,d):
    i=((a*m)+(b*c))/(b*d)
    return (i)
print(a,'/',b,'+',c,'/',d,'=',adunare(a,b,c,d),sep='')

def inmultire(a,b,c,d):
    i=(a*c)/(b*d)
    return(i)
print(a,'/',b,'*',c,'/',d,'=',inmultire(a,b,c,d),sep='')