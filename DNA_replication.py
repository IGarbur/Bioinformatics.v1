#The point of this project is to mimic DNA replication
"""I will use two singly linked lists running in parallel """
"""Let's start by building a class Node which will have"""
"""1. Nitrogenous base, 2. reference to next node, 3. bond to complementary node"""

class Node:
    def __init__(self,nuc,next=None,bond=None):
        self.nuc = nuc
        self.next = next
        self.bond = bond
    def set_bond(self,new):
        self.bond = new
        
    def __str__(self):
        return str(self.nuc)
    
class Helicase:
    def __init__(self,lead_node):
        self.lead_node = lead_node
        #self.count = 0
        #****you need to give a node to a primer, lag_node = lead_node.bond.next
    def unwind(self):
        while self.lead_node:
            #print(self.lead_node)
            if self.lead_node.bond:
                self.lead_node.bond = None
            self.lead_node = self.lead_node.next
            #self.count+=1
            #if count == num -> yeild

class Primase: #This isn't particularly accurate since there is a protein that replaces primer
    #remember primase is called once helicase broke bond
    #so we need to find a complement to the node.nuc
    def __init__(self,lead_or_lag_node):#*******leading node is a node at the origin, lagging node depends on Helicase count
        self.lead_or_lag_node = lead_or_lag_node
        self.complement_nuc = complement(self.lead_or_lag_node.nuc)
    def set_primer(self):
        primer = Node(self.complement_nuc, next=None, bond=self.lead_or_lag_node) #***its actually lead_or_lag_node that needs to set the bond, so remember to fix this
        return primer
        
def complement(seq):
    match = {"A":"T","T":"A","C":"G","G":"C"}
    comp = ""
    for base in seq:
        comp+=match[base.upper()]
    return comp
    
class Polymerase:
    def __init__(self,primer):
        #the node that was originally given to primase is like a ptr
        #primer has a bond to original node that is used like a pointer to build a strand
        self.origin = primer.bond.next
        self.primer = primer
        self.old_primer = primer
    def elongate(self):
        while self.origin: #****you will need to add a case were another primer is reached to stop so ligace can take action
            self.primer.next = Node(complement(self.origin.nuc))
            self.origin.bond = self.primer.next
            self.origin = self.origin.next
            self.primer = self.primer.next
        return self.old_primer
    
class Ligace:
    #does the ligase know exactly where to ligate or does it actively search by iterating?
    def __init__(self,old_primer,primer):
        self.old_primer = old_primer
        self.primer = primer
    def ligate(self):
        self.primer.next = self.old_primer
        
    
    
# I will build a structure of 10 nodes in each list and connect them with H-bonds

#Nodes and their connections forming leading strand
#Note:this is counterintuitive but the leading strand 5'->3' is build up from leading strand template which goes in 3'<-5'
#So to traverse the linked list to build up leading strand we make leading strand template 5'->3' in a sense
a = Node("A")
b = Node("T")
c = Node("C")
d = Node("G")
e = Node("A")
f = Node("T")
g = Node("C")
h = Node("G")
i = Node("A")
j = Node("T")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j

#Nodes and their connections forming lagging strand
t = Node("T")
s = Node("A")
r = Node("G")
q = Node("C")
p = Node("T")
o = Node("A")
n = Node("G")
m = Node("C")
l = Node("T")
k = Node("A")

k.next = l
l.next = m
m.next = n
n.next = o
o.next = p
p.next = q
q.next = r
r.next = s
s.next = t

#How lets make hydrogen bonds between them (i could make 2 or 3 references to mimic but god damn)
#lets stick to 1 reference from leading strand nodes to lagging strand nodes

#WHY LEADING BONDING TO LAGGING? WELL HELICASE WORKS IN SAME DIRECTION AS LEADING THUS WHY ITS CALLED LEADING

#and no references from laging to leading in order to simplify a little
#interesting Note is that there are at least 2 H bonds sort of like a doubly linked list thing
j.bond = k
i.bond = l
h.bond = m
g.bond = n
f.bond = o
e.bond = p
d.bond = q
c.bond = r
b.bond = s
a.bond = t

#print(j.bond)
h = Helicase(a)
h.unwind()
#print(j.bond)
#print(j)
p = Primase(a)
primer = p.set_primer()
poly = Polymerase(primer)
strand = poly.elongate()
while strand:
    print(strand)
    strand = strand.next

''' Testing Ligace
old_primer = e
primer = d
primer.next = None
origin = a
while origin:
    print(origin)
    origin = origin.next
print("let's apply ligace")
l = Ligace(old_primer,primer)
l.ligate()
origin = a
while origin:
    print(origin)
    origin = origin.next'''