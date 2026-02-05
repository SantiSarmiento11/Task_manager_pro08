import json
import os

#Este es un cambio de informacion de y de prueba de la rama
def menu():
    tareas = cargar_tareas()

    while True:
        print("""
TASK MASTER PRO
1. Ver tareas
2. Agregar tarea
3. Completar tarea
4. Eliminar tarea
5. Salir
        """)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()


