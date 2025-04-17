#1. is_prime(n) funksiyasi
#s_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
n = int(input('Enter number that you whant to check: '))
def  is_prime(n): 
  if n % 2 != 0: 
    print('True')
  else:
    print("False")
is_prime(n)

# 2 Найдите сумму цифр данного числа
def sum_of_digits(a):
    num = 0 
    for digit in str(a): 
      num += int(digit)
    return num 

print(sum_of_digits(4567))



#3  Ikki sonning darajalari
daraja = int(input(" "))
d = range(1,daraja+1)
def sqr(daraja):
    for i in range(1,daraja+1):
     print(2**i)
sqr(daraja)
    
    

