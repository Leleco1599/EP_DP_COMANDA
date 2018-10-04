#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:43:50 2018

@author: Juan
"""


cardápio = {}
comanda = {}
import json

try:
   with open('cardápio.txt','r') as cardápio:
    cardápio = json.loads(cardápio.read())
   with open('comanda.txt','r') as comanda:
    comanda = json.loads(comanda.read())
    
except: FileNotFoundError


#==== HUB de ações ====#


coma = True

while coma:
    print("COMANDA")
    print("0 - Sair")
    print("1 - Cardápio")
    print("2 - Comanda")
    print()
    escolha1 = input("Faça sua escolha: ")
    loop = True
    while loop:
        if escolha1 == "0":
            print(" Até logo, volte sempre!")
            coma = False
            break
    
#==== CARDÁPIO ====#  


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
            
#==== IMPRIMIR CARDÁPIO ====#
                    
                if escolha1_1 == "1":
                    print("Cardápio")
                    if len(cardápio) == 0:
                        print("O cardápio está Vazio")
                        break
                    else: 
                        for produto,preço in cardápio.items():
                            print("{0} (R${1:.2f})".format(produto, preço))
                        break
                
#==== ADICIONAR NO CARDÁPIO ====#
                
                if escolha1_1 == "2":
                    nome_produto = input("Qual é o nome do produto: ")
                    preço_produto = float(input("Qual é o preço: "))
                    cardápio[nome_produto] = preço_produto
                    print("Item adicionado: {0} (R${1:.2f})".format(nome_produto, cardápio[nome_produto]))
                    break
                
#==== REMOVER DO CARDÁPIO ====#
            
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
                    
#==== ALTERAR PREÇO DO CARDÁPIO ====#

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


#==== COMANDA ====#

        if escolha1 == "2":
            if len(cardápio)==0:
                print("Cardápio está vazio. Adicione um produto ao cardápio para iniciar a comanda")
                break
            else:
                n_mesa = int(input("Insira o número da mesa: "))
                while n_mesa > 0:
                    
#==== MENU ====#
                    
                    print("0 - Voltar")
                    print("1 - Adicionar item à comanda")
                    print("2 - Remover algum item da comanda")
                    print("3 - Imprimir a comanda")
                    escolha1_2 = input("Escolha uma opção: ")
                    if escolha1_2 == "0":
                        loop = False
                        break
             
                
#==== ADICIONAR ITEM À COMANDA ====#
                    
                    if escolha1_2 == "1":
                        nome_produto = input("Produto a ser adicionado: ")
                        if nome_produto not in cardápio:
                            print("Este produto não se encontra no cardápio.")
                        else:
                            while True:
                                n_produto = int(input("Quantidade do produto a ser adicionada: "))
                                if n_produto<0:
                                    print("A quantidade não pode ser menor que zero.")
                                else:
                                    if nome_produto in comanda:
                                        comanda[nome_produto] += n_produto
                                        print("Quantidade de {0}: {1}".format(nome_produto, int(comanda[nome_produto])))
                                        break
                                    else:
                                        comanda[nome_produto] = n_produto
                                        print("Quantidade de {0}: {1}".format(nome_produto, int(n_produto)))
                                        break
                                    
        
#==== REMOVER ITEM DA COMANDA ====#                            
                                    
                    if escolha1_2 == "2":
                        nome_produto = input("Produto a ser removido: ")
                        if nome_produto not in comanda:
                            print("O item {0} não existe na comanda".format(nome_produto))
                        else:
                            loop3 = True
                            while loop3:
                                while True:
                                    n_produto = int(input("Quantidade a ser removida: "))
                                    if n_produto < 0:
                                        print("Números negativos são invalidos")
                                        break
                                    if n_produto > comanda[nome_produto]:
                                        print("Impossível remover um valor maior que a quantidade atual.")
                                        break
                                    else:
                                        comanda[nome_produto] -= n_produto
                                        if comanda[nome_produto] == 0:
                                            print("Quantidade de {0}: {1}".format(nome_produto, int(comanda[nome_produto])))
                                            comanda.pop(nome_produto)
                                            loop = False
                                            break
                                        else:
                                            print("Quantidade de {0}: {1}".format(nome_produto, int(comanda[nome_produto])))
                                            loop = False
                                            break
                 
#==== IMPRIMIR A COMANDA ====#
                    
                    if escolha1_2 == "3":
                        if len(comanda) == 0:
                            print("A comanda está vazia.")
                        else:
                            soma_total = 0
                            print("COMANDA")
                            for elemento, valor in comanda.items():
                                soma = valor*cardápio[elemento]
                                print("{0}: {1} | Preço Individual: R${2:.2f} | Preço Total: R${3:.2f}".format(elemento, int(valor), cardápio[elemento], soma))
                                soma_total += soma
                            tip = soma_total+(0.1*soma_total)
                            print("Total: R${0:.2f} | Total com gorjeta: R${1:.2f}".format(soma_total, tip))
    
    
#==== ATUALIZA OS ARQUIVOS 'CARDÁPIO' E 'COMANDA' ====#
            
    Final = json.dumps(cardápio, sort_keys = True)
    with open('cardápio.txt','w') as cardápio: 
        cardápio.write(Final)
        
    Final_2 = json.dumps(comanda, sort_keys = True) 
    with open('comanda.txt','w') as comanda: 
        comanda.write(Final_2)
            