#Feito por Leonardo Machado;
print("Digite o comprimento da barra mais comprimida(L efetivo)[cm]:")
lef=float(input())
print("Digite o valor de Ncd máximo já com o peso próprio aplicado[kN]:")
ncd=float(input())
print("Digite o valor de Ecof[kN/cm2]:")
ecof=float(input())
print("Digite o valor de fcod[kN/cm2]:")
fcod=float(input())
b=1.5#Foi fixado esse valor pois para valores menores que isso o fator de comparação é menor que 0;
comp=25.0#Foi fixado para que o programa pudesse atender ao critério inicial do loop "while";
while comp>1.00:
    b=b+0.0001
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
print("Momento de inercia[cm4]: "+str(inercia))
print("ea[cm]: "+str(ea))
print("ei[cm]: "+str(ei))
print("e1[cm]: "+str(eum))
print("Fe[kN]: "+str(fe))
print("ed[cm]: "+str(ed))
print("Md[kN.cm]: "+str(md))
print("wf[cm3]: "+str(wf))
print("T(Md)[kN/cm2]: "+str(tmd))
print("T(cd)[kN/cm2]: "+str(tcd))
print("Comparação entre tensões e fc0d: "+str(comp*100)+"%")
print("Digite qualquer coisa para fechar o programa")
fecha=input()

