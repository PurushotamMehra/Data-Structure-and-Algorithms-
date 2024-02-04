	def printLL(self):
		current_node = self.head
        llstr = ''
		while(current_node):
			llstr += str(current_node) + '->'
			current_node = current_node.next