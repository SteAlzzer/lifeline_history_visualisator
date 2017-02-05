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
	def __init__(self, message_text, message_type):
		pass

class GameTree(object):
	def __init__(self, savefile=None):
		pass
	def add_message(self, message, message_type):
		pass
	def __find_same_message(self, message):
		pass
	def add_user_reply(self, message1, message2):
		pass
	def save_tree(self, savefile):
		pass
	def load_tree(self, savefile):
		pass

