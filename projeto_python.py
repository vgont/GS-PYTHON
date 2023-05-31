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
            case 'a' | 'c':
                if moradia == 'a':
                    moradia = 'apartamento'
                if moradia == 'c':
                    moradia = 'casa'
                break
            case _:
                print('Opção inválida')
    return moradia

def des_horta():
    h_urb_trad = 'Este tipo de cultivo é o que se realiza na terra, o de sempre. Destina-se um espaço do jardim e como substrato usa-se o do próprio terreno'
    h_urb_hidro = 'Este tipo de cultivo caracteriza-se por usar água misturada com soluções ricas em minerais. A terra tradicional não é usada, apostando-se antes num cultivo mais experimental e enriquecido. \n*perfeito para plantar espécies herbáceas, aromáticas e vegetais.*'
    h_urb_vert = 'construção realizada de forma perpendicular ao solo. Seu objetivo principal é o de *otimizar o espaço* para plantar frutas, hortaliças, plantas aromáticas ou espécies decorativas.'
    h_urb_contentor = 'Este tipo de cultivo é onde o meio utilizado é um recipiente, vaso, floreiras ou outro tipo de elemento. Ideais para aproveitar o espaço, já que pode escolher o contentor que melhor se adapte ao lugar disponível.'
    hortas = [h_urb_trad, h_urb_hidro, h_urb_vert, h_urb_contentor]

    return hortas

def menu_horta(nome, moradia, hortas):
    if moradia == 'casa':
        print('*TIPOS DE HORTA DISPONÍVEIS*\n1-Horta urbana tradicional\n2-Horta urbana hidropônica\n3-Horta urbana vertical\n4-Horta urbana em contentores')
        escolha = input(f'Certo, {nome}. Você possui alguma dúvida sobre os tipos de horta? [s]im ou [n]ão\n:')
        if escolha == 's':
            while escolha == 's':
                op = int(input('Digite o número da horta que você gostaria de saber mais\n:')) 
                match op:
                    case 1 | 2 | 3 | 4:
                        print(hortas[op-1])
                        escolha = input('Mais alguma dúvida? [s]im ou [n]ão\n:')
                    case _:
                        print('Opção inválida')
    else: 
        print('*TIPOS DE HORTA DISPONÍVEIS*\n1-Horta urbana hidropônica\n2-Horta urbana vertical\n3-Horta urbana em contentores')
        escolha = input(f'Certo, {nome}. Você possui alguma dúvida sobre os tipos de horta? [s]im ou [n]ão\n:')
        if escolha == 's':
            while escolha == 's':
                op = int(input('Digite o número da horta que você gostaria de saber mais\n:')) 
                match op:
                    case 1 | 2 | 3:
                        print(hortas[op-2])
                        escolha = input('Mais alguma dúvida? [s]im ou [n]ão\n:')
                    case _:
                        print('Opção inválida')
    


#principal
nome = inserir_nome()
hortas = des_horta()
menu = menu_horta(nome, hortas)
                


    


