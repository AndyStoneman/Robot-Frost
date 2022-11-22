from generate_poem import GeneratePoem
import spacy
import pyttsx3
import os


def main():
    nlp = spacy.load("en_core_web_lg")
    text = "I really like Robert Frost, so much so that I think I can " \
           "write just like him!\nIn fact, I have a special power that " \
           "allows me to rank how similar his poems are to a particular " \
           "word.\nWhy don't you give me a word, I'll tell you the most " \
           "similar Frost poem, and then I'll make a short one that's " \
           "better (Inspired by Frost, of course)!\n"
    print(text)
    word = input("So, what word is inspiring you?\n")
    gp = GeneratePoem(word, nlp)
    poems = gp.make_poems()

    gp.most_similar_poem(poems)
    best_poem_score = gp.get_most_similar_poem_score()
    print("\nThis is Frost's most similar poem to your word:\n")
    print("~" * 40, "\n")
    print(gp.get_most_similar_poem_text() + "\n")
    print("~" * 40)
    print("\nThis is the similarity score of that poem: ")
    print("{:.2f}%\n".format(best_poem_score * 100))

    new_poem = gp.generate_frost()

    final_poem = gp.clean_poem_add_synonyms(new_poem)

    print("\nHere's my new poem:\n")
    print("~" * 40, "\n")
    print(final_poem[:-1])
    print("~" * 40)
    if len(final_poem) != 0:
        print("\nAnd this is the score of my new poem:")
        final_score_poem = nlp(final_poem).similarity(nlp(word))
        print("{:.2f}%".format(final_score_poem * 100))
        if final_score_poem > best_poem_score:
            print("\nMine is more similar!\n")
        else:
            print("\nOh no, mine wasn't as similar!\n")

    # Read poem out loud
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(final_poem)
    engine.runAndWait()

    answer = input("Did you like the poem? (yes or no)\n")
    if answer == "yes":
        print("\nGreat! I'll save it!")
        if os.stat("saved_poems.txt").st_size == 0:
            with open("saved_poems.txt", "w") as f:
                f.write(final_poem)
                f.write("~" * 40 + "\n")
        else:
            with open("saved_poems.txt", "a") as f:
                f.write(final_poem)
                f.write("~" * 40 + "\n")
    else:
        print("\nBummer, I'll get rid of it then. Maybe try running me again?")


if __name__ == "__main__":
    main()
