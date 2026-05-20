import app.dados as dados

def mostrar_estoque_completo():
    if not dados.estoque:
        print('Estoque vazio!')
        return
    for produto in dados.estoque:
        print(f"{produto['id']} - {produto['nome']} | Quantidade: {produto['quantidade']} | preço:R$ {produto['preco']}")