import paho.mqtt.client as mqtt
from threading import Thread

class sentence:
    
    sentence_words = []
    sentence_multi_shift = []
    
    def __init__(self, prmCadena):
        self.sentence_words = prmCadena.split(" ")
        
    def shift(self):

        temporal_sentence_words = self.sentence_words.copy()
        temporal_sentence_words.insert(0, temporal_sentence_words[-1])
        temporal_sentence_words = temporal_sentence_words[:-1]
        self.sentence_words = temporal_sentence_words.copy()
        
        return sentence(" ".join(temporal_sentence_words))
    
    
    def getSentenceString(self): 
        return " ".join(self.sentence_words)
    
    
    def getTamaño(self):
        return len(self.sentence_words)
    
    
    def getSentence(self):
        return self.sentence_words
    
    def imprimir(self):
        print(self.sentence_words)

 
        
       
    
   
