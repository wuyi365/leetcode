class Node:
	def __init__(self, value = None, next = None):
		self.data= value
		self.next = next

	def __str__(self):
		return 'Node ['+str(self.value)+']'




class LinkedList:
	def __init__(self):
		self.cur_node = None

	def add_node(self,data):
		new_node = Node()
		new_node.data = data
		new_node.next = self.cur_node
		self.cur_node = new_node

	def list_print(self):
		node = self.cur_node
		while node:
			print node.data
			node = node.next

	def reverseList(self):
		pre = None
		cur = self.cur_node
		while cur:
			next_node = cur.next
			cur.next = pre
			pre = cur
			cur = next_node

		return pre





ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()

ll.reverseList()
ll.list_print()
