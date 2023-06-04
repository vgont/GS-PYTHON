#INFORMAÇÕES DO USUÁRIO

def inserir_nome():
    print('Area do cadastro')
    '''
    Pergunta e armazena o nome de usuário, retornando pra variável 'nome'
    '''
    nome = input('Digite seu nome\n: ')
    return nome

def cadastrar_email():
    '''
    Cadastra um email do usuário (só será válido caso tiver @ e .com)
    '''
    while True:
        email = input('Digite um E-mail\n:')
        arroba = '@'
        ponto_com = '.com'
        if arroba  and ponto_com not in email:
            print('O E-mail não é válido! Tente novamente')
        else:
            break
    return email

def cadastrar_senha():
    '''
    Cadastra uma senha criada pelo usuário
    '''
    senha = input('Digite uma senha\n:')
    return senha


def fazer_login_email(email):
    '''
    Valida o email do usuário, caso exceder o número de tentativas, redefine o email do usuário
    '''
    print('Area de login')
    while True:
        login_email = input('Digite seu E-mail\n:')
        if login_email != email:
            for i in range(4):
                login_email = input('E-mail incorreto!\nDigite novamente\n:')
                if login_email == email:
                    break 
                if i == 3:
                    while True:
                        email = input('Números de tentativas excedidas! Redefina o seu E-mail\n:')
                        arroba = '@'
                        ponto_com = '.com'
                        if arroba  and ponto_com not in email:
                            print('O E-mail não é válido! Tente Novamente')
                        else:
                            break
        else:
            break
    return login_email

def fazer_login_senha(senha, nome):
    '''
    Valida a senha do usuário, caso exceder o número de tentativas, redefine a senha do usuário
    '''
    while True:
        login_senha = input('Digite sua senha\n:')
        if login_senha != senha:
            for i in range(4):
                login_senha = input('Senha incorreta!\nDigite novamente\n:')
                if login_senha == senha:
                    break
                if i == 3:
                    senha = input('Números de tentativas excedidas! Redefina sua senha\n:')  
        else:
            break 
    print(f'Bem-vindo, {nome}! Vamos começar com algumas informações suas.')
    return login_senha

def inserir_moradia():
    '''
    Pergunta e armazena o tipo de moradia do usuário, retornando pra variável 'moradia'
    '''
    while True:
        moradia = input('----------------------------------------------------\nVocê mora em [a]partamento ou [c]asa?\n: ')
        match moradia:
            case 'a':
                moradia = 'apartamento'
                break
            case 'c':
                moradia = 'casa'
                break 
            case _:
                print('----------------------------------------------------\nOpção inválida')           
    return moradia

def luz_solar(nome):
    '''
    Pergunta e armazena se o usuário possui bastante disponibilidade à luz solar // Armazena o 'sim' ou o 'não' do usuário
    '''
    while True:
        luz = input(f'----------------------------------------------------\n{nome}, onde você mora tem bastante disponibilidade de luz solar?\n[s]im/[n]ão\n:')
        match luz:
            case 's' | 'n' :
                if luz == 's':
                    luz = 'sim'
                else:
                    luz ='não'
                break
            case _:
                print('----------------------------------------------------\nOpção inválida!')
    return luz

def jardim_casa(moradia):
    '''
    Pergunta e armazena se o usuário possui jardim // APENAS SE A MORADIA DO USUÁRIO FOR 'CASA'
    '''
    if moradia == 'casa':
        while True:
            jardim = input('----------------------------------------------------\nSua casa possui um jardim?\n[s]im/[n]ão\n:')
            match jardim:
                case 's' | 'n':
                    break
                case _:
                    print('----------------------------------------------------\nOpção inválida')
        return jardim
    
def espaco_moradia(moradia, jardim):
    '''
    Pergunta e armazena se o usuário tem POUCO ou MUITO espaço em sua moradia // APENAS SE NÃO TIVER JARDIM
    '''
    if jardim == 'n' or moradia == 'apartamento':
        #IF e ELSE usados apenas para mudar os pronomes das perguntas, se casa então "sua casa" // se apto então "seu apartamento"
        if moradia == 'casa':
            while True:
                    espaco = input(f'----------------------------------------------------\nPossui muito espaço em sua {moradia}?\n[s]im/[n]ão\n:')
                    match espaco:
                        case 's' | 'n':
                            if espaco == 's':
                                espaco = 'sim'
                            else:
                                espaco = 'não'
                            break
                        case _:
                            print('----------------------------------------------------\nOpção inválida')
            return espaco
        else:
            while True:
                    espaco = input(f'----------------------------------------------------\nPossui muito espaço em seu {moradia}?\n[s]im/[n]ão\n:')
                    match espaco:
                        case 's' | 'n':
                            if espaco == 's':
                                espaco = 'sim'
                            else:
                                espaco = 'não'
                            break
                        case _:
                            print('----------------------------------------------------\nOpção inválida')
            return espaco

