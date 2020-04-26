#  File: Josephus.py

#  Description: Print out the order soldiers get eliminated. Linked lists.


class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next


class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, item ):
    new_link = Link(item)
    current = self.first

    if (self.first == None):
      self.first = new_link
      self.first.next = self.first
      return

    while (current.next != self.first):
      current = current.next
    
    current.next = new_link
    new_link.next = self.first
      

  # Find the link with the given key (value)
  def find ( self, key ):
    current = self.first

    if (self.first == None):
      return None
    while (key != current.data):
      if (current.next == self.first):
        return None
      else:
        current = current.next
    return current
    

  # Delete a link with a given key (value)
  def delete ( self, key ):
    current = self.first
    previous = self.first

    while (current.data != key):
      previous = current
      current = current.next

    if (current == self.first):
      self.connect_last()
      self.first = self.first.next
      
    previous.next = current.next

    return current #should this be current.data? 
      

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    current = self.find(start)

    for i in range (0, n - 1):
      current = current.next
    new_first = current.next
    print (current.data)
    death = self.delete(current.data)

    return new_first.data
    
    

  # Return a string representation of a Circular List
  def __str__ ( self ):
    st = ''
    current = self.first.next
    while (current.next != self.first):
      st += (str(current.data) + ' ')
      current = current.next
    st += (str(current.data) + ' ')
    return st

  # used for delete fuction. Find the link that has next as first and move it's next to first.next.
  def connect_last(self):
    current = self.first
    while(current.next != self.first):
      current = current.next
    current.next = self.first.next

    return

def main():
  infile = open('josephus.txt', 'r')

  num_soldiers = infile.readline()
  num_soldiers = int(num_soldiers.strip())

  start = infile.readline()
  start = int(start.strip())

  n = infile.readline()
  n = int(n.strip())

  circle = CircularList()

  # inserting the soldiers in the list
  for i in range(1, num_soldiers + 1):
    circle.insert(i)

  # delete soldiers
  for j in range (1, num_soldiers + 1):
    start = circle.delete_after(start, n)



main()
