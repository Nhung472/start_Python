#def
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalzer(object):
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        self.fmtText = formattedText

    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        return freqMap

    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

analyzed = TextAnalzer(givenstring)
print("Formatted Text:", analyzed.fmtText)
freqMap = analyzed.freqAll()
print(freqMap)

word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")

x="Go"

if(x=="Go"):

  print('Go ')

else:

  print('Stop')

print('Mike')

x=5
while(x!=2):
  print(x)
  x=x-1


class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points(1,2)
p1.print_point()

for i,x in enumerate(['A','B','C']):
    print(i+1,x)

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=2

p2.print_point()

def delta(x):
  if x==0:
    y=1
  else:
    y=0
  return(y)

a=1

def do(x):
    a=100
    return(x+a)

print(do(1))
