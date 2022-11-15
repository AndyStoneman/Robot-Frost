import csv
import random
import spacy
from poem import Poem
from verse import Verse
from autocorrect import Speller
from wordhoard import Synonyms

class GeneratePoem:

    def __init__(self, word, nlp):
        self.word = word
        self.description_word = nlp(word)
        self.nlp = nlp
        self.all_verses = []
        self.most_similar_poem_score = -1.0
        self.most_similar_poem_text = ""

    def make_poems(self):
        with open("poems.csv", 'r') as file:
            reader = csv.reader(file)
            poems = []
            poem_index = 0
            next(reader)
            for line in reader:
                poem = self.nlp(line[2])
                if poem.vector_norm:
                    # print("Poem " + str(poem_index) + ":\n" + line[2])
                    poem_index += 1
                    #similarity = (self.description_word.similarity(poem))
                    # print("Similarity to ~" + description_word.text + "~ is " + str(
                    #   similarity))
                    split_to_verses = line[2].split("\n")
                    for verse in split_to_verses:
                        if verse != '':
                            verse = verse.strip()
                            self.all_verses.append(
                                Verse(poem_index, verse, self.description_word))
                poems.append(
                    Poem(poem_index, line[2], self.description_word))
        return poems

    def most_similar_poem(self, poems):
        most_similar_poem = 0.0
        for poem in poems:
            poem_score = poem.get_similarity()
            if poem_score > self.most_similar_poem_score:
                self.most_similar_poem_score = poem_score
                self.most_similar_poem_text = poem.text
    def get_all_verses(self):
        return self.all_verses

    def get_most_similar_poem_score(self):
        return self.most_similar_poem_score

    def get_description_word(self):
        return self.description_word

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