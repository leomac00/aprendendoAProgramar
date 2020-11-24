def spam():
    eggs='spam local'
    print(eggs)
def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs='global'
print('printando bacon-----------')
bacon()
print(eggs)
print('printando spam------------')
spam()
print(eggs)
