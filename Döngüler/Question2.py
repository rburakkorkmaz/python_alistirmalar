n = int(input("Lütfen bir N tamsayısı giriniz.\n"))
sum = 0
for number in range(1, n+1):
  sum = sum + number
print(f"{n}'e kadar olan sayıların toplamı: {sum}")