año_nacimiento=int(input('Ingrese el año cuando nacio: '))
año= 2025
Edad= año -año_nacimiento
print(f'Tu edad actual es de {Edad} años')
if Edad < 13: 
    print ("Esta en la etapa de la Infancia")
elif 13 <= Edad < 20:
    print('Estas en la etapa de la adolescencia')
elif 20 <= Edad < 65:
    print("Estas en la etapa de la adultez")
elif 65 <= Edad <= 110:
    print('Estas en la etapa de la tercera edad')
elif Edad >= 110:
    print('Estas muerto')
