
from sentence import sentence

class sorter:
    
    sentences = []
        
    def __init__(self) -> None:
        pass
    

    def agregarSentence(self, prmSentence: sentence):
        self.sentences.append(prmSentence.shift()) 
             

    def ordenarSentences(self):
        self.sentences.sort(lambda x: x.sentence_words[0])
    
    
    def imprimirS(self):
        for i in range(0, len(self.sentences), 1):
            self.sentences[i].imprimir()
        

    
    def getElemento(self, prmPosicion):
        return self.sentences[prmPosicion]   
    
    def acomodar(self, prmSentencia: sentence):
        temporal = prmSentencia.getSentenceString()
        for i in range(0, len(prmSentencia.getSentence()), 1):

            self.agregarSentence(sentence(temporal))
            temporal = self.sentences[-1]    

    
    
   
