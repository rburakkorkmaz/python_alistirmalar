def faktöriyel(n):
  if n == 1:
    return 1
  return n*faktöriyel(n-1)


n = int(input("Lütfen sayı giriniz\n"))
print(f"Sum: {faktöriyel(n)}")
