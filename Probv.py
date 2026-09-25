#diccionario
contactos = {}

while True:
    print("\n1. Agregar contacto\n2. Mostrar contactos\n3. Eliminar contacto\n4. Buscar contacto\n5. Salir")
    opcion = input("Opción: ")

    #Insertar datos
    if opcion == '1':
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        contactos[nombre] = telefono

    #Mostrar información
    elif opcion == '2':
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre} - Teléfono: {telefono}")

    #Operación eliminar
    elif opcion == '3':
        nombre = input("Nombre a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]

    #Operación buscar
    elif opcion == '4':
        nombre = input("Nombre a buscar: ")
        if nombre in contactos:
            print(f"Teléfono de {nombre}: {contactos[nombre]}")
            
    elif opcion == '5':
        break