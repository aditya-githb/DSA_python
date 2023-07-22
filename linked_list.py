class node(object):
	def __init__(self,value):
		self.value=value
		self.next = None

class singlelinkedlist(object):
	def __init__(self):
		self.head = None
		self.tail = None

linked_list = singlelinkedlist()
linked_list.head = node(45)
linked_list.head.next = node(50)
linked_list.head.next.next=node(55)

print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)				
