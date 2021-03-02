'''
Decompression File, just one simple function.
How it works: At the bottom of the compressed file there is a dictionary that contains what each words has been compressed into.
'''

def decompress(compressedfile, outputfile):
    if outputfile == '':
        outputfile = 'decompressed.txt'
    with open(compressedfile, 'r') as f:
        data = f.readlines()[-1]              # gets dictionary from last line of file
    replacedvals = eval(data)
    with open(compressedfile) as input_file:
        data = input_file.read()
        for key in replacedvals:
            data = data.replace(key, replacedvals.get(key))      # replaces values to original form
    with open(outputfile, 'w') as output_file:
        output_file.write(data)
    fileread=open(outputfile,"r")           # removes last line from dictionary (could probably be done in less code)
    info=fileread.read()
    fileread.close()
    info=info.split("\n")
    data="\n".join(info[:-1])
    fileread=open(outputfile,"w+")
    for i in range(len(data)):
        fileread.write(data[i])
    fileread.close()

decompress(input('file name: '), input('Outputfile(canbeleftblank): '))