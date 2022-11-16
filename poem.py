import spacy


class Poem:
    def __init__(self, title, text, description_word, nlp):
        self.title = title
        self.text = text
        self.description_word = description_word
        self.similarity = -1.0
        self.nlp = nlp

    def get_text(self):
        return self.text

    def get_verses(self):
        return self.verses

    def get_similarity(self):
        if self.similarity == -1.0:
            self.calculate_similarity()
        return self.similarity

    def calculate_similarity(self):
        description_word = self.nlp(self.description_word)
        line = self.nlp(self.text)
        if line.vector_norm:
            self.similarity = (description_word.similarity(line))
        else:
            self.similarity = 0.0

    def __repr__(self):
        """Lets us make an object of the same value."""
        return "Poem('{0}' | '{1}' similarity threshold = {2})\n".format(
            self.title, self.description_word, self.similarity)
