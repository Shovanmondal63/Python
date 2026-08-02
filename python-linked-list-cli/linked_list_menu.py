import os

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    # 'cls' for Windows (nt), 'clear' for Linux/macOS
    os.system("cls" if os.name == "nt" else "clear")


class Node:
    """Represents an individual node in a singly linked list."""

    def __init__(self, data):
        self.data = data  # Holds the value of the node
        self.next = None  # Pointer/reference to the next node in the list


class Linkedlist:
    """Implements a Singly Linked List and its core operations."""

    def __init__(self):
        # Initialize an empty linked list with head pointer set to None
        self.head = None

    def append(self, val):
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(val)

        # If list is empty, set the new node as head
        if self.head is None:
            self.head = new_node
            print(f"{new_node.data} inserted successfully.\n")
        else:
            # Traverse to the last node
            current = self.head
            while current.next is not None:
                current = current.next

            # Link the last node to the new node
            current.next = new_node
            print(f"{new_node.data} inserted successfully.\n")

    def display(self):
        """Prints all values present in the linked list from head to end."""
        if self.head is None:
            print("LinkedList is Empty!\n")
        else:
            current = self.head
            print("\nAll data in LinkedList:")
            # Traverse and output node values formatted with arrows
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def insert_at(self, value, position):
        """Inserts a new node with 'value' at a specified 0-based 'position'."""
        new_node = Node(value)

        # Case 1: Attempting to insert into an empty list
        if self.head is None:
            print("LinkedList is Empty!\n")
            input("Press Enter to continue...")

        # Case 2: Insert at position 0 (new head node)
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"{new_node.data} inserted successfully at position 0.\n")
            input("Press Enter to continue...")

        # Case 3: Insert at a middle or end position
        else:
            count = 0
            current = self.head
            prev = None

            # Traverse until reaching the requested position
            while count != position and current is not None:
                prev = current
                current = current.next
                count += 1

            # Rewire pointers to place new_node between prev and current
            prev.next = new_node
            new_node.next = current
            print(f"{value} inserted successfully at position {position}.\n")
            input("Press Enter to continue...")

    def delnode(self, value):
        """Deletes the first occurrence of a node containing 'value'."""
        current = self.head
        prev = None

        # Case 1: Empty list check
        if self.head is None:
            print("LinkedList is Empty!!!")
            input("Press Enter to continue...")
            clear_screen()

        # Case 2: Node to delete is the head node
        elif current.data == value:
            self.head = current.next
            current = None
            print(f"{value} is deleted from LinkedList...")
            input("Press Enter to continue...")
            clear_screen()

        # Case 3: Search for the node in the rest of the list
        else:
            found = False
            while current is not None:
                if current.data == value:
                    found = True
                    break
                prev = current
                current = current.next

            # Unlink node if match was found
            if found:
                prev.next = current.next
                print(f"{value} is deleted from LinkedList.")
                input("Press Enter to continue...")
                clear_screen()
            else:
                print("Data not found!!!")
                input("Press Enter to continue...")
                clear_screen()


def main():
    """Main loop controlling the menu CLI interface."""
    loop = 0
    sl = Linkedlist()

    while loop == 0:
        # User choices display
        print("\n--- Linked List Options ---")
        print("0: Exit")
        print("1: Insert data (Append)")
        print("2: Display data")
        print("3: Insert value at position")
        print("4: Delete value")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            input("Press Enter to continue...")
            clear_screen()
            continue

        # Option 0: Exit script
        if choice == 0:
            loop += 1
            print("Program end...\n")

        # Option 1: Append item(s) to list
        elif choice == 1:
            loop2 = "y"
            while loop2.lower() == "y":
                val = int(input("Enter a value: "))
                sl.append(val)
                loop2 = input("Do you want to continue (y/n): ")
            print()
            clear_screen()

        # Option 2: Print list content
        elif choice == 2:
            sl.display()
            input("Press Enter to continue...")
            clear_screen()

        # Option 3: Insert item at custom index
        elif choice == 3:
            val = int(input("Enter a value: "))
            position = int(input("Enter position: "))
            sl.insert_at(val, position)
            clear_screen()

        # Option 4: Delete item by value
        elif choice == 4:
            val = int(input("Enter value to delete: "))
            sl.delnode(val)
            clear_screen()

        # Handle options outside range 0-4
        else:
            print("Invalid choice!!!")
            input("Press Enter to continue...")
            clear_screen()


# Entry point trigger
if __name__ == "__main__":
    main()
