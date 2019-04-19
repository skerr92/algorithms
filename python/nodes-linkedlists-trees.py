class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next


class NodeTree:

    def __init__(self, data, l, r):
        self.data = data
        self.left = l
        self.right = r


class RedBlackTree:

    def __init__(self, data, l, r, color):
        self.data = data
        self.left = l
        self.right = r
        """color is either 0 for red or 1 for black"""
        self.color = color


def addRBNode(parent, node):
    if parent.color == 0 & node.color == 0:
        parent.color = 1
        if parent.left is None & parent.right is None:
            if node.data < parent.data:
                parent.left = node
            else:
                parent.right = node
    else:
        if parent.left is None & parent.right is None:
            if node.data < parent.data:
                parent.left = node
            else:
                parent.right = node


def buildingtree(vtree):
    return


def inorder(tree):
    if tree is None:
        return
    else:
        inorder(tree.left)
        print(tree.data)
        inorder(tree.right)


def postorder(tree):
    if tree is None:
        return
    else:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.data)


def preorder(tree):
    if tree is None:
        return
    else:
        print(tree.data)
        preorder(tree.left)
        preorder(tree.right)


if __name__=='__main__':
