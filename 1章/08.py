def cipher(str1):
  result=""
  for i in range(len(str1)):
    if str1[i].islower():
      result += chr(219 - ord(str1[i]))
    else:
      result += (str1[i])
  return result

str1="378g87238ge872"
print(cipher(str1))