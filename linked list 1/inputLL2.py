class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None 

def takeInput():
    inputlist = [int(x) for x in input().split()]
    head = None 
    tail = None
    for data in inputlist:
        if data == -1:
            break 
        newNode = Node(data)
        if head is None:
            head = newNode 
            tail = newNode
        else:
            tail.next = newNode 
            tail = newNode 
    return head 

def printLL(head):
    while head is not None:
        print(head.data,'->',end=' ')
        head = head.next 
    print('None')


if __name__ == '__main__':
    head = takeInput()
    printLL(head)