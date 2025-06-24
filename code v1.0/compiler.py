from lexical import LexicalAnalyzer
from sintactic import SintacticAnalyzer
from semantic import SemanticAnalyzer

class Compiler:
    def compile_and_print_output(self, code: str):
        """Compila el código y muestra los tokens, validación sintáctica y resultado semántico."""
        print("Lexical Analysis:")
        tokens_ = LexicalAnalyzer.lex(code)
        for token in tokens_:
            print(token)

        print("\nSyntactic Analysis:")
        sintactic_analyzer = SintacticAnalyzer(tokens_)
        sintactic_analyzer.parse()
        print("Syntax OK")

        print("\nSemantic Analysis:")
        semantic_analyzer_ = SemanticAnalyzer(tokens_)
        notes, time_signature = semantic_analyzer_.analyze()
        print("Notes:")
        for n in notes:
            print(n)
        print(f"Time Signature: {time_signature}")


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
    compiler.compile_and_print_output(script)
