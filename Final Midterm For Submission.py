#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = LinkedList()
        self.subdirectories = []

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def add_file(self, name):
        new_file = Node(name)
        if not self.first:
            self.first = new_file
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = new_file

    def delete_file(self, name):
        current = self.first
        prev = None
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.first = current.next
                print(f"File '{name}' deleted.")
                return
            prev = current
            current = current.next
        print(f"File '{name}' not found.")

    def display_list(self):
        current = self.first
        while current:
            print(current.name)
            current = current.next


class LIFO:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def push(self, action):
        self.stack.append(action)

class FIFO:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, action):
        self.queue.append(action)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None

class TreeNode:
    def __init__(self, key):
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

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            return None
        
        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        # If key is the same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)
            
            # Copy the inorder successor's content to this node
            node.key = successor.key
            
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, successor.key)
        
        return node

    def _min_value_node(self, node):
        current = node
        # Loop down to find the leftmost leaf
        while current.left:
            current = current.left
        return current


class FileSystemOperations:
    def __init__(self):
        self.filesystem = {}
        self.fifo = FIFO()
        self.lifo = LIFO()
        self.directories = {}
        self.directory_bst = BinarySearchTree()

    def create_directory(self, directory_name):
        if directory_name not in self.directories:
            self.directories[directory_name] = LinkedList()
            print(f"Directory '{directory_name}' created.")
        else:
            print(f"Directory '{directory_name}' already exists.")

    def create_file(self, directory_name, file_name):
        if directory_name in self.directories:
            self.directories[directory_name].add_file(file_name)
            self.directory_bst.insert(file_name)
            print(f"File '{file_name}' created in directory '{directory_name}'.")
        else:
            print(f"Directory '{directory_name}' not found.")

    def move_file(self, source_dir, name, destination_dir):
        self.fifo.enqueue((source_dir, name, destination_dir))
        print(f"File movement request for '{name}' enqueued.")

    def find_file(self, name):
        if self.directory_bst.search(name):
            print(f"File '{name}' found.")
        else:
            print(f"File '{name}' not found.")

    def rename_file(self, old_name, new_name):
        found = False
        for linked_list in self.directories.values():
            if linked_list.search(old_name):
                linked_list.rename(old_name, new_name)
                self.directory_bst.delete(old_name)
                self.directory_bst.insert(new_name)
                found = True
                break
        if not found:
            print(f"File '{old_name}' not found.")

    def display_directory_contents(self, directory_name):
        if directory_name in self.directories:
            print(f"Files in directory '{directory_name}':")
            self.directories[directory_name].display_list()
        else:
            print(f"Directory '{directory_name}' not found.")

    def delete_file(self, file_name):
        if self.directory_bst.search(file_name):
            self.directory_bst.delete(file_name)
            for linked_list in self.directories.values():
                linked_list.delete_file(file_name)
            print(f"File '{file_name}' deleted.")
        else:
            print(f"File '{file_name}' not found.")

    def delete_directory(self, directory_name):
        if directory_name in self.directories:
            del self.directories[directory_name]
            print(f"Directory '{directory_name}' deleted.")
        else:
            print(f"Directory '{directory_name}' not found.")

    def process_file_movement_requests(self):
        while not self.fifo.is_empty():
            source_dir, name, destination_dir = self.fifo.dequeue()
            if source_dir in self.directories:
                self.directories[source_dir].delete_file(name)
                if destination_dir in self.directories:
                    self.directories[destination_dir].add_file(name)
                    print(f"File '{name}' moved from '{source_dir}' to '{destination_dir}'.")
                else:
                    print(f"Directory '{destination_dir}' not found.")
            else:
                print(f"Directory '{source_dir}' not found.")
    def rename_directory(self, old_name, new_name):
        if old_name in self.directories:
            self.directories[new_name] = self.directories.pop(old_name)
            print(f"Directory '{old_name}' renamed to '{new_name}'.")
        else:
            print(f"Directory '{old_name}' not found.")


# In[2]:


def main():
    # Initialize file system operations
    filesystem = FileSystemOperations()

    def display_instructions():
        print("Welcome to the Basic File System.")
        print("Instructions:")
        print("To create a new file, use command: create file <directory_name> <file_name>")
        print("To create a new directory, use command: create directory <directory_name>")
        print("To move a file, use command: move file <source_directory> <file_name> <destination_directory>")
        print("To delete a file, use command: delete file <file_name>")
        print("To delete a directory, use command: delete directory <directory_name>")
        print("To display the contents of a directory, use command: display directory <directory_name>")
        print("To search for a file, use command: search file <file_name>")
        print("To rename a directory, use command: rename directory <old_directory_name> <new_directory_name>")
        print("To process file movement requests, use command: process")
        print("To quit the program, use command: quit")

    display_instructions()

    # Command-line interface loop
    while True:
        # Get user input
        command = input("Enter command: ").strip()

        # Check if the command is valid and perform operations
        if command.startswith("create file "):
            parts = command[len("create file "):].split()
            if len(parts) == 2:
                filesystem.create_file(parts[0], parts[1])
            else:
                print("Invalid command. Please provide directory name and file name.")
        elif command.startswith("create directory "):
            directory_name = command[len("create directory "):].strip()
            filesystem.create_directory(directory_name)
        elif command.startswith("move file "):
            parts = command[len("move file "):].split()
            if len(parts) == 3:
                filesystem.move_file(parts[0], parts[1], parts[2])
            else:
                print("Invalid command. Please provide source directory, file name, and destination directory.")
        elif command.startswith("delete file "):
            file_name = command[len("delete file "):].strip()
            filesystem.delete_file(file_name)
        elif command.startswith("delete directory "):
            directory_name = command[len("delete directory "):].strip()
            filesystem.delete_directory(directory_name)
        elif command.startswith("display directory "):
            directory_name = command[len("display directory "):].strip()
            filesystem.display_directory_contents(directory_name)
        elif command.startswith("search file "):
            file_name = command[len("search file "):].strip()
            filesystem.find_file(file_name)
        elif command.startswith("rename file "):
            parts = command[len("rename file "):].split()
            if len(parts) == 2:
                filesystem.rename_file(parts[0], parts[1])
            else:
                print("Invalid command. Please provide old file name and new file name.")
        elif command.startswith("rename directory "):
            parts = command[len("rename directory "):].split()
            if len(parts) == 2:
                filesystem.rename_directory(parts[0], parts[1])
            else:
                print("Invalid command. Please provide old directory name and new directory name.")
        elif command == "process":
            filesystem.process_file_movement_requests()
        elif command == "undo":
            filesystem.undo_last_operation()
        elif command == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")
            display_instructions()

# Call the main function to start the program
if __name__ == "__main__":
    main()


# In[ ]:




