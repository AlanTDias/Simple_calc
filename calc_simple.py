a = int (input('Digite o primeiro valor:\n' ))
b = int (input('Digite o segundo valor :\n'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#modos de print
#modo1
print ('soma:  {} \n subtracao: {} \n multiplicacao: {} \n divisao: {} \n resto {} '
       .format (soma,
                subtracao,
                multiplicacao,
                divisao,
                resto ))

#modo2
#print ('soma: {som} subtracao: {sub} multiplicacao: {mult} divisao: {div} resto {rest} '.format (som=soma, sub=subtracao, mult=multiplicacao, div=divisao, rest=resto ))


#modo3
# print ('soma: ' + str (soma) )
# print ('subtracao: ' + str (subtracao))
# print ('multiplicacao: ' + str (multiplicacao))
# print ('divisao: ' + str (divisao))
# print ('resto: ' + str (resto))

# x = '2'
# soma2 = int(x) + 1
# print ("Soma2: " + str (soma2))