#Feito por Leonardo Machado;
print('-----------------------------------------------------------')
print('Este programa serve APENAS para barras medianamente esbeltaz.')
print('-----------------------------------------------------------')
print("Digite o comprimento da barra mais comprimida(L efetivo)[cm]:")#70.500cm;float(input())
lef=70.500
print("Digite o valor de Ncd máximo já com o peso próprio aplicado[kN]:")#4.674kN;
ncd=4.674
print("Digite o valor de Ntd máximo já com o peso próprio aplicado[kN]:")#4.183kN;
ntd=4.183
#Material=E. Saligna;
print("Digite o valor de Ecof[kN/cm2]:")#836.248kN/cm2;
ecof=836.248
print("Digite o valor de fcod[kN/cm2]:")#1.310kN/cm2;
fcod=1.310
print("Digite o valor de ftod[kN/cm2]:")#2.080kN/cm2;
ftod=2.080
print("Digite o valor de b inicial[cm]:")
b=float(input())#Foi fixado esse valor pois para valores menores que isso o fator de comparação é menor que 0;
comp=25.0#Foi fixado para que o programa pudesse atender ao critério inicial do loop "while";

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
while comp>1.00:
    b=b+0.00001
    h=1.9*b
    inercia=(b*h**3)/12
    ea=lef/300
    ei=h/30
    eum=ei+ea
    fe=(3.14**2*ecof*inercia)/(lef**2)
    ed=eum*((fe)/(fe-ncd))
    md=ncd*ed
    wf=(inercia)/(h/2)
    tmd=md/wf
    tcd=ncd/(b*h)
    comp=(tmd+tcd)/(fcod) 

print("b[cm]: "+str(b))
print("h[cm]: "+str(h))
print("Momento de inércia[cm4]: "+str(inercia))
print("ea[cm]: "+str(ea))
print("ei[cm]: "+str(ei))
print("e1[cm]: "+str(eum))
print("Fe[kN]: "+str(fe))
print("ed[cm]: "+str(ed))
print("Md[kN.cm]: "+str(md))
print("wf[cm3]: "+str(wf))
print("T(Md)[kN/cm2]: "+str(tmd))
print("T(cd)[kN/cm2]: "+str(tcd))
comp=round(comp, 4)
print("Fator de comparação: [T(Md)+T(cd)]/fc0d = "+str(comp))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('Conforme  os resultados para "b", "h" e conquentemente "hc" deve-se adotar um "b" maior do que o obtido, para que assim quando as tensões passaram pela seção de "hc" a verificação de compressão seja validada')
print('Digite um novo valor para "b" em [cm], que seja maior do que o "b" já obtido:')
b=float(input())
print('Digite um novo valor para "h" em [cm], que seja maior do que o "h" já obtido:')
h=float(input())
hc=h*(1-0.12)
print('hc[cm]='+str(round(hc, 2)))
print('-----------------------------------------------------------')
#Inicio da verificação de Tração;
print('-----------------------------------------------------------')
print("Verficação da Tensão de Tração para a menor seção("+str(b)+"x"+str(hc)+"[cm]):")
vtra=ntd/(b*hc)
vtra=round(vtra, 4)
print(str(ntd)+"/("+str(hc)+" x "+str(b)+")="+str(vtra))
if vtra<=ftod:
    print("Está Ok com relação à NBR 7190.")
else:
        print("Não atende aos critérios da NBR 7190, é necessário que se adote uma seção maior.")
print('-----------------------------------------------------------')
#Inicio da verificação de Compressão;
print('-----------------------------------------------------------')
print("Verficação da Tensão de compressão para a menor seção("+str(b)+"x"+str(hc)+"[cm]):")
inercia=(b*hc**3)/12
ea=lef/300
ei=h/30
eum=ei+ea
fe=(3.14**2*ecof*inercia)/(lef**2)
ed=eum*((fe)/(fe-ncd))
md=ncd*ed
wf=(inercia)/(h/2)
tmd=md/wf
tcd=ncd/(b*h)
comp=(tmd+tcd)/(fcod) 
comp=round(comp, 4)
print("Fator de comparação: [T(Md)+T(cd)]/fc0d = "+str(comp))
if comp<=1:
    print("Está Ok com relação à NBR 7190.")
else:
        print("Não atende aos critérios da NBR 7190, é necessário que se adote uma seção maior.")
print('-----------------------------------------------------------')
#Fim das verificações;
print('-----------------------------------------------------------')
print("Digite qualquer coisa para fechar o programa:")
fecha=input()

