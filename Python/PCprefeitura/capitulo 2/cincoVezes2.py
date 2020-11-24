i=0
while i<10:
    print('REPETI: '+str(i+1))
    i=i+1
    print('deseja sair?s=sim;qlq coisa=n')
    terminator=input()
    if terminator=='s':
        break
    else:
        continue
print('prontinho!')
