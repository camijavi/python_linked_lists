class Contact:
    def __init__(self, phoneNumber: str, name: str, network: str, rank: int):
        self.phoneNumber = phoneNumber
        self. name = name # order key 
        self.network = network
        self.rank = rank
        self.next = None # It's neccesary since it's a linked list

    def print(self):
        print(f"{self.name} | [{self.phoneNumber}:{self.network}-{sefl.rank}]")


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