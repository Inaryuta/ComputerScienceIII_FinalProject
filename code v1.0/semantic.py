class SemanticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens

    def analyze(self):
        notes = []
        i = 0

        while i < len(self.tokens):
            # Esperamos: play NOTE for NUMBER at NUMBER
            if self.tokens[i].type_ == "KEYWORD" and self.tokens[i].value == "play":
                if i + 4 >= len(self.tokens):
                    raise Exception("Incomplete instruction after 'play'.")
                if self.tokens[i + 1].type != "NOTE":
                    raise Exception("Expected NOTE after 'play'.")
                if self.tokens[i + 2].type != "KEYWORD" or self.tokens[i + 2].value != "for":
                    raise Exception("Expected 'for' after NOTE.")
                if self.tokens[i + 3].type != "NUMBER":
                    raise Exception("Expected NUMBER after 'for'.")
                if self.tokens[i + 4].type != "KEYWORD" or self.tokens[i + 4].value != "at":
                    raise Exception("Expected 'at' after NUMBER.")
                if i + 5 >= len(self.tokens) or self.tokens[i + 5].type != "NUMBER":
                    raise Exception("Expected NUMBER after 'at'.")

                note = self.tokens[i + 1].value
                duration = float(self.tokens[i + 3].value)
                start_time = float(self.tokens[i + 5].value)
                notes.append((note, duration, start_time))
                i += 6
            else:
                raise Exception(f"Unexpected token: {self.tokens[i].value}")
        return notes, (4, 4)  # Time signature default
