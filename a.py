from gensim.models import Word2Vec
import string
import nltk

model = Word2Vec.load('models/word2vec.model')


def tokenizer(text: str):
    doc = str.lower(text)
    alpha = list([])

    for token in nltk.word_tokenize(doc):
        if token in string.punctuation:
            continue
        alpha.append(token)

    return alpha


def vectors_sum_combinaion(words_numbers):
    result = np.zeros(300)

    for token in words_numbers:
        try:
            result += model.wv.get_vector(token)
        except KeyError:
            if str.isnumeric(token):
                result += 0*len(token)
            else:
                result += 0

    return result


def vector_matrix(text):
    x = len(text)
    y = 300
    matrix = np.zeros((x, y))

    for i in range(x):
        words_numbers = tokenizer(text[i])
        matrix[i] = vectors_sum_combinaion(words_numbers)

        return matrix


print(model.wv.most_similar(positive=tokenizer('bebê')))
