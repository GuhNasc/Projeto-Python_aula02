# DESAFIOS 

################################ INT ###################################################

# 1 Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#valor1 = int(input("Digite o valor1: "))
#valor2 = int(input("Digite o valor2: "))
#
#resultado = valor1 + valor2
#print(f'A soma dos dois valores é: {resultado}')
#########

# 2 Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5

#numero_usuario = int(input("Digite um valor numério: "))
#
#resto = numero_usuario % 5
#
#print(f"O resto da divisão é: {resto}")

# 3 Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#valor1  = int(input("Digite o valor1: "))
#valor2  = int(input("Digite o valor2: "))
#
#resultado = valor1 * valor2
#
#print(f'O resutado da multiplicação é: {resultado}')

# 4 Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#valor1  = int(input("Digite o valor1: "))
#valor2  = int(input("Digite o valor2: "))
#
#resultado = valor1 // valor2
#
#print(f'A divisão inteira é: {resultado}')

# 5 Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#valor = int(input("Digite um valor: "))
#
#resultado = valor ** 2
#
#print(f"O Valor final é : {resultado}")

# Escreva um programa que receba dois números flutuantes e realize sua adição.


###################################### FLOAT #####################################


# 6 Escreva um programa que receba dois números flutuantes e realize sua adição.
#valor1 = float(input("Digite o primeiro valor: "))
#valor2 = float(input("Digite o segundo valor: "))
#
#
#resultado = valor1 + valor2
#
#print(f'o resultado é {resultado}')

# 7 Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#valor1 = float(input("Digite o primeiro valor: "))
#valor2 = float(input("Digite o segundo valor: "))
#
#
#resultado = (valor1 + valor2) / 2
#
#print(f'o resultado é {resultado}')


# 8 Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#base = float(input("Digite a base: "))
#expoente = float(input("Digite o expoente: "))
#
#potencia = base ** expoente
#
#print(f'A potencia é {potencia}')

# 9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# FORMULA PARA CONVERSAO: ( °C × 9/5) + 32 = °F

#celsius = float(input("Digite o grau em °C: "))
#
#fahre = (celsius * 9/5) + 32
#
#print(f"{celsius} em Fahrenheit são: {fahre}")



# 10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# FORMULA A = π*r²

#raio = float(input("Digite o raio do circulo: "))
#
#area = 3,14159 * raio ** 2
#
#print(f"A area do circulo é igual: {area}")


################################## STRING ##########################################
# 11 Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#texto = str(input("Digite seu texto:"))
#
#texto_M = texto.upper()
#
#print(f"O seu texto de forma maiuscula: {texto_M}")

# 12 Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#nome = str(input("Digite seu nome: "))
#
#nome_completo = nome.lower()
#
#print(f"Nome minusculo: {nome_completo}")

# 13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#frase = str(input("Digite seu frase: "))
#
#frase_completa = frase.strip()
#
#print(f"Frase sem espaços em branco: {frase_completa}")

# 14 Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente

#data = input("Digite uma data no formato dd/mm/aaaa: ")
#dia,mes,ano = data.split("/")
#
#print("Dia:", dia)
#print("Mês:", mes)
#print("Ano:", ano)


# 15 Escreva um programa que concatene duas strings fornecidas pelo usuário.
parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")

texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)