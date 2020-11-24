# Heart with grid project
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

spam = 0
eggs = 0
bacon = ''

for eggs in range (0,6): #as the book hints we should go row by row so that's why this first 'for'
    for spam in range (0,9):
        bacon += '{}  '.format(grid[spam][eggs]) # Here we swap rows with columns because we want to transpose it; we start by increasing the first value,that's why we use 'spam' first and 'eggs' on the second '[]' and then we proced to the next line.
    print('{}'.format(bacon)) # Here we print the line created for 'bacon'
    bacon = '' #then we need to reset this because otherwise it will stack multiple 'bacons' together
print('There`s our pretty heart!')