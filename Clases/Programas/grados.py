def listaC(Cmin, Cmax, n):
    gradosC = []
    dC = (Cmax-Cmin)/float(n-1)
    for i in range(n):
        C=Cmin+i*dC
        gradosC.append(C)
    return gradosC

def listaF(gradosC):
    gradosF = []
    for C in gradosC:
        F=(9.0/5)*C+32
        gradosF.append(F)
    return gradosF

def mostrarListas(gradosC, gradosF):
    for i in range(len(gradosC)):
        C = gradosC[i]
        F = gradosF[i]
        print "%5.1f %5.1f" %(C, F)

def mostrarListas1(gradosC, gradosF):
    for C,F in zip(gradosC,gradosF):
        print "%5.1f %5.1f" %(C,F)
