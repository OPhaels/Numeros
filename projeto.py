
num1 = int(input('Digíte um número: '))
while num1 != int:
    print('Por favor, verifique os campos selecionados: ')
    num1 = int(input('Digíte um número: '))

num2 = str(input('Qual é a formula desejada? (+) (-) (*) (/) :  '))
while num2 != '+' and num2 != '-' and num2 != '*' and num2 != '/':
    print('Por favor, verifique os campos selecionados: ')
    num2 = str(input('Qual é a formula desejada? (+) (-) (*) (/) :  '))

num3 = int(input('Digíte outro número ou digíte '))
while num1 != int:
    print('Por favor, verifique os campos selecionados: ')
    num1 = int(input('Digíte um outro número: '))


if num2 == '+':
    print(num1 + num3, end='')
elif num2 == '-':
    print(num1 - num3, end='')
elif num2 == '*':
    print(num1 * num3, end='')
else:
    print(num1 / num3, end='')



print(f'Seu cálculo entre {num1} e {num3} é igual a: ')


