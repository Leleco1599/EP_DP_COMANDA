#====== EP COMANDA =======


cardápio = {}
comanda = {}

#HUB de ações

print("Comanda Eletrônica")
print("0 - sair",
	  "1 - imprimir cardápio",
      "2 - adicionar item",
      "3 - remover item",
	  "4 - imprimir comanda")

escolha = int(input("O que deseja fazer?:"))


while escolha > 0:


# ====== IMPRIMIR CARDÁPIO =======

if escolha == 1:

	print("O cardápio tem os seguintes itens:")
	print(cardápio)



#====== ADICIONAR ITEM ==========



if escolha == 2 :
        nome_produto = input('Digite o Produto: ')
        while nome_produto not in cardápio:
            print('Essa opção ainda não existe em nosso cardápio...")                                                                                                                                                                                                                                                                                                                                   
            #EM BREVE ADD CODIGO PRA COLOCAR PRODUTO NO CARDÁPIO	
            nome_produto = input("Digite o Produto: ")
        quantidade = int(input('Digite a quantidade do produto: '))
        while quantidade < 0:
        	print("Não é possível adcionar quantidade não positiva")
        	quantidade = int(input('Digite a quantidade do produto: '))

        if nome_produto not in comanda:
        	comanda[nome_produto]  = quantidade
        else:
        	comanda[nome_produto] += quantidade
        	






        	
   



