import math

print("="*30)
print("Área y perímetro del círculo")
print("="*30)

# input
r = int(input("Digite el valor del radio: "))
r= int(r)

# processing
p = 2 * math.pi * r
a = math.pi * r * r

# output
print("="*30)
print("El área es: " + str(a))
print("El perímetro es: " + str(p))
print("="*30)
