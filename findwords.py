''' objective of this program is to find letter(s) in a given words
in a given sentence. The result will true if letters found in a sentence are in same order
as in the word. Otherwise result will be false ( that include letter in the sentence is less than
the letter in the word)
for example: given word is "dog"
sentence is: "the {d}ay {o}f mine starts with {g}reen tea"
This program will check the sequence as identified in {}. '''

def word_count(str):
    count_dict = {}
    for char in str:
        if not char in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

'''def word_location(str):
    loc_dict = {}
    last_loc = {}
    for char in str:
        if not char in loc_dict:
            last_loc[char] = str.index(char)
            loc_dict[char] = [str.index(char,last_loc[char])]
            continue
        loc_dict[char].append(str.index(char,last_loc[char]+1))
        last_loc[char] = str.index(char,(last_loc[char]+1))
    return loc_dict
'''

def check_count(c_result1, c_result2):
    count_check = {}
    for key in c_result1:
        if key in c_result2:
            if c_result1[key] <= c_result2[key]:
                count_check[key] = True
            else:
                count_check[key] = False
        else:
            count_check[key] = False
    return count_check

def order_result(str1, str2, c_check):
    results={}
    location = 0
    if all(value == True for value in c_check.values()):
        for char in str1:
            try:
                if str2.index(char, location) >= location:
                    results[char] = True
                    location = (str2.index(char, location)) + 1
                else:
                    results[char] = False
            except:
                results[char] = False
        if all(value == True for value in results.values()):
            results = "The letter in words in order in sentence"
        else:
            results = "The letter in words are not in order, in sentence"
    else:
        results= "The sentence do not contain letter(s) or contain less than required"
    return results

def pos(str1, str2):
    count_result1 = word_count(str1)
    count_result2 = word_count(str2)
    #position_result1 = word_location(str1)
    #position_result2 = word_location(str2)
    count_eva = check_count(count_result1, count_result2)
    results = order_result(str1, str2, count_eva)
    return results


cond = True
while cond:
    word = input("Enter a word: ")
    if word.isalpha():
        cond = False
    else:
        print("Please enter word comprising of alphabets only")

sentence = input("Enter letters or sentence to find letter word: ")

print(pos(word, sentence))