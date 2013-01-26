import sys
class otp:
  def __init__(self, key="", pt="attack at dawn", ct="6c73d5240a948c86981bc294814d"):
    ct = self.splitCount(ct,2)
    # print strToHex(pt)
    pt = map(self.charToHex, self.splitCount(pt,1))
    print 'ciphertext1'
    print ct
    print 'plaintext1'
    print pt
    key = map(self.xor, ct, pt) 

    print 'key'
    print key
    print map(hex, key)

    print 'plaintext2'
    pt2 = map(self.charToHex, list("attack at dusk"))
    print pt2

    q=[]
    for x in pt2:
      x='0x' + x
      q.append(int(x,16))
    print q
    print 'ciphertext2'
    ct2 =  map(self.xorIntList, q, key)
    f=[]
    for x in ct2:
      val = ((str(hex(x)).strip('0x')))
      if len(val)==1:
        val="0"+val
      f.append(val)
    ct2=f
    print ct2
    print ''.join(ct2)


  def xorIntList(self, q, w):
    return (q ^ w)
  def xor(self, q , w):
    return (int(q, 16) ^ int(w, 16))
  def splitCount(self, s, count):
    return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
  def charToHex(self, c):
    r = hex(ord(c)).strip('0x')
    if len(r) == 1:
      r = "0"+r
    return r
  def strToHex(self, astring):
    hexStr = ""
    for x in astring:
      hexStr = hexStr + "%02X " % ord(x)
    return hexStr
  def Crypt(self, aString):
      kIdx = 0
      cryptStr = ""
      for x in range(len(aString)):
          cryptStr = cryptStr + \
                     chr( ord(aString[x]) ^ ord(self.key[kIdx]))
          # use the mod operator - % - to cyclically loop through
          # the keyword
          kIdx = (kIdx + 1) % len(self.key)
      return cryptStr

if __name__ == "__main__":
  o = otp()
