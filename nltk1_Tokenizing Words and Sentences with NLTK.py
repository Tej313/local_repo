from nltk.tokenize import sent_tokenize,word_tokenize
example_text="hello Mr Smith,how are you doing today? The weather is great and python is awaesome. the sky in pinkish blue. you should not eat cardboard"
#print(sent_tokenize(example_text))
#print(word_tokenize(example_text))
for i in word_tokenize(example_text):
    print (i)