#importa bibliotecas p/ verificação de cep e idade
import datetime 
import requests
import random
import string
# Dicionário com os vinhos disponíveis e seus preços
vinhos = {
    'cabernet franc': 70,
    'syrah': 80,
    'grenache': 60,
    'cabernet sauvignon': 100,
    'pinot noir': 120,
    'tinto malbec': 80,
    'tinto merlot': 90,
    'tinto syrah': 100,
    'chardonnay': 80,
    'sauvignon blanc': 70,
    'riesling': 90,
    'pinot grigio': 60
}



carrinho = []  # Lista para armazenar os itens do carrinho
#carronho.pop( [intex] ) -> remove item
#imprime a listas de vinhos
def listar_vinhos():
    print("\nVINHOS DISPONÍVEIS:\n")
    print("\tCATEGORIA: ROSÉS\n")

    for vinho, preco in vinhos.items():

        if vinho in ['cabernet franc', 'syrah', 'grenache']:
            print(f"{vinho} - R${preco}")
    
    print("\n\tCATEGORIA: TINTOS\n")

    for vinho, preco in vinhos.items():
        if vinho in ['cabernet sauvignon', 'pinot noir', 'tinto malbec', 'tinto merlot', 'tinto syrah']:
            print(f"{vinho} - R${preco}")
    print("\n\tCATEGORIA: BRANCOS\n")
    
    for vinho, preco in vinhos.items():
        if vinho in ['chardonnay', 'sauvignon blanc', 'riesling', 'pinot grigio']:
            print(f"{vinho} - R${preco}")

    print('\n')
    comprar_vinhos()


def comprar_vinhos():
    #tratamento de dados
    try:
        vinho = input("Digite o nome do vinho que deseja comprar: \t")
        vinho = vinho.lower()
        quantidade = int(input("Digite a quantidade desejada: \t"))
        if quantidade <= 0:
            print("Erro: Valor inválido no arquivo!")
        else:
            if vinho in vinhos:
                preco_total = vinhos[vinho] * quantidade
                carrinho.append((vinho, quantidade, preco_total))
                print('________________________________________')
                print("Item adicionado ao carrinho com sucesso!")
                print('________________________________________')
            else:
                print("Vinho indisponível.")
    except ValueError:
        print("Erro: Valor inválido para quantidade. Certifique-se de inserir um número inteiro.")
        comprar_vinhos()
    opcaos()

    


def visualizar_carrinho():

    print('\n')
    print('_____________________')
    print("CARRINHO DE COMPRAS:")
    print('_____________________')
    print('\n')
    

    total_compra = 0
    for item in carrinho:
        vinho, quantidade, preco_total = item
        print(f"{vinho} - Quantidade: {quantidade} - Preço total: R${preco_total}")
        total_compra += preco_total

    if len(carrinho) > 0:
        #aplicar_desconto(total_compra)
        """ 
        • Na compra de 3 garrafas,o cliente receberá um desconto de 10%. 
        • Na compra de 4 garrafas,o cliente receberá um desconto de 20%.
        • Na compra de 5 ou mais garrafas,o cliente receberá um descontode 30%.

        """ 
        q = 0
        for x in carrinho:
            q += x[1]
        if q >= 5:
          total_compra = total_compra - (total_compra * 0.3) #30%
        elif q == 4:
            total_compra *= 0.8 #20%
        elif q == 3:
            total_compra *= 0.9 #10%
            
        print(f"Valor total com desconto: R${total_compra:.2f} \n\n")
    opcao = int(input('Selecione uma opção: \n \t (1)finalizar compra \t(2)apagar carrinho \nOpção: '))

    # Verifica a opção escolhida
    match opcao:
        case 1:
            finalizar_compra(total_compra)
        case 2:
            carrinho.clear()
            print('_________________')
            print('CARRINHO APAGADO')
            print('_________________')

            opcaos()
        case _:
            print('___________opção invalida___________')
            visualizar_carrinho()

