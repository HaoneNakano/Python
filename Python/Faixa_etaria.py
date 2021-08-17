import datetime
today = datetime.date.today()
todaynow = datetime.datetime.now()
print("Hoje é (completo): ", todaynow)
print("Hoje é (simplificado): ", today)

nascimento = int(input("Digite ano de nascimento: "))
idade = todaynow.year - nascimento
print("Sua idade é: ", idade)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")
