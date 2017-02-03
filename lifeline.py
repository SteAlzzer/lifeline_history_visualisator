from treelib import Tree


# class Tree(object):
# 	element_id = ''
# 	message = ''
# 	type_of_message = 0  # 1 - Сообщение от Тейлора; 2 - [Сообщение системы], 3 - Выбор пользователя
# 	left = None
# 	right = None

# 	def __init__(self, message, type):
# 		pass

# 	def add_message(self, message_text, type=1):
# 		pass
# 	def add_reply(self):
# 		pass
# 	def __find_same(self):
# 		pass
# 	def save_tree(self):
# 		pass
# 	def load_tree(self):
# 		pass


tree = Tree()
n1 = tree.create_node('Root')
print(tree.root)
n2 = tree.create_node('Howdy', 'hd', parent=tree.root)
print('----')
print(n1.identifier)
print(n1.tag)

tree.show()


for node in tree:
	print(node)