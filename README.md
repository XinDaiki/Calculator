# BRIEF EXPLANATION 

### 1-2 : Imports
<img width="250" height="150" alt="image" src="https://github.com/user-attachments/assets/c9afa223-be18-4dd1-9134-3182131920de" />

Imports the tkinter library for creating the GUI (Graphical User Interface) <br>
**font** module allows custom fonts (though not heavily used here)
# 

### 4-20 : The  def __init__ (self)  
<img width="550" height="400" alt="image" src="https://github.com/user-attachments/assets/d22800ba-94c4-4490-9c52-d5b3a4238cac" /> <br> 
This runs automatically when you create a calculator. It:

- Creates the main window <br>
- Sets up variables to track the calculator's state <br>
- Calls helper methods to build the UI

**Key variables:**

- self.expression = "" - stores the calculation being built (e.g., "5+3") <br>
- self.result_text - displays the current number <br> 
- self.expression_text - shows the calculation history <br> 
