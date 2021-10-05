base=int(input("Введите основание системы счисления:"))
n=int(input("Введите целое положительное число:"))
k=''
if base==8 or base==2:
	while n>0:
		k=str(n%base)+k
		n//=base
else:
	print("Ошибка")
print(k)