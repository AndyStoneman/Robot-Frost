import spacy


class Verse:
    def __init__(self, poem_title, line, description_word):
        self.poem_title = poem_title
        self.line = line
        self.description_word = description_word
        self.similarity = 0.0

    def calculate_similarity(self):
        nlp = spacy.load("en_core_web_lg")
        description_word = nlp("beautiful")
        line = nlp(self.line)
        if line.vector_norm:
            similarity = (description_word.similarity(line))
        else:
            similarity = 0.0
        return similarity

    def __repr__(self):
        """Lets us make an object of the same value."""
        return "Verse(From Poem: '{0}' || '{1}' || '{2}' similarity threshold = {3})\n".format(
            self.poem_title, self.line, self.description_word, self.similarity)
