def ngram(str1):
  trigram=[]
  bigram=[]
  tango = str1.split()
  for i in range(len(tango)-1):
    bigram.append(tango[i]+tango[i+1])
  for i in range(len(str1)-2):
    trigram.append(str1[i]+str1[i+1]+str1[i+2])
  return bigram,trigram

str1="I am an NLPer"
print(ngram(str1))

