from random import choice
from time import sleep
# -> Introdução do Programa -
print(f'*'*30)
print('JOGO DA FORCA'.center(30))
print(f'*'*30)
# -> Elementos dados pelo usuario
palavras = ['CARRO', 'LARANJA', 'ANIMAL', 'APARTAMENTO']
# Importação do Metodo Random/Choice para retorna de uma palavra da minha lista
sorteio_palavra = choice(palavras)
# lista vazia para adicionar a minha palavra dada pelo meio sorteio
palavra = list()

# Adicionar uma lista de letrar para que meu jogo funcione
for c in range(0, len(sorteio_palavra)):
    palavra.append(sorteio_palavra[c])

# Dados dado pelo usuario, a lista inicial começa vazia
usuario = []

# Bonus para se o usuario quiser uma dica, ele importa o [S] ou [N]
while True:
    dica = str(input('O computador sorteou uma palavra, quer uma dica? [S/N] ').upper().strip()[0])

    # metodo para o metodo de repetição infinito até o usuario utilizar [S] ou [N]
    if dica in 'SsNn':
        break

    # retorna essa mensagem caso o If acima seja Falso
    else:
        print('ERRO! Responda Sim ou Não!')

# Dicas para ajudar mais o usuario
if dica == 'S':

    print('Vou te dar uma dica:')
    sleep(2)

    if sorteio_palavra == 'CARRO':

        print("USADO PARA MEIO DE TRANSPORTE NO DIA A DIA.")

    elif sorteio_palavra == 'LARANJA':

        print("UM ALIMENTO, OU MELHOR, UMA FRUTA.")

    elif sorteio_palavra == 'ANIMAL':

        print("UM SER VIVO.")

    elif sorteio_palavra == 'APARTAMENTO':

        print("UM LOCAL DE MORADIA.")

# Estrutura para adicionar '-' a minha lista de usuario para ser trocada por letras que correspondem a
# minha palavra sorteada
for c in range(0, len(palavra)):
    usuario.append('-')

# Para inicio do programa
acertou = False

# Para contagem de tentativas
cont = len(palavra)
sleep(2)
# Estrutura para adicionar numeros a minha lista de usuario
while acertou == False:
    print(f'Você tem {cont} tentativas.')
    sleep(2)
    # Escolha da letra
    escolha = str(input('Escreva uma letra: ')).upper().strip()
    cont -= 1

    # Metodo para adicionar a letra ao programa
    for c in range(0, len(palavra)):
        if escolha == palavra[c]:
            usuario[c] = escolha

    # Estrutura para deixar o meu programa legivel
    for l in usuario:
        print(l, end='')
    print()

    # Estrutura para por fim ao meu programa
    acertou = True

    # Estrutura para identificar se ainda existe '-' na minha lista de usuario
    for i in range(0, len(usuario)):
        if usuario[i] == '-':
            # Se por ainda existir '-' na minha lista de usuario, o programa continua até finalizar
            acertou = False

    # Se o número de tentativas esgotar, o programa finaliza obrigatoriamente
    if cont <= 0:
        break
print('*' * 30)
# Se o usuario completar o programa
if acertou == True:
    print('Parabéns! Você Ganhou!')
# Se o usuario esgotar as tentativas
else:
    print('Você perdeu! Tente novamente!')
