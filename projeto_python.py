#INFORMAÇÕES DO USUÁRIO
def inserir_nome():
    '''
    Pergunta e armazena o nome de usuário, retornando pra variável 'nome'
    '''
    nome = input('Digite seu nome\n: ')
    return nome

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
    if jardim == 'n' or moradia == 'apartamento':
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

#FUNÇÕES PARA HORTA
def lista_horta():
    h_urb_trad = '----------------------------------------------------\n*HORTA TRADICIONAL*\nEste tipo de cultivo é o que se realiza na terra, o de sempre. Destina-se um espaço do jardim e como substrato usa-se o do próprio terreno'
    h_urb_vert = '-----------------------------------------------------\n*HORTA VERTICAL*\nconstrução realizada de forma perpendicular ao solo. Seu objetivo principal é o de *otimizar o espaço* para plantar frutas, hortaliças, plantas aromáticas ou espécies decorativas.'
    h_urb_contentor = '----------------------------------------------------\n*HORTA COM CONTENTORES*\nEste tipo de cultivo é onde o meio utilizado é um recipiente, vaso, floreiras ou outro tipo de elemento. Ideais para aproveitar o espaço, já que pode escolher o contentor que melhor se adapte ao lugar disponível.'
    hortas = [h_urb_trad, h_urb_vert, h_urb_contentor]
    return hortas

def tipo_horta(nome, moradia, jardim, espaco):
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
    while True:
        if (espaco == 'sim' or jardim == 's') and luz == 'sim':    
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Pimentão\n-> Tomate\n-> Alface\n-> Berinjela\n-> Morango\n-> Abóbora\nDestas opções, digite o número de sementes que você quer cultivar\n(ATÉ 6 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=6:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')

        elif (espaco == 'sim' or jardim == 's') and luz == 'não':
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Alface\n-> Pimenta\n-> Beterraba\n-> Boldo\n-> Rabanete\n-> Cebolinha\nDestas opções, digite o número de sementes que você quer cultivar\n(ATÉ 6 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=6:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')

        elif espaco == 'não' and luz == 'sim':    
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Pimentão\n-> Tomate\n-> Alface\n-> Berinjela\n-> Morango\n-> Abóbora\nDestas opções, digite o número de sementes que você quer cultivar\n(ATÉ 3 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=3:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')

        else: 
            qtd_sementes = int(input(f'----------------------------------------------------\n{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n-> Alface\n-> Pimenta\n-> Beterraba\n-> Boldo\n-> Rabanete\n-> Cebolinha\nDestas opções, digite o número de sementes que você quer cultivar\n(ATÉ 3 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=3:
                break
            else:
                print('----------------------------------------------------\nQuantidade de sementes inválida')
    return qtd_sementes

def lista_sementes(qtd_sementes):
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
    for i in range(len(sementes)):
        if sementes[i] == (sementes[0] and sementes[-1]):
            print('Sementes escolhidas:', sementes[i], end ='.')
        elif sementes[i] == sementes[0]:
            print('Sementes escolhidas:', sementes[i], end =', ')
        elif sementes[i] == sementes[-1]:
            print(sementes[i], end ='.')
        else:
            print(sementes[i], end = ', ')

#EXIBIR INFORMAÇÕES DO USUÁRIO
def exibir_info(nome, moradia, luz, jardim, espaco, horta, sementes):
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
while True:
    nome = inserir_nome()
    moradia = inserir_moradia()
    jardim = jardim_casa(moradia)
    luz = luz_solar(nome)
    espaco = espaco_moradia(moradia, jardim)
    hortas = lista_horta()
    horta = tipo_horta(nome, moradia, jardim, espaco)
    menu = des_horta(nome, horta, hortas)
    qtd_semente = qtd_sementes(espaco, luz, jardim, nome)
    sementes = lista_sementes(qtd_semente)
    exibir_infos = exibir_info(nome, moradia, luz, jardim, espaco, horta, sementes)
    refazer_operacao = input('\n----------------------------------------------------\nDeseja refazer a operação?\n[s]im/[n]ão\n: ')
    match refazer_operacao:
        case 'n':
            print('Operação finalizada, até mais!')
            break
        case 's':
            print('*----NOVA OPERAÇÃO----*')
        case _: 
            print('Resposta inválida')