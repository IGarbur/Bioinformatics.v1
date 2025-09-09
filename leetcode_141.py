#I was originally thinking of adding additional attributes to a node class
#such as visited = true/false and then checking this attribute

#but you can use a set of objects and
#just check if that object is already in the set
'''
class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        print(self.val)

def hasCycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

head = a
a.next = b
b.next = c
c.next = d
d.next = b #toggle this on and off to see detection of cycle
'''

#There is an algorithm to Solve this problem its Called Floyed's alg
#remember a question of cars coming in groups because one car is moving
#faster so it was able to catch up, so when you have a cycle 
#eventually it will catch up and be exactly on the same spot as the
#other car
#So you can have two pointers one is slow which moves one node
#and the other is fast moving two nodes
#eventually they will point to the same node

class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        print(self.val)

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        #increment pointers first otherwise slow and fast will be equal or make a dummy node dummy = ListNode(0),dummy.next = head,slow = dummy
        slow = slow.next
        fast = fast.next.next #imagine fast.next is None then you try to call .next on None you will get attribute error, the solution is to chech fast.next in while loop
        if slow == fast:
            return True
    return False


a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

head = a
a.next = b
b.next = c
c.next = d
#d.next = b
print(hasCycle(head))

