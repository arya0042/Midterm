#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
Class BinarySearchTree:
    

