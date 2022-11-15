from generate_poem import GeneratePoem
import csv
import random
import spacy
from poem import Poem
from verse import Verse
from autocorrect import Speller
from wordhoard import Synonyms


def merge_lines(verses, description_word):
    print(verses)
    nlp = spacy.load("en_core_web_lg")
    first_verse = nlp(verses[0])
    second_verse = nlp(verses[1])
    first_verse_nouns = [token.text for token in first_verse if token.pos_ == "NOUN"]
    #first_verse_verbs = [token.lemma_ for token in first_verse if token.pos_ == "VERB"]
    second_verse_nouns = [token.text for token in second_verse if token.pos_ == "NOUN"]
    #second_verse_verbs = [token.lemma_ for token in second_verse if
    #                    token.pos_ == "VERB"]
    # print("Noun phrases first verse:", first_verse_nouns)
    # print("Verbs first verse:", first_verse_verbs)
    # print("Noun phrases second verse:", second_verse_nouns)
    # print("Verbs second verse:", second_verse_verbs)
    if len(first_verse_nouns) != 0 and len(second_verse_nouns) != 0:
        print("first_verse_nouns ", first_verse_nouns)
        print("second_verse_nouns ", second_verse_nouns)
        new_verse_one = verses[0].replace(random.choice(first_verse_nouns), random.choice(second_verse_nouns))
        new_verse_two = verses[1].replace(random.choice(second_verse_nouns), random.choice(first_verse_nouns))
    # print("this is the first new verse '" + new_verse_one + "'")
    # print("this is the second new verse '" + new_verse_two + "'")
        if (nlp(new_verse_one).similarity(description_word) > nlp(new_verse_two).similarity(description_word)):
            return new_verse_one
        else:
            return new_verse_two
    return ""

def main():
    nlp = spacy.load("en_core_web_lg")
    word = input("What would you like the poem to be like?\n")
    description_word = nlp(word)
    with open("poems.csv", 'r') as file:
        reader = csv.reader(file)
        all_verses = []
        poems = []
        poem_index = 0
        next(reader)
        for line in reader:
            verses = []
            poem = nlp(line[2])
            if poem.vector_norm:
                #print("Poem " + str(poem_index) + ":\n" + line[2])
                poem_index += 1
                similarity = (description_word.similarity(poem))
                #print("Similarity to ~" + description_word.text + "~ is " + str(
                 #   similarity))
                split_to_verses = line[2].split("\n")
                for verse in split_to_verses:
                    if verse != '':
                        verse = verse.strip()
                        verses.append(Verse(poem_index, verse, description_word))
                        all_verses.append(verse)
            poems.append(Poem(poem_index, line[2], description_word, similarity, verses))

    temp = all_verses
    most_similar_poem = 0.0
    best_poem = Poem('x', 'x', 'x', 'x', 'x')
    for poem in poems:
        if poem.get_similarity() > most_similar_poem:
            most_similar_poem = poem.get_similarity()
            best_poem = poem
    print("most similar poem score = ", most_similar_poem)
    #print(best_poem.get_text())
    count = 0
    new_poem = []
    threshold = 0.05
    while count < 4:
        two_pair = 0
        random_verses = []
        while two_pair < 2:
            random_verse = random.choice(temp)
            random_verse_nlp = nlp(random_verse)
            random_similarity = description_word.similarity(random_verse_nlp)
            while random_similarity < most_similar_poem - threshold:
                random_verse = random.choice(temp)
                random_verse_nlp = nlp(random_verse)
                random_similarity = description_word.similarity(random_verse_nlp)
            random_verses.append(random_verse.strip().lower())
            two_pair += 1
            temp.remove(random_verse)
        new_poem.append(merge_lines(random_verses, description_word))
        count += 1
    spell = Speller()
    final_poem = ""
    for line in new_poem:
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.replace("'", "")
        #print(line)
        new_line = spell(line)
        #print(new_line)
        final_poem += line + "\n"
    print(final_poem)
    print(nlp(final_poem).similarity(description_word))
    print("WORDHOARD TEST")
    syn_words = []
    for i in Synonyms(word).find_synonyms():
        syn_words.append(i)
    print(syn_words)


        #print(random_verse)
        #print(random_similarity)








    '''
            if line[1] == '0':
                poem.append(line[2].strip())

            if line[1] != '0':
                break
            #print(line)
            poem_string += line[2]
        poem_objects.append(GeneratePoem(poem))
    '''
    # random.shuffle(poem)
    #print(poem_string)
    #poem_v2 = nlp("fear")
    # docs = nlp.pipe(poem)
    # new_poem = nlp(poem_string)
    # train_corpus = nlp("love")
    #train_corpus = nlp(" ".join([token.text for token in train_corpus if
          #                       not token.is_stop and len(token) > 4]))
    # print("Noun phrases:", [chunk.text for chunk in poem_v2.noun_chunks])
    # print("Verbs:", [token.lemma_ for token in poem_v2 if token.pos_ == "VERB"])
    # for token in poem_v2:
    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #           token.shape_, token.is_alpha, token.is_stop)
    # total = 0
    # count = 0
    # for sent in docs:
    #     if sent.vector_norm:
    #         similarity = (train_corpus.similarity(sent))
    #         print(train_corpus.text + " " + sent.text + " " + str(similarity))
    #         total += similarity
    #         count += 1
    # print("average similarity = " + str(total / count))
    # print("overall calculated similarity = " + str(train_corpus.similarity(new_poem)))



main()
