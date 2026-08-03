# Import the os module for operating system related functions.
import os


# Function to clear the terminal screen.
def clear_screen():
    """Clears the terminal screen based on the operating system."""
    # 'cls' for Windows (nt), 'clear' for Linux/macOS
    os.system("cls" if os.name == "nt" else "clear")


# Node class represents a single node of the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked_list class contains all linked list operations.
class Linked_list:
    def __init__(self):
        self.head = None

    # Insert one or more values at the end of the linked list.
    def append(self):
        loop = "y"
        print("-" * 10, "Data insert in Linked List", "-" * 10)
        while (loop == "y"):
            value = int(input("Enter a value:"))
            new_node = Node(value)
            if (self.head == None):
                self.head = new_node
                print(new_node.data, "insert successfully in Linked List...\n")
            else:
                current = self.head
                while (current.next != None):
                    current = current.next
                current.next = new_node
                print(new_node.data, "insert successfully in Linked List...\n")
            loop = input("Do you want to continue(y / n):")


    # Display all elements of the linked list.
    def display(self):
        print("-" * 10, "All data in Linked List", "-" * 10)
        if(self.head == None):
            print("Linked List is empty!!!\n")
        else:
            current = self.head
            print("Linked List value: ")
            while(current != None):
                print(current.data,end="->")
                current = current.next
            print("None")


    # Search for a value in the linked list.
    def search(self):
        print("-" * 10, "Search value in Linked List", "-" * 10)
        loop = "y"
        while (loop == "y"):
            if((self.head == None)):
                print("Linked List is empty!!!\n")
                break
            else:
                value = int(input("Which value you want to search:"))
                current = self.head
                counter = 0
                found = False
                while (current != None):
                    if (current.data == value):
                        print(value, "is found in ",counter," Index.\n")
                        found = True
                        break
                    else:
                        counter += 1
                        current = current.next
                if(found == False):
                    print("Value not found in Linked List!!!\n")
            loop = input("Do you want to search more value(y / n):")


    # Insert a new value at a specified position.
    def insert_at(self):
        print("-" * 10, "Insert value at any position in Linked List", "-" * 10)
        loop = "y"
        current = self.head
        counter = 0
        while (current != None):
            counter += 1
            current = current.next

        while (loop == "y"):
            value = int(input("Enter a value for Insert in Linked List:"))
            new_node = Node(value)
            position = int(input("Enter the position you want to insert that value:"))
            if(self.head == None):
                print("Linked List is empty!!!\n")
            elif(position >= counter):
                print("Position does not exist in Linked List!!!\n")
            elif(position < 0):
                print("Position must be greater than 0!!!\n")
            elif(position == 0):
                new_node.next = self.head
                self.head = new_node
                print(new_node.data, "insert successfully in ",position,"Position in Linked List.\n")
            else:
                current = self.head
                previous = None
                counter = 0
                while(counter != position):
                    previous = current
                    current = current.next
                    counter += 1
                previous.next = new_node
                new_node.next = current.next
                print(new_node.data, "insert successfully in ",position,"Position in Linked List.\n")

            loop = input("Do you insert more value in Linked list(y / n):")

    # Delete a node by its value.
    def delete_at(self):
        print("-" * 10, "Delete value at any position in Linked List", "-" * 10)
        loop = "y"
        while (loop == "y"):
            value = int(input("Enter a value for Delete from Linked List:"))
            if(self.head == None):
                print("Linked List is empty!!!\n")
            else:
                current = self.head
                previous = None
                if(current.data == value):
                    print(current.data, "is deleted in Linked List!!!\n")
                    self.head = current.next
                else:
                    found = False
                    while (current != None):
                        if (current.data == value):
                            found = True
                            break
                        else:
                            previous = current
                            current = current.next
                    if(found == False):
                        print("Value not found in Linked List!!!\n")
                    else:
                        print(value, "deleted successfully in Linked List!!!\n")
                        previous.next = current.next
            loop = input("Do you want to delete more value in Linked List(y / n):")


# Main function to display the menu and control program execution.
def main():
    loop = 0
    sl = Linked_list()
    while(loop == 0):
        print("=" * 10, "Main Menu", "=" * 10)
        print("Press 0 for Exit")
        print("Press 1 for Insert at any position in Linked List.")
        print("Press 2 for Display all value in Linked List.")
        print("Press 3 for Search value in Linked List.")
        print("Press 4 for Insert value at any position in Linked List.")
        print("Press 5 for Delete value in Linked List.")
        print("=" * 32,"\n")
        choise = int(input("Enter your choice:"))
        if(choise == 0):
            print("Program End...\n")
            loop +=1
        elif(choise == 1):
            sl.append()
            input("\nPress Enter to continue...")
            clear_screen()
        elif(choise == 2):
            sl.display()
            input("\nPress Enter to continue...")
            clear_screen()
        elif(choise == 3):
            sl.search()
            input("\nPress Enter to continue...")
            clear_screen()
        elif(choise == 4):
            sl.insert_at()
            input("\nPress Enter to continue...")
            clear_screen()
        elif(choise == 5):
            sl.delete_at()
            input("\nPress Enter to continue...")
            clear_screen()
        else:
            input("\nInvalid Choice!!!")
            clear_screen()


# Program execution starts from here.
if __name__ == "__main__":
    main()