#FUNÇÕES PARA HORTA
def lista_horta():
    '''
    Lista com descrição dos 3 tipos de hortas possíveis em nosso programa.
    '''
    h_urb_trad = '----------------------------------------------------\n*HORTA TRADICIONAL*\nEste tipo de cultivo é o que se realiza na terra, o de sempre. Destina-se um espaço do jardim e como substrato usa-se o do próprio terreno'
    h_urb_vert = '-----------------------------------------------------\n*HORTA VERTICAL*\nconstrução realizada de forma perpendicular ao solo. Seu objetivo principal é o de *otimizar o espaço* para plantar frutas, hortaliças, plantas aromáticas ou espécies decorativas.'
    h_urb_contentor = '----------------------------------------------------\n*HORTA COM CONTENTORES*\nEste tipo de cultivo é onde o meio utilizado é um recipiente, vaso, floreiras ou outro tipo de elemento. Ideais para aproveitar o espaço, já que pode escolher o contentor que melhor se adapte ao lugar disponível.'
    hortas = [h_urb_trad, h_urb_vert, h_urb_contentor]
    return hortas

def tipo_horta(nome, moradia, jardim, espaco):
    '''
    Define o tipo de horta para o usuário de acordo com as informações MORADIA | JARDIM | ESPACO
    '''
    if (moradia == 'casa' and jardim == 's'):
        horta = 'horta tradicional'
        print(f'----------------------------------------------------\n{nome}, analisando os dados que me forneceu, sugiro a {horta}. Ela é uma ótima opção para casas com jardim.')  
        return horta     
    elif (moradia == 'casa' | 'apartamento') and espaco == 'não':
        horta = 'horta vertical'
        print(f'----------------------------------------------------\n{nome}, analisando os dados que me forneceu, sugiro a {horta}. Ela é a mais adequada quando há pouco espaço.')  
        return horta  
    else:
        horta = 'horta com contentores'
        print(f'----------------------------------------------------\n{nome}, analisando os dados que me forneceu, sugiro a {horta}.')
        return horta
    
def des_horta(nome, horta, hortas):
    '''
    Pergunta ao usuário se ele possui dúvidas sobre o tipo de horta definido pelo sistema 
    -----------------------
    caso SIM: Exibe a descrição da horta em específico
    caso NÃO: Não exibe nada
    '''
    while True:
        escolha = input(f'----------------------------------------------------\n{nome}, você possuí alguma dúvida sobre a {horta}?\n[s]im/[n]ão\n:')
        if escolha == 's':
            if horta == 'horta tradicional':
                print(hortas[0])
            elif horta == 'horta vertical':
                print(hortas[1])
            else:
                print(hortas[2])
            break
        elif escolha == 'n':
            break
        else:
            print('----------------------------------------------------\nOpção inválida!')
    return escolha

#FUNÇÕES PARA SEMENTES
def qtd_sementes(espaco, luz, jardim, nome):
    '''
    Define a quantidade certa de sementes de acordo com a informação ESPACO
    -------
    caso ESPACO = SIM: Usuário pode escolher até 6 sementes das sugeridas;
    caso ESPACO = NÃO: Usuário pode escolher até 3 sementes das sugeridas;
    -------
    Sugere diferentes tipos de sementes de acordo com a informação LUZ SOLAR
    -------
    caso LUZ = SIM: Sementes - Pimentão, Tomate, Alface, Berinjela, Morango, Abóbora;
    caso LUZ = NÃO: Sementes - Alface, Pimenta, Beterraba, Boldo, Rabanete, Cebolinha.
    '''
    while True:
        if (espaco == 'sim' or jardim == 's') and luz == 'sim':    
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Pimentão\n-> Tomate\n-> Alface\n-> Berinjela\n-> Morango\n-> Abóbora\nDestas opções, digite o *NÚMERO* de sementes que você quer cultivar\n(ATÉ 6 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=6:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')

        elif (espaco == 'sim' or jardim == 's') and luz == 'não':
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Alface\n-> Pimenta\n-> Beterraba\n-> Boldo\n-> Rabanete\n-> Cebolinha\nDestas opções, digite o *NÚMERO* de sementes que você quer cultivar\n(ATÉ 6 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=6:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')

        elif espaco == 'não' and luz == 'sim':    
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Pimentão\n-> Tomate\n-> Alface\n-> Berinjela\n-> Morango\n-> Abóbora\nDestas opções, digite o *NÚMERO* de sementes que você quer cultivar\n(ATÉ 3 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=3:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')

        else: 
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Alface\n-> Pimenta\n-> Beterraba\n-> Boldo\n-> Rabanete\n-> Cebolinha\nDestas opções, digite o *NÚMERO* de sementes que você quer cultivar\n(ATÉ 3 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=3:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')
    return qtd_sementes

def lista_sementes(qtd_sementes):
    '''
    Adiciona as sementes escolhidas (caso forem sementes válidas) pelo usuário em uma lista.
    '''
    sementes = []
    cont = 1
    for i in range(qtd_sementes):
        while True:
            semente = input(f'----------------------------------------------------\nDigite a {cont}° semente que você deseja\n: ')
            match semente:
                case 'Pimentão' | 'Tomate' | 'Alface'| 'Berinjela' | 'Morango' | 'Abóbora' | 'Pimenta' | 'Beterraba' | 'Boldo' | 'Rabanete' | 'Cebolinha':
                    break
                case _:
                    print('----------------------------------------------------\nSemente inválida')
        sementes.append(semente)
        cont+=1
    return sementes

def exibir_lista_sementes(sementes):
    '''
    Exibe as sementes escolhidas pelo usuário em ordem
    --------
    EXEMPLO: "Alface, Tomate, Berinjela."
    '''
    for i in range(len(sementes)):
        if (sementes[i] == sementes[0]) and (sementes[i] == sementes[-1]):
            print('Sementes escolhidas:', sementes[i], end ='.')
        elif sementes[i] == sementes[0]:
            print('Sementes escolhidas:', sementes[i], end =', ')
        elif sementes[i] == sementes[-1]:
            print(sementes[i], end ='.')
        else:
            print(sementes[i], end = ', ')

#EXIBIR INFORMAÇÕES DO USUÁRIO
def exibir_info(nome, moradia, luz, jardim, espaco, horta, sementes):
    '''
    Exibe todas as informações, no console, dadas pelo usuário.
    '''
    print('\n-------------------------- *INFORMAÇÕES DO USUÁRIO* --------------------------\n')
    if jardim == 's':
        print(f'Seu nome: {nome}')
        print(f'Moradia: {moradia}')
        print(f'Bastante luz solar disponível?: {luz}')
        print(f'Espaço disponível: Jardim')
        print(f'Horta sugerida: {horta}')
        exibir_lista_sementes(sementes)
    else:
        print(f'Seu nome: {nome}')
        print(f'Moradia: {moradia}')
        print(f'Bastante luz solar disponível?: {luz}')
        print(f'Possui muito espaço?: {espaco}')
        print(f'Horta sugerida: {horta}')
        exibir_lista_sementes(sementes)

#PRINCIPAL

#laço criado para o refazimento da operação (caso o usuáro desejar)
ref = 's'
while ref == 's':
    #Pergunta o nome do usuário
    nome = inserir_nome()
    #Cadastra o email do usuário
    email = cadastrar_email()
    #Cadastra a senha do usuário
    senha = cadastrar_senha()
    #Valida o email do usuario, caso errar 4 vezes, redefine o email
    login_email = fazer_login_email(email) 
    #Valida a senha do usuario, caso errar 4 vezes, redefine a senha
    login_senha = fazer_login_senha(senha, nome)
    #Pergunta o tipo de moradia do usuário
    moradia = inserir_moradia()
    #Pergunta se o usuário possui um jardim *(APENAS PERGUNTA SE O TIPO DE MORADIA FOR CASA)*
    jardim = jardim_casa(moradia)
    #Pergunta se o usuário tem bastante disponibilidade à luz solar
    luz = luz_solar(nome)
    #Pergunta se o usuário possui muito ou pouco espaço em sua moradia *(APENAS PERGUNTA SE O USUÁRIO NÃO POSSUIR UM JARDIM)*
    espaco = espaco_moradia(moradia, jardim)
    #Cria a lista das hortas disponíveis
    hortas = lista_horta()
    #A partir das informações do usuário, determina qual melhor horta se encaixa no perfil dele
    horta = tipo_horta(nome, moradia, jardim, espaco)
    #Pergunta se o usuário possui alguma dúvida sobre a horta determinada para ele
    menu = des_horta(nome, horta, hortas)
    #Exibe as sementes disponíveis de acordo com as informações do usuário e pergunta a quantidade de sementes q ele deseja (de acordo com as proporções)
    qtd_semente = qtd_sementes(espaco, luz, jardim, nome)
    #Armazena as sementes escolhidas em uma lista
    sementes = lista_sementes(qtd_semente)
    #Exibe as informações do usuário
    exibir_infos = exibir_info(nome, moradia, luz, jardim, espaco, horta, sementes)
    #Pergunta se o usuário deseja refazer a operação
    while True:
        refazer_operacao = input('\n----------------------------------------------------\nDeseja refazer a operação?\n[s]im/[n]ão\n: ')
        match refazer_operacao:
            case 'n':
                print('Operação finalizada, até mais!')
                ref = 'n'
                break
            case 's':
                print('*----NOVA OPERAÇÃO----*')
                break
            case _: 
                print('Resposta inválida')