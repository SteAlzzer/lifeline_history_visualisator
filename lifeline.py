from treelib import Tree



# tree = Tree()
# n1 = tree.create_node('Root')
# print(tree.root)
# # n2 = tree.create_node('Howdy', 'hd', parent=tree.root)
# prev = tree.create_node('Hello', parent=n1.identifier)
# tree.create_node('Hello', parent=n1.identifier)
# prev = tree.create_node('Hello', parent=prev.identifier)
# tree.show(line_type='ascii')

class Message(object):
	'''
	message_type:
		1 - Basic Tyler message
		2 - [System message]
		3 - User reply
	'''
	def __init__(self, message_text, message_type):
		self.message_text = message_text
		self.type = message_type

class GameTree(object):
	def __init__(self, savefile=None):
		self.game_tree = Tree()
		if savefile:
			self.load_tree(savefile)
		else:
			self.prev_node = self.game_tree.create_node('Начало')
	def add_message(self, message, message_type):
		if self.__find_same_message(message):
			pass
		else:
			msg = Message(message, message_type)
			self.prev = self.game_tree.create_node(data=msg, parent=self.prev)

	def __find_same_message(self, message):
		pass
	def add_user_reply(self, message1, message2):
		self.add_message(message1, 3)
		self.add_message(message2, 3)
		
	def save_tree(self, savefile):
		pass
	def load_tree(self, savefile):
		pass
	def visualize(self):
		'''
		ascii
		ascii-ex
		ascii-emh
		ascii-exr
		ascii-em
		ascii-emv
		'''
		self.game_tree.show(line_type='ascii')

