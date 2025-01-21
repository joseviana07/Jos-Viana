precio=float(input('Ingrese el precio del producto: '))
miembro=input('Eres miembro de la tienda?(si/no) -->')
if miembro == 'si' and precio>=50:
    descuento=0.15
elif miembro== 'si':
    descuento=0.10
elif precio>=50:
    descuento=0.05
else:
    descuento=0
total=precio*(1 - descuento)
print(f'El precio final de el producto es de:{total}')
