# #Itens de um inventario de RPG
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} #Itens do inventario
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']#Itens para ser adicionados
# def displayInventory(inventory):#Funcao que retorna todos os itens do inventario e suas quantidades
#     print("Inventory:")
#     item_total = 0
#     for itemName, numberOfItens in inventory.items():
#         print('- {} {}'.format(numberOfItens, itemName))
#         item_total += numberOfItens
#     print("Total number of items: " + str(item_total))
#
# def addToinventory(inventory, addedItems):#Funcao que adiciona os itens de uma lista no dicionario utilizado como inventario
#     for item in addedItems:
#         if item in inventory:
#             inventory[item] += 1
#         inventory.setdefault(item ,1)
#     print('New itens added to inventory!'.format(addedItems))
#
# addToinventory(stuff, dragonLoot)
# displayInventory(stuff)
####################################
# #Meu codigo
# bigBag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} #inventario
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  # Itens para ser adicionados
#
# def showInventory(inventory):
#     totalOfItems = 0
#     for i in inventory.items():
#         print('{} {}'.format(i[1], i[0]))
#         totalOfItems += i[1]
#     print('Total number of items: {}'.format(totalOfItems))
#
# def addItems(inventory, newItems):
#     for item in newItems:
#         if item in inventory:
#             inventory[item] += 1
#         inventory.setdefault(item, 1)
#     print('New items added to inventory!' )
#
# addItems(bigBag,dragonLoot)
# showInventory(bigBag)