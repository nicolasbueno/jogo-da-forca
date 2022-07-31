# JOGO DA FORCA

# IMPORTAÇÕES
import random
import os
from time import sleep

#PALAVRAS PARA FORCA
palavras_forca = list()
palavras_frutas = ['MACA', 'BANANA', 'MORANGO', 'JACA', 'MANGA', 'PERA', 'BERGAMOTA', 'MAMAO', 'KIWI', 'CARAMBOLA', 'MELANCIA', 'ABACATE', 'ABACAXI', 'ACAI', 'ACEROLA', 'AMORA', 'CAQUI', 'CEREJA', 'FRAMBOESA', 'FIGO', 'GOIABA', 'JABUTICABA', 'LARANJA', 'LIMAO', 'MARACUJA', 'MELAO', 'MORANGO', 'PESSEGO', 'PITANGA', 'PITAYA', 'UVA']
palavras_animais = ['CACHORRO', 'GATO', 'GALINHA', 'PORCO', 'BOI', 'VACA', 'MACACO', 'COELHO', 'JAVALI', 'LEAO', 'LEOPARDO', 'PEIXE', 'TUBARAO', 'GOLFINHO', 'ELEFANTE', 'GIRAFA', 'TARTARUGA', 'COBRA', 'TIGRE', 'LEBRE', 'CAPIVARA', 'VEADO', 'HIPOPOTAMO', 'GUAXINIM', 'GAMBA', 'FOCA', 'BALEIA', 'RATO']
palavras_cidades = ['PORTO-ALEGRE', 'PARIS', 'CANOAS', 'GRAVATAI', 'NOVA-YORK', 'JERUSALEM', 'BERLIM', 'AMSTERDA', 'GRAMADO', 'CANELA', 'MOSCOU', 'CAIRO', 'BUENOS-AIRES','PUNTA-DEL-LESTE', 'MONTEVIDEU', 'ASSUNCAO', 'CURITIBA', 'SANTIAGO', 'SYDNEY']

# PERGUNTANDO O NOME
nome_jogador = input('Olá, qual é o seu nome? ')

# LIMPANDO O CONSOLE
os.system('cls')

jogar_novamente = 'S'

while jogar_novamente == 'S':

    print(f'Olá, {nome_jogador}! Seja bem-vindo(a) ao Jogo da Forca!\n')
    tipo_de_palavras = int(input(('Que tipo de palavras você prefere?\n1 - Frutas\n2 - Animais\n3 - Cidades\n---> ')))

    # LIMPANDO O CONSOLE
    os.system('cls')

    # DEFININDO TIPO DE PALAVRAS
    if tipo_de_palavras == 1:
        palavras_forca.extend(palavras_frutas)
        print('Legal, você escolheu frutas!!\n')
    elif tipo_de_palavras == 2:
        palavras_forca.extend(palavras_animais)
        print('Legal, você escolheu animais!!\n')
    elif tipo_de_palavras == 3:
        palavras_forca.extend(palavras_cidades)
        print('Legal, você escolheu cidades!!\n')
    else:
        palavras_forca.extend(palavras_frutas)
        print('Você não escolheu uma opção válida :/\nEntão escolhemos frutas para você!\n')

    # DEFININDO PALAVRA ALEATÓRIA E OBTENDO NÚMERO DE LETRAS - CRIAÇÃO DE VARIÁVEIS
    indice_aleatório = random.randint(0, 30)
    palavra = palavras_forca[indice_aleatório]
    qtde_letras = len(palavra)
    lista_palavra = palavra
    list(lista_palavra)
    erros_faltantes = 6
    palavra_mostrada = list()
    contador = 0
    letras_erradas = list()
    acertos = 0
    aux = 0
    letras_usadas = list()
    aux2 = 0

    for i in range(qtde_letras):
        palavra_mostrada.append('_ ')   

    print(f'Sua palavra tem {qtde_letras} letras!')
    input('Pressione ENTER para iniciar o jogo... ')

    # LIMPANDO O CONSOLE
    os.system('cls')

    while erros_faltantes > 0:
        print(f'Você só pode errar {erros_faltantes} vezes até acertar a palavra!')
        print('\n')
        print(''.join(palavra_mostrada))
        print('\n')
        if erros_faltantes < 6:
            print('Letras erradas: ', ' '.join(letras_erradas))
            print('\n')
        letra = input('Escolha uma letra: ').upper()
        print('\n')

        # IDENTIFICA SE A LETRA JÁ FOI DIGITADA ANTES
        if len(letras_usadas) > 0:
            for i in range(len(letras_usadas)):
                if letras_usadas[i] == letra:
                    aux2 = aux2 + 1        

        # TESTA SE A LETRA FOI DIGITADA
        if aux2 > 0:
            print('Você já digitou essa letra, tente outra!')
            aux2 = 0
        else:
            # IDENTIFICA SE EXISTE A LETRA NA PALAVRA
            for i in range(qtde_letras):
                if lista_palavra[i] == letra:
                    contador = contador + 1
                    palavra_mostrada.pop(i)
                    palavra_mostrada.insert(i, letra + ' ')
                    acertos = acertos + 1
            letras_usadas.append(letra)

            # IMPRIME NA TELA SE ELE ACERTOU OU NÃO A LETRA
            if contador > 0:
                print('Woow! Essa letra existe na sua palavra!')
                contador = 0
            else:
                print('Essa letra não existe na palavra!')
                contador = 0
                letras_erradas.append(letra)
                erros_faltantes = erros_faltantes - 1

        # AGUARDA 3 SEGUNDOS PARA O PROGRAMA CONTINUAR
        sleep(3)

        # LIMPANDO O CONSOLE
        os.system('cls')

        # IDENTIFICA SE PALAVRA FOI ACERTADA
        if acertos == qtde_letras:
            erros_faltantes = 0

    if acertos == qtde_letras:
        print('Parabéns! Você Acertou a palavra!\n')
    else:
        print('Infelizmente você errou 6 vezes! Mas não desista, tente novamente!\n')

    print('A palavra era', palavra)
    print('\n')
    print('\n')
    erros_faltantes = 6

    while aux == 0:
        jogar_novamente = input('Deseja jogar novamente? (S/N)').upper()
        if jogar_novamente == 'S' or jogar_novamente == 'N':
            aux = 1
            os.system('cls')
        else:
            print('Você digitou algo diferente de (S/N), por favor informe a tecla correta!')
            sleep(3)
            os.system('cls')






