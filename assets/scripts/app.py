import gensim

w2v = gensim.models.Word2Vec.load('../../models/word2vec.model')

w2v.wv.vector_size