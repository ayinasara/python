words=["apple","banana","apple","orange","banana","apple"]
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)

text='apple,is good for health'
text_1=text.split()
word_count={}
for word in text_1:
    word_count[word]=word_count.get(word,0)+1
print(word_count)