import argparse
import os
import csv
from treelib import Tree

# tree = Tree()
# n1 = tree.create_node('Root')
# print(tree.root)
# # n2 = tree.create_node('Howdy', 'hd', parent=tree.root)
# prev = tree.create_node('Hello', parent=n1.identifier)
# tree.create_node('Hello', parent=n1.identifier)
# prev = tree.create_node('Hello', parent=prev.identifier)
# tree.show(line_type='ascii')

SAVE_FILE = './save'


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
        self.message_display = self.make_message_display()

    def __str__(self):
        return self.make_message_display()

    def make_message_display(self):
        if self.type == 1:
            return self.message_text
        elif self.type == 2:
            return '[{}]'.format(self.message_text)
        elif self.type == 3:
            return '({})'.format(self.message_text)


class GameTree(object):
    def __init__(self, savefile=None):
        self.game_tree = Tree()

        if savefile:
            self.load_tree(savefile)
            self.prev_node = self.game_tree.root
            self.prev_node = self.game_tree.create_node(
                             'Начало', data=Message('Начало', 2))  # todo: remove that line when save-load will be done
        else:
            self.prev_node = self.game_tree.create_node(
                             'Начало', data=Message('Начало', 2))

    def add_message(self, message, message_type):
        if self.__find_same_message(message):
            pass
        else:
            msg = Message(message, message_type)
            self.prev_node = self.game_tree.create_node(
                             data=msg, parent=self.prev_node.identifier)

    def __find_same_message(self, message):
        pass

    def add_user_reply(self, message1, message2):
        self.add_message(message1, 3)
        self.add_message(message2, 3)

    def save_tree(self, savefile):
        with open(savefile, 'w', newline='') as save:
            save_writer = csv.writer(save, quoting=csv.QUOTE_NONNUMERIC)
            for node_id in self.game_tree.expand_tree():
                list_to_write = [node_id, self.game_tree[node_id].fpointer,
                                 self.game_tree[node_id].data.message_text,
                                 self.game_tree[node_id].data.type]
                save_writer.writerow(list_to_write)
            save_writer.writerow([self.prev_node.identifier])

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
        self.game_tree.show(line_type='ascii', data_property='message_display')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['message', 'reply', 'save', 'show'])
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    save_file = os.path.abspath(os.path.realpath(SAVE_FILE))
    if not os.path.isfile(save_file):
        print('Save file not found. Let\'s make a new one, buddy')
        with open(save_file, 'w') as _:
            pass

    game = GameTree(save_file)

    if args.action == 'message':
        if not len(args.args):
            print('There should be `message_text` and `message_type`')
            exit(-1)
        if len(args.args) == 1:
            message_text = args.args[0]
            message_type = 1
        elif len(args.args) == 2:
            message_text = args.args[0]
            message_type = args.args[1]
        game.add_message(message_text, message_type)
        game.add_message(message_text, message_type)
        game.add_message(message_text, 3)

    game.visualize()
    game.save_tree(save_file)
