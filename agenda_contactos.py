def show_menu():
    print("\nAgenda de contactos: ")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")

def add_contact(book):
    name = input("Por favor introduce el nombre del contacto: ")
    phone = input("Por favor introduce el número de contacto: ")
    if phone.isdigit():
        phone = int(phone)
    else:
        print("El número de teléfono debe ser numérico.")
    email = input("Por favor introduce el correo electrónico: ")

    book[name] = {"Teléfono": phone, "email":email}
    print(f"Se ha agregado el contacto {name} exitosamente")

def delete_contact(book):
    name = input("Ingrese el nombre del contacto que desea eliminar: ")
    if name in book:
        del book[name]
        print(f"el contacto de {name} hasido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {name}")

def looking_contact(book):
    name = input("Ingrese el nombre del contacto que desea buscar: ")
    if name in book:
        print(f"Nombre: {name}")
        print(f"Teléfono: {book[name]['Teléfono']}")
        print(f"Email: {book[name]['email']}")
    else:
        print(f"El contacto {name} no ha sido encontrado en la agenda")

def contact_list(book):
    if book:
        print("\nLista de contactos: ")
        for name, info in book.items():
            print(f"Nombre: {name}")
            print(f"Teléfono: {info['Teléfono']}")
            print(f"Email: {info['email']}")
            print('-'*15)
    else:
        print("La agenda aún está vacía")

def contact_book():

    book = {}

    while True:
        show_menu()
        option = input("Elija una opción: ")

        if option == "1":
            add_contact(book)
        elif option == "2":
            delete_contact(book)
        elif option == "3":
            looking_contact(book)
        elif option == "4":
            contact_list(book)
        elif option == "5":
            print("Saliendo de la agenda de contactos")
            break
        else:
            print("Por favor, escoja una opción válida (del 1 al 5)")

contact_book()
