class Verse:
    """
    Class for holding an individual Frost verse/line. This is used to store
    information about each saved frost line.

    Args:
        text (str): The actual text of the line.

        description_word (str): The user inputted word that we are trying to
        relate the generated poem too.

        nlp (nlp object): An nlp object that's used to do similarity
        computations.
    """
    def __init__(self, text, description_word, nlp):
        self.text = text
        self.description_word = description_word
        self.similarity = -1.0
        self.nlp = nlp

    def get_text(self):
        """ Returns a verse's text """
        return self.text

    def get_similarity(self):
        """ Returns a verse's similarity to the user's description word """
        if self.similarity == -1.0:
            self.calculate_similarity()
        return self.similarity

    def calculate_similarity(self):
        """
        Calculates a lines similarity to the user's description word and
        stores it in the instance variable.
        """
        description_word = self.nlp(self.description_word)
        line = self.nlp(self.text)
        if line.vector_norm:
            self.similarity = (description_word.similarity(line))
        else:
            self.similarity = 0.0

    def __repr__(self):
        """ Lets us make a representation of a Verse object """
        return "Verse(From Poem: '{0}' || '{1}' || '{2}' similarity " \
               "threshold = {3})\n".format(self.poem_title, self.text,
                                           self.description_word,
                                           self.similarity)
