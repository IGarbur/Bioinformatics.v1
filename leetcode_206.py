#The point of this question is to reverse all connections 
#ex: 3 which is our current lest say should point 
# to 2 which is our previous
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
def reverseList(head):
    current = head
    previous = None
    while current: #we use current not head because current is the one being updated as we iterate
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
head = a
a.next = b
b.next = c

head = reverseList(head)

while head:
    print(head.val)
    head = head.next




