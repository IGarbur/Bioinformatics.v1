class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeTwoLists(head1,head2):
    #stupid edge case where one of inputs is None
    if not head1:
        return head2
    if not head2:
        return head1

    current1 = head1
    current2 = head2
    #initializing a first node for merged list
    if current1.val <= current2.val:
        new_list = current1
        current1 = current1.next
    else:
        new_list = current2
        current2 = current2.next
    current3 = new_list
    start = new_list
    
    while current1 and current2:
        if current1.val <= current2.val:
            current3.next = current1
            current3 = current3.next
            current1 = current1.next
        else:
            current3.next = current2
            current3 = current3.next
            current2 = current2.next
    #link remaining nodes
    if current1:
        current3.next = current1
    else:
        current3.next = current2
    return start


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
head1 = a
a.next = b
b.next = c

x = ListNode(1)
y = ListNode(3)
z = ListNode(4)
head2 = x
x.next = y
y.next = z

start = mergeTwoLists(head1,head2)
while start:
    print(start.val)
    start = start.next
