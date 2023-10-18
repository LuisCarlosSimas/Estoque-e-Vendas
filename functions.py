import json
from time import sleep
import os

def checkFloat(txt):
    try:
        return float(txt)
    except:
        print('\n>>> \033[31m[ERRO]\033[m Digite Apenas Números Neste Campo!\n')
        return None

def checkInt(txt):
    try:
        return int(txt)
    except:
        print('\n>>> \033[31m[ERRO]\033[m Digite Apenas Números Inteiros Neste Campo!\n')
        return None

#verifica se o cod nao se repete na lista de produtos
#se cod se repete o resultado é o produto com aquele cod. Se nao resultado e falso
def codExiste(cod):
    with open('Produtos.txt', 'r') as arquivo:
        conteudo=json.load(arquivo)
    for item in conteudo:
        if item['cod']==cod:
            return item
    return False

# retorna {nome, cod, preço e quant. do produto}, ou None!
def addProduto():
    produto={}

    nome=str(input('\nNome do Produto: ')).lower().strip().capitalize()
    if nome =='Voltar':
        return None
    produto['nome']=nome

    while True:
        cod=str(input('Código de Referência: ')).lower().strip().capitalize()
        check=codExiste(cod)
        if check:
            print('\n>>> \033[31m[ERRO]\033[m Codigo já Cadastrado no Estoque!\n')     
        else:
            produto['cod']=cod
            break
    
    while True:
        preco=str(input('Valor Unitário: R$')).replace(',', '.').strip()
        preco=checkFloat(preco) #tenta retornar um float(), se nao mostra mensagem de erro e retorna None!
        if preco != None:
            produto['preco']=preco
            break
    
    while True:
        quantidade=str(input('Quantidade de Unidades Recebidas: '))
        quantidade=checkInt(quantidade) #tenta retornar um int(), se nao mostra mensagem de erro e retorna None!
        if quantidade != None and quantidade > 0:
            produto['quantidade']=quantidade
            break
        if quantidade != None and quantidade <= 0:
            print('\n>>> \033[31m[ERRO]\033[m Dígite Apenas Quantidades Positivas!\n') 

    return produto

