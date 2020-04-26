#  File: TestBinaryTree.py

#  Description: adding to the classes Node and Tree


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
    
class Tree (object):
  def __init__ (self):
    self.root = None

  # search for a node with a key
  def search (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order(aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data)

  # return the node with minimum value
  def min_node (self):
    current = self.root

    if (current == None):
      return None

    while (current.lchild != None):
      current = current.lchild

    return current



  # return the node with maximum value
  def max_node (self):
    current = self.root
    
    return current
      

  # delete a node with a given key
  def delete (self, key):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the delete node
    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if (key < delete_node.data):
        delete_node = delete_node.lchild
        is_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if delete node is a leaf node
    if (delete_node.lchild == None) and (delete_node.rchild == None):
       if (delete_node == self.root):
         self.root = None
       elif (is_left):
         parent.lchild = None
       else: 
         parent.rchild = None

    # delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    # delete node has both left and right children
    else:
      # find delete node's successor and the successor's parent node
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      # successor node is right child of delete node
      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect delete node's left child to be the successor's left child
      successor.lchild = delete_node.lchild

      # successor node left descendant of delete node
      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

      return delete_node



  
  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    if ((self.root == None) and (pNode.root == None)):
      return True
    elif (self.num_nodes() != pNode.num_nodes()):
      return False
    else:
      return self.is_similar_helper (self.root, pNode.root)

  def is_similar_helper (self, node1, node2):
    if ((node1 == None) and (node2 == None)):
      return True
    elif ((node1.data == node2.data) and (self.is_similar_helper (node1.lchild, node2.lchild)) and (self.is_similar_helper (node1.rchild, node2.rchild))):
      return True
    else:
      return False

  # Prints out all nodes at the given level
  def print_level (self, level):
    s = self.print_level_help(self.root, 1, level)
    print(s)
    return



  def print_level_help (self, node, curr_level, level):
    s = ""
    if (node == None):
      return ""
    elif (curr_level == level):
      s += str(node.data)
      s += " "
    else:
      s += self.print_level_help (node.lchild, curr_level + 1, level)
      s += self.print_level_help (node.rchild, curr_level + 1, level)

    return s


  # Returns the height of the tree
  def get_height (self):
    return self.get_height_helper(self.root, -1)
    
  def get_height_helper (self, node, count):
    if (node == None):
      return count
    else: 
      return max(self.get_height_helper(node.lchild, count + 1),self.get_height_helper(node.rchild, count + 1))

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    return self.num_nodes_helper(self.root)
    


  def num_nodes_helper(self, node):
    if (node == None):
      return 0
    else:
      return (1 + self.num_nodes_helper(node.lchild) + self.num_nodes_helper(node.rchild))
  
    


def main():
    # Create three trees - two are the same and the third is different
    a_tree = Tree()
    insert_list_a = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
    for i in insert_list_a:
      a_tree.insert(i)


    # b is the same as a_tree
      
    b_tree = Tree()
    insert_list_b = [11, 6, 8, 19, 4, 10, 5, 17, 43, 31, 49]
    for i in insert_list_b:
      b_tree.insert(i)
      
    # c is not the same as a_tree

    c_tree = Tree()
    insert_list_c = [11, 6, 8, 19, 4, 10, 5, 17, 31, 43, 49, 87, 99, 100, 24, 36]
    for i in insert_list_c:
      c_tree.insert(i)

      

    # Test your method is_similar()

    # Testing a and b
    if (a_tree.is_similar(b_tree) == True):
      print ("a and b are similar")
    else:
      print ("a and b are not similar")

    print()

    # Testing a and c
    if (a_tree.is_similar(c_tree) == True):
      print ("a and c are similar")
    else:
      print ("a and c are not similar")

    print()
      
      
    
    

    # Print the various levels of two of the trees that are different
    
    for i in range(1,9):
      print ("Level " + str(i) + " nodes for a_tree: ")
      a_tree.print_level(i)
      print()
      print ("Level " + str(i) + " nodes for c_tree: ")
      c_tree.print_level(i)
      print()
      
    
    
    
    

    # Get the height of the two trees that are different
    a_height = a_tree.get_height()
    c_height = c_tree.get_height()
    print ("The height of a_tree is " + str(a_height))
    print()
    print ("The height of c_tree is " + str(c_height))
    print()

    # Get the total number of nodes a binary search tree
    print("number of nodes in a_tree is " + str(a_tree.num_nodes()))
    print()
    print("number of nodes in c_tree is " + str(c_tree.num_nodes()))


    
    
    


main()
