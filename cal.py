import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),('sin', 1, 4), 
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),('cos', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),('tan', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),('sqrt', 4, 4),  
            ('^', 6, 0), ('ln', 6, 1), ('exp', 6, 2), ('(', 6, 3), (')', 6, 4), 
            ('log', 7, 0), (',', 7, 1), ('%', 7, 2), ('1/x', 7, 3), ('pi', 7, 4),
            ('AC',8, 2, 1),('c',8,1,1)
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1  

            if text == 'AC':
                tk.Button(self.root, text=text, font=("Arial", 18), command=self.all_clear).grid(row=row, column=col, columnspan=colspan, sticky='nsew')
            elif text=='c':
                tk.Button(self.root, text=text, font=("Arial", 18), command=self.clear).grid(row=row, column=col, columnspan=colspan, sticky='nsew')    
            elif text == '=':
                tk.Button(self.root, text=text, font=("Arial", 18), command=self.calculate).grid(row=row, column=col, sticky='nsew')
            else:
                tk.Button(self.root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky='nsew')

        
        for i in range(8):  
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):  
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.display.get()
        if char == '.' and (current_text == '' or current_text[-1] in '+-*/.'):
            return
        elif char in ('sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'exp', '1/x', 'pi','EE'):
            if char == 'pi':
                self.display.insert(tk.END, str(math.pi))
            else:
                self.display.insert(tk.END, f"{char}(")
        elif char == '^':
            self.display.insert(tk.END, '**')
        else:
            self.display.insert(tk.END, char)

    def clear(self):
        self.display.delete(0, tk.END)
    def all_clear(self):
        self.display.delete(0,tk.END)    

    def calculate(self):
        try:
            expression = self.display.get()
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            expression = expression.replace('exp', 'math.exp')
            expression = expression.replace('1/x', '1/')
            expression = expression.replace('pi', str(math.pi))
           

            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

