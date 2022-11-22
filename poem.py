class Poem:
    """
    Class for holding an individual Frost verse/line. This is used to store
    information about each saved frost line.

    Args:
        title (str): the title of the poem.

        text (str): The actual text of the line.

        description_word (str): The user inputted word that we are trying to
        relate the generated poem too.

        nlp (nlp object): An nlp object that's used to do similarity
        computations.
    """
    def __init__(self, title, text, description_word, nlp):
        self.title = title
        self.text = text
        self.description_word = description_word
        self.similarity = -1.0
        self.nlp = nlp

    def get_text(self):
        """ Returns a poem's text"""
        return self.text

    def get_similarity(self):
        """ Returns a poem's similarity to the user's description word """
        if self.similarity == -1.0:
            self.calculate_similarity()
        return self.similarity

    def calculate_similarity(self):
        """ Calculates a poem's similarity to the user's description word """
        description_word = self.nlp(self.description_word)
        line = self.nlp(self.text)
        if line.vector_norm:
            self.similarity = (description_word.similarity(line))
        else:
            self.similarity = 0.0

    def __repr__(self):
        """ Lets us make a representation of a Poem object """
        return "Poem('{0}' | '{1}' similarity threshold = {2})\n".format(
            self.title, self.description_word, self.similarity)
