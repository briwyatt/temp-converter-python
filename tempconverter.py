# 
# created this temp-converter as homage to my growth as a software developer since my first days learning to code in Javascript
# compare this to my first stab at creating a temp-converter using vanilla Javascript: https://github.com/briwyatt/temp-converter
# 
# Ask the user for a temperature in Celsius
celsius = int(input('Temp. in Celsius:    '))

#  Calculate the conversion
fahrenheit = celsius*9/5 + 32

#   Ouput the converted temperature as a result
print(fahrenheit, 'Fahrenheit')
