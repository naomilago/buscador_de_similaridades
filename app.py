from flask import Flask, render_template, request
from gensim.models import Word2Vec
import string
import nltk

app = Flask(__name__)

model = Word2Vec.load('models/word2vec.model')

def tokenizer(text: str):
    doc = str.lower(text)
    alpha = list([])

    for token in nltk.word_tokenize(doc):
        if token in string.punctuation:
            continue
        alpha.append(token)

    return alpha

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/credits.html')
def credits():
    return render_template('credits.html')
  
@app.route('/find_similarities.html', methods=['POST', 'GET'])
def find_similarities():
    if request.method == 'POST':
        query = request.form['pesquisa']
        
        results = model.wv.most_similar(positive=tokenizer(query))
        
        res1 = str.capitalize(results[0][0])
        res2 = str.capitalize(results[1][0])
        res3 = str.capitalize(results[2][0])

        return render_template('find_similarities.html', res1=res1, res2=res2, res3=res3)
    else:
        res1, res2, res3 = 'Digite sua pesquisa acima', 'Digite sua pesquisa acima', 'Digite sua pesquisa acima'
        return render_template('find_similarities.html', res1=res1, res2=res2, res3=res3)
  
@app.route('/faq.html')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)
