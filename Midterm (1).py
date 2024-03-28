#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = none
    def addfile(self, name)
        new_file = FileNode(name)
        if not self.first:
            self.first = new_file
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = new.node
    def display_list(self)
    while current
        print(current.name)
        current = current.next


# In[ ]:


class FIFO:
    def __init__(self):
        self.FIFO = []
    def is_empty(self):
        return len(self.FIFO) == 0
    def enqueue(self, action)
        self.FIFO.append(action)
    def dequeue(self)
        if not self.is_empty()
            return self.FIFO.pop(0)
        else:
            return None


# In[ ]:


class LIFO:
    def __init__(self):
        self.LIFO = []
    def is_empty(self):
        return len(self.LIFO) == 0
    def pop(self):
        if not self.is_empty():
            return self.LIFO.pop()
        else:
            return None
    def push(self, action):
        self.LIFO.append(action)


# In[ ]:


class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if not node.left:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if not node.right:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


# In[ ]:


class NormalFile:
    def __init__(self):
        self.head = None
    def create_new(self, name):
        new_node = Node(name)
        if not self.first:
            self.first = new_file
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = new.node
    def move_file(self, destination, name):
        if not self.head:
            return
        

