#====== EP COMANDA =======


cardápio = {}
comanda = {}
import json

try:
   with open('cardápio.txt','r') as cardapio:
    cardapio = json.loads(cardápio.read())
   with open('comanda.txt','r') as comanda:
    comanda = json.loads(comanda.read())
    
except: FileNotFoundError


#HUB de ações


coma = True

while coma:
    print("COMANDA")
    print("0 - Sair")
    print("1 - Cardápio")
    print("2 - Comanda")
    print()
    escolha1 = input("Faça sua escolha: ")
    loop = True
    if escolha1 == "0":
        print(" Até logo, volte sempre!")
        loop = False
        break
    
#====== CARDÁPIO =====    


    if escolha1 == "1":
        print("0 - Voltar")
        print("1 - Imprimir Cardápio")
        print("2 - Adicionar item no cardápio")
        print("3 - Remover item do cardápio")
        print("4 - Alterar preço de item")
        print()
        escolha1_1 = input("Qual a sua escolha: ")
        while True:
            
        
            if escolha1_1 == "0":
                loop = False
                break
            
            #IMPRIMIR CARDÁPIO
                    
            if escolha1_1 == "1":
                print("Cardápio")
                if len(cardápio) == 0:
                    print("O cardápio está Vazio")
                    break
                else: 
                    for produto,preço in cardápio.items():
                        print("{0} (R${1})".format(produto, preço))
                    break
                
            #ADICIONAR NO CARDÁPIO
                
            if escolha1_1 == "2":
                nome_produto = input("Qual é o nome do produto: ")
                preço_produto = float(input("Qual é o preço: "))
                cardápio[nome_produto] = preço_produto
                print("Item adicionado ao cardápio: {0} (R${1})".format(nome_produto, cardapio[nome_produto]))
                break
                
            #REMOVER DO CARDÁPIO
            
            if escolha1_1 == "3": 
                nome_produto = input("Nome produto a ser removido: ")
                if nome_produto not in cardápio: 
                    print("Este produto não existe no cardápio")
                    break
                else:
                    cardápio.pop(nome_produto)
                    if len(cardápio) != 0:
                        print("{0} foi removido do cardápio".format(nome_produto))
                        break
                    else:
                        print("O cardápio está vazio")
                        break
                    
            #ALTERAR PREÇO DO CARDÁPIO

            if escolha1_1 == "4":
                nome_produto = input("Qual é o produto?: ")
                if nome_produto not in cardápio:
                    print("Este produto não existe no cardápio: ")
                    break
                else:
                    preço = float(input("Novo preço do produto: "))
                    cardápio[nome_produto] = preço
                    print("{0} Novo preço: R${1}".format(nome_produto, cardápio))
                    break
                    
                
                        
        
    
    




        	
   



