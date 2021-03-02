# Compression

Steps I took to complete this:
1. Created a compression class
2. Created a dictionary that contains every single word used in the file and the amount of times it is used
I realized that it took 40 seconds for me to do this , but libraries such as collection take 1 second
3. Sorted that dictionary to order it from most common word to least common word
4. Created a list that assigned random characters to the most common words
5. Created a function to compress it using the method in step 4
Compressed to 90 percent of original file size
6. Realized there were more ascii characters so I found a list of characters that could be used to replace words and used that
7. Created a function again to compress the top approx 100 most common words. Approx 100 because thats how many asci chararacters that had not been used
Compressed to 82.6714801444 percent of original size
8. Created a function to decompress the file
Decompression works perfectly
9. Realized a smarter way to choose which words should be replaced is to times the amount of times the words appears by the letters in the words to find
out how much would be saved in total and found the top values in that instead
Compressed to 80.1444043321 percent of original size
10. Tries running the compression algorithm on the compressed file, brought it down to 79.7 percent of original file size
11. Trying to make it so sub-componenets of words like 'the', is compressed after a word like there
Compressed to 74 percent 
12. started to check the efficiency of using two letter words to replace the ot
Drawbacks to the method I'm using: It requries files where there are spaces in between words like books, stories etc


Decompression File, just one simple function.
How it works: At the bottom of the compressed file there is a dictionary that contains what each words has been compressed into.
