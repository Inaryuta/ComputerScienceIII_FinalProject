import matplotlib.pyplot as plt
from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer
from semantic import SemanticAnalyzer

def note_to_y(nota):
    """Convierte una nota musical (ej: 'C4', 'F#5') a una posición numérica en el eje Y."""
    # Mapa de notas robusto que incluye bemoles como equivalentes a sostenidos
    notas_map = {
        'C': 0, 'B#': 0,
        'C#': 1, 'Db': 1,
        'D': 2,
        'D#': 3, 'Eb': 3,
        'E': 4, 'Fb': 4,
        'F': 5, 'E#': 5,
        'F#': 6, 'Gb': 6,
        'G': 7,
        'G#': 8, 'Ab': 8,
        'A': 9,
        'A#': 10, 'Bb': 10,
        'B': 11
    }
    octava = int(nota[-1])
    nombre_nota = nota[:-1]
    
    posicion_nota = notas_map.get(nombre_nota)
    if posicion_nota is None:
        raise ValueError(f"Nota desconocida: {nota}")
        
    return octava * 12 + posicion_nota

def y_to_note(y):
    """Convierte una coordenada Y numérica de vuelta a su nombre de nota (ej: 61 -> 'C#5')."""
    # Usamos sostenidos como la representación estándar
    nota_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octava = y // 12
    indice_nota = y % 12
    return f"{nota_names[indice_nota]}{octava}"

def visualize(notes):
    """Crea y muestra una visualización de piano roll a partir de las notas procesadas."""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    min_y = note_to_y('C3')
    max_y = note_to_y('B5')

    y_ticks_completos = list(range(min_y, max_y + 1))
    y_labels_completos = [y_to_note(y) for y in y_ticks_completos]

    for y in range(min_y, max_y + 1):
        if '#' in y_to_note(y):
            # Dibuja un rectángulo horizontal negro semitransparente
            ax.axhspan(y - 0.5, y + 0.5, facecolor='black', alpha=0.5, zorder=0)


    y_ticks_completos = list(range(min_y, max_y + 1))
    y_labels_completos = [y_to_note(y) for y in y_ticks_completos]

    # Barras de las notas
    for nota, duracion, inicio in notes:
        y = note_to_y(nota)
        ax.broken_barh([(inicio, duracion)], (y - 0.4, 0.8), facecolors='cornflowerblue', edgecolor='black')
        ax.text(inicio + duracion / 2, y, nota, ha='center', va='center', color='white', weight='bold', size=10)

    # Líneas horizontales para separar cada nota en el eje
    for y in range(min_y, max_y + 2):
        ax.axhline(y - 0.5, color='gray', linestyle='--', linewidth=0.5)
    
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
    ax.set_yticks(y_ticks_completos)
    ax.set_yticklabels(y_labels_completos)
    ax.set_ylim(min_y - 0.5, max_y + 0.5) # Ajustar límites para que se vean bien las líneas

    for tick_label in ax.get_yticklabels():
            if '#' in tick_label.get_text():
                tick_label.set_color('white')
                # Se establece un cuadro de fondo negro para la etiqueta
                tick_label.set_bbox(dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0.2'))

    
    ax.grid(True, axis='x', linestyle=':', color='black', alpha=0.7) # Mantenemos solo la rejilla vertical
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
    play D#4 for 2.0 at 13.0
    """
    compiler = Compiler()
    compiler.compile_and_visualize(script)