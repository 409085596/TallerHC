C = -20
iC = 5
gradosC = []
while C <= 40:
    F = (9.0/5)*C +32
    print C, F
    #C = C + iC
    gradosC.append(C)
    C += iC
print '\n'

print '   c    F'
for grado in gradosC:
    F=(9.0/5)*grado+32
    print '%5d %5.1f' %(grado, F)
print '\n'

indice = 0
print '   c    F'
while indice < len(gradosC):
    C = gradosC[indice]
    F=(9.0/5)*C+32
    print '%5d %5.1f' %(C, F)
    indice += 1
print '\n'

gradosC=[]
for C in range(-20,45,5):
    gradosC.append(C)
print gradosC
print '\n'

gradosC=[]
for i in range(0,21):
    C=-20 + i*2.5
    gradosC.append(C)
print gradosC
print '\n'
