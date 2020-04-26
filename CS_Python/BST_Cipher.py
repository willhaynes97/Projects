#  File: BST_Cipher.py

#  Description: Encrypt and decrypt using trees

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None

    self.e_str = encrypt_str
    self.et_str = self.e_str.lower()
    new_string = ''
    for i in range(len(self.e_str)):
      if ((self.e_str[i] >= 'a' and self.e_str[i] <= 'z') or (self.e_str[i] == ' ')):
        new_string += self.e_str[i]
    self.e_str = new_string

    for i in range (len(self.e_str)):
      self.insert(self.e_str[i])

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    
    if (self.find(ch) != None):
      return
    else:
      new_node = Node (ch)
      if (self.root == None):
        self.root = new_node
      else:
        current = self.root
        parent = self.root
        while (current != None):
          parent = current
          if (ch < current.data):
            current = current.lchild
          else:
            current = current.rchild
        if (ch < parent.data):
          parent.lchild = new_node
        else:
          parent.rchild = new_node


  def find (self, ch):
    current = self.root
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current
          

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    string = ''
    current = self.root
    if (self.root.data == ch):
      return '*'
    else:
      while (current != None) and (current.data != ch):
        if (ch < current.data):
          string += '<'
          current = current.lchild
          
        else:
          string += '>'
          current = current.rchild
          
      if (current == None):
        return ''
      else:
        return string
      

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root

    if len(st) == 0:
      return ''
    

    if (st[0] == '*'):
      return current.data
    
    for i in range(len(st)):
      if ((st[i] == '<') and (current.lchild != None)):
        current = current.lchild
        
      elif ((st[i] == '>') and (current.rchild != None)):
        current = current.rchild

      else:
        return ''
      
    return current.data
      
    

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    string = ''
    if (st == ''):
      return string

    st = st.lower()

    for i in range(len(st)):

      if (st[i] in self.e_str):
        string += self.search(st[i]) + '!'


    return string

      

    
    

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    string = ''
    if (st == ''):
      return string

    st = st.split('!')

    for i in range(len(st)):
      string += self.traverse(st[i])


    return string


def main():
  key = str(input('Enter encryption key: '))
  print()
  tree = Tree(key)

  str_for_encryption = str(input('Enter string to be encrypted: '))
  encrypted_str = tree.encrypt(str_for_encryption)
  print ('Encrypted string: ' + encrypted_str)
  print()

  str_for_decryption = str(input('Enter string to be decrypted: '))
  decrypted_str = tree.decrypt(str_for_decryption)
  print ('Decrypted string: ' + decrypted_str)
  print()


main()
