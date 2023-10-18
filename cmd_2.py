from time import sleep
import json

print(f'\n{" Estoque ":=^85}')
sleep(1)
try:
    with open('Produtos.txt','r') as arquivo:
        estoque=json.load(arquivo)
    
    print(f'\n{"Nome":<25}{"Código":^15}{"Preço":<15}{"Quantidade":^13}')
    sleep(1)
    estoque=sorted(estoque, key=lambda x: x['nome'])
    for produto in estoque:
        print(f'{produto["nome"]:<25}{produto["cod"]:^15}{produto["preco"]:<15,.2f}{produto["quantidade"]:^13}'.replace(',','@').replace('.',',').replace('@','.'))
    totalProdutos=len(estoque)
    totalItens=0
    precoTotal=0
    for p in estoque:
        quantidade=int(p['quantidade'])
        totalItens+=quantidade
        valor=float(p['preco'])
        valor*=quantidade
        precoTotal+=valor
    print(f'\nTotal de Produtos em Estoque {totalProdutos}')
    print(f'Total de Itens em Estoque {totalItens}')
    print(f'Preço Total de Todos os Produtos em Estoque {precoTotal:,.2f}'.replace(',','@').replace('.',',').replace('@','.'))
    sleep(1)
    print('\n>>> \033[31m[Atenção]\033[m Dítite "\033[31mexit\033[m" Quando Não Precisar Mais Desta Lista E For Fecha-la!')

except:
    print('\n>>> \033[31m[ERRO]\033[m Você Ainda não Possui Estoque!\n Adicione um Novo Produto ao Estoque!')
