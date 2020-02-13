import math
a= float(input("Digite a:"))
b= float(input("Digite b:"))
c= float(input("Digite c:"))
delta=(b**2)-(4*a*c)
print ("O valor de Delta é %2.0f" % delta)
if delta<0 :
        print ("Raiz negativa, não pode ser extraida.")
        exit()
else :
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
print ("X1 = %s \nX2 = " % x1, x2)
