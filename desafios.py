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
#parte1 = input("Digite a primeira parte do texto: ")
#parte2 = input("Digite a segunda parte do texto: ")
#
#texto_concatenado = parte1 + parte2
#print("Texto concatenado:", texto_concatenado)



###############################################################################################
###############################################################################################


# EXERCICIOS DE TRY EXECPT

# 1 Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

#try:
#    celsius = float(input("Digite o grau em °C: "))
#
#    fahre = (celsius * 9/5) + 32
#
#    print(f"{celsius} em Fahrenheit são: {fahre}")
#except ValueError:
#    print("Digite um valor numerico")

# EXERCICIO FINAL

# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")