# Rule-Based Musical Interpreter – Computer Science III Project

**Institution**: Francisco José de Caldas District University  
**Program**: Systems Engineering

**Course**: Computer Science III  
**Professor**: Eng. Carlos Andrés Sierra, M.Sc.

---

## Team Members

- Esteban Villalba Delgadillo - 20212020064  
  eavillalbad@udistrital.edu.co  
- Daniel Felipe Barrera Suarez - 20212020097 
  dfbarreras@udistrital.edu.co

---

## Project Description

This project focuses on the design and partial implementation of a **domain-specific language (DSL)** for rule-based musical composition. Users can input structured commands like `play C4 for 1.0 at 0.0`, and the interpreter compiles this into a visual representation in a **piano roll** style, using Python and `matplotlib`.

Although still in early stages, this project lays the foundation for a complete musical interpreter that may later incorporate **real-time graphical rendering** and **sound playback** using `pygame`.

### Objectives

- Define a custom mini-language (DSL) for symbolic musical instructions.
- Parse and compile user input into a structured internal representation.
- Visualize the output using a piano roll-style plot generated with `matplotlib`.
- Establish the groundwork for future integration with audio playback and dynamic visualization libraries like `pygame`.

---

## Project Components

### 1. **Musical Language and Interpreter**:
- Users can define melodies using commands such as:

```bash
    play E4 for 1.0 at 0.0
    play G4 for 0.5 at 1.0
```
- The language supports basic note names (`C4`, `D#5`), durations (in seconds), and starting times.

### 2. **Compiler and Internal Representation**:
- Input commands are parsed into Python dictionaries with note, duration, and time.
- Notes are mapped to vertical positions using MIDI-like encoding.

### 3. **Piano Roll Visualization**:
- The compiled notes are plotted using `matplotlib` as horizontal bars.
- Each bar represents a note's pitch, duration, and starting time.
- Example visualization included in the `/figures` folder: **“Ode to Joy”** rendered from DSL input.

---

## Features

- **Custom Rule Syntax**: Simple, readable structure inspired by real musical notation.
- **Visual Output**: A clear piano roll allows verification of correct note timing and pitch.
- **Modular Architecture**: Separated into parsing, compiling, and rendering stages.
- **Theoretical Foundation**: Based on context-free grammars and parsing theory from Workshop 1.

---

## Future Work

- **Audio Playback**: Use `pygame.mixer` or `sounddevice` for real-time sound.
- **Graphical Animation**: Replace static plots with animated rendering via `pygame`.
- **Loops, Variables, and Macros**: Extend the DSL to support repeating structures and custom definitions.
- **Error Handling**: Add feedback for invalid syntax or unsupported inputs.

---

## Example Melody

Here’s a sample input that recreates the opening of **Beethoven’s “Ode to Joy”**:

```text
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
```

## Execution Instructions

1. **Cloning the repository:**
   To work with the ER model and supporting materials, clone the repository using the following command:
```bash
   git clone https://github.com/Inaryuta/ComputerScienceIII_FinalProject
```

2. **Navigating to the project directory & Accessing the ER Diagram, Essay, and Poster:**
```bash
   cd ComputerScienceIII_FinalProject
```