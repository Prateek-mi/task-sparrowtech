#1. this code will provide the longest two words contained in the input file that can be comprised of other words
#2. And the count of words in the document that can be comprised of other words

file = open('temp/words.txt', 'r')  #opening file words.txt
lines = file.readlines()            #reading file


def sorting(lst, reverse):                 #function which sort the words of file in reverse order according to length of words, means descending order
    lst2 = sorted(lst, key=len, reverse=reverse)
    return lst2


def find_comprised_words(source_word, ascending_list):  #this function compare each word of descending list with ascending list
    length = 0
    if source_word in ascending_list:
        ascending_list.remove(source_word)
    for k in ascending_list:
        if k in source_word:
            length = length + len(k)
            if length == len(source_word):
                return source_word
    return None


source_list = []  #empty list used as source list

for line in lines:
    source_list.append(line)

asc_list = sorting(source_list, False)   #ascending ordered list
desc_list = sorting(source_list, True)   #descending ordered list

count = 0
desc_count = 0

for x in desc_list:                     #this loop will run untill every word is traversed
    desc_count += 1
    found_word = find_comprised_words(source_word=x, ascending_list=asc_list)
    if found_word is not None:    #if root word found in ascending list count increases
        count += 1
        if count <= 2:
            print(found_word)     #printing two longest words comprised of other words

print(count)             #printing total no. of words comprised of other words
#end