from app.banco import cursor,conexao 

def mostrar_estoque_completo():
    sql = '''select id,nome,categoria ,preco , quantidade from produtos'''

    cursor.execute(sql)
    produtos = cursor.fetchall()

    if not produtos :
        print('estoque vazio!')
        return

    print('\n===ESTOQUE COMPLETO===\n')

    for produto in produtos:
        print(
            f'ID: {produto[0]} | '
            f'Produto: {produto[1]} | '
            f'Categoria: {produto[2]} | '
            f'Preço: {produto[3]:.2f} | '
            f'Quantidade: {produto[4]} '
        )