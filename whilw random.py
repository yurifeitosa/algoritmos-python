import random

s = 's'

while s in ['S', 's']:
    num = random.randint(1,10)
    print ("O número sorteado foi o: ",num)
    s = input ("Deseja Continuar [s/n] ?")
