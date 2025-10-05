import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("440x680")
        self.root.resizable(False, False)
        self.root.config(bg="#f8f7ff")
        
        # State variables
        self.expression = ""
        self.result_text = tk.StringVar(value="0")
        self.expression_text = tk.StringVar(value="")
        
        # Setup UI
        self._setup_display()
        self._setup_buttons()
        self._setup_keyboard_bindings()
        
    def _setup_display(self):
        """Create the display area for calculator"""
        # Display area with gradient-like background
        display_area = tk.Frame(self.root, bg="#f8f7ff", height=170)
        display_area.pack(fill=tk.BOTH, expand=False)
        display_area.pack_propagate(False)
        
        # Expression label (shows the calculation)
        expr_label = tk.Label(
            display_area,
            textvariable=self.expression_text,
            bg="#f8f7ff",
            fg="#a5b4fc",
            font=("Arial", 16),
            anchor="e",
            padx=30,
            pady=5
        )
        expr_label.pack(side=tk.TOP, fill=tk.X)
        
        # Result label (shows current input/result)
        result_label = tk.Label(
            display_area,
            textvariable=self.result_text,
            bg="#f8f7ff",
            fg="#1e293b",
            font=("Arial", 56, "bold"),
            anchor="e",
            padx=30
        )
        result_label.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
    def _setup_buttons(self):
        """Create the button grid"""
        # Button container with subtle gradient background
        button_container = tk.Frame(self.root, bg="#e0d4ff")
        button_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Inner padding frame
        inner_frame = tk.Frame(button_container, bg="#e0d4ff")
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Configure grid weights
        for i in range(5):
            inner_frame.rowconfigure(i, weight=1)
        for i in range(4):
            inner_frame.columnconfigure(i, weight=1)
        
        # Button layout definition
        buttons = [
            ("C", 0, 0, "#e8e3ff", "#1e293b", self.clear_all),
            ("x²", 0, 1, "#e8e3ff", "#1e293b", self.square),
            ("√x", 0, 2, "#e8e3ff", "#1e293b", self.sqrt),
            ("÷", 0, 3, "#7c3aed", "white", lambda: self._add_operator("/")),
            
            ("7", 1, 0, "white", "#1e293b", lambda: self._add_digit("7")),
            ("8", 1, 1, "white", "#1e293b", lambda: self._add_digit("8")),
            ("9", 1, 2, "white", "#1e293b", lambda: self._add_digit("9")),
            ("×", 1, 3, "#7c3aed", "white", lambda: self._add_operator("*")),
            
            ("4", 2, 0, "white", "#1e293b", lambda: self._add_digit("4")),
            ("5", 2, 1, "white", "#1e293b", lambda: self._add_digit("5")),
            ("6", 2, 2, "white", "#1e293b", lambda: self._add_digit("6")),
            ("−", 2, 3, "#7c3aed", "white", lambda: self._add_operator("-")),
            
            ("1", 3, 0, "white", "#1e293b", lambda: self._add_digit("1")),
            ("2", 3, 1, "white", "#1e293b", lambda: self._add_digit("2")),
            ("3", 3, 2, "white", "#1e293b", lambda: self._add_digit("3")),
            ("+", 3, 3, "#7c3aed", "white", lambda: self._add_operator("+")),
            
            (".", 4, 0, "white", "#1e293b", lambda: self._add_digit(".")),
            ("0", 4, 1, "white", "#1e293b", lambda: self._add_digit("0")),
        ]
        
        # Create buttons with rounded corners effect
        for text, row, col, bg, fg, cmd in buttons:
            self._create_button(inner_frame, text, row, col, bg, fg, cmd)
        
        # Equals button (spans 2 columns) - vibrant green
        equals_btn = tk.Button(
            inner_frame,
            text="=",
            font=("Arial", 24, "bold"),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            bd=0,
            relief=tk.FLAT,
            command=self.calculate,
            cursor="hand2"
        )
        equals_btn.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=4, pady=4)
        
    def _create_button(self, parent, text, row, col, bg_color, fg_color, command):
        """Helper to create a styled button"""
        btn = tk.Button(
            parent,
            text=text,
            font=("Arial", 22 if bg_color == "#7c3aed" else 20),
            bg=bg_color,
            fg=fg_color,
            activebackground="#f3f4f6" if bg_color in ["white", "#e8e3ff"] else "#6d28d9",
            activeforeground=fg_color,
            bd=0,
            relief=tk.FLAT,
            command=command,
            cursor="hand2"
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)
        
    def _add_digit(self, digit):
        """Add a digit to current input"""
        current = self.result_text.get()
        if current == "0" or current == "Error":
            self.result_text.set(digit)
        else:
            self.result_text.set(current + digit)
            
    def _add_operator(self, operator):
        """Add an operator and move current value to expression"""
        current = self.result_text.get()
        if current == "Error":
            return
            
        if self.expression and self.expression[-1] in "+-*/%":
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += current + operator
            
        self.expression_text.set(self._format_expression(self.expression))
        self.result_text.set("0")
        
    def _format_expression(self, expr):
        """Format expression for display"""
        return expr.replace("*", "×").replace("/", "÷").replace("-", "−")
        
    def square(self):
        """Square the current number"""
        try:
            current = self.result_text.get()
            if current != "Error":
                result = float(current) ** 2
                if result.is_integer():
                    result = int(result)
                self.result_text.set(str(result))
        except Exception:
            self.result_text.set("Error")
            
    def sqrt(self):
        """Square root of current number"""
        try:
            current = self.result_text.get()
            if current != "Error":
                result = float(current) ** 0.5
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
                self.result_text.set(str(result))
        except Exception:
            self.result_text.set("Error")
            
    def calculate(self):
        """Evaluate the expression"""
        try:
            current = self.result_text.get()
            if current == "Error":
                return
                
            full_expr = self.expression + current
            if not full_expr or full_expr[-1] in "+-*/%":
                return
                
            result = eval(full_expr)
            
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
                    
            self.result_text.set(str(result))
            self.expression_text.set(self._format_expression(full_expr))
            self.expression = ""
            
        except Exception:
            self.result_text.set("Error")
            self.expression = ""
            
    def clear_all(self):
        """Clear everything"""
        self.expression = ""
        self.result_text.set("0")
        self.expression_text.set("")
        
    def _setup_keyboard_bindings(self):
        """Bind keyboard keys"""
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<KP_Enter>", lambda e: self.calculate())
        self.root.bind("<Escape>", lambda e: self.clear_all())
        
        for i in range(10):
            self.root.bind(str(i), lambda e, d=str(i): self._add_digit(d))
            
        self.root.bind("+", lambda e: self._add_operator("+"))
        self.root.bind("-", lambda e: self._add_operator("-"))
        self.root.bind("*", lambda e: self._add_operator("*"))
        self.root.bind("/", lambda e: self._add_operator("/"))
        self.root.bind(".", lambda e: self._add_digit("."))
        
    def run(self):
        """Start the calculator"""
        self.root.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()