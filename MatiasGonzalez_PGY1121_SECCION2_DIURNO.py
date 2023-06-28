import os
os.system ("cls")

ListaProductos  = []
ListaCodigos = []
ListaNombre = []
ListaCategoria = []
ListaPrecios = []
ListaStock = []
MENU = """
   MENU
1. Registrar Producto
2. Buscar Producto
3. Listar producto
0. Salir
"""
while True:
    try:
          opc = int(input(MENU))
          if opc == 0:
               print ("Hasta luego")
               break
          elif opc == 1:
            while True: 
             try:
               codigo = int(input("Codigo: "))
               if codigo >= 100000 and codigo <= 1000000:
                ListaCodigos.append(codigo)
                break
               else:
                print("El codigo tiene que ser mayor a 6 digitos")
             except:
                print ("Ha ocurrido una excepcion")
    #Fin del while de codigo
            while True:
             try:
              nombre = input("nombre: ")
              if len(nombre) >= 2 and len(nombre) <= 50:
                ListaNombre.append(nombre)
                break
              else:
                print ("El nombre del producto tiene que ser entre 2 a 50 caracteres")
             except: 
              print ("Ha ocurrido una excepcion")
    #Fin del while de Nombre
            while True:
              try:
                 categoria = input ("Paquete o Sobre: ")
                 if categoria == "paquete" or categoria == "sobre":
                  ListaCategoria.append(categoria)
                  break
                 else:
                  print("El nombre de la categoria debe tener al menos 2 caracteres para ser valido")
              except:
               print("Ha ocurrido una excepcion")
    #Fin del while de categoria
            while True:
              try:
                precio = int(input("Precio: "))
                if precio > 0:
                  ListaPrecios.append(precio)
                  print(precio)
                  break
                else:
                  print ("Ha ocurrido un error, el precio debe ser mayor a 0")

              except:
                print ("Ha ocurrido una excepcion")
    #Fin del while de precio
            while True:
              try:
                stock = int (input("Stock: "))
                if stock > 0:
                  ListaStock.append(stock)
                  break
                else:
                  print ("El numero tiene que ser mayor a 0")
              except:
                print ("Ha ocurrido una excepcion")
          elif opc == 2:
            print ("OPCION 2")
            print ("BUSQUEDA DEL PRODUCTO")
            print ("N° CODIGO | NOMBRE PRODUCTO          | CATEGORIA    | PRECIO | STOCK |")
            print ("----------|--------------------------|--------------|--------|-------|")
            buscar = int(input("Ingrese el codigo de 6 digitos de la categoria que requiere buscar: "))
            print (f"Codigo a buscar: {buscar} \n")
            for i in range (len(ListaCodigos)):
                if buscar == ListaCodigos[i] and buscar >= 100000 and buscar < 1000000:
                    print(f"{i+1} | {ListaCodigos[i]:6d} | {ListaProductos[i]:20s} | {ListaCategoria[i]:10s} | {ListaPrecios[i]:8d} | {ListaStock[i]:6d}")

          elif opc == 3:
             print ("OPCION 3")
             print ("LISTA DE PRODUCTOS")
             print ("N° CODIGO | NOMBRE PRODUCTO          | CATEGORIA    | PRECIO | STOCK |")
             print ("----------|--------------------------|--------------|--------|-------|")
             conts = 0
             for i in range (len(ListaCodigos)):
              if ListaStock [i] < 5:
               stock = "Quedan pocos productos"
              else:
               print ("Quedan muchos productos")
               print(f"{i+1} | {ListaCodigos[i]:6d} | {ListaProductos[i]:20s} | {ListaCategoria[i]:10s} | {ListaPrecios[i]:2d} | {ListaStock[i]:6d}")
    except:
       print ("Ha ocurrido una excepcion")
