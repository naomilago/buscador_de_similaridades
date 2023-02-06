from flask import Flask, render_template
from gensim.models import Word2Vec
import string
import nltk

app = Flask(__name__)

model = Word2Vec.load('models/word2vec.model')

word = 'it\'s workin'

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


@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/credits.html')
def credits():
    return render_template('credits.html')
  
@app.route('/find_similarities.html')
def find_similarities():
    return render_template('find_similarities.html')
  
@app.route('/faq.html')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)
