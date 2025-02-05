import tkinter as tk
from tkinter import messagebox

class MagicSquareGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ramanujan's Magic Square Game")
        self.grid_size = None
        self.cells = []
        self.correct_magic_square = [
            [22, 12, 18, 87],
            [88, 17, 11, 20],
            [21, 19, 16, 89],
            [92, 14, 13, 23]
        ]
        self.create_dimension_input()

    def create_dimension_input(self):
        self.dimension_label = tk.Label(self.root, text="Enter the dimension of the grid (e.g., 4):")
        self.dimension_label.pack()
        
        self.dimension_entry = tk.Entry(self.root)
        self.dimension_entry.pack()
        
        self.dimension_button = tk.Button(self.root, text="Submit", command=self.set_grid_size)
        self.dimension_button.pack()
    
    def set_grid_size(self):
        try:
            self.grid_size = int(self.dimension_entry.get())
            if self.grid_size != 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer (e.g., 4).")
            return

        self.dimension_label.pack_forget()
        self.dimension_entry.pack_forget()
        self.dimension_button.pack_forget()
        
        self.create_grid()
        self.create_check_button()

    def create_grid(self):
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                entry = tk.Entry(self.root, width=5, font=("Helvetica", 20))
                entry.grid(row=i, column=j, padx=5, pady=5)
                row.append(entry)
            self.cells.append(row)

    def create_check_button(self):
        check_button = tk.Button(self.root, text="Check Magic Square", command=self.check_magic_square)
        check_button.grid(row=self.grid_size, column=0, columnspan=self.grid_size, pady=10)

    def check_magic_square(self):
        matrix = []
        try:
            for i in range(self.grid_size):
                row = []
                for j in range(self.grid_size):
                    value = int(self.cells[i][j].get())
                    row.append(value)
                    self.cells[i][j].config(bg="white")  # Reset the background color
                matrix.append(row)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers in all cells.")
            return

        if self.is_magic_square(matrix):
            messagebox.showinfo("Result", "Congratulations! It's a valid Ramanujan's magic square!")
        else:
            self.highlight_errors(matrix)
            self.show_correct_magic_square()

    def is_magic_square(self, matrix):
        n = len(matrix)
        magic_constant = sum(matrix[0])

        # Check sums of rows
        for row in matrix:
            if sum(row) != magic_constant:
                return False

        # Check sums of columns
        for col in range(n):
            if sum(matrix[row][col] for row in range(n)) != magic_constant:
                return False

        # Check sums of diagonals
        if sum(matrix[i][i] for i in range(n)) != magic_constant:
            return False
        if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_constant:
            return False

        return True

    def highlight_errors(self, matrix):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if matrix[i][j] != self.correct_magic_square[i][j]:
                    self.cells[i][j].config(bg="red")

    def show_correct_magic_square(self):
        correct_square = "\n".join(["\t".join(map(str, row)) for row in self.correct_magic_square])
        messagebox.showinfo("Result", f"Sorry, it's not a valid Ramanujan's magic square.\n\nThe correct magic square is:\n{correct_square}")

# Creating the main window
root = tk.Tk()
game = MagicSquareGame(root)

# Run the GUI event loop
root.mainloop()
