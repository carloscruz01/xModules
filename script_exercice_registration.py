#Aqui estarão outras variaveis, que irá armazenar os valores inseridos pelo usuário na lista.
w = 2
names = []
ages = []
emails = []
telefones = []
separacao = []
#A estrutura de repetição contém varias de interação com usuário.
for y in range(w):
    name = str(input('Enter your name:'))
    age = int(input('Enter your age:'))
    email = input('Sign in with an email:')
    telefone = int(input('Enter a number phone:'))
    separar = str('__________')
#"""Append irá adicionar um tipo int or str or float ao final de uma lista."""
    names.append(name)
    ages.append(age)
    emails.append(email)
    telefones.append(telefone)
    separacao.append(separar)
for y in range(w):
    print('Name:\t', names[y])
    print('Age:\t', ages[y])
    print('E-mail:\t', emails[y])
    print('Phone:\t', telefones[y])
    print(separacao[y])
