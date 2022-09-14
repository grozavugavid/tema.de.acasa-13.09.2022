def fact(x):
    c=1
    for i in range (1,x+1):
    c=c*x
    return c
n=int(input('introdu n' )
m=int(input('introdu m'))
if n<m:
    print('eroare')
    else:
        print('c=', fact(n)/fact(m)*fact(m-n))
