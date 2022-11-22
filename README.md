# Mission 6
Github Link: https://github.com/AndyStoneman/M6-PoetrySlam

## System Name: Robot Frost
### Submission Date: 11/17/2022

## Project Description:
### Sources:

Web Scraping source: https://towardsdatascience.com/creating-a-poems-generator-using-word-embeddings-bcc43248de4f
Autocorrect source: https://github.com/filyp/autocorrect
Inspiring articles:
1) https://arxiv.org/abs/2002.02511
   I chose this source because I liked the idea of "dream poetry," where we can create poetry based on particular 
   emotions or themes, which I think is something I try and do in my system.
2) https://www.aaai.org/Papers/Workshops/2006/WS-06-04/WS06-04-010.pdf
   While I didn't use any of the actual computation ideas from this paper, I was inspired by the idea of a
   computationally produced poem conveying some type of desired meaning, which I tried to incorporate in my system too.
3) http://computationalcreativity.net/iccc2012/wp-content/uploads/2012/05/095-Colton.pdf
   This paper gave me an idea for how to actually go about implementing my system once I had the idea. While my system 
   is certainly not anywhere close to as complex as the system in the paper, I liked the idea of analyzing something
   as a base, using it to find something that already exists (such as an article, or in my case, a Frost poem), and
   then ultimately generates something new based on the same dataset!

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
already existing Frost poem. This is a critical self-evaluation step!
5) Read poem aloud.
6) Ask user if they like poem, and if so save it. If not, ask if they want to try again.

### How to run the code

It's simple, just make sure you have all necessary packages, and then run main() and follow the prompts!

### Challenges

This system was VERY challenging. I spent a ton of time trying to first figure out exactly what I wanted to do, and 
then figuring out how to actually implement it. A lot of the frustrating parts came from trying to get certain packages
to work, but also trying to create a reasonable end product. I had to learn how to do a bunch of new things, including
spaCy stuff, web scraping, nlp, among others, and then had to remember a lot of coding skills from the past. Another
really challenging aspect was the amount of debugging I had to do, as I was constantly getting errors throughout the
process of implementing. Trying to quickly figure out errors was quite difficult at times! Last, I think one of the 
hardest parts was to ultimately create a Frost inspired poem that was somewhat coherent. I made a ton of changes before
getting something that was (usually) reasonable to read! Overall, I think I learned a lot about computer science things,
but also about myself, in that I was able to overcome some pretty stressful moments throughout the development of this
system. So to finally see the entire system come together now is really awesome!
