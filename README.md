# Mission 6
Github Link: https://github.com/AndyStoneman/M6-PoetrySlam

## System Name: Robot Frost
### Submission Date: 11/17/2022

## Project Description:
### Sources:

Web Scraping source: https://towardsdatascience.com/creating-a-poems-generator-using-word-embeddings-bcc43248de4f
Autocorrect: https://github.com/filyp/autocorrect
Inspiring articles:
1) https://arxiv.org/abs/2002.02511
2) https://www.aaai.org/Papers/Workshops/2006/WS-06-04/WS06-04-010.pdf
3) http://computationalcreativity.net/iccc2012/wp-content/uploads/2012/05/095-Colton.pdf

// Write why I chose these sources

### Description

Inspired by Robert Frost, "Robot Frost" aims to generate poetry similar to Frost's style, 
embodying his beautiful descriptions of rural New England, and his thought-provoking
language. 

The goal of "Robot Frost" is to take in any user-inputted word and generate a Robert Frost inspired
poem based on the word, with the goal of creating a poem that is more similar to the word than any of Frost's already
written poems (that is, based on the ones I have saved in 'poems.csv', but obviously he has a lot more!). Note
that similarity is entirely based on the spaCy similarity method, which uses vectors to determine the similarity of a 
word, phrase, or poem in our case, to another. Also note that the final output is most certainly in the blank verse
poetry style, as sometimes the output works very well, and other times, well, you'll see...

Here's how the system works:
1) Scrape the web for a ton of Robert Frost poetry content, and save it into a csv file. 
2) Take in a user-inputted descriptive word and determine the most similar Frost poem to the word.
3) Generate new poem that has a higher similarity ranking to the inputted word than one of the initially inputted poems:
   1) At particular probability either execute:
      1) Randomly select two lines until both are above a similarity threshold (the threshold is based on the most 
      similar already existing Frost poem) to the user-inputted word. Then combine the two verses to form a new child 
      verse. Repeat until desired number of lines reached, careful to not repeat any lines already used. 
      2) Add a random original Frost line that exceeds the threshold (threshold is same as above).
   2) At specified probability, replace either noun or verb in line with synonym or synonymous phrase.
4) Return new poem that is inspired by Frost and ideally more similar to the inputted word than the most similar 
already existing Frost poem. 
5) Read poem aloud.
6) Ask user if they like poem, and if so save it. If not, ask if they want to try again.

### How to run the code

It's simple, just make sure you have all necessary packages, and then run main() and follow the prompts!

### Challenges

// To do

