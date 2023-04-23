# Gerador de números randomicamente
import random

# Numero teto é o número maximo para ser a margem criada randomicamente.
print('Seja muito bem vindo ao Guess Number feito por mim!')
choice_number = input('Digite o número teto do desafio: ')
# .isdigit verifica se foi adicionado um número corretamente
if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('Erro: valor informado não é numérico. Favor execute novamente e informe um número!')
    # se o usuario digitar uma leta ou um numero fracionado o programa irá identificar o ero, informar o usuario e encerrar o programa.
    quit()

# variavel random_number é uma variavel que vai armazenar a operação.
random_number = random.randint(0, choice_number)

n_choices = 0  # adicionei essa função para ir somando cada tentativa de acerto do numero random. No final do jogo, ele irá somar quantas vezes o usuario tentoua acertar o numero random

while True:  # enquanto for verdadeiro ele vai continuar em loop ate o usuario acertar.
    answer_user = input('Adivinhe o número:')

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        # repetimos o else para ter certeza que o usuario vai colocar um número. Qualquer outro caracteria vai repetir a pergunta
        print('Erro: valor informado não é um númerico. Favir informar um número!')
        continue  # continue repete o laço do loop

    n_choices = n_choices + 1  # soma das tentativas
    if answer_user == random_number:
        # resposta que será gerada ao acertar o numero correto.
        print('Acertou')
        break  # finaliza o loop é necessario colocar para acabar a aplicação
    # elif verifica as condições. No caso o número que o usuario digitou é maior ou menor do número gerado.
    elif answer_user > random_number:
        print('Chutou alto, o número randomico é menor que isso...')
    else:
        print('Chutou baixo, o número randomico é maior que isso...')

print('Nº de tentativas: ' + str(n_choices))
