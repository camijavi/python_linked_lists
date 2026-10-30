class Contact:
    def __init__(self, phoneNumber: str, name: str, network: str, rank: int):
        self.phoneNumber = phoneNumber
        self. name = name # order key 
        self.network = network
        self.rank = rank
        self.next = None # It's neccesary since it's a linked list

    def print(self):
        print(f"{self.name} | [{self.phoneNumber}:{self.network}-{self.rank}]")


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new: Contact)-> bool:   # receive contact as new and return bool value
        ''' Return True if insert and false if node already exists'''
       

        # Empty lists
        if self.head == None:
            self.head = new
            return True

        # Has 1 or more nodes
        if new.name.lower() < self.head.name.lower():
            new.next = self.head 
            self.head = new
            return True 

        # new node > or new last 
        if new.name.lower() > self.head.name.lower():
            previous = self.head
            temporalVariable = self.head.next

            while temporalVariable != None:
                if new.name.lower()> temporalVariable.name.lower():
                    previous = temporalVariable
                    temporalVariable = temporalVariable.next
                else:
                    previous.next = new
                    new.next = temporalVariable
                    return True
            previous.next = new
            return True
        return False

    def print(self):
        if self.head == None:
            print("Lista vacía...")
        else:
            temporalVariable = self.head
            while temporalVariable != None:
                temporalVariable.print()
                temporalVariable = temporalVariable.next

    def remove (self, name: str)-> Contact:
        contact = None
        if self.head == None:
            return contact
        
        if name.lower() == self.head.name.lower():
            prefix =self.head
            contact = Contact(prefix.phoneNumber, prefix.name, prefix.network, prefix.rank)
            self.head = self.head.next
            return contact
        
        if name.lower() > self.head.name.lower():
            previous = self.head

            temporalVariable = self.head.next
            while temporalVariable != None:
                if name.lower() == temporalVariable.name.lower():
                    previous.next = temporalVariable.next
                    return Contact(
                        temporalVariable.phoneNumber,
                        temporalVariable.name,
                        temporalVariable.network,
                        temporalVariable.rank,
                    )
                else:
                    previous = temporalVariable
                    temporalVariable = temporalVariable.next
        return None