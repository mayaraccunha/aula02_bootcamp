CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario = input("Digite o seu nome: ")
    
    # Verifica se o nome está vazio
    if len(nome_usuario) == 0:
        raise ValueError("O nome não pode estar vazio.")
    
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome_usuario):
        raise ValueError("O nome não deve conter números.")
    
    # Verifica se só tem espaços
    elif nome_usuario.isspace():
        raise ValueError("Você só digitou espaço.")
        
    else:
        print("Nome válido:", nome_usuario)

except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
        exit()
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
        exit()
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

# Lógica de cálculo
bonus_final = bonus_recebido * 1.2 
kpi = (salario + bonus_final) / 1000 

# Imprime as informações
print(f"Seu KPI é: {kpi:.2f}")
# ATENÇÃO: Aqui faltava um parênteses no final
print(f"{nome_usuario}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")