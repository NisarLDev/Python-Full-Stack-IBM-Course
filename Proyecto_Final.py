

# Bucle principal
while True:
    print("\n***** --- Gestor de tareas Python Full Stack Proyecto Final IBM 2024 --- ******\n ")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    # Entrada para el usuario
    opcion = input("Introduzca una opción: ")

    print("\n")

    # Menú de opciones
       match opcion:
        case "1":
            Gestion_Tareas.agregar_tarea(funciones.tareas)

        case "2":
            Gestion_Tareas.ver_tareas(Gestion_Tareas.tareas)

        case "3":
            Gestion_Tareas.tarea_completada(Gestion_Tareas.tareas)

        case "4":
            Gestion_Tareas.eliminar_tarea(Gestion_Tareas.tareas)

        case "5":
		print("Saliendo... Gracias por haber usado el programa")
			break

        case _:
			print("Esta opción no es válida. Inténtelo de nuevo.")
            break
	# Clase creada Gestion_Tareas para la parte del modelo del Modelo Vista Controlador (MVC). Para CRUD.
	class Gestion_Tareas:
		# Lista de tareas
		tareas = []

		# Funciones del programa
		def agregar_tarea(lista):
    		# Entrada para la tarea
    		tarea = input("Introduzca la descripción de la tarea: ")

    		# Añadir la tarea al final de la lista
    		lista.append(tarea)

    		# Informe de tarea añadida
    		print("\nLa tarea se añadió a la lista de tareas pendientes.\n")

    		# Imprime la tarea añadida
    		print("La tarea añadadida es esta:")

    		print(f"{tarea}")

    		# Informa del número de tarea
    		print(f"La tarea se almacenó en la posición {len(lista)}\n")

		def ver_tareas(lista):
    		# Condicional que evalúe si algo está en la lista
    		# Si hay algo en la lista se presenta
    		if lista:
        		for indice, tarea in enumerate(lista):
            		print(f"{indice + 1}. {tarea}")
    		# Si la lista está vacía avisa de ello
    		else:
        		print("No hay tareas pendientes.")

    		# Mensaje del final del listado
    		print("--- FIN DEL LISTADO DE TAREAS ---")

		def tarea_completada(lista):
			pass

		def eliminar_tarea(lista):
			pass
