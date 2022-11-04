from generate_poem import GeneratePoem
import csv


def main():
    with open("sentences_poems.csv", 'r') as file:
        reader = csv.reader(file)
        poem_objects = []
        poem = []
        for line in reader:
            if line[0] == '':
                continue

            if line[1] == '0':
                poem.append(line[2].strip())

            if line[1] != '0':
                break
        poem_objects.append(GeneratePoem(poem))
    print(poem_objects[0])


main()