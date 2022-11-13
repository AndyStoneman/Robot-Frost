class Poem:
    def __init__(self, title, text, description_word, similarity, verses):
        self.title = title
        self.text = text
        self.description_word = description_word
        self.similarity = similarity
        self.verses = verses

    def get_text(self):
        return self.text

    def get_verses(self):
        return self.verses

    def __repr__(self):
        """Lets us make an object of the same value."""
        return "Poem('{0}' | '{1}' similarity threshold = {2})\n".format(
            self.title, self.description_word, self.similarity)