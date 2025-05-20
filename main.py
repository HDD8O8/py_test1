import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hallo Henning")
        label = tk.Label(self.root, text="Hallo Henning", font=("Arial", 16))
        label.pack(padx=20, pady=20)
        self.root.mainloop()
    
    def hallo_sagen(self):
        print("Hallo!")

# This is a simple GUI application using tkinter that displays "Hallo Henning" in a window.
if __name__ == "__main__":
    Main()