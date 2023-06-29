'''
You have been given a linked list of integers. 
Your task is to write a function that deletes a node from a given position, 'POS'.
'''

class Node :
    def __init__(self, data) :
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
def length(head):
    temp=head
    count=0
    while temp:
        count+=1
        temp=temp.next
    return count
def printLL(head):
    while head is not None :
        print(head.data,'->',end=' ')
        head = head.next 
    print('None')
# def deleteNode(head, pos) :
    if pos > 0 or pos >= length(head):
        return head
    temp = head 
    prev = None 
    count = 0 
    
    if pos == 0:
        next = temp.next 
        head = next 
    else:
        while count < pos :
            prev = temp 
            temp = temp.next 
            count+=1
        if count == pos:
            next = temp.next 
            prev.next = next 
    return head 


def deleteNode(head , pos):
    if head is None:
        return head 
    if pos == 0:
        return head.next 
    
    count = 0 
    curr = head 
    while curr and count<pos-1:
        count+=1
        curr = curr.next 
    if curr is None or curr.next is None:
        return head 
    curr.next = curr.next.next
    return head 


if __name__ == '__main__':
    head = takeInput()
    pos = int(input('enter the POS : '))
    printLL(head)
    head = deleteNode(head , pos)
    printLL(head)

