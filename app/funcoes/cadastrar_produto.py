import app.dados as dados 
def cadastrar_produto():

    try:
        nome = input('Digite o nome do produto: ')
        categoria = input('Digite a categoria do produto: ')
    except ValueError:
        print('Apenas letras alfabéticas são válidas!')
    try:
        preco = float(input('Digite o preço do produto: '))
        quantidade_inicial = float(input('Digite a quantidade inicial do produto: '))
    except ValueError:
        print('Apenas números sãoválidos!')

    produto ={
        'id': dados.proximo_id,
        'nome':nome,
        'categoria':categoria,
        'preco':preco,
        'quantidade':quantidade_inicial
        }
    
    dados.estoque.append(produto)
    dados.proximo_id += 1
    print(f"Produto '{produto['nome']}' adicionado ao estoque!")
    
