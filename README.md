# Mission 6
Github Link: https://github.com/AndyStoneman/M6-PoetrySlam

## System Name: TBD
### Submission Date: 11/17/2022

## Project Description:

Web Scraping inspiration: https://towardsdatascience.com/creating-a-poems-generator-using-word-embeddings-bcc43248de4f
Autocorrect: https://github.com/filyp/autocorrect

Inspired by Robert Frost, this system aims to generate poetry similar to Frost's style, 
embodying his beautiful descriptions of rural New England, and his thought-provoking
language. 

Here's how the system will work:
1) Scrape the web for a ton of Robert Frost poetry content, and save it into a csv file. 
2) Pick n words for description choices, and rank every poem's similarity to each of the chosen words
3) Generate new poem that has a higher similarity ranking to the inputted word than one of the initially inputted poems
   1) Randomly select two lines until either both are above or their average is above the threshold of all poems for 
   particular input word. Then combine them to form a new child line. Repeat until desired number of lines reached, 
   careful to not repeat any lines already used. 
   2) At specified probability, replace either noun or verb in line with synonym or synonymous phrase
   3) Add one more unique modifier 
   4) If the description word is the same as a word in the line, change the word in the line to a synonym
4) Return new poem that is inspired by Frost but more similar to a particular inputted word than any of the poems in the file
5) Read poem aloud
6) Save poem in .csv file. 