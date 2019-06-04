sentence = str(input("Input some text. It can be a phrase, a sentence, or multiple sentences."))

sentence == sentence[::-1]
sentence = sentence.lower()
import re
sentence = re.sub(r'[^A-Za-z]', "", sentence)
print(sentence)

if sentence == sentence[::-1]:
    print("is a palindrome")
else:
    print("is not a palindrome")