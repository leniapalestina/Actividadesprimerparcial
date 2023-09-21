def multiplicación (a,b):
  x = a * b
  return x 

def división (a,b):
  x=a/b
  return x

print("Dame el primer número:")
a= int(input())
print("Dame el segundo número:")
b= int(input())
print("Si multiplicas los números el resultado es:", multiplicación (a,b),"Y si los divides es:", división(a,b),)
