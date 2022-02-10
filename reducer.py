from operator import itemgetter
import sys

current_word = None
current_count = 0
min_len= 9999
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=line.lower()

    # parse the input we got from mapper.py
    word, count, min_word_len = line.split('\t')
    try:
      count = int(count)
      min_word_len= int(min_word_len)
    except ValueError:
      #count was not a number, so silently
      #ignore/discard this line
      continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        if (min_word_len < min_len):
                min_len=min_word_len
        current_count += count
    else:
        if current_word:
            if min_word_len<min_len:
                min_len=min_word_len
            # write result to STDOUT
            print ('%s\t%s\t%s' % (current_word, current_count, min_len))
        current_count = count
        min_len=min_word_len
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if min_word_len<min_len:
        min_len=min_word_len
    print( '%s\t%s\t%s' % (current_word, current_count, min_len))
