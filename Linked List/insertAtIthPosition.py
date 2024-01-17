class Node :
    def __init__(self,data):
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
    while head is not None :
        print(head.data,'->',end=' ')
        head = head.next 
    print('None')

def lengthLL(head):
    count=0
    while head is not None:
        count+=1
        head = head.next
    return count 
def insertAtI(head , i , data):
    if i > lengthLL(head) or i < 0:
        print('Data cannot be inserted ')
    newNode = Node(data)
    prev = None
    temp = head 
    if i == 0:
        newNode.next = head 
        head = newNode
    elif i < lengthLL(head):
        curr = 0
        while temp:
            if curr == i:
                prev.next = newNode 
                newNode.next = temp 
            curr+=1
            prev = temp 
            temp = temp.next 
    else:
        while temp.next is not None :
            temp = temp.next 
        temp.next = newNode
    return head



def insertAtI2(head , i ,data):
    prev = None 
    curr = head
    if i < 0 or i > lengthLL(head):
        return head
    count = 0
    while count < i:
        prev = curr 
        curr = curr.next 
        count+=1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode 
    else:
        head = newNode 
    newNode.next = curr 
    return head 

    

if __name__ == '__main__':
    head = takeInput() 
    i = int(input('enter the position : '))
    data =  int(input('enter the new data :'))
    printLL(head)
    head = insertAtI2(head , i , data)
    printLL(head)