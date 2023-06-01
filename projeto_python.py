#inicio do projeto
def inserir_nome():
    '''
    Pergunta e armazena o nome de usuário, retornando pra variável 'nome'
    '''
    nome = input('Digite seu nome\n: ')
    return nome

def inserir_onde_mora():
    '''
    Pergunta e armazena o tipo de moradia do usuário, retornando pra variável 'moradia'
    '''
    while True:
        moradia = input('Você more em [a]partamento ou [c]asa?\n: ')
        match moradia:
            case 'a':
                moradia = 'apartamento'
                break
            case 'c':
                moradia = 'casa'
                break 
            case _:
                print('Opção inválida')           
    return moradia

def des_horta():
    h_urb_trad = 'Este tipo de cultivo é o que se realiza na terra, o de sempre. Destina-se um espaço do jardim e como substrato usa-se o do próprio terreno'
    h_urb_vert = 'construção realizada de forma perpendicular ao solo. Seu objetivo principal é o de *otimizar o espaço* para plantar frutas, hortaliças, plantas aromáticas ou espécies decorativas.'
    h_urb_contentor = 'Este tipo de cultivo é onde o meio utilizado é um recipiente, vaso, floreiras ou outro tipo de elemento. Ideais para aproveitar o espaço, já que pode escolher o contentor que melhor se adapte ao lugar disponível.'
    hortas = [h_urb_trad, h_urb_vert, h_urb_contentor]
    return hortas

def luz_solar(nome):
    while True:
        luz = input(f'{nome}, onde você mora tem bastante disponibilidade de luz solar? [s]im/[n]ão\n:')
        match luz:
            case 's' | 'n' :
                break
            case _:
                print('Opção inválida!')
    return luz

def jardim_casa(moradia):
    if moradia == 'casa':
        while True:
            jardim = input('Sua casa possui um jardim? [s]im/[n]ão\n:')
            match jardim:
                case 's' | 'n':
                    break
                case _:
                    print('Opção inválida')
        return jardim
    
def espaco_moradia(moradia, jardim):
    if jardim == 'n' or moradia == 'apartamento':
        if moradia == 'casa':
            while True:
                    espaco = input(f'Possui muito espaço em sua {moradia}? [s]im/[n]ão\n:')
                    match espaco:
                        case 's' | 'n':
                            break
                        case _:
                            print('Opção inválida')
        else:
            while True:
                    espaco = input(f'Possui muito espaço em seu {moradia}? [s]im/[n]ão\n:')
                    match espaco:
                        case 's' | 'n':
                            break
                        case _:
                            print('Opção inválida')
            return espaco

def qtd_sementes(espaco, luz, nome):
    while True:
        if espaco == 's' and luz == 's':    
            qtd_sementes = int(input(f'{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n -> Pimentão\n-> Tomate\n-> Alface\n-> Berinjela\n-> Morango\n-> Abóbora\nDestas opções, digite o número de sementes que você quer cultivar (ATÉ 6 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=6:
                break
            else:
                print('Quantidade de sementes inválida')

        elif espaco =='s' and luz == 'n':
            qtd_sementes = int(input(f'{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n -> Alface\n-> Pimenta\n-> Beterraba\n-> Boldo\n-> Rabanete\n-> Cebolinha\nDestas opções, digite o número de sementes que você quer cultivar (ATÉ 6 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=6:
                break
            else:
                print('Quantidade de sementes inválida')

        elif espaco == 'n' and luz == 's':    
            qtd_sementes = int(input(f'{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n -> Pimentão\n-> Tomate\n-> Alface\n-> Berinjela\n-> Morango\n-> Abóbora\nDestas opções, digite o número de sementes que você quer cultivar (ATÉ 3 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=3:
                break
            else:
                print('Quantidade de sementes inválida')

        else: 
            qtd_sementes = int(input(f'{nome}, de acordo com seus dados, sugiro cultivar estas sementes: \n -> Alface\n-> Pimenta\n-> Beterraba\n-> Boldo\n-> Rabanete\n-> Cebolinha\nDestas opções, digite o número de sementes que você quer cultivar (ATÉ 3 SEMENTES)\n:'))
            if qtd_sementes >= 1 and qtd_sementes <=3:
                break
            else:
                print('Quantidade de sementes inválida')
    return qtd_sementes

def lista_semente(qtd_sementes):
    sementes = []
    cont = 1
    for i in range(qtd_sementes):
        while True:
            semente = input(f'Digite a {cont}° semente que você deseja\n: ')
            match semente:
                case 'Pimentão' | 'Tomate' | 'Alface'| 'Berinjela' | 'Morango' | 'Abóbora' | 'Pimenta' | 'Beterraba' | 'Boldo' | 'Rabanete' | 'Cebolinha':
                    break
                case _:
                    print('Semente inválida')
        sementes.append(semente)
        cont+=1
    return sementes

def horta_trad(nome, moradia, jardim, luz):
    if (moradia == 'casa' and jardim == 's'):
        horta == 'horta tradicional'
        print(f'{nome}, analisando os dados que me forneceu, sugiro a {horta}. Ela é uma ótima opção para casas com jardim.')
        return horta
                
    
def horta_vert(moradia, espaco, nome):
    if (moradia == 'casa' or  moradia == 'apartamento') and espaco == 'n':
        horta == 'horta vertical'
        print(f'{nome}, analisando os dados que me forneceu, sugiro a {horta}. Ela é a mais adequada quando há pouco espaço.')
        return horta
    
def horta_contentor(moradia, nome, espaco):
    if (moradia == 'casa' or moradia =='apartamento') and espaco == 's':
        horta == 'horta tradicional'
        print(f'{nome}, analisando os dados que me forneceu, sugiro a {horta}.') 
        return horta

def menu_horta(nome, horta, hortas):
    while True:
        escolha = input(f'{nome}, você possuí alguma dúvida sobre a {horta}? s/n')
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
            print('Opção inválida!')
    return escolha
    
    
#principal
nome = inserir_nome()
moradia = inserir_onde_mora()
jardim = jardim_casa(moradia)
luz = luz_solar(nome)
espaco = espaco_moradia(moradia, jardim)
hortas = des_horta()
menu = menu_horta(nome, moradia, hortas)
tradicional = horta_trad(nome, moradia, jardim, luz)
vertical = horta_vert(moradia, espaco, nome)
contentor = horta_contentor(moradia, nome, espaco)
                


    


