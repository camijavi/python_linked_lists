class Contact:
    def __init__(self, phoneNumber: str, name: str, network: str, rank: int):
        self.phoneNumber = phoneNumber
        self. name = name # order key 
        self.network = network
        self.rank = rank
        self.next = None # It's neccesary since it's a linked list

    def print(self):
        print(f"{self.name} | {self.phoneNumber}: {self.network}")
