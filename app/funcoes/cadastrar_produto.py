import app.dados as dados  # importa o arquivo app.dados com dados 
def cadastrar_produto():

    try:
        nome = input('Digite o nome do produto: ')
        categoria = input('Digite a categoria do produto: ')
    except ValueError:
        print('Apenas letras alfabéticas são válidas!')
    try:
        preco = float(input('Digite o preço do produto: '))
        quantidade_inicial = int(input('Digite a quantidade inicial do produto: '))
    except ValueError:
        print('Apenas números são válidos!')

    produto ={
        'id': dados.proximo_id, 
        'nome':nome,
        'categoria':categoria,
        'preco':preco,
        'quantidade':quantidade_inicial
        }
    
    dados.estoque.append(produto)   # Adiciona o dicionário na lista 
    dados.proximo_id += 1           # Atualiza a variavel proximo_id, adicionado +1
    print(f"Produto '{produto['nome']}' adicionado ao estoque!") # Mensagem que confirma que cadastrou o produto 
    
