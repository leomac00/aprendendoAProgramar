def spam():
    global eggs
    eggs='spam this is the global' #this is the global
def bacon():
    eggs='bacon this is local'#this is local
def ham():
    print(eggs)#this is the global

eggs=42 #global
spam()
print(eggs)
print('--------------')
bacon()
print(eggs)
