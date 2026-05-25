from app.banco import conexao , cursor 
def registrar_saida ():

    sql = 'select id, nome,quantidade from produtos'

    cursor.execute(sql)

    produtos = cursor.fetchall()

    if not produtos:
        print('nenhum produto cadastrado!')
        return

    print('\n===PRODUTOS CADASTRADOS===')

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f'Quantidade: {produto[2]}'
            )

    try:    
        produto_id = int(input('digite o ID do produto: '))
        quantidade_saida = int(input('digite a quantidade que será retirada: '))
    
    except ValueError:
        print('digite apenas numeros')
        return
    
    sql = '''select nome ,quantidade 
    from produtos 
    where id = %s'''

    cursor.execute(sql,(produto_id,))

    produto = cursor.fetchone()

    if produto is None:
        print('Produto nao encontrado')
        return
    
    nome_produto = produto[0]
    quantidade_atual = produto[1]

    if quantidade_saida > quantidade_atual:
        print('Quantidade insufisciente no estoque')
        return

    sql = '''
    update produtos 
    set quantidade = quantidade - %s
    where id = %s  '''

    valores = (
        quantidade_saida,
        produto_id
    )

    cursor.execute(sql,valores)

    conexao.commit()
    
    sql = '''select quantidade from produtos 
    where id = %s'''

    cursor.execute(sql,(produto_id,))

    nova_quantidade = cursor.fetchone()[0]

    print(
        f'\nSaida registrada com sucesso!\n'
        f'\nProduto: {nome_produto}'
        f'\nQuantidade Atual: {nova_quantidade}'
    )
  