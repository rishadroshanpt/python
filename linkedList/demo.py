class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        newNode = Node(val)
        
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.val,end=' -> ')
            temp = temp.next
        print('None')

ll = LinkedList()
while True:
    val = input(' Enter a element or q to quit : ')
    if val.lower() == 'q':
        break
    ll.insert(int(val))
ll.display()
