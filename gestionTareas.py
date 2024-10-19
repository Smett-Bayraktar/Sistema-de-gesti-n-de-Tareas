#Sistema de Gestion de tareas

opcion = 0
lista = []

print("Bienvenido al sistema de creacion de tareas")
print("Eliga una opcion \n")
while opcion != 5:
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Actualizar tarea")
    print("5. Salir \n")
    opcion = int(input("Escogiendo: "))
    
    aux = [] #Creamos una variable auxiliar para guardar los indices 0, 1, 2...etc
    for i in range(len(lista)):
        aux.append(i)

    match opcion:
        case 1:
            agregar = input("Agregar tarea: ").capitalize()
            if agregar in lista:
                print("La tarea ya existe")
            else:
                lista.append(agregar)
                print()
                print("Tarea agregada!")
            print("-"*20)
        case 2:
            if lista == []:
                print()
                print("Cree una tarea antes.")
            else:
                for i in range (len(lista)):
                    print()
                    print(f"id {i} - {lista[i]}")
            print("-"*20)
        case 3:
            eliminar = int(input("Ingrese el id: "))
            
            if eliminar in aux: #Preguntamos si el id que le pasamos esta dentro de la lista aux significa que el id si existe en la lista principal con la tarea
                lista.pop(eliminar)
                print()
                print("Eliminado con exito")
            else:
                print()
                print("Id no encontrado")
            print("-"*20)
        case 4:
            actualizar = int(input("Ingrese el id de la tarea ah actualizar: "))
            if actualizar in aux:
                textoActualizar = input("Actualice la tarea: ")
                lista.pop(actualizar)
                lista.insert(actualizar, textoActualizar)
                print()
                print("Actualizado con exito")
            else:
                print()
                print("Id no encontrado")   
            print("-"*20)
        case 5:
            print()
            print("Hasta luego :)")
        case _:
            print("Ingrese una opcion valida")

print("El programa ah finalizado!")