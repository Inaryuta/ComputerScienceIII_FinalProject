import tkinter as tk
from tkinter import messagebox, scrolledtext
from compiler import Compiler

class PianoCompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador de Notas Musicales")
        self.compiler = Compiler()

        # Editor
        self.editor = scrolledtext.ScrolledText(root, width=80, height=20, font=("Courier", 12))
        self.editor.pack(padx=10, pady=10)

        # Botón de Compilación
        self.compile_button = tk.Button(root, text="Compilar y Visualizar", command=self.compile_code, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.compile_button.pack(pady=(0,10))

    def compile_code(self):
        code = self.editor.get("1.0", tk.END).strip()
        if not code:
            messagebox.showwarning("Advertencia", "Por favor escribe alguna instrucción.")
            return

        try:
            self.compiler.compile_and_visualize(code)
        except SyntaxError as e:
            messagebox.showerror("Error de Sintaxis", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PianoCompilerGUI(root)
    root.mainloop()