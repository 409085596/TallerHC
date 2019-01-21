n=12; gradosC=[-5 + i*0.5 for i in range(n)]
gradosF=[i*1.8+32 for i in gradosC]

ListaCombinada=[[C,F] for C,F in zip(gradosC,gradosF)]
print ListaCombinada
