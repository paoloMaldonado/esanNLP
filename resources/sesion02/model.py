from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

class Model:
    def __init__(self, vectorization_type='tfidf'):
        self.vectorization_type = vectorization_type
        self.model = None

    def fit(self, X, y):
        steps = [("tfidf", TfidfVectorizer()),
                  ("svm", SVC(kernel="rbf"))]
        
        self.model = Pipeline(steps)
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    
