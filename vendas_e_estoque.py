import functions
import json
from time import sleep
import os

print()
print('>'*25, end=' ')
print('Gerenciamento de Estoque e Vendas', end=' ')
print('<'*25,)
while True:
    sleep(1)
    print(f'\n{" Menu de Interação ":=^85}')
    sleep(1)
    print("""
        \033[32m[1]\033[m Adicionar Novo Produto ao Estoque
        \033[32m[2]\033[m Atualizar Produto em Estoque
        \033[32m[3]\033[m Registrar Venda de Produto
        \033[32m[4]\033[m Verificar Estoque
        \033[32m[5]\033[m Encerar Programa
    """)
    while True:
        opcao=str(input('Dígite o \033[32mNúmero\033[m da Operação Desejada:\033[32m ')).strip()
        print('\033[m',end='')
        opcao=functions.checkInt(opcao)
        if opcao != None:
            if opcao <=0 or opcao >5:
                print('\n>>> \033[31m[ERRO]\033[m Opção Inválida!\n')
            else:
                break

    #encerra o programa
    if opcao ==5:
        print(f'\n{" Prgrama Encerrado! ":=^85}')
        sleep(3)
        break

    #Adiciona novo produto ao estoque
    if opcao ==1:
        os.system('cls')
        #verifica se o arquivo existe, se sim abre, se nao cria!
        try:
            with open('Produtos.txt', 'r') as arquivo:
                conteudo=json.load(arquivo)
        except:
            with open('Produtos.txt', 'w') as arquivo:
                print('\n>>> Novo Estoque Criado!')
                conteudo=[]
        sleep(1)
        print(f'\n{" Novo Cadastro de Produto ":=^86}')
        produto=functions.addProduto() # retorna {nome, cod, preço e quant. do produto}, ou None
        #salva o arquivo se ele existir
        if produto !=None:
            conteudo.append(produto)
            with open('Produtos.txt', 'w') as arquivo:
                json.dump(conteudo,arquivo,separators=(',',':'), indent=4)
            os.system('cls')
            print(f'\n>>> Produto {produto["nome"]}, Código: {produto["cod"]} Adicionado ao Estoque!')

    #Atualiza algum produto do estoque
    if opcao ==2:
        sleep(1)
        os.system('cls')
        print(f'\n{" Alteração de Estoque ":=^85}\n')
        encontrado=False
        #procurando o produto!
        while True:
            while not encontrado:
                #abre o arquivo em leitura
                try:
                    with open('Produtos.txt', 'r') as arquivo:
                        conteudo=json.load(arquivo)
                except:
                    print('\n>>> \033[31m[ERRO]\033[m Você Ainda não Possui Estoque!\n Adicione um Novo Produto ao Estoque!')
                    conteudo=False
                    break
                produtosNome=[]
                continua=' '
                
                nome=str(input('Nome ou Código do Produto a Ser Alterado: ')).lower().strip().capitalize()
                #verifica se o produto foi encontrado no estoque e se tem mais de 1 produto com esse nome e salva na lista = produtos' com o mesmo 'Nome
                for item in conteudo:
                    if item['nome']==nome or item['cod']==nome:
                        sleep(1)
                        print(f'\n{">>> Produto Encontrado!":^85}')
                        print(f'''{f'>>> {item["nome"]}, Código: {item["cod"]}, Preço: R${item["preco"]:,.2f}':^85}'''.replace(',','@').replace('.',',').replace('@','.'))
                        produtosNome.append(item)
                if len(produtosNome)==0 and nome != 'Voltar':
                    print('\n>>> \033[31m[ERRO]\033[m Produto Não Encontrado Na Lista de Produtos em Estoque!\n')
                elif len(produtosNome) ==1:
                    produto=produtosNome[0]
                    encontrado=True
                #se tem mais de 1 produto com o mesmo nome no estoque pede o codigo do produto e verifica se o codigo foi encontrado no estoque
                elif len(produtosNome) > 1:
                    print(f'\n>>> Mais de 1 {nome}s, Encontrados No Estoque!\n')
                    while True:
                        cod=str(input('Dígite o Código do Produto a Ser Alterado: ')).strip().lower().capitalize()
                        for p in produtosNome:
                            if p['cod']==cod:
                                produto=p
                                encontrado=True
                                break
                        if not encontrado:
                            print(f'\n>>> \033[31m[ERRO]\033[m Dígite o Código de Um dos {nome}s Acima!\n')
                        else:
                            break
                else:
                    break

            if conteudo == False:
                break
            else:
                if nome != 'Voltar':
                    os.system('cls')
                    produtoAlterado=functions.atualizaProduto(produto)#recebe um produto para a alteração! retorna o produto alterado ou 'Excluir'!
                    #salva o arquivo com o produto ja alterado, verificando quais aspectos do produto foram alterados. ou exclui o produto se for a opção escolhida na função!
                    if produtoAlterado != 'excluir':
                        cont=0
                        for p in conteudo:
                            cont+=1
                            if p==produto:
                                if not 'nome' in produtoAlterado:
                                    produtoAlterado['nome']=produto['nome']
                                if not 'cod' in produtoAlterado:
                                    produtoAlterado['cod']=produto['cod']
                                if not 'preco' in produtoAlterado:
                                    produtoAlterado['preco']=produto['preco']
                                if not 'quantidade' in produtoAlterado:
                                    produtoAlterado['quantidade']=produto['quantidade']
                                conteudo[cont-1]=produtoAlterado
                                break
                    elif produtoAlterado == 'excluir':
                        for p in conteudo:
                            if p==produto:
                                conteudo.remove(p)
                                break
                    with open('Produtos.txt', 'w') as arquivo:
                        json.dump(conteudo,arquivo,separators=(',',':'), indent=4)
                    while continua not in 'SN':
                        continua=str(input('\nMais Alterações no Estoque? [S, N]: ')).upper().strip()[0]
                        if continua not in 'SN':
                            print('\n>>> \033[31m[ERRO]\033[m Dígite apenas Sim ou Não!')
                        else:
                            break
                    if continua =='N':
                        os.system('cls')
                        break
                    else:
                        print()
                        encontrado=False
                else:
                    os.system('cls')
                    break
        
    #vender produtos
    if opcao ==3:
        os.system('cls')
        while True:
            try:
                with open('Produtos.txt', 'r') as arquivo:
                    conteudo=json.load(arquivo)
            except:
                print('\n>>> \033[31m[ERRO]\033[m Você Ainda não Possui Estoque!\n Adicione um Novo Produto ao Estoque!')
                conteudo=False
                break
            listaCompras=functions.venda()#retorna uma lista de compras ou None
            if listaCompras == None:
                os.system('cls')
                break
            else:
                excluiProduto=' '
                break
        if conteudo != False:
            if listaCompras!=None:
                while excluiProduto not in 'SN':
                    excluiProduto=str(input('\nGostaria de Remover Algum Produto da Compra? [S, N]: ')).upper().strip()[0]
                    if excluiProduto not in 'SN':
                        print('\n>>> \033[31m[ERRO]\033[m Dígite apenas Sim ou Não!')
                    elif excluiProduto =='N':
                        break
                    else:
                        print()
                        while True:
                            produtoExcluir=str(input('Nº do Produto a Excluir na Lista de Compras: ')).lower().strip().capitalize()
                            if produtoExcluir == 'Voltar':
                                excluiProduto=' '
                                break
                            else:
                                produtoExcluir=functions.checkInt(produtoExcluir)
                            if produtoExcluir is not None:
                                if produtoExcluir <=0 or produtoExcluir >len(listaCompras)-1:
                                    print('\n>>> \033[31m[ERRO]\033[m Número de Compra Inválido!\n')
                                else:
                                    precoProduto=listaCompras[produtoExcluir-1]['preco']
                                    precoProduto=float(precoProduto)
                                    quantidadeComprada=listaCompras[produtoExcluir-1]['quant. comprada']
                                    quantidadeComprada=int(quantidadeComprada)
                                    total=listaCompras[-1]['total compra']
                                    total=float(total)
                                    total=total-(precoProduto*quantidadeComprada)
                                    listaCompras.pop(produtoExcluir-1)
                                    listaCompras[-1]['total compra']=total
                                    sleep(1)
                                    print(f'\n{"n":<2}{"Produto":<25}{"cod":^8}{"Preço":<15}{"Quantidade":^13}{"Total":>15}')
                                    sleep(1)
                                    for n,i in enumerate(listaCompras):
                                        if n < len(listaCompras)-1:
                                            print(f'{n+1:<2}',end='')
                                            print(f'{i["nome"]:<25}',end='')
                                            print(f'{i["cod"]:<8}',end='')
                                            print(f'''{f'R${i["preco"]:,.2f}':<15}'''.replace(',','@').replace('.',',').replace('@','.'),end='')
                                            print(f'{i["quant. comprada"]:^13}',end='')
                                            print(f'''{f'R${i["preco total"]:,.2f}':>15}'''.replace(',','@').replace('.',',').replace('@','.'))
                                        else:
                                            print(f'''{f"= R${i['total compra']:,.2f}":>78}'''.replace(',','@').replace('.',',').replace('@','.'))
                                    continua=' '
                                    while continua not in 'SN':
                                        continua=str(input('\nMais Produtos a Excluir? [S, N]: ')).upper().strip()[0]
                                        if continua not in 'SN':
                                            print('\n>>> \033[31m[ERRO]\033[m Dígite apenas Sim ou Não!\n')
                                        else:
                                            break
                                    if continua =='S':
                                        print()
                                    if continua =='N':
                                        break
            if listaCompras!=None:
                os.system('cls')
                sleep(1)
                print(f'\n{"n":<2}{"Produto":<25}{"cod":^8}{"Preço":<15}{"Quantidade":^13}{"Total":>15}')
                sleep(1)
                for n,i in enumerate(listaCompras):
                    if n < len(listaCompras)-1:
                        print(f'{n+1:<2}',end='')
                        print(f'{i["nome"]:<25}',end='')
                        print(f'{i["cod"]:<8}',end='')
                        print(f'''{f'R${i["preco"]:,.2f}':<15}'''.replace(',','@').replace('.',',').replace('@','.'),end='')
                        print(f'{i["quant. comprada"]:^13}',end='')
                        print(f'''{f'R${i["preco total"]:,.2f}':>15}'''.replace(',','@').replace('.',',').replace('@','.'))
                    else:
                        print(f'''{f"= R${i['total compra']:,.2f}":>78}'''.replace(',','@').replace('.',',').replace('@','.'))
                with open('Produtos.txt', 'r') as arquivo:
                    conteudo=json.load(arquivo)
                for pE in conteudo:
                    for n, pC in enumerate(listaCompras):
                        if n < len(listaCompras)-1:
                            if pC['cod'] == pE['cod']:
                                s1=int(pE['quantidade'])
                                s2=int(pC['quant. comprada'])
                                r=s1-s2
                                pE['quantidade']=r
                with open('Produtos.txt', 'w') as arquivo:
                    json.dump(conteudo,arquivo,separators=(',',':'), indent=4)
                print('\n>>> Fim da Venda!')
                sleep(1)
                os.system('cls')
    
    if opcao ==4:
        try:
            with open('Produtos.txt', 'r') as arquivo:
                conteudo=json.load(arquivo)
            os.system("start cmd /k cmd_2.exe")
            os.system('cls')
        except:
            os.system('cls')
            print('\n>>> \033[31m[ERRO]\033[m Você Ainda não Possui Estoque!\n Adicione um Novo Produto ao Estoque!')
            