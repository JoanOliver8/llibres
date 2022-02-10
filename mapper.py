import re
from unicodedata import normalize
import sys
import io
import re
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

stop_words = stopwords.words('spanish') + stopwords.words('french')
stop_words = set(stop_words)

# Bucle per llegir cada línia dels fitxers, passar el text a minúscules i eliminar els signes de puntuació.
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
for line in input_stream:
  line = line.strip()
  line = re.sub(r'[^\w\s]', '',line)
  line = line.lower()
  for x in line:
    if x in punctuations:
      line=line.replace(x, " ")

  words=line.split()
# Eliminam els signes d'accentuació de les lletres amb una regular expression (no elimina la ñ)
# Link regex: https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l
  for word in words: 
    if word not in stop_words:
      if word[0:1]!='ç':
        word = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                normalize( "NFD", word), 0, re.I
            )
        word = normalize( 'NFC', word)
        
      letra = word[0:1]
      if letra in list('abcdefghijklmnñopqrstuvwxyzç'):
        print('%s\t%s' % (letra, 1))
