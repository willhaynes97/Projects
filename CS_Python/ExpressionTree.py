#  File: ExpressionTree.py

#  Description: Read a file expression.txt and create an expression tree.

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))


def operate (oper1, oper2, token):
  if (token == "+"):
    return oper1 + oper2
  elif (token == "-"):
    return oper1 - oper2
  elif (token == "*"):
    return oper1 * oper2
  elif (token == "/"):
    return oper1 / oper2

class Node (object):
  def __init__ (self, data):
    if (data == None):
      self.data = None
    else:
      self.data = data
    self.lchild = None
    self.rchild = None

  def insert_left(self, aNode):
    if (self.lchild == None):
      self.lchild = Node(aNode)

  def insert_right(self, aNode):
    if (self.rchild == None):
      self.rchild = Node(aNode)

class Tree (object):
  def __init__ (self):
    self.root = Node(None)


  def createTree (self, expr):
    expr_stack = Stack()
    current = self.root
    expression = expr.split()
    operators = ["+", "-", "*", "/"]
    for token in expression:
      if (token == "("):
        
        current.insert_left(None)
        expr_stack.push(current)
        current = current.lchild
      elif (token in operators):
        current.data = token
        expr_stack.push(current)
        current.insert_right(None)
        current = current.rchild
      elif (token == ")"):
        if (expr_stack.is_empty() == False):
          current = expr_stack.pop()
      else:
        current.data = eval(token)
        current = expr_stack.pop()
        
    

  def evaluate (self, aNode):

    operators = ["+", "-", "*", "/"]

    if(aNode.data == None):
      return 0

    elif(not (aNode.data in operators)):
      return float(aNode.data)

    else:
      if (aNode.data == "+"):
        return(self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild))
      elif (aNode.data == "-"):
        return(self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild))
      if (aNode.data == "*"):
        return(self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild))
      if (aNode.data == "/"):
        return(self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild))

  def preOrder (self, aNode):
    string = ""
    if (aNode != None):
      string += str(aNode.data)
      string += " "
      string += self.preOrder (aNode.lchild)
      string += self.preOrder (aNode.rchild)

    return string

  def postOrder (self, aNode):
    string = ""
    if (aNode != None):
      string += self.postOrder (aNode.lchild)
      string += self.postOrder (aNode.rchild)
      string += str(aNode.data)
      string += " "

    return string

def main():
  in_file = open ("./expression.txt", "r")
  expr = in_file.readline().rstrip("\n")

  tree = Tree()
  tree.createTree(expr)
  value = tree.evaluate(tree.root)
  if (value.is_integer() == True):
    value = int(value) 
  print(expr + " = " + str(value))
  prefix = tree.preOrder(tree.root)
  print("Prefix Expression: " + prefix)
  postfix = tree.postOrder(tree.root)
  print("Postfix Expression: " + postfix)

  in_file.close()
  
  

main()
