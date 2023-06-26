class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def takeInput():
    head = None 
    inputlist = [int(ele) for ele in input().split()]
    for data in inputlist :
        if data == -1:
            break 
        newNode = Node(data)
        if head is None:
            head = newNode 
        else:
            curr = head 
            while curr.next is not None:
                curr = curr.next 
            curr.next = newNode 
    return head

def printLL(head):
    while head is not None:
        print(head.data , '->' , end = ' ')
        head = head.next
    print(-1)


if __name__ == '__main__':
    head = takeInput()
    printLL(head)