'''
Created on Nov 28, 2018

@author: penumr
'''

class Node:

    def __init__(self, key):
        self.left = None;
        self.right = None;
        self.val = key;

        
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

                
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

   
def search(root, val):
    print(root.val, val)
    if root is None:
        return False
    elif root.val == val:
        return True
    elif root.val < val:
        search(root.left, val)
    else:
        search(root.right, val)
             

r = Node(50)
insert(r, Node(30))
insert(r, Node(10))
insert(r, Node(20))
insert(r, Node(90))
insert(r, Node(80))
insert(r, Node(50))
insert(r, Node(40))
insert(r, Node(4))
insert(r, Node(60))
insert(r, Node(1))

inorder(r)

print(search(r, 40))
