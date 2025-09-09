class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next
    def __str__(self):
        print(self.val)

def reorderList(head):
    l = head
    r = head
    while r:
        r = r.next
    new_head = l
    if l:
        l = l.next
    while l!=r:
        new_head.next = r
        new_head = new_head.next
        new_head.next = l
        new_head = new_head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
head = a
a.next = b
b.next = c
c.next = d

#new_head = reorderList(head)
'''
while new_head:
    print(new_head)
    new_head = new_head.next
'''