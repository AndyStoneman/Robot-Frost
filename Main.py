from generate_poem import GeneratePoem
import csv
import random
import spacy
from poem import Poem
from verse import Verse
from autocorrect import Speller
from wordhoard import Synonyms


def main():
    nlp = spacy.load("en_core_web_lg")
    word = input("What would you like the poem to be like?\n")
    gp = GeneratePoem(word, nlp)
    poems = gp.make_poems()

    gp.most_similar_poem(poems)

    new_poem = gp.generate_frost()

    final_poem = gp.clean_poem(new_poem)

    print(final_poem[:-1])
    if len(final_poem) != 0:
        print(nlp(final_poem).similarity(nlp(word)))


if __name__ == "__main__":
    main()
