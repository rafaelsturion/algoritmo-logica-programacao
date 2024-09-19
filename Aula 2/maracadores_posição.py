nota = 8.5
mensagem = 'Você tirou %f na disciplina de Lógica de Programação e Algoritmos' % nota
print(mensagem)
mensagem2 = 'Você tirou %.2f na disciplina de Lógica de Programação e Algoritmos' % nota #.2 limita a quantidade de casas decimais
print(mensagem2)



nome = 'João'
mensagem3 = '%s, você tirou %.2f na disciplina de Lógica de Programação e Algoritmos' % (nome, nota)   
print(mensagem3) 

#Composição moderna

mensagem4 = '{}, você tirou {} na disciplina de Lógica de Programação e Algoritmos'.format(nome, nota)
print(mensagem4)

# Composção com f-string

mensagem5 = f'{nome}, você tirou {nota} na disciplina de Lógica de Programação e Algoritmos'