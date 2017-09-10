original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  new_word = word + word[0] + 'ay'
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'Empty string. Please enter a valid input'
