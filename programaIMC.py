peso = float(input("digite o seu peso em quilos :"))
altura = float(input("digite a sua altura em metros :"))

imc = peso/(altura*altura)

print("Seu Índice de Massa Corporal é ", str(imc))

if imc < 18.5:
	print("Abaixo do peso")

elif imc >18.6 and imc <24.9:
	print("Peso ideal (Parabéns)")

elif imc >25.0 and imc <29.9:
	print("Levemente acima do peso")

elif imc >30.0 and imc <34.9:
	print("Obesidade grau I")

elif imc >35.0 and imc <39.9:
	print("Obesidade grau II (severa)")

else:
	print("Obesidade Grau III (mórbida)")