#busca pelo cep e imprime endereço        
def verificar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        endereco = response.json()
        print("CEP encontrado:")
        print(f"CEP: {endereco['cep']}")
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Complemento: {endereco['complemento']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
    else:
        print("CEP não encontrado.")

def verificar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (caso contrário, o CPF é inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11 % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11 % 10

    # Verifica se os dígitos verificadores são iguais aos dígitos do CPF
    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        return False

    # CPF válido
    return True


def gerar_codigo_pix():
    # Gera um código de 10 caracteres alfanuméricos para o Pix
    codigo = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return codigo

def gerar_codigo_boleto():
    # Gera um código de 20 dígitos numéricos para o boleto
    codigo = ''.join(random.choices(string.digits, k=20))
    return codigo

def gerar_codigo_debito():
    # Gera um código de 8 dígitos numéricos para o débito
    codigo = ''.join(random.choices(string.digits, k=8))
    return codigo

def gerar_codigo_credito():
    # Gera um código de 16 dígitos numéricos para o crédito
    codigo = ''.join(random.choices(string.digits, k=16))
    return codigo

def gerar_codigo_pagamento():
    print("Escolha a forma de pagamento:")
    print("1. Pix")
    print("2. Boleto")
    print("3. Débito")
    print("4. Crédito")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        return gerar_codigo_pix()
    elif opcao == 2:
        return gerar_codigo_boleto()
    elif opcao == 3:
        return gerar_codigo_debito()
    elif opcao == 4:
        return gerar_codigo_credito()
    else:
        print("Opção inválida. Tente novamente.")
        return gerar_codigo_pagamento()


# def aplicar_desconto(total_compra):
def finalizar_compra(total_compras):
    print('_____________________')
    print("  FINALIZAR COMPRA:")
    print('_____________________')
    print('\n') 
    nome = input("Digite o nome completo: ")
    email = input("Digite o email: ")
    if '@gmail.com' in email:
      print("Endereço de e-mail válido!")
    else:
      print("Endereço de e-mail inválido!")

    cpf = input("Digite o CPF a ser verificado: ")

    if verificar_cpf(cpf):
        print("CPF válido.")
    else:
        print("CPF inválido.")
    
    data_nascimento_str = input("Digite sua data de nascimento (formato: DD-MM-AAAA): ")
    cep = input("Digite o seu cep: ")
    verificar_cep(cep)
    
    data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d-%m-%Y").date()
    data_18_anos_atras = datetime.date(2005, 1, 1)
    
    if data_nascimento <= data_18_anos_atras:
        print('__________________')
        print('COMPRA AUTORIZADA!')
        print('__________________')
        print('\n')
        print('______________________________________________________')
        codigo_pagamento = gerar_codigo_pagamento()
        print("Código de pagamento gerado: \t", codigo_pagamento)
        print("Valor total do carrinho: R${:.2f}".format(total_compras))
        print('______________________________________________________')
        opcao_um = int(input('Selecione uma opção: \n \t (1)Pagamento efetuado  \t(2)Comprar novamente \nOpcao:'))
        print('\n')
        # Verifica a opção ecolhida
        match opcao_um:
            case 2:
                listar_vinhos()
            case 1: 
                print('\n....Pagamento efeituado........')
                print('\n....FINALIZADO........')
            case _:                 # default
                print('Opção Inválida')
    else:
        print('\n')
        print('_____________________')
        print('  COMPRA CANCELADA!')
        print('   MENOR DE IDADE ')
        print('_____________________')
        print('\n')
        opcao_um = int(input('Selecione uma opção: \n \t (1)Voltar a compras  \t(2)Fechar programa \nOpcao:'))
        print('\n')
        # Verifica a opção ecolhida
        match opcao_um:
            case 1:
                listar_vinhos()
            case 2: 
                print('\n....Programa finalizado')
            case _:                 # default
                print('Opção Inválida')

    
def opcaos():
    print('\n')
    opcao = int(input('Selecione uma opção: \n \t (1)continuar comprando \t(2)visualizar carrinho \nOpcao:'))
    print('\n')
    # Verifica a opção ecolhida
    match opcao:
        case 1:
            listar_vinhos()
        case 2: 
            visualizar_carrinho()
        case _:                 # default
            print('Opção Inválida')

    
print('\n\tSeja bem vindo a VINHERIA AGNELLO\n')
listar_vinhos()
