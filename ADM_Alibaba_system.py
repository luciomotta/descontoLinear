import time


def login():
    print('''    ALIBABA DISTRI LOUNG
                [1] Cadastrar
                [2] Login
                [3] Sair
            ''')
    opcao = int(input("Digite sua opção: "))
    while opcao != 0:

        if opcao == 2:
            arq = open('registradosSenhas.txt')  # abrindo no modo de leitura
            print('Efetue o seu login')

            nome_login = input('Digite o seu nome de usuario: ')

            registrados = arq.readlines()
            if nome_login + '\n' in registrados:
                print(1 * "\n")
                print('Bem vindo, {}!'.format(nome_login))
                print(1 * "\n")
                arq.close()

                calculo()
            else:
                print(100 * "\n")
                print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
            return login()

        elif opcao == 3:
            input("Pressione <enter> para encerrar!")
            exit()


        elif opcao == 10:
            arq = open('registradosSenhas.txt', 'a')
            print('Olá, aqui você pode adicionar uma nova conta!')
            nome_usuario = int(input('Digite o nome de usuário: '))

            arq.write('{}\n'.format(nome_usuario))
            '''
            Adição da constante \n new line
            Uma vez que write não o adiciona automaticamente
            '''

            print('Cadastro realizado com sucesso!\n')
            return login()
            arq.close()  # O arquivo é fechado do modo de adição para ser aberto
            # posteriormente no modo de leitura

        else:
            print(100 * "\n")
            print(50 * '-')
            print("                 Opção erra")
            print(50 * "-")
            return login()


def calculo():
    repetir = True
    while repetir:

        valor = float(input("Digite o valor do Produto: "))
        percent = float(valor / 100)
        desc = float(input("Valor R$ de desconto: "))
        try:
            result = desc / percent
        except ZeroDivisionError:
            result = 0

        print("O valor de desconto e:{}%".format(result))

        resposta = input('Deseja executar novamente? (s/n)')
        if resposta[0].lower() == 'n':
            input("Pressione <enter> para encerrar!")
            repetir = False


print(50 * '*')
print("           Bem vindo sistema Alibaba                 ")
print(50 * '*')

login()
calculo()
