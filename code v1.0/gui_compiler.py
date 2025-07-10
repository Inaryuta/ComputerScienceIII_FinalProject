import tkinter as tk
from tkinter import messagebox, scrolledtext
from compiler import Compiler

class PianoCompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PianoDSL Compiler")
        self.compiler = Compiler()

        # Editor
        self.editor = scrolledtext.ScrolledText(root, width=40, height=10, font=("Courier", 12))
        self.editor.pack(padx=10, pady=10)

        # Botón de Compilación
        self.compile_button = tk.Button(root, text="Compile and Visualize", command=self.compile_code, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.compile_button.pack(pady=(0,10))

    def compile_code(self):
        code = self.editor.get("1.0", tk.END).strip()
        if not code:
            messagebox.showwarning("Warning", "Expecting instructions.")
            return

        try:
            self.compiler.compile_and_visualize(code)
        except SyntaxError as e:
            messagebox.showerror("Sintax Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PianoCompilerGUI(root)
    root.mainloop()