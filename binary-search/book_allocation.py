# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1?utm_source=youtube&utm_medium=collab_codefromscratch_description&utm_campaign=allocate-minimum-number-of-pages
# Allocate minimum number of pages

# You have N books, each with Ai number of pages. M students need to be allocated contiguous books, with each student getting at least one book.

def findPages(A, N, M):
    def isAllocation(A,N,M,mid):
        stud,curr = 1,0
        
        for i in A:
            if i>mid:return False
            if curr+i>mid:
                stud+=1
                if stud>M:
                    return False
                curr=i
            else:
                curr+=i
        return True
            
    if M>N:
        return -1
        
    res=-1
    l,r = A[-1],sum(A)
    
    while l<=r:
        mid = l + (r-l)//2
        if isAllocation(A,N,M,mid):
            res = mid
            r=mid-1
        else:
            l=mid+1
    return res


if __name__ == '__main__':
    M = int(input("Enter the number of students: "))
    N = int(input("Enter the number of books: "))
    A = list(map(int, input("Enter the Ai number of pages: ").split()))
    print(findPages(A,N,M))