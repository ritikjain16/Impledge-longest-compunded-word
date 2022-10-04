import time
start = time.time()
#End of word symbol
_end = '_end_'

#Make a trie out of nested HashMap, UnorderedMap, dict structures
def MakeTrie(words):
  root = dict()
  for word in words:
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
  return root

def LongestCompoundWord(original_trie, trie, word, level=0):
  first_letter = word[0]
  if not first_letter in trie:
    return False
  if len(word)==1 and _end in trie[first_letter]:
    return level>0
  if _end in trie[first_letter] and LongestCompoundWord(original_trie, original_trie, word[1:], level+1):
    return True
  return LongestCompoundWord(original_trie, trie[first_letter], word[1:], level)

#Words that were in your question
# f = open("file_name", 'r')
f = open("./Input_01.txt", 'r')
# f = open("./Input_02.txt", 'r')

lines = f.readlines()
words=[]
for line in lines:
    words.append(line.replace("\n",""))

# words = words[:87000]
trie = MakeTrie(words)

# #Sort words in order of decreasing length
words = sorted(words, key=lambda x: len(x), reverse=True)

# First Longest Compounded word 
for word in words:
  if LongestCompoundWord(trie,trie,word):
    print("Longest Compound Word:'{0:}'".format(word))
    words.remove(word)
    break

# Second Largest Compounded word 
for word in words:
  if LongestCompoundWord(trie,trie,word):
    print("Second Longest Compound Word:'{0:}'".format(word))
    words.remove(word)
    break

end = time.time()
elapsed = end-start

# Time to process input file
print("Input File Execution time is:" + str(elapsed) + " seconds.")