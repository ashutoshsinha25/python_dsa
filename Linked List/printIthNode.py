'''
For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.
'''
class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 

def takeInput():
    inputlist = [int(x) for x in input().split()]
    head = tail = None 
    for data in inputlist:
        if data == -1:
            break 
        newNode = Node(data)
        if head is None:
            head = tail = newNode 
        else:
            tail.next = newNode 
            tail = newNode 
    return head 

def printLL(head):
    while head is not None:
        print(f'{head.data} ->',end=' ')
        head = head.next 
    print('None')

def printIthNode(head , i):
    curr = 0
    while head is not None:
        if curr == i:
            return head.data
        curr+=1
        head = head.next
    return None

if __name__ == '__main__':
    head = takeInput()
    i = int(input('enter the ith value for LL : '))
    printLL(head)
    print(printIthNode(head, i))