
lista_compras = []

while True:
    
  producto =  input("Ingrese el nombre del producto (o 'terminar' para finalizar): "
)
  print(f"Lista de compras{producto}")
  
  if producto== 'terminar':
    break


  lista_compras.append(producto)

  print (lista_compras)

  for producto in lista_compras:
    print(producto)