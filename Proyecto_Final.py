import time
import os
import sys
def agenda():      #Este programa sirve para agregar, modificar, eliminar y consultar contactos de una agenda
	tareas = {}
	salir=True
	while(salir):

		print('Bienvenido A la lista de tareas\n')
		print(' 1.) Ver Tareas\n 2.) Agregar Tareas\n 3.) Buscar Tareas\n 4.) Modificar Tareas\n 5.) Eliminar Tareas\n 6.) Para ir al menú principal\n 7.) Para salir del programa')
		
		opcion=input('Escriba el número de la opción que desea ver: ')
		os.system('clear')
		if opcion == '1': # <----Muestra los contactos
			for contacto in contactos:
				for numero in contactos:
					print('Contacto / Número')
					print( numero,contactos[contacto])
				
			time.sleep(4)
			os.system('clear')

		elif opcion == '2': # <----Registra los Tareas
			nombre_tarea=input('Tareas: ')
			if nombre_tarea in tareas:
				print('Error el contacto ya existe')
				time.sleep(3)
				os.system('clear')
				continue
			try:
				nombre_tarea=string(input('Tarea: '))
				if nombre_tarea != string:
					print('El número es muy largo')
					time.sleep(3)
					os.system('clear')
					continue
				elif numero<100000000:
					print('El número es muy corto\n Deben de ser 9 digitos')
					time.sleep(2)
					os.system('clear')
					continue
				
			except:
				print('Valor no válido')
				time.sleep(3)
				os.system('clear')
			contactos[(nombre)] = numero
			print('Contacto agregado')
			print(contactos)
			time.sleep(3)
			os.system('clear')

		elif opcion == '3': # <----- Buscar Contacto
			buscar=input('Contacto a Buscar: ')
			print (contactos[buscar])
			time.sleep(3)
			os.system('clear')
			if buscar not in contactos:
				print('El contacto no existe., agréguelo desde el menú')
				continue

		elif opcion == '4': # <------- Modificar contacto
			contacto = input('Contacto a modificar: ')
			if contacto not in contactos:
				print ('El contacto no existe, agréguelo desde el menú')
				continue
			try:
				nuevo=int(input('Nuevo Número: '))
				contactos[contacto]=nuevo
				if numero>999999999:
					print('El numero es muy largo')
					time.sleep(3)
					os.system('clear')
					continue
				elif numero<100000000:
					print('El número es muy corto\nDeben de ser 9 digitos')
				print('Contacto modificado con éxito')
				time.sleep(3)
				os.system('clear')
				continue
			except:
				print('¡Dato no válido!')
				time.sleep(3)
				os.system('clear')
				continue

		elif opcion == '5':
			eliminar=input('Contacto a eliminar: ')
			if eliminar not in contactos:
				print ("El contacto no existe")
				continue
			del(contactos[eliminar])
			print('Contacto',eliminar,'eliminado con éxito')
			time.sleep(4)
			os.system('clear')
			continue
		elif opcion == '6': # <---- regresar al menú principal
			os.system('exit')
		elif opcion == '7': # <---- Para salir del programa
			sys.exit()
		else:
			print('opción no válida,\nElija una opción del 1 al 7')
			time.sleep(3)
			os.system('clear')
agenda()

