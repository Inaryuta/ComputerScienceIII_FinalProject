import re

class Token:
    """Represents a token with type and value."""
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type_}, {self.value})"

class LexicalAnalyzer:
    """Lexical analyzer for the piano DSL."""

    @staticmethod
    def lex(code):
        tokens = []
        token_specification = [
            ("KEYWORD", r"\b(play|for|at)\b"),
            ("NOTE", r"[A-G](#|b)?[0-8]"),     # Ej: E4, C#5, Gb3
            ("NUMBER", r"\d+(\.\d+)?"),        # e.g., 1, 2.0, 0.5
            ("SKIP", r"[ \t]+"),               # spaces and tabs
            ("NEWLINE", r"\n"),                # line breaks
            ("MISMATCH", r"."),                # unrecognized characters
        ]

        tok_regex = "|".join(
            f"(?P<{name}>{pattern})" for name, pattern in token_specification
        )

        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()

            if kind in ("SKIP", "NEWLINE"):
                continue
            elif kind == "MISMATCH":
                raise RuntimeError(f"Unexpected character: {value}")
            elif kind == "NUMBER":
                value = float(value)
            tokens.append(Token(kind, value))

        return tokens
