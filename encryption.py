from tools import bin_num,decimal,base64_list,session_key
def converttobase(binary:list):
  enc_hash = ""
  i = 0
  if len(binary)>24:
    while i<24:
      enc_hash+=base64_list[decimal(binary[i:i+6])]
      i+=6
    enc_hash+=converttobase(binary[24:])
  else:
    org_length = len(binary)
    binary.extend([0]*(24-len(binary)))
    i = 0
    while i < 24:
      enc_hash+=base64_list[decimal(binary[i:i+6])]
      i+=6
    enc_hash = list(enc_hash)
    j = -1
    for i in range((24-org_length)//8):
       enc_hash[j] = '='
       j-=1
    enc_hash = ''.join(enc_hash)
  return enc_hash

def encrypt(msg:str):
  enc_msg = []
  for i in msg:
    enc_msg.append(ord(i)^session_key)
  enc_hash = converttobase(bin_num(enc_msg))
  return (enc_hash,session_key)