text = input("Enter text: ")
word = input("Enter the word you are looking for: ")
words = text.split()
word_checker = False
for i in range(len(words)):
    if words[i] == word:
        word_checker = True
        break

if word_checker:
    if i == 0:
        print("The word you searched for was found in the {}st word of the sentence.".format(str(i+1)))
    elif i == 1:
        print("The word you searched for was found in the {}nd word of the sentence.".format(str(i+1)))
    elif i == 2:
        print("The word you searched for was found in the {}rd word of the sentence.".format(str(i+1)))
    else:
        print("The word you searched for was found in the {}th word of the sentence.".format(str(i+1)))
else:
    print("The word you searched for was not found.")
