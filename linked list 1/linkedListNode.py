class Node:

    def __init__(self , data):
        self.data = data 
        self.next = None

    
if __name__ == '__main__':
    a = Node(13)
    b = Node(14)
    a.next = b
    print('data a :' , a.data)
    print('b data :' , b.data)
    print('a.next data : ' , a.next.data)