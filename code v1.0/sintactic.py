# GRAMMAR DEFINITION FOR PIANO DSL:

# <S>            -> <INSTRUCTION> <S> | <INSTRUCTION>
# <INSTRUCTION>  -> "play" <NOTE> "for" <NUMBER> "at" <NUMBER>
# <NOTE>         -> <LETTER> [<ACCIDENTAL>] <OCTAVE>
# <LETTER>       -> "A" | "B" | "C" | "D" | "E" | "F" | "G"
# <ACCIDENTAL>   -> "#" | "b"
# <OCTAVE>       -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8"
# <NUMBER>       -> <DIGITS> ["." <DIGITS>]
# <DIGITS>       -> <DIGIT> <DIGITS> | <DIGIT>
# <DIGIT>        -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

class SintacticAnalyzer:
    """This class represents the behavior of a syntactic analyzer for the piano DSL."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    def advance(self):
        """Advances to the next token."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        """Parses a sequence of instructions."""
        if not self.current_token:
            self.error("Expected instruction, got empty input")

        self.instruction()
        while self.current_token:
            self.instruction()

    def instruction(self):
        """Parses one instruction: play NOTE for NUMBER at NUMBER."""
        self.expect("KEYWORD", "play")
        self.note()
        self.expect("KEYWORD", "for")
        self.number()
        self.expect("KEYWORD", "at")
        self.number()

    def note(self):
        """Parses a NOTE token (e.g., C4, D#5)."""
        if self.current_token and self.current_token.type_ == "NOTE":
            self.advance()
        else:
            self.error("NOTE")

    def number(self):
        """Parses a NUMBER token (e.g., 1, 0.5)."""
        if self.current_token and self.current_token.type_ == "NUMBER":
            print(f"Number parsed: {self.current_token.value}")
            self.advance()
        else:
            self.error("NUMBER")

    def expect(self, type_, value=None):
        """Checks that the current token matches type and optional value, then advances."""
        if not self.current_token:
            self.error(f"Expected {type_} {'with value ' + value if value else ''}, got None")
        if self.current_token.type_ != type_:
            self.error(f"Expected type {type_}, got {self.current_token.type_}")
        if value is not None and self.current_token.value != value:
            self.error(f"Expected value '{value}', got '{self.current_token.value}'")
        self.advance()

    def error(self, expected):
        raise SyntaxError(f"Syntax error: expected {expected}, got {self.current_token}")
