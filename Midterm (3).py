#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def addfile(self, name):
        new_file = Node(name)
        if not self.first:
            self.first = new_file
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = new_file

    def display_list(self):
        current = self.first
        while current:
            print(current.name)
            current = current.next
        
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
        
class FIFO:
    def __init__(self):
        self.FIFO = []
    def is_empty(self):
        return len(self.FIFO) == 0
    def enqueue(self, action):
        self.FIFO.append(action)
    def dequeue(self):
        if not self.is_empty():
            return self.FIFO.pop(0)
        else:
            return None


# In[11]:


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
class NormalFile:
    def __init__(self):
        self.first = None

    def create_new(self, name):
        new_node = Node(name)
        if not self.first:
            self.first = new_node
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = new_node
        # Assuming bst is defined elsewhere and accessible through self
        self.bst.insert(name)

    def move_file(self, destination, name):
        if not self.bst.search(name):
            print("File not found.")
            return

        prev = None
        current = self.first
        while current and current.name != name:
            prev = current
            current = current.next

        if prev:
            prev.next = current.next
        else:
            self.first = current.next

        destination.add_file(name)
        destination.bst.insert(name)
        print(f"File '{name}' moved to '{destination}'.")

    def delete_file(self, name):
        if not self.bst.search(name):
            print("File not found.")
            return

        prev = None
        current = self.first
        while current and current.name != name:
            prev = current
            current = current.next

        if prev:
            prev.next = current.next
        else:
            self.first = current.next

        # Remove the file from the binary search tree
        self.bst.delete(name)
        print(f"File '{name}' deleted.")

    def display_directory(self):
        current = self.first
        while current:
            print(current.name)
            current = current.next
class File:
    def __init__(self, name):
        self.name = name

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []

    def add_file(self, file):
        self.files.append(file)

    def add_subdirectory(self, directory):
        self.subdirectories.append(directory)

class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root

    def create_file(self, name):
        new_file = File(name)
        self.current_directory.add_file(new_file)
        print(f"File '{name}' created.")

    def create_directory(self, name):
        new_directory = Directory(name)
        self.current_directory.add_subdirectory(new_directory)
        print(f"Directory '{name}' created.")


# In[13]:


def main():
    print("Welcome to the Basic File System.")
    print("To create a new file, use the command: create file <file_name>")
    print("To create a new directory, use the command: create directory <directory_name>")
    print("To move a file, use the command: move file <source_directory> <file_name> <destination_directory>")
    print("To delete a file, use the command: delete file <file_name>")
    print("To display the contents of the current directory, use the command: display")
    print("To search for a file, use the command: search file <file_name>")
    print("To quit the program, use the command: quit")

    fs = FileSystem()

    while True:
        command = input(f"{fs.current_directory.name}> ")

        if command.startswith("create file "):
            file_name = command[12:]
            fs.create_file(file_name)

        elif command.startswith("create directory "):
            directory_name = command[17:]
            fs.create_directory(directory_name)

        elif command.startswith("move file "):
            parts = command.split()
            if len(parts) != 4:
                print("Invalid command.")
                continue
            source_dir_name = parts[2]
            file_name = parts[3]
            destination_dir_name = parts[4]
            fs.move_file(source_dir_name, file_name, destination_dir_name)

        elif command.startswith("delete file "):
            file_name = command[12:]
            fs.delete_file(file_name)

        elif command == "display":
            fs.display_directory()

        elif command == "quit":
            print("Exiting...")
            break

        elif command.startswith("search file "):
            file_name = command[12:]
            fs.search_file(file_name)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




