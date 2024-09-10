comeco = int(input('Digite um numero: '))
fim = int(input('Digite mais um numero: '))
soma = 0

for numero in range(comeco, fim+1):
    if numero % 2 == 0:
           soma += numero
    
else:
     if soma == 0:
                print('nao ha numeros pares no intervalo') 
     else:
            print(soma)       
         
      


   




        