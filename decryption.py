from tools import bin_num,decimal,base64_dict


def decrypt(hash:str,session_key:int=27):
  count = 0
  for i in range(len(hash)-2,len(hash)):
    if '='==hash[i]:
      count+=1
  j = -1
  hash = list(hash)
  for i in range(count):
    hash[-(i+1)]='A'
  hash = bin_num([base64_dict[i] for i in hash],6)
  hash = hash[:len(hash)-(8*count)]
  msg = ""
  i = 0
  while i<len(hash):
    msg+=(chr(decimal(hash[i:i+8])^session_key))
    i+=8
  return msg
