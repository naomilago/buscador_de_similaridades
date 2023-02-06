from flask import Flask, render_template
from gensim.models import Word2Vec

app = Flask(__name__)

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
