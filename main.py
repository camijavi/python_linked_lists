from listExample import Contact, LinkedList

def main():
    list = LinkedList()
    c = Contact("85458745", "Julissa Parrales", "Claro", 3)
    list.insert(c)
    c = Contact("69784521", "Julio Aragón", "Tigo", 4) 
    list.insert(c)
    c = Contact("85458745", "Julissa Parrales", "Claro", 3)
    list.insert(c)
    c = Contact("78548569","Paulo Andino", "Claro", 5)
    list.insert(c)

    list.print()

main()