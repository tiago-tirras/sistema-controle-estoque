import app.dados as dados

def registrar_entrada():
    for produto in dados.estoque:
        print(f"{produto['id']} - {produto['nome']} | Quantidade: {produto['quantidade']}")
    
    try:
        produto_id = int(input('Digite o ID do produto: '))
        nova_quantidade = int(input('Digite a quantidade que será adicionada ao produto: '))
    except ValueError:
        print("Apenas números inteiros são válidos!")
    
    for produto in dados.estoque:
        if produto['id'] == produto_id:
            produto['quantidade'] += nova_quantidade
            print(f"Entrada registrada com sucesso! Quantidade atualizada do produto: {produto['quantidade']}")
            return
    print('Produto não encontrado no estoque!')