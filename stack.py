from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
	value: any
	next: Node

class Stack:
	top: Node

	def __init__(self):
		self.top = None

	def isEmpty(self) -> bool:
		if self.top is None:
			return True
		return False

	def pop(self, isPeek = False) -> any:
		# empty
		if not hasattr(self.top, 'next'):
			return None
		
		# not last item
		if self.top.next is not None:
			r = self.top.value
			if (not isPeek):
				self.top = self.top.next
			return r

		# last item
		r = self.top.value
		if (not isPeek):
			self.top = None
		return r

	def push(self, value) -> None:
		if (self.isEmpty()):
			self.top = Node(value, None)
		else:
			self.top = Node(value, self.top)

	def peek(self) -> any:
		return self.pop(True)

	def size(self) -> int:
		# empty
		if not hasattr(self.top, 'next'):
			return 0

		num_encountered = 1 # top
		current_node = self.top
		while current_node.next is not None:
			current_node = current_node.next
			num_encountered+=1
		return num_encountered
