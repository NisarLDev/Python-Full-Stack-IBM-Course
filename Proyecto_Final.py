# Clase creada Gestion_Tareas para la parte del modelo del Modelo Vista Controlador (MVC). Para CRUD.
class Gestion_Tareas:
		# Lista de tareas
		tareas = []

		# Funciones del programa
def agregar_tarea(lista):
    # Entrada para la tarea
    tarea = input("Introduzca la descripción de la tarea: ")

    # Añadir la tarea al final de la lista
    list.append(tarea)

    # Informe de tarea añadida
    print("\nLa tarea se añadió a la lista de tareas pendientes.\n")

    # Imprime la tarea añadida
    print("La tarea añadadida es esta:")

    print(f"{tarea}")

    # Informa del número de tarea
    print(f"La tarea se almacenó en la posición {len(list)}\n")

def ver_tareas(list):
    # Condicional que evalúe si algo está en la lista
    # Si hay algo en la lista se presenta
    if lista:
        for indice, tarea in enumerate(list):
            print(f"{indice + 1}. {tarea}")
    # Si la lista está vacía avisa de ello
    else:
        print("No hay tareas pendientes.")

    # Mensaje del final del listado
    print("--- FIN DEL LISTADO DE TAREAS ---")

def tarea_completada(lista):
    # Llamamos a la función ver_tareas()
    ver_tareas(list)

    # Entrada para que el usuario introduzca una tarea
    completada = int(input("Introduzca el número de la tarea a marcar como completada: "))

    # Condicional para marcar tareas como completadas
    if completada > 0 and completada <= len(list):
        # Condicional para evaluar si la tarea ya estaba completada
        # Si la tarea ya está en la lista...
        if "(Completada)" in lista[completada - 1]:
            print("La tarea ya estaba marcada como completada.")
        # En cambio, si no está...
        else:
            list[completada - 1] = "(Completada) " + list[completada - 1]
            print("Se marcó la tarea como completada.")
    # Avisar si la opción elegida es inválida
    else:
        print("Opción inválida.")

def eliminar_tarea(lista):

	if list:
		#Llamamos a la función ver_tareas()
		ver_tareas(list)

		# Entrada para que el usuario introduzca una tarea
		tarea = int(input("Introduzca el número de la tarea a eliminar: "))

		# Opción inválida si la tarea no está en el rango de la lista
		if tarea <= 0 or tarea > len(list):
			print("Opción inválida.")

		# Si la opción es válida se elimina la tarea
		else:
			del list[tarea - 1]
			print("Se eliminó la tarea.")

		# Si la lista está vacía se avisa de ello
	else:
		print("No hay tareas.")





# Bucle principal
while True:
    print("\n***** --- Gestor de tareas Python Full Stack Proyecto Final IBM 2024 --- ******\n ")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    print("\n")

     #Entrada de opcion para el usuario
    opcion = int(input("\nIngresar opcion: "))

    #Menu de opciones
    if opcion == 1:
        Gestion_Tareas.añadir_tareas(Gestion_Tareas.tareas)
    elif opcion == 2:
        Gestion_Tareas.ver_tareas(Gestion_Tareas.tareas)
    elif opcion == 3:
        Gestion_Tareas.marcar_completada(Gestion_Tareas.tareas)
    elif opcion == 4:
        Gestion_Tareas.eliminar_tarea(Gestion_Tareas.tareas)
    elif opcion == 5:
        break
