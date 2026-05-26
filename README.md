# Nome do projeto: Sistema-controle-estoque 


## Descrição do projeto 

- Peojeto desenvolvido em Python, tem como finalidade ajuda no gerenciamento de estoque, através de uma sistema que permite cadastra produtos, nomenado seu: Nome, Categoria, Preço e Quantidade, com funçoes de adicionar e retirar produtos de estoque, visualizar estoque, checar limite e um menu com todas as funcoes presente no no sitema de estoque, conta com um sistema de ID para cada produto cadastrado  junto com uma interação limpa e focada diretamente na esperiência do usuário via terminal.
    
---
## Objetivo do projeto 

- Tem como objetivo ajudar e auxiliar usuários que nessecitam de um gerenciado de estoque eficiente e inteligente.
   
---

## Funcionalidades implementadas

 1 -  def
 
 2 -  variáveis
 
 4 -  inputs
 
 5 -  if/elif/else 
 
 6 -  for e while 
 
 7 -  try/exept
 
 8 -  append
 
 9 -  global
 
 10 - return 
 
 11 - variáveis de controle 

 12 - import 


- def cadastrar_produto(nome,categoria,preco,quantidade_inicial): # Reponsável por receber os input e enviar para lista e atualizar os ID´s
- def registrar_entrada(produto_id,nova_quantidade):              # Responsável por gerenciar o sistema de aumentar a quantidade do estoque por ID
- def registrar_saida (produto_id, nova_quantidade):              # Responsável por gerenciar o sistema de diminuir a quantidade do estoque por ID
- def consultar_estoque(produto_id):                              # Responsável por mostra os items do estoque por ID
- def alertar_estoque_baixo(limite):                              # Responsável por fazer um varredura estoque e mostra os items  com quantidades menores ou iguais ao limite 
- def estoque_completo():                                         # Responsável por mostra os items do estoque completo
- def menu():                                                     # Responsável por mostra o menu das funções 

---

## Instruções de execução do código

Como o sistema usa **MySQL**, os dados ficam salvos em um servidor. A configuração abaixo é feita uma única vez. Depois disso, o uso no dia a dia é bem rápido.


## 1. O que você precisa instalar

Baixe e instale estes três itens gratuitos no seu computador:

1. **Python** (O motor do programa)
   * Baixe em: [python.org](https://www.python.org/)
   * Muito Importante: Logo na primeira tela da instalação, marque a caixinha **"Add python.exe to PATH"** antes de avançar. Se esquecer disso, o computador não reconhecerá o Python.
2. **WampServer** (O servidor do banco de dados)
   * Baixe em: [wampserver.com/en/](https://www.wampserver.com/en/)
   * Instale avançando as telas normalmente.
3. **VS Code** (Onde você vai abrir o código, se preferir)
   * Baixe em: [code.visualstudio.com](https://code.visualstudio.com/)

---

## 2. Configuração Inicial (Faça apenas na primeira vez)

### Passo A: Ligar o Servidor e Criar o Banco 
1. Abra o **WampServer** (procure no menu iniciar do Windows). 
2. Olhe para o canto inferior direito da sua tela, perto do relógio do Windows. Um ícone do WampServer vai aparecer ali. Ele precisa ficar **Verde** (isso significa que o servidor ligou com sucesso).
3. Clique com o **botão esquerdo** em cima desse ícone verde e selecione **phpMyAdmin**. Uma página de internet vai abrir.
4. No campo de usuário, digite `root` e deixe a senha em branco (é o padrão). Clique em Continuar.
5. No menu esquerdo da página que abriu, clique em **"Novo"** (ou *New*).
6. No campo do meio, digite exatamente o nome: `estoque` (tudo em minúsculo) e clique em **"Criar"**. Pronto, a base de dados está criada.

### Passo B: Preparar o ambiente (Escolha uma das duas formas abaixo)

* **Opção 1: Se você prefere usar o TERMINAL comum do Windows**
  1. Abra o menu iniciar do Windows, digite `cmd` e abra o **Prompt de Comando** (a tela preta) ou da pasta nos caminhos de pastas (C:\Usuários\Nome\Área de Trabalho) digitar 'cmd'
  3. Cole o comando abaixo e aperte **Enter**:
     ```cmd
     python -m pip install mysql-connector-python
     ```
  4. Espere carregar e feche a tela preta.
 Nota: ele instalará a biblioteca do mysql no seu computador

* **Opção 2: Se você prefere usar o VS CODE**
  1. Abra o VS Code, vá no menu do topo em **File** ➜ **Open Folder** e selecione a pasta do projeto (`sistema-controle-estoque-master`).
  2. No menu esquerdo (ícone de 4 quadradinhos), busque por `Python` e clique no botão azul **Install**.
  3. No menu do topo, clique em **Terminal** ➜ **New Terminal**. Na barra que abrir embaixo, cole o comando abaixo e aperte **Enter**:
     ```bash
     pip install mysql-connector-python
     ```

---

## 3. Como Ligar o Programa no Dia a Dia

> **Aviso fixo:** O programa só funciona se o **WampServer** estiver aberto e com o ícone **Verde** perto do relógio. Certifique-se disso antes de tentar ligar o sistema.

Escolha por onde prefere rodar o programa hoje:

### Pelo VS Code (Mais visual)
1. Com a pasta do projeto aberta no VS Code, procure pela pasta **`app`** no menu esquerdo.
2. Clique no arquivo **`main.py`** para abrir o código dele na tela.
3. Olhe para o canto superior direito da tela e clique no botão de **"Play"** (um triângulo deitado).
4. O menu vai aparecer na parte de baixo da tela. Digite o número da opção que quiser e use!

### Pelo Terminal / Atalho rápido (Mais prático)
Se não quiser abrir o VS Code toda vez, crie um "botão de ligar":
1. Abra a pasta do projeto no seu computador.
2. Clique com o botão direito em um espaço em branco, vá em **Novo** ➜ **Documento de Texto**.
3. Abra esse bloco de notas e cole apenas esta linha:
   ```text
   python -m app.main

##  Tutoriais em Vídeo de Referência

Se você prefere ver o passo a passo em vídeo para ter certeza de que está fazendo certo, aqui estão quatro ótimas referências:

* **Como instalar e ligar o WampServer:** [Assista ao tutorial de instalação no YouTube](https://www.youtube.com/watch?v=kYv_w76v8f0) (Canal: Bóson Treinamentos). Esse vídeo mostra o clique a clique da instalação e como o ícone fica verde perto do relógio.
* **Como mexer no phpMyAdmin para criar o banco:** [Assista ao tutorial do phpMyAdmin no YouTube](https://www.youtube.com/watch?v=P3M8Vp82wZc) (Canal: Curso em Vídeo). Mostra exatamente como entrar na página de internet do Wamp e criar uma base de dados nova.
* **Como instalar e configurar o VS Code:** [Assista ao guia do VS Code no YouTube](https://www.youtube.com/watch?v=DiXbJL3iWvs) (Canal: Curso em Vídeo). Este vídeo mostra como baixar, instalar e mudar o idioma do VS Code para português, deixando ele pronto para uso.
* **Como usar o terminal e rodar comandos:** [Assista ao guia de Terminal para Iniciantes no YouTube](https://www.youtube.com/watch?v=333M7t7g9N4) (Canal: Rocketseat). Um guia excelente que tira o medo da "tela preta", mostrando como abrir o terminal e digitar comandos sem erro.

  
## Nome do aluno

-
-
-
---
