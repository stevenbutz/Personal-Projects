from collections import defaultdict


def GroupAnagrams(strs):
    res = defaultdict(list) #creates a default hashmap of keys to lists. The keys need to be immutible so change at end. 

    for s in strs: #takes each string in the list of strings

        count = [0] * 26 #makes a list of count for the amount of each characters in a specific string a-z

        for c in s: # for each character in the string

            count[ord(c) - ord("a")] += 1 # at position 0 to 25 in the array for a-z whataver the character in unicode subtract a so "a" - "a: would be position 0 in count becoming the letter a for 
                    # a specific string of characters. 
        
        res[tuple(count)].append(s) # Makes the count of the specific word to the key and the value is that string in the form of a list

    return res.values() # returns that list
print (GroupAnagrams(["sugma","ligma","sugma","sugma","sumga","umags"]))