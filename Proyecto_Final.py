# Bucle principal
while True:
    print("\n***** --- Gestor de tareas de ConsoleTec --- ******\n ")
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
            pass

        case "2":
			pass

        case "3":
			pass

        case "4":
			pass

        case "5":
		print("Saliendo... Gracias por haber usado el programa")
			pass

        case _:
			print("Esta opción no es válida. Inténtelo de nuevo.")
            pass
