def areatriangulo():
  print("¿Me puedes decir cual es la base del triangulo? Por favor")
  B= input()
  B= int(B)
  print("Gracias, ahora puedes decirme la altura del triangulo?")
  a=input()
  a=int(a)
  A=(B*a)/2
  print("El area total de este triangulo es:", A)
   
areatriangulo()
