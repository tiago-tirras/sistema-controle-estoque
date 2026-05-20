import app.dados as dados 

def consultar_estoque():
    for produto in dados.estoque:
        print(f"{produto['id']} - {produto['nome']}")
    
    try:
        produto_id = int(input('Digite o ID do produto: '))
    except ValueError:
        print('Apenas números inteiros são válidos!')
    
    for produto in dados.estoque:
        if produto['id'] == produto_id:
            print(f"{produto['nome']} | Quantidade disponivel: {produto['quantidade']}")
            return
    print('Produto não encontrado no estoque!')