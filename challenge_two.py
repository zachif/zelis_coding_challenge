#Python 3.11.3
#My intitial thoughts on this challenge is to go through and find all the substrings that are, for lack of a better term, symmetrical and keep track of the longest one
    
    #starting out convert all the characters in the string a lowercase

    #create a loop that goes through the string character by character to check if it is part of a symmetrical string.

    #keep track of the longest string so far

    #return the longest string

string = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

def findLongestPalindrome(string):
    #converts entire string to lower case
    string=string.casefold()
    #this variable will be used to keep track of the longest palindrome in the loop
    longestPalindrome=string[0]
    #this variable will be used on the loop to keep track of the largest ii value and therefore the largest string
    longestii=0
    #looping through the string
    for i in range(0, len(string)-1, 1):
        ii=1 #this is another iterator which will come into play shortly. Here it is reset to 0 at the start of the for loop

        #the idea here is to check if the characters before and after the character at index "i" are the same, and if they are, check if the characters before and after that set are the same and so on until we come to a set of characters which aren't identical 
        #I'm planning to use the second iterator "ii" to keep track of the length of the substring
        #the idea is the substrings will look like this: string[(i-ii)+1:i+ii]
        #ii will increase as we go through the second loop so even though "ii" isn't really the length of the substring, the substring with the biggest "ii" value before exiting the loop will still be the biggest palindrome substring
        #aside from using "ii" to keep track of the longest substring it will also be used to make sure the loop doesn't go out of bounds by making sure the loop stops if "i"-"ii" is less than zero or if "i"+"ii" is greater than the last index in the string
        while i-ii >= 0 and i+ii < len(string) and string[i-ii] == string [i+ii]:
            #ii increased by one each time through the while loop
            ii=ii+1
        #if "ii" comes out of the loop larger than the value currently stored at "longestii" its value will become the new value at "longestii" and the corrisponing substring "string[(i-ii)+1:i+ii]" will replace the string at "longestPalindrome"
        if longestii < ii:
            longestii = ii
            longestPalindrome=string[(i-ii)+1:i+ii]
    #this first while loop really only works if the longest palendrome has an odd number of characters so I'm gonna also make a second loop that basically does the same thing but checks for palindrome with an even number of character which would have been missed by my first loop just in case
        #the palindrome with the even number of characters is literally only possible if the character at "string[i]" is the same as the character at "string[i+1]" so this second while loop wont even run if they aren't
        if string[i] == string[i+1]:
            ii=1
            while i-ii >= 0 and i+ii+1 < len(string) and string[i-ii] == string [i+1+ii]:
                ii=ii+1
                if longestii <= ii:
                    longestii = ii
                    longestPalindrome=string[(i-ii)+1:i+ii+1]
    return longestPalindrome

print(findLongestPalindrome("Ilikeracecarsthatgofast"))
print(findLongestPalindrome(string))