from listExample import Contact, LinkedList

def main():
    lista = LinkedList()
    c = Contact("85458745", "Julissa Parrales", "Claro", 3)
    lista.insert(c)
    c = Contact("69784521", "Julio Aragón", "Tigo", 4) 
    lista.insert(c)
    c = Contact("85458745", "Amelia West", "Claro", 3)
    lista.insert(c)
    c = Contact("78548569","Paulo Andino", "Claro", 5)
    lista.insert(c)

    lista.print()
    print("*"*20)
    lista.remove("Julissa Parrales")
    lista.print()


main()