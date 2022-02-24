alt = float(input("Informe a sua altura: "))
sexo = (input("Informe o seu sexo H para homem M para mulher: "))

if sexo == 'H' or sexo == 'h':
    pesoIdeal = (72.7 * alt)-58
    print("O peso ideal é: ", pesoIdeal)
elif sexo == 'M' or sexo == 'm':
    pesoIdeal = (62.1 * alt) - 44.7
    print("O peso ideal é: ", pesoIdeal)
else:
    print("Você informou o comando errado.")
