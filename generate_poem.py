import csv
import random
import spacy
from poem import Poem
from verse import Verse
from autocorrect import Speller
from wordhoard import Synonyms
import string


class GeneratePoem:
    """
    An object used to generate a Robert Frost style poem using spaCy, and a
    user inputted description_word.

    Args:
        word (str): The user inputted word to relate both Robert Frost's most
        similar poem and a newly generated poem too.

        nlp (nlp object): An nlp object that's used to do similarity
        computations.
    """
    def __init__(self, word, nlp):
        self.word = word
        self.description_word = nlp(word)
        self.nlp = nlp
        self.all_verses = []
        self.most_similar_poem_score = -1.0
        self.most_similar_poem_text = ""

    def make_poems(self):
        """
        Method used to read in a file containing Robert Frost poetry. Takes
        this poetry and generates both Poem and Verse objects. A list of
        the poem objects is then returned and all the verses are kept as
        an instance variable list.

        :return:
            A list of the Robert Frost poem objects.
        """
        print("\nHmmmm let me think about that...")
        with open("poems.csv", 'r') as file:
            reader = csv.reader(file)
            poems = []
            poem_index = 0
            next(reader)
            for line in reader:
                poem = self.nlp(line[2])
                if poem.vector_norm:
                    poem_index += 1
                    split_to_verses = line[2].split("\n")
                    for verse in split_to_verses:
                        if verse != '':
                            verse = verse.strip()
                            self.all_verses.append(
                                Verse(verse, self.description_word,
                                      self.nlp))
                poems.append(
                    Poem(poem_index, line[2], self.description_word, self.nlp))
        return poems

    def most_similar_poem(self, poems):
        """
        Calculates the most similar Robert Frost poem to the description word
        based on the Frost poems contained in the csv file.
        :param poems:
            A list of all the Frost poem objects.
        :return:
            The most similar poem to the description word.
        """
        for poem in poems:
            poem_score = poem.get_similarity()
            if poem_score > self.most_similar_poem_score:
                self.most_similar_poem_score = poem_score
                self.most_similar_poem_text = poem.text

    def get_all_verses(self):
        """ Returns a list of all the Frost Verse objects """
        return self.all_verses

    def get_most_similar_poem_score(self):
        """ Returns the similarity score of the most similar Frost poem """
        return self.most_similar_poem_score

    def get_most_similar_poem_text(self):
        """ Returns the text of the most similar Frost poem """
        return self.most_similar_poem_text

    def get_description_word(self):
        """ Returns the description word as an nlp object """
        return self.description_word

    def generate_frost(self):
        """
        Generates a Robert Frost style poem based on the user inputted
        description word. Does this by searching for lines within a certain
        threshold of similarity to the word, and at a certain probability,
        either injecting them into the final poem or forming a new line with
        two of them.
        :return:
            A newly generated Robert Frost poem, made up of both his lines
            from various poems and newly generated lines from his poems.
        """
        print("\nBut I think I can do better...")
        probability = 0.55
        count = 0
        temp = self.all_verses
        new_poem = []
        threshold = 0.1
        while count < 8:
            two_pair = 0
            random_verses = []
            while two_pair < 2:
                random_verse = random.choice(temp)
                random_similarity = random_verse.get_similarity()
                while random_similarity < self.most_similar_poem_score \
                        - threshold:
                    random_verse = random.choice(temp)
                    random_similarity = random_verse.get_similarity()
                random_verses.append(random_verse.get_text().strip().lower())
                if random.random() < probability:
                    two_pair += 1
                    temp.remove(random_verse)
                else:
                    two_pair += 2
                    temp.remove(random_verse)
            new_poem.append(
                self.merge_lines(random_verses))

            count += 1
        return new_poem

    def merge_lines(self, verses):
        """
        Takes two Frost verses and creates one child verse by swapping
        the nouns in the verse and returning the one that is more similar
        to the description word. Returns a blank line if nouns can't be
        extracted from both lines.
        :param verses:
            A list of the two verses we are attempting to combine.

        :return:
            Returns either a newly created line if successfully merged
            the two Frost lines, or a blank line if nouns couldn't be
            extracted from both verses.
        """
        if len(verses) == 1:
            return verses[0]
        nlp = spacy.load("en_core_web_lg")
        first_verse = nlp(verses[0])
        second_verse = nlp(verses[1])
        first_verse_nouns = [token.text for token in first_verse if
                             token.pos_ == "NOUN"]
        second_verse_nouns = [token.text for token in second_verse if
                              token.pos_ == "NOUN"]
        if len(first_verse_nouns) != 0 and len(second_verse_nouns) != 0:
            new_verse_one = verses[0].replace(random.choice(first_verse_nouns),
                                              random.choice(
                                                  second_verse_nouns))
            new_verse_two = verses[1].replace(
                random.choice(second_verse_nouns),
                random.choice(first_verse_nouns))
            if (nlp(new_verse_one).similarity(self.description_word) > nlp(
                    new_verse_two).similarity(self.description_word)):
                return new_verse_one
            else:
                return new_verse_two
        return ""

    def input_synonyms(self, verse, final_poem):
        """
        Inputs random synonyms for nouns in a newly-generated verse that are
        related to the user inputted word, making sure that the poem does not
        already use this word.
        :param verse:
            The verse we will change.
        :param final_poem:
            The soon-to-be newly generated Frost poem.
        :return:
            The newly modified verse with new synonyms.
        """
        first_verse = self.nlp(verse)
        first_verse_nouns = [token.text for token in first_verse if
                             token.pos_ == "NOUN"]
        if len(first_verse_nouns) != 0:
            synonyms = Synonyms(self.word).find_synonyms()
            random_index = random.randint(0, 20)
            while random_index > len(synonyms):
                random_index = random.randint(0, 20)
            synonym = synonyms[random_index].strip()
            while synonym in final_poem:
                random_index = random.randint(0, 20)
                if random_index < len(synonyms):
                    synonym = synonyms[random_index].strip()
            verse = verse.replace(random.choice(first_verse_nouns), synonym)
            return verse
        return verse

    def clean_poem_add_synonyms(self, new_poem):
        """
        Method both cleans up the newly generated poem so that it is more
        readable by doing some formatting and spell checking. Also, at a
        specified probability, calls the input_synonyms() method to inject
        synonyms into the lines.
        :param new_poem:
            The newly generated poem from the generate_frost() method.
        :return:
            The newly generated poem in a more readable format with a few
            other minor adjustments.
        """
        print("\nAlmost done, just a few final touches...")
        spell = Speller()
        probability = 0.4
        final_poem = ""
        for line in new_poem:
            for character in string.punctuation:
                if character == "'":
                    continue
                line = line.replace(character, '')
            if random.random() > probability:
                line = self.input_synonyms(line, final_poem)
            new_line = spell(line)
            final_poem += new_line + "\n"
            final_poem += "\n"
        return final_poem

    def __repr__(self):
        """ Lets us make a representation of a GeneratePoem object """
        has_score = hasattr(self, 'score')
        add_to_repr = 1
        if has_score:
            add_to_repr = self.score
        return "Generate Poem Object based on ('{0}') word\n".format(self.word)
