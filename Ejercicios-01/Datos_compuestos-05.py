def poker(*_poker):
    tupla[]=_poker
    counter=0
    counter2=0
    devolver_si_poker='poker'
    no_poker='No hay un poker'

for j in range(5):
    carta=tupla[j][0]
    for i in range(counter2,5):
        if carta==tupla[i][0]:
           counter +=1
    if counter==4:
        print (devolver_si_poker)
    else :
         print( no_poker)


    counter=0
    counter2 +=1

print(poker('4h','4s','Ad','3p','4s'))
