import random

vidas = int(input("Informe O numero de vidas: "))
while vidas <= 0:
     vidas=int(input('Você digitou um numero de vidas inválido. Tente Novamente.\n'))
qtd = int(input("Digite a quantidade de palavras: "))

while qtd <= 0:
    qtd=int(input('Você digitou uma quantidade de palavras inválida. Tente Novamente.\n'))

listaPalavras = list()
i = 1
while i <= qtd:
        palavra = str(input(f"Digite a {i} º palavra:  ")).upper()
        listaPalavras.append(palavra)#adiciona as palavras na lista de palavras.
        i += 1

continuacao = 'sim'
while continuacao == 'sim':
     
     palAleatoria = random.choice(listaPalavras)#sorteia e armazena uma das palavras da lista.
     palDescrypt = list() 
     palCrypt = list()

     for i in palAleatoria: #transforma a palavra aleatoria em uma lista de letras dentro da variavel palDescrypt
        palDescrypt.append(i)    
     tam = len(palAleatoria)     

     for i in range(0, tam):#verifica o tamanho da varivel tam e adiciona um hífen na variável palCrypt a cada passada pelo for
        palCrypt.append("-")
     print("".join(palCrypt))

     acertou = False
     vidasPerdidas = 0
     while acertou == False and vidasPerdidas < vidas:
          letra = input("Digite uma letra: ").upper()
          if letra in palDescrypt:
            for i in range(0, tam):
               if letra == palDescrypt[i] :#verifica se a letra digitada esta na palDescrypt e se estiver, substitui a letra na palCrypt a partir do índice i
                    palCrypt[i]= letra
          else:
            vidasPerdidas += 1#se a letra nao estiver na palDescrypt soma +1 nas vidas perdidas.
            print("Essa letra não existe na palavra.")
          print("".join(palCrypt))
          acertou = True

          for i in range(0, tam):
            if palCrypt[i] == "-" :#verifica se ainda existe hífen na palCrypt 
                acertou = False
     if palDescrypt == palCrypt:#verifica se as palavras da palDescrypt e palCrypt são iguais
        print("Parabéns! você ganhou o jogo!")
     else:
        print("Infelizmente, você perdeu!")