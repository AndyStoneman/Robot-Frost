from generate_poem import GeneratePoem
import csv
import random
import spacy
from poem import Poem
from verse import Verse


def main():
    nlp = spacy.load("en_core_web_lg")
    description_word = nlp("beautiful")
    with open("poems.csv", 'r') as file:
        reader = csv.reader(file)
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
                        verse.strip()
                        verses.append(Verse(poem_index, verse, description_word))
            poems.append(Poem(poem_index, line[2], description_word, similarity, verses))

        for poem in poems:
            print(poem.get_verses())





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
