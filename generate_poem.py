class GeneratePoem:

    def __init__(self, poem):
        self.poem = poem

    def __str__(self):
        final_string = ''
        for line in self.poem:
            final_string += line + "\n"
        return final_string

    def __repr__(self):
        """Lets us make an object of the same value."""
        has_score = hasattr(self, 'score')
        add_to_repr = 1
        if has_score:
            add_to_repr = self.score
        return "GeneratePoem('{0}')\n".format(self.poem)