#recebe um produto para a alteração! retorna o produto alterado ou 'Excluir'!
def atualizaProduto(produto):
    alteracoesProduto={}
    escolheu=False
    #qual alteração vai ser feita no produto
    while True:
        os.system('cls')
        sleep(1)
        try:
            print(f'''\n{f" Alteração do produto {alteracoesProduto['nome']} " :=^85}''')
        except:
            print(f'''\n{f" Alteração do produto {produto['nome']} " :=^85}''')
        try:
            print(f'''{f" Código {alteracoesProduto['cod']} ":=^85}''')
        except:
            print(f'''{f" Código {produto['cod']} ":=^85}''')
        print('''
        \033[32m[1]\033[m Alterar o Nome do Produto
        \033[32m[2]\033[m Alterar o Código do Produto
        \033[32m[3]\033[m Alterar o Preço do Produto
        \033[32m[4]\033[m Alterar a Quantidade em Estoque
        \033[32m[5]\033[m Excluir Produto
        \033[32m[6]\033[m Voltar
        ''')
        while True:
            alteracao=str(input('Dígite o \033[32mNúmero\033[m da Operação Desejada: \033[32m')).strip()
            print('\033[m')
            alteracao=checkInt(alteracao)
            if alteracao != None:
                if alteracao <=0 or alteracao >6:
                    print('\033[31m[ERRO]\033[m Opção Inválida!')
                else:
                    break
                
        sleep(1)
        if alteracao==1:#alterando nome
            while True:
                novoNome=str(input('Novo nome do Produto: ')).lower().strip().capitalize().replace(',','.')
                if novoNome=='Voltar':
                    break
                else:
                    escolheu=True
                    sleep(1)
                    try:
                        print(f'\n>>> {alteracoesProduto["nome"]}', end=', ')
                    except:
                        print(f'\n>>> {produto["nome"]}', end=', ')
                    try:
                        print(f'Código: {alteracoesProduto["cod"]}')
                    except:
                        print(f'Código: {produto["cod"]}')
                    print(f'>>> Nome Alterado Para {novoNome}!\n')
                    alteracoesProduto['nome']=novoNome
                    break

        if alteracao==2:#alterando codigo
            while True:
                novoCod=str(input('Novo Código do Produto: ')).lower().strip().capitalize()
                if novoCod=='Voltar':
                    break
                else:
                    check=codExiste(novoCod)
                if check and check!=produto:
                    print('\n>>> \033[31m[ERRO]\033[m Codigo já Cadastrado no Estoque!\n')
                else:
                    escolheu=True
                    sleep(1)
                    try:
                        print(f'\n>>> {alteracoesProduto["nome"]}', end=', ')
                    except:
                        print(f'\n>>> {produto["nome"]}', end=', ')
                    try:
                        print(f'Código: {alteracoesProduto["cod"]}', end=', ')
                    except:
                        print(f'Código: {produto["cod"]}', end=', ')
                    print(f'Alterado Para {novoCod}!\n')
                    alteracoesProduto['cod']=novoCod
                    break

        if alteracao==3:#alterando preço
            while True:
                novoPreco=str(input('Novo Preço do Produto: R$')).strip().lower().capitalize()
                if novoPreco=='Voltar':
                    break
                else:
                    novoPreco=checkFloat(novoPreco)
                if novoPreco!=None:
                    escolheu=True
                    sleep(1)
                    try:
                        print(f'\n>>> {alteracoesProduto["nome"]}', end=', ')
                    except:
                        print(f'\n>>> {produto["nome"]}', end=', ')
                    try:
                        print(f'Código: {alteracoesProduto["cod"]}', end=', ')
                    except:
                        print(f'Código: {produto["cod"]}', end=', ')
                    print(f'Preço Alterado Para R${novoPreco:.2f}!\n')
                    alteracoesProduto['preco']=novoPreco
                    break

        if alteracao==4:#alterar a quantidade em estoque
            while True:
                novaQuantidade=str(input('Quantidade de Unidades em Estoque: ')).strip().lower().capitalize()
                if novaQuantidade=='Voltar':
                    break
                else:
                    novaQuantidade=checkInt(novaQuantidade)
                if novaQuantidade!=None:
                    escolheu=True
                    sleep(1)
                    try:
                        print(f'\n>>> {alteracoesProduto["nome"]}', end=', ')
                    except:
                        print(f'\n>>> {produto["nome"]}', end=', ')
                    try:
                        print(f'Código: {alteracoesProduto["cod"]}', end=', ')
                    except:
                        print(f'Código: {produto["cod"]}', end=', ')
                    print(f'Estoque Alterado Para {novaQuantidade} Unidades!\n')
                    alteracoesProduto['quantidade']=novaQuantidade
                    break

        if alteracao==5:#quero excluir esse produto!
            return 'excluir'

        if alteracao==6:#voltar. Apesar de ja conseguir voltar antes de entrar nessa funçao!
            return alteracoesProduto

        #so entra aqui se fez alguma alteração no produto!
        if escolheu:
            continua=' '
            while True:
                continua=str(input('Mais Alterações Para Esse Produto? [S/N]: ')).strip().lower().capitalize()[0]
                if continua not in 'SN':
                    print('\n>>> \033[31m[ERRO]\033[m Dígite apenas Sim ou Não!\n')
                else:
                    break
            if continua == 'N':
                return alteracoesProduto

