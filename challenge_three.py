#Python 3.11.3
#My intial thoughts looking at this challenge:

    #this one seems a lot simpler than the last two I'm planing on using two loops to iterate through list of word concatinating them together in all possible combinations, printing them out, and checking if they match any words from the given list

#the list of words
words=[
    "albums",
    "barely",
    "befoul",
    "convex",
    "hereby",
    "jigsaw",
    "tailor",
    "weaver"
]

#the list of peices
peices=[
    "al",
    "bums",
    "bar",
    "ely",
    "be",
    "foul",
    "con",
    "vex",
    "here",
    "by",
    "jig",
    "saw",
    "tail",
    "or",
    "we",
    "aver"
]#they are all in order?

#I'm honestly not really sure what I'm supposed to get interms of output based on the example in the document:

    #albar != albums
    #alely != albums
    #albe != albums
    #etc …

#The issus is based on the above example output it seems I'm supposed to look for each word one at a time rather than using "find()" or something similar to check if each combination of peices is present in the list of words so thats what I'm gonna do, but if I'm iterating through the list of peices in order "albums" is gonna come up before "alber" so based on the example I'm gonna assume I'm supposed to check all words starting with "al" against "albums" even after I already find it in the list and by that reasoning I'm gonna assume I'm supposed to check all the words that start with "bar" against "barley" even after I've already found the combination that makes "barley". I'm also not sure if I'm supposed to be removing peices and words from the list as I go, but based on the example I'm gonna assume I don't

#this iterator will keep track of the current word I'm searching for even after finding it per the example
iii=0
#this is the first loop
for i in peices:
    #this is the second loop
    for ii in peices:
        #this is just a variable to hold the current concatination
        currentString = i + ii
        #checks if the concatination matches the word
        if currentString == words[iii]:
            print(f"{currentString} == {words[iii]}")
        else:
            print(f"{currentString} != {words[iii]}")
    #this increments through the list of "words" after every two "peices" in the outer loop to produce the expected output based on the instructions and example
    if (peices.index(i) + 1) % 2 == 0:
        iii = iii+1 