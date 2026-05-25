from app.banco import conexao , cursor 
def cadastrar_produto():
    
    
    nome = input('digite o nome do produto: ').strip().lower()
    categoria = input('digite a categoria do produto: ').strip().lower()
    

    if not nome.replace(' ',' ').isalpha():
        print('O nome deve conter apenas letras!')
        return

    if not categoria.replace(' ',' ').isalpha():
        print('A categoria deve conter apenas letras!')
        return
    
    try:    
        preco = float(input('digite o preço do produto: '))
        if preco < 0:
            print('O preço não pode ser negativo!')
            return
    except ValueError:
        print('Digite um preço valido!')
        return
    
    try:
        quantidade_inicial = int(input('digite a quantidade inicial do produto: '))

        if quantidade_inicial < 0:
            print('A quantidade nao pode ser negativa!')
            return
    except ValueError:
        print('Digite apenas números inteiros!')
        return
    

    sql = ''' insert into produtos
    (nome,categoria,preco,quantidade)
    values (%s,%s,%s,%s)
    '''
    valores = (
        nome,
        categoria,
        preco,
        quantidade_inicial
     )
     
    cursor.execute(sql , valores)
    conexao.commit()


    print(f'Produto adicionado ao estoque!')
