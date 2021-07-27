from snowballstemmer import TurkishStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk

neg=open('negative_words_tr.txt',"r",encoding="utf-8").readlines()
pos=open('positive_words_tr.txt',"r",encoding="utf-8").readlines()

stoplist=stopwords.words('turkish')
letters=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"," "]

class WordAnalysis():
    def __init__(self,sentence):
        self.sentence=sentence
    
    def remove_stopwords(self,text):
        """
        This function removes stopwords and returns sentence without stopwords.
        """
        return " ".join([word for word in str(text).split() if word not in stoplist])

    def stemming_tokenizer(self,text): 
        """
        This function breaks down the words in the sentence and returns the final form of the sentence.
        """
        stemmer = TurkishStemmer()
        return [stemmer.stemWord(w) for w in word_tokenize(text)]

    def negative(self,x):
        """
        returns count of negative words(int)
        """
        count=0
        for i in x:
            if i+"\n" in neg:
                count=count+1
        return count

    def positive(self,x):
        """
        returns count of positive words(int)
        """
        count=0
        for i in x:
            if i+"\n" in pos:
                count=count+1
        return count

    def preprocessing(self):
        """
        This function removes non-Turkish characters in the sentence and returns the final form of the sentence.
        """
        new_sentence=""
        for letter in self.sentence.lower():
            if letter in letters:
                new_sentence=new_sentence+letter
        return new_sentence
    
    def analysis(self):   
        """
        Returns
        negative_words_count -> int
        positive_words_count -> int
        all_words_count -> int
        risk_rate -> int
        """
        new_sentence=self.preprocessing()         
        new_sentence=self.stemming_tokenizer(new_sentence)
        negative_words=self.negative(new_sentence)
        positive_words=self.positive(new_sentence)
        all_words=len(new_sentence)
        risk=(negative_words-positive_words)*100/(all_words-10)
        if positive_words>negative_words:
            risk=(negative_words/positive_words)*100/(all_words-10)
        return negative_words,positive_words,all_words,round(risk,2)

