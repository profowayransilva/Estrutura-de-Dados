bola = input('--> Insira um valor ou uma mensagem: ')
print(f"O valor inserido foi: {bola}")

array = ["bola", "gol", "trave", "jogador"]

for items in array:
    if bola == "bola":
        print("Encontrei o elemento bola", array[items])
        break
    else:
        print("Não encontrei o elemento bola")
        