import csv
import random
import spacy
from poem import Poem
from verse import Verse
from autocorrect import Speller
from wordhoard import Synonyms
import string


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
                    poem_index += 1
                    split_to_verses = line[2].split("\n")
                    for verse in split_to_verses:
                        if verse != '':
                            verse = verse.strip()
                            self.all_verses.append(
                                Verse(poem_index, verse, self.description_word,
                                      self.nlp))
                poems.append(
                    Poem(poem_index, line[2], self.description_word, self.nlp))
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

    def get_most_similar_poem_text(self):
        return self.most_similar_poem_text

    def get_description_word(self):
        return self.description_word

    def generate_frost(self):
        probability = 0.7
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
                self.merge_lines(random_verses, self.description_word))

            count += 1
        return new_poem

    def merge_lines(self, verses, description_word):
        print(verses)
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
            print("first_verse_nouns ", first_verse_nouns)
            print("second_verse_nouns ", second_verse_nouns)
            new_verse_one = verses[0].replace(random.choice(first_verse_nouns),
                                              random.choice(
                                                  second_verse_nouns))
            new_verse_two = verses[1].replace(
                random.choice(second_verse_nouns),
                random.choice(first_verse_nouns))
            if (nlp(new_verse_one).similarity(description_word) > nlp(
                    new_verse_two).similarity(description_word)):
                return new_verse_one
            else:
                return new_verse_two
        return ""

    def input_synonyms(self, verse, word, final_poem):
        first_verse = self.nlp(verse)
        first_verse_nouns = [token.text for token in first_verse if
                             token.pos_ == "NOUN"]
        if len(first_verse_nouns) != 0:
            print("CHANGED")
            print("before synonyms === ", verse)
            synonyms = Synonyms(word).find_synonyms()
            random_index = random.randint(0, 20)
            synonym = synonyms[random_index].strip()
            while synonym in final_poem:
                random_index = random.randint(0, 20)
                synonym = synonyms[random_index].strip()
            verse = verse.replace(random.choice(first_verse_nouns), synonym)
            print("after synonyms === ", verse)
            return verse
        return verse

    def clean_poem_add_synonyms(self, new_poem):
        spell = Speller()
        probability = 0.5
        final_poem = ""
        for line in new_poem:
            for character in string.punctuation:
                if character == "'":
                    continue
                line = line.replace(character, '')
            if random.random() > probability:
                line = self.input_synonyms(line, self.word, final_poem)
            # print(line)
            new_line = spell(line)
            # print(new_line)
            final_poem += new_line + "\n"
        return final_poem

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
