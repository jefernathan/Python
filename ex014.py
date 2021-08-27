# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Digite a temperatura: '))

print(f'{temperatura}°C corresponde a {temperatura * 1.8 + 32:.1f}°F')
