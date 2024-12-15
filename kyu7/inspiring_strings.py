def longest_word(string_of_words):
   output= {}
   word_list = string_of_words.split()
   for idx,word in enumerate(word_list):
       output.update({idx: len(word)})
   max(output.values())
   