#retorna uma lista de compras ou None
def venda():
    sleep(1)
    print(f'\n{" Nova Venda ":=^85}')
    totalVendido=0  #total da soma de todos os produtos vendido
    listaCompras=[] # uma lista com um dicionario pra cada produto comprado e um dicionario com o total da venda no fim
    quantidadeVendidaProduto=None   #quantidade vendida de cada produto
    while quantidadeVendidaProduto ==None:
        print()
        produtoComprado={}
        encontrado=False    #produto certo foi encontrado no estoque?
        while not encontrado:
            produtosNome=[] # produtos com esse nome no estoque
            produto=str(input('Nome ou Código do Produto: ')).lower().strip().capitalize()
            if produto == 'Voltar':
                return None #quero voltar!
            with open('Produtos.txt', 'r') as arquivo:
                conteudo=json.load(arquivo)
            #verifica se o produto foi encontrado no estoque e se tem mais de 1 produto com esse nome
            for item in conteudo:
                if item['nome']==produto or item['cod']==produto:
                    sleep(1)
                    print(f'\n{">>> Produto Encontrado!":^85}')
                    print(f'''{f'>>> {item["nome"]}, Código: {item["cod"]}, Preço: R${item["preco"]:.2f}':^85}''')
                    produtosNome.append(item)
            if len(produtosNome) ==1:
                produto=produtosNome[0]
                encontrado=True
            #se tem mais de 1 produto com o mesmo nome no estoque pede o codigo do produto e verifica se o codigo foi encontrado no estoque
            elif len(produtosNome) > 1:
                print('\n>>> Mais de 1 Produto Com Esse Nome Encontrado Na Lista de Produtos!\n')
                while True:
                    cod=str(input('Dígite o Código do Produto a Ser Vendido: ')).strip().lower().capitalize()
                    cod=codExiste(cod)
                    if cod:
                        produto=cod
                        encontrado=True
                        break
                    else:
                        print(f'\n>>> \033[31m[ERRO]\033[m Dígite o Código de Um dos {produto}s Acima!\n')
            if not encontrado:
                print('\n>>> \033[31m[ERRO]\033[m Produto Não Encontrado Na Lista de Produtos em Estoque!\n')
                
        nome= produto['nome']
        produtoComprado['nome']=nome
        cod=produto['cod']
        produtoComprado['cod']=cod
        preco=produto['preco']
        produtoComprado['preco']=preco
        quantidadeEstoque=produto['quantidade']
        produtoComprado['quant. estoque']=quantidadeEstoque
        print()
        while True:
            quantidadeVendidaProduto=str(input('Quantidade: ')).lower().strip().capitalize()
            if quantidadeVendidaProduto == 'Voltar':
                quantidadeVendidaProduto=None
                break
            else:
                quantidadeVendidaProduto=checkInt(quantidadeVendidaProduto)
                if quantidadeVendidaProduto !=None:
                    break
        if quantidadeVendidaProduto!=None:
            if quantidadeVendidaProduto>int(quantidadeEstoque):
                print(f'\n>>> \033[31m[ERRO]\033[m Produto {nome}, {cod} Possui Apenas {quantidadeEstoque} em Estoque!\n')
            elif quantidadeVendidaProduto <=0:
                print('\n>>> \033[31m[ERRO]\033[m Dígite uma Quantidade de Venda Válida!\n')
            else:
                totalProduto=float(preco)*quantidadeVendidaProduto
                totalVendido+=totalProduto
                produtoComprado['quant. comprada']=quantidadeVendidaProduto
                produtoComprado['preco total']=totalProduto
                sleep(1)
                print(f'\n{"n":<2}{"Produto":<25}{"cod":^8}{"Preço":<15}{"Quantidade":^13}{"Total":>15}')
                sleep(1)
                listaCompras.append(produtoComprado)
                for n,i in enumerate(listaCompras):
                    print(f'{n+1:<2}',end='')
                    print(f'{i["nome"]:<25}',end='')
                    print(f'{i["cod"]:<8}',end='')
                    print(f'''{f'R${i["preco"]:,.2f}':<15}'''.replace(',','@').replace('.',',').replace('@','.'),end='')
                    print(f'{i["quant. comprada"]:^13}',end='')
                    print(f'''{f'R${i["preco total"]:,.2f}':>15}'''.replace(',','@').replace('.',',').replace('@','.'))
                print(f"{f'= R${totalVendido:,.2f}':>78}".replace(',','@').replace('.',',').replace('@','.'))
                    
        if quantidadeVendidaProduto !=None:
            continua=' '
            while continua not in 'SN':
                continua=str(input('\nMais compras para esse cliente? [S, N]: ')).upper().strip()[0]
                if continua not in 'SN':
                    print('\n>>> \033[31m[ERRO]\033[m Dígite apenas Sim ou Não!')
                else:
                    break
            if continua =='S':
                quantidadeVendidaProduto=None
            else:
                totalCompra={}
                totalCompra['total compra']=totalVendido
                listaCompras.append(totalCompra)
                return listaCompras
