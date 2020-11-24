
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(array):
    colWidths = [0]*len(array)
    for i in range (len(array)):
        colWidths[i] = len(max(array[i], key = len))

    for i in range (len(array[0])):
        for j in range (len(array)):
            print(array[j][i].rjust(colWidths[j], ' '), end = ' ')
        print()

printTable(tableData)
