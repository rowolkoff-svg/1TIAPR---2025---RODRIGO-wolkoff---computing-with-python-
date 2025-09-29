#EXERCICIOS CHECKPOINT 1 -  COMPUTINGG WITH PYTHON!




#EX1 – NUMERO NEGATIVO  OU POSITIVO OU ZERO 

# pede um número e diz se é positivo, negativo ou zero
num = int(input("Digite um número: "))

if num > 0:
    print("numero positivo")
elif num < 0:
    print("numero negativo")
else:
    print("é zero")  # talvez colocar "Zero" ou "é zero" 






#EX2 – NUMERO IMPAR OU PAR 



n = int(input("digite um número: "))

if n % 2 == 0:
    print("é par")
else:
    print("é impar")  


#EX3 –  MAIOR OU MENOR DE IDADE 



idade = int(input("Qual sua idade? "))

if idade >= 18:
    print("vc é maior de idade")
else:
    print("vc ainda é menor")  

   



#EX4 – NOTAS 


nota = float(input("Digite a nota (0-10): "))

if nota >= 6:
    print("passou")
else:
    print("reprovou") 




#EX5 –  NUMERO COMPARADO 

n1 = int(input("primeiro numero: "))
n2 = int(input("segundo numero: "))

if n1 > n2:
    print("primeiro maior")
elif n2 > n1:
    print("segundo maior")
else:
    print("iguais")  


#EX6 - DESCONTO 

preco = float(input("valor do produto: "))

if preco > 100:
    preco = preco - (preco * 0.1)  # 10% desconto
    print("com desconto:", preco)
else:
    print("sem desconto:", preco)




#EX7 – LOGIN 

user = input("usuario: ")
senha = input("senha: ")

if user == "admin" and senha == "1234":
    print("ok acesso liberado")
else:
    print("acesso negado")  


#EX8 –  MULTIPLOS DE 5 

num = int(input("digite um numero: "))

if num % 2 == 0:
    print("par")
elif num % 5 == 0:
    print("multiplo de 5") 
else:
    print("outro")  










#EX9 –  TERMOMETRO 

temp = float(input("digite a temperatura: "))

if temp < 0:
    print("ta congelando")
elif temp <= 30:
    print("agradavel")
else:
    print("quente demais") 







#EX10 – CALCULADORA 

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
op = input("operação (+ - * /): ")

if op == "+":
    print("resultado:", n1+n2)
elif op == "-":
    print("resultado:", n1-n2)
elif op == "*":
    print("resultado:", n1*n2)
elif op == "/":
    if n2 == 0:
        print("erro, divisao por zero")
    else:
        print("resultado:", n1/n2)
else:
    print("operação invalida")  