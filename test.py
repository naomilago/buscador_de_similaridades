from gensim.models import Word2Vec
import string
import nltk

def tokenizer(text: str):
    doc = str.lower(text)
    alpha = list([])

    for token in nltk.word_tokenize(doc):
        if token in string.punctuation:
            continue
        alpha.append(token)

    return alpha

model = Word2Vec.load('models/word2vec.model')

a = model.wv.most_similar(positive=tokenizer('tecnologia'))

print(str.capitalize(a[0][0]))
print('{:,.1f}'.format(a[0][1] * 100))

print()

print(str.capitalize(a[1][0]))
print('{:,.1f}'.format(a[1][1] * 100))

print()

print(str.capitalize(a[2][0]))
print('{:,.1f}'.format(a[2][1] * 100))