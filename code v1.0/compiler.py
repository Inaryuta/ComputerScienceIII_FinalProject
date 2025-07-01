import matplotlib.pyplot as plt
from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer
from semantic import SemanticAnalyzer

def note_to_y(nota):
    """Convierte una nota musical (ej: 'C4', 'F#5') a una posición numérica en el eje Y."""
    notas_map = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    nombre_nota = nota[:-1]
    octava = int(nota[-1])
    
    posicion_nota = notas_map.get(nombre_nota)
    if posicion_nota is None:
        # Manejo de bemoles si fuera necesario, por ahora se asumen sostenidos
        return -1 # O manejar el error de otra forma
        
    return octava * 12 + posicion_nota

def visualize(notes):
    """Crea y muestra una visualización de piano roll a partir de las notas procesadas."""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Obtener las posiciones Y y las etiquetas de las notas únicas
    y_positions = sorted(list(set(note_to_y(n[0]) for n in notes)))
    y_labels = []
    
    # Crear un mapa de posición a nombre de nota para las etiquetas del eje Y
    pos_to_note_map = {note_to_y(n[0]): n[0] for n in notes}
    y_labels = [pos_to_note_map[y] for y in y_positions]

    for nota, duracion, inicio in notes:
        y = note_to_y(nota)
        ax.broken_barh([(inicio, duracion)], (y - 0.4, 0.8), facecolors='cornflowerblue')
        ax.text(inicio + duracion / 2, y, nota, ha='center', va='center', color='white', weight='bold')

    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Notas Musicales")
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.title("Visualización de Piano Roll")
    plt.tight_layout()
    plt.show()

class Compiler:
    def compile_and_visualize(self, code: str):
        """Compila el código, muestra los resultados en consola y genera la visualización."""
        print("--- Análisis Léxico ---")
        tokens = LexicalAnalyzer.lex(code)
        for token in tokens:
            print(token)

        print("\n--- Análisis Sintáctico ---")
        sintactic_analyzer = SintacticAnalyzer(tokens)
        sintactic_analyzer.parse()
        print("Sintaxis OK")

        print("\n--- Análisis Semántico ---")
        semantic_analyzer = SemanticAnalyzer(tokens)
        notes, time_signature = semantic_analyzer.analyze()
        print("Notas extraídas:")
        for n in notes:
            print(n)
        print(f"Compás: {time_signature}")
        
        print("\n--- Generando Visualización ---")
        visualize(notes)
        print("Visualización mostrada.")


if __name__ == "__main__":
    script = """
    play E4 for 1.0 at 0.0
    play E4 for 1.0 at 1.0
    play F4 for 1.0 at 2.0
    play G4 for 1.0 at 3.0
    play G4 for 1.0 at 4.0
    play F4 for 1.0 at 5.0
    play E4 for 1.0 at 6.0
    play D4 for 1.0 at 7.0
    play C4 for 1.0 at 8.0
    play C4 for 1.0 at 9.0
    play D4 for 1.0 at 10.0
    play E4 for 1.0 at 11.0
    play E4 for 1.0 at 12.0
    play D4 for 1.0 at 13.0
    play D4 for 1.0 at 14.0
    """
    compiler = Compiler()
    compiler.compile_and_visualize(script)