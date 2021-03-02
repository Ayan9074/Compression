'''
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
'''

class Compression:
    def __init__(self, filename):
        self.filename = filename    # name of file to be compressed
        self.final_list = []
        self.sorted_dict = {}
        self.storagedict = {}

        self.openfile(filename)

    def openfile(self, filename):       # this function opens the file and gets a list of the total amount of characters used by the word for each word
        with open(filename) as input_file:
            data = input_file.read().split()
            words2 = []
            words = {}
            for i in data:
                if i not in words2 and len(i) > 1:
                    words2.append(i)
                    words[i] = int(data.count(i)) * (len(i))
        self.sortdict(words)
        print('File data retrieval complete')
        
    def sortdict(self, words):           # this function sorts the list of words by the most used(the one that uses the most characters)
        self.sorted_dict = {}
        sorted_keys = sorted(words, key=words.get)

        for w in sorted_keys:
            self.sorted_dict[w] = words[w]
            self.storagedict[w] = words[w]
        self.getsubstitutevalues(self.filename)
        print('Most common words sorted complete')

    def getsubstitutevalues(self, filename):   # this function assigns values to the top most common letters by checking which ascii characters are not used in the textfile
        symbols = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '/', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z', '{', '|', '}', '~', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ']
        with open(filename) as input_file:
            data = input_file.read()
            temp_list = [symbol in data for symbol in symbols]
            to_zip =  zip(symbols, temp_list)
            matched_list = dict(to_zip)
            self.final_list = {k:v for k,v in matched_list.items() if v != True}
        self.compression()
        print('Value substitution complete')
    
    def compression(self):   # this function compresses the file, first it compresses words that are not subwords of other words than the subwords of other words
        with open(self.filename) as input_file:
            replacedvals = {}
            data = input_file.read()
            for key in self.final_list:
                try:
                    replacedvals[key] = max(self.sorted_dict, key=self.sorted_dict.get)
                except:
                    print("No more repititions everything done")
                try:
                    to_delete = max(self.sorted_dict, key=self.sorted_dict.get)
                    del self.sorted_dict[to_delete]
                except:
                    print("No more to delete/ words to go through")
            checkedamount = 0
            neededamount = len(replacedvals) - 2
            for key in replacedvals:
                for key2 in replacedvals:
                    if replacedvals.get(key2).find(replacedvals.get(key)) != -1:
                        checkedamount -= 1
                    else:
                        checkedamount += 1

                if checkedamount == neededamount:
                    data = data.replace(replacedvals.get(key), key)

                checkedamount = 0
            for key in replacedvals:
                data = data.replace(replacedvals.get(key), key)


        with open('CompressedFile.txt', 'w') as output_file:
            output_file.write(data+'\n'+str(replacedvals))
        print('Compression Complete')

Compression = Compression(input('Enter the file to Compress here: '))