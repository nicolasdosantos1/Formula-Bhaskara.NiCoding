#NiCoding / EP1 - Python: Equações do 2º grau
#Fórmula de Bhaskara

import math #importação da biblioteca de modularidade "math"

#
# 1) Inserção de dados do usuário + Fórmula de Delta com os dados inseridos e impressão
#

a = float(input('Qual o valor de a ?')) #inserção de dados inteiros pelo usuário (a)
b = float(input('Qual o valor de b ?')) #inserção de dados inteiros pelo usuário (a)
c = float(input('Qual o valor de c ?')) #inserção de dados inteiros pelo usuário (a)

delta = b ** 2 - (4 * a * c) #fórmula de delta com uso de operadores matemáticos

print('') #print para espaço (se repete durante todo o código)
print(f'O valor de Δ é {delta}') #imprimir o valor da fórmula de delta
print('')

#
# 2) Estrutura condicional do valor de delta + Fórmula de Bhaskara restante no código + Impressão dos dados
#

if delta < 0: #estrutura condiconal padrão (if e else)
    print('Não existem raízes reais.') #imprimir texto de primeiro caso if
else: #execução do restante da fórmula de bhaskara com os dois dados + ou - (±)
   x1 = (-b + math.sqrt(delta)) / (2 * a) #executar primeiro com soma
   x2 = (-b - math.sqrt(delta)) / (2 * a) #executar depois com subtração

print(f'O valor de x¹ é {x1}') #imprimir valor da variável x1
print(f'O valor de x² é {x2}') #imprimir valor da variável x2
print('')

#
# 3) Cálculos adicionais e impressão dos mesmos para desenvolver o plano cartesiano (Vértice da Parábola + Intercepto Y + Concavidade)
#

Xv = -b / (2 * a) #fórmula de cálculo do vértice da parábola
Yv = -delta / (4 * a) #fórmula de cálculo do vértice da parábola
 
print(f'O Vértice da Parábola é: {Xv} e {Yv}.')
print('')

print(f'O Intercepto Y é: 0, {c}.') #indentificação do intercepto Y e impressão

print('')
print('Concavidade da parábola:')
print('')

if a > 0: #estrutura condicional de concavidade
    print('Concavidade voltada para cima.')
elif a < 0: 
    print('Concavidade voltada para baixo.')