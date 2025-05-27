n = int(input())
#%- resto

cem = n//100

cinquenta = (n % 100)//50
resto50 = (n % 100) % 50
vinte = (resto50)//20
resto20 = (resto50 % 20)
dez = resto20//10
resto10 = (resto20 % 10)
cinco = resto10//5
resto5 = (resto10 % 5)
dois = resto5//2
resto2 = (resto5 % 2)
um = resto2//1

print(n)
print(cem, 'nota(s) de R$ 100,00')
print(cinquenta, 'nota(s) de R$ 50,00')
print(vinte, 'nota(s) de R$ 20,00')
print(dez, 'nota(s) de R$ 10,00')
print(cinco, 'nota(s) de R$ 5,00')
print(dois, 'nota(s) de R$ 2,00')
print(um, 'nota(s) de R$ 1,00')
