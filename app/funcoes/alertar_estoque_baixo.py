import app.dados as dados

def alertar_estoque_baixo():
    estoque_baixo = False
    try:
        limite = int(input('Digite a quantidade limite para alertar estoque baixo '))
    except ValueError:
        print('Apenas números inteiros são válidos!')
    
    for produto in dados.estoque:
        if produto['quantidade'] <= limite:
            print(f"O produto '{produto['nome']}' está com o estoque baixo! | Quantidade disponivel:{produto['quantidade']}")
            estoque_baixo = True 
    if not estoque_baixo:
        print('Não há produtos com o estoque baixo!')
        