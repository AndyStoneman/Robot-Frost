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
2) Input a descriptive word and rank every poem's similarity level to the word
3) Generate new poem that has a higher similarity ranking to the inputted word than one of the initially inputted poems
   1) Randomly select two lines until either both are above or their average is above the threshold of all poems for 
   particular input word. Then combine them to form a new child line. Repeat until desired number of lines reached, 
   careful to not repeat any lines already used. 
   2) At specified probability, replace either noun or verb in line with synonym or synonymous phrase
   3) Add one more unique modifier 
4) Return new poem that is inspired by Frost but more similar to a particular inputted word than any of the poems in the file
5) Read poem aloud
6) Ask user if they like poem, and if so save it. If not, ask if they want to try again. 


## TODO:
1. Try to make the poems a little more readable
   A) Introduce a probability that causes a direct frost line to be put into the poem when not triggered
   B) Add another unique way of changing the lines
2. Create a format_poem() method that makes the poem a little more attractive to read 
3. Clean up all methods so that they're readable and elegant 
4. Insert comments for all methods
5. Make the input writing a little more interesting/exciting