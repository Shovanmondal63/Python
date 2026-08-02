# Singly Linked List CLI

A simple command-line application built in Python that demonstrates the core operations of a **Singly Linked List** data structure — including insertion, deletion, traversal, and display — through an interactive menu.

## Features

- **Append** — Add new values to the end of the list
- **Display** — View all elements currently stored in the list
- **Insert at Position** — Insert a value at any given index
- **Delete by Value** — Remove the first node matching a given value
- Cross-platform screen clearing (Windows / Linux / macOS)
- Simple, menu-driven CLI interface

## Project Structure

```
.
├── linked_list_menu.py   # Main script containing Node, Linkedlist classes and CLI logic
└── README.md
```

## Requirements

- Python 3.x (no external dependencies — uses only the built-in `os` module)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Shovanmondal63/Python/python-linked-list-cli.git
   cd Python
   ```
2. Run the script:
   ```bash
   python linked_list.py
   ```

## Usage

When you run the program, you'll see a menu like this:

```
--- Linked List Options ---
0: Exit
1: Insert data (Append)
2: Display data
3: Insert value at position
4: Delete value

Enter your choice:
```

Simply enter the number corresponding to the action you want to perform and follow the on-screen prompts.

### Example

```
Enter your choice: 1
Enter a value: 10
10 inserted successfully.

Do you want to continue (y/n): n

Enter your choice: 2

All data in LinkedList:
10 -> None
```

## Code Overview

- **`Node`** — Represents a single element in the list, holding `data` and a `next` pointer.
- **`Linkedlist`** — Manages the list itself with the following methods:
  - `append(val)` — Adds a node to the end of the list
  - `display()` — Prints the list from head to tail
  - `insert_at(value, position)` — Inserts a node at a specific index
  - `delnode(value)` — Deletes the first node matching a value
- **`main()`** — Runs the interactive CLI loop.

## Possible Improvements

- Add input validation for non-integer values in insert/delete operations
- Add a `delete_at(position)` method for index-based deletion
- Add unit tests
- Support insertion beyond current list length gracefully

## License

This project is open source and available under the [MIT License](LICENSE).
