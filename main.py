from listExample import Contact, Linkedlist

def main():
    lista = Linkedlista()
    c = Contact("85458745", "Julissa Parrales", "Claro", 3)
    lista.insert(c)
    c = Contact("69784521", "Julio Aragón", "Tigo", 4) 
    lista.insert(c)
    c = Contact("85458745", "Julissa Parrales", "Claro", 3)
    lista.insert(c)
    c = Contact("78548569","Paulo Andino", "Claro", 5)
    lista.insert(c)

    lista.print()
    lista.print("*"*20)
    lista.remove("Julissa Parrales")
    lista.print()


main()