"""5x5 için yapılmış olup diğer nxn'lik bir matris için n kadar for yazılması gerekmektedir.
Fikir olması için eklenmiştir."""
boyut = int(input("Boyut kaç olsun: "))
x=1
a=0
b=boyut*x
while(a<boyut):
    for i in range(x,b+x):
        print(i, end = " ")

    print(" ")
    
    a = a+1
    for j in range(x+1,(boyut*2)+1,2):

        print(j, end = " ") 

    print(" ")

    for i in range(x+2,(boyut*3)+1,3):
        print(i, end = " ")

    print(" ")

    for j in range(x+3,(boyut*4)+1,4):
        print(j, end = " ") 

    print(" ")

    for j in range(x+4,(boyut*5)+1,5):
        print(j, end = " ") 
        
    print(" ")
