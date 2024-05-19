#Python 3.11.3
#My intial thoughts looking at this challenge:

    #check if the number is negative, use the words "thousand" and "million" to divide the written numbers into substrings of at most three digits, create a function which will translate the substrings into digits, multiply the digits by thier respective position (millions, thousands, hundreds), add the three numbers to gether
        
        #checking if the number is negative is as simple as checking if "negative" is at the begining of the string

        #for example by finding the words "million" and "thousand" we can devide the number "nine hundered seventy million eighteen thousand four hundred two" into three substrings
            #"nine hundered seventy"(millions)
            #"eighteen" (thousands)
            #"four hundred two" (hundreds)

        #create a function that can translate the substrings into digits. I suspect this will be the most difficult part
            #"nine hundred seventy" -> 970 (millions)
            #"eighteen" -> 18 (thousand)
            #"four hundred two" -> 402

        #multiply the digits by thier respective position (millions, thousands, hundreds)
            #970 (millions) -> 970,000,000
            #18 (thousands) -> 18,000
            #402 -> 402

        #assemble our number
            #970,000,000 + 18,000 + 402 = 970,018,402

#this is a dictionary of all the strings that will need to be translated into numbers
stringNumberDict = {
    #zero is only gonna be used in one case
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
    "eleven" : 11,
    "twelve" : 12,
    "thirteen" : 13,
    "fourteen" : 14,
    "fifteen" : 15,
    "sixteen" : 16,
    "seventeen" : 17,
    "eighteen" : 18,
    "nineteen" : 19,
    "twenty" : 20,
    "thirty" : 30,
    "forty" : 40,
    "fifty" : 50,
    "sixty" : 60,
    "seventy" : 70,
    "eighty" : 80,
    "ninety" : 90
}
#the idea is I'm gonna use the spaces between words to pull out smaller substrings which I'll match to the keys in this dictionary"translate" them into numbers and add them together 

#this is a function which will divide a string into an list of substrings using the " " character
def substringBySpace(string):
    #first I'm gonna remove any spaces on the ends of the string
    string=string.strip()
    #now I'm gonna splite the string into substrings using the " " character
    #I'm gonna check if there are any spaces in our substring. If there aren't I'll just return an array with one string
    if string.find(" ") == -1:
        subsubstrings=[string]
        return (subsubstrings)
    #if there are spaces this will split the string into multiple strings divided by spaces
    return string.split(" ")

#this function will use the dictionary to "translate" the strings to numbers
def translateStringToDigits(string, stringNumberDict):
    #the one string which isn't in the dictionary is "hundred" because there will be a special way to handle it
    if string == "hundred":
        #I'll handle this when I'm putting the number together
        return -1
    #otherwise this function will return the number based on the corresponding dictionary value
    return stringNumberDict [string]

#this is gonna be the function that translates our substrings into digits
def substringToDigits(substring, stringNumberDict):
    #this array that will hold the substrings we get from our substring using the "substringBySpace" function
    subSubStrings = substringBySpace(substring)
    #this array will hold our numbers
    numbers=[]
    #this for loop will convert the strings into numbers using the "translateStringToDigits" function
    for substring in subSubStrings:
        numbers.append(translateStringToDigits(substring, stringNumberDict))
    #time to handle the hundred
    #if there was a hundred present it will always be in the second spot (index[1]) so we will check if its present and if so it will be removed and the number at index[0] will be multiplied bv 100
    if len(numbers) >=2: 
        if numbers [1]== -1:
            #multipying by 100
            numbers[0] = numbers[0]*100
            #removing the 100 placeholder from the array
            numbers.pop(1)
    #now we just add our numbers in the array together
    #this varible will hold our sum
    sum = 0
    #this for loop will loop throgh the array of numbers so they can be added together
    for number in numbers:
        sum = sum + number
    return sum

#this function will handle "negative", check if the substrings "million" and "thousand" are present in the string, split it into substrings accoundingly, use the "substringToDigits" function to convert the strings into numbers, mutiply them by 1,000,000 or 1,000 as necessary and add them together to get our number
def stringWithThouOrMilToNumber(string, stringNumberDict):
    #this variable will hold our final number
    number=0
    #this variable will keep track of if the number is negative
    isNegative=False
    #check if "negative" is in the string
    if string[:8]=="negative":
        string=string[8:]
        isNegative=True
    #check if "million" is present and pull out the approprate substring to convert to numbers and multilpy by 1,000,000
    if string.find("million") != -1:
        #pulls out millions from our string
        millions=string.split("million")[0]
        #this is whats left over
        string=string.split("million")[1]
        #here the substring to digits is called and the result is multipied by 1,000,000 and added to the "number" variable
        number=number + (1000000 * substringToDigits(millions, stringNumberDict))
        #if the leftover is blank we can return the number here
        if string == '':
            #check if negative
            if isNegative:
                number = number * -1
            return number
    #check if "thousand" is present pull out the approprate substring to convert to numbers and multilpy by 1,000
    if string.find("thousand") != -1:
        #pulls out thousands from our string
        thousands=string.split("thousand")[0]
        #this is whats left over
        string=string.split("thousand")[1]
        #here the substring to digits is called and the result is multipied by 1,000 and added to the "number" variable
        number=number + (1000 * substringToDigits(thousands, stringNumberDict))
        #if the leftover is blank we can return the number here
        if string == '':
            #check if negative
            if isNegative:
                number = number * -1
            return number
    #if there is any of the string leftover at this point it will be converted to a number, added to the total and returned
    number = number + substringToDigits(string, stringNumberDict)
    #check if negative
    if isNegative:
        number = number * -1
    return number


print(stringWithThouOrMilToNumber("six", stringNumberDict))
print(stringWithThouOrMilToNumber("negative seven hundred twenty nine", stringNumberDict))
print(stringWithThouOrMilToNumber("one million one hundred one", stringNumberDict))

