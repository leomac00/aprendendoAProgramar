import random
def resposta(nresp):
    if nresp==1:
        return 'Com certeza'
    elif nresp==2:
        return 'Sim'
    elif nresp==3:
        return 'Decididamente'
    elif nresp==4:
        return 'Tente de novo'
    elif nresp==5:
        return 'Pergunte depois'
    elif nresp==6:
        return 'Concentre-se e pergunte depois'
    elif nresp==7:
        return 'Minha resposta é não'
    elif nresp==8:
        return 'Não parece muito bom'
    elif nresp==9:
        return 'Muito pouco provável'
r=random.randint(1,9)
magica=resposta(r)
print(magica)
    
    
