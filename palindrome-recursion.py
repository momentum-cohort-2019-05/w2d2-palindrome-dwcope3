#Recursion Palindrome Program

sentence = str(input("Input some text. It can be a phrase, a sentence, or multiple sentences."))

# # make all characters lower case
sentence = sentence.lower()
# # remove spacing and punctuation
import re
sentence = re.sub(r'[^A-Za-z]', "", sentence)



def palindrome(sentence):
    if len(sentence) <= 1:
        return True
    elif sentence[0] != sentence[-1]:
        return False
    else:
        sentence = sentence[1:-1]
        return palindrome(sentence)

if palindrome(sentence):
    print("is a palindrome")
else:
    print("is not a palindrome")

