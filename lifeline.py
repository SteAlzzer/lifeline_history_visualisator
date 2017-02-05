import argparse
import os
import csv
import re
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
        return str(self.make_message_display())

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
            self.prev_node = self.load_tree(savefile)
        else:
            self.prev_node = self.game_tree.create_node(
                             'Начало', data=Message('Начало', 2))

    def add_message(self, message, message_type, parent=None):
        parent_for_message = parent.identifier if parent else self.prev_node.identifier
        if self.__find_same_message(message):
            pass
        else:
            msg = Message(message, message_type)
            self.prev_node = self.game_tree.create_node(
                             data=msg, parent=parent_for_message)

    def __find_same_message(self, message):
        pass

    def add_user_reply(self, message1, message2):
        prev = self.prev_node
        self.add_message(message1, 3, parent=prev)
        self.add_message(message2, 3, parent=prev)

    def save_tree(self, savefile):
        with open(savefile, 'w', newline='') as save:
            save_writer = csv.writer(save, quoting=csv.QUOTE_NONNUMERIC)
            for node_id in self.game_tree.expand_tree():
                list_to_write = [node_id, self.game_tree[node_id].fpointer,
                                 self.game_tree[node_id].bpointer,
                                 self.game_tree[node_id].data.message_text,
                                 self.game_tree[node_id].data.type]
                save_writer.writerow(list_to_write)
            save_writer.writerow([self.prev_node.identifier])

    def load_tree(self, savefile):
        print('Loading...')
        with open(savefile, newline='') as save:
            save_reader = csv.reader(save)
            self.game_tree = Tree()
            for row in save_reader:
                if len(row) == 1:
                    return self.game_tree[row[0]]
                node_id = row[0]
                parent = row[2] if row[2] else None
                msg = Message(row[3], int(row[4]))
                self.game_tree.create_node(identifier=node_id, parent=parent, data=msg)

    def debug_visualize(self):
        print('----DEBUG----')
        for node_id in self.game_tree.expand_tree():
            print('node_id:', node_id)
            print('parent:', self.game_tree[node_id].bpointer)
            print('childen:', self.game_tree[node_id].fpointer)
            print('message:', self.game_tree[node_id].data)
        print('----DEBUG----')


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

    def save_visualization(self, save_file):
        self.game_tree.save2file('./tmp')
        with open(save_file, 'w', encoding='utf-8') as visualization:
            for line in open('./tmp', encoding='utf-8'):
                found_ids = re.findall('[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}', line)
                for found_id in found_ids:
                    msg = self.game_tree[found_id].data.message_display
                    line = line.replace(found_id, msg)
                visualization.write(line)
        os.remove('./tmp')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['message', 'reply'])
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    save_file = os.path.abspath(os.path.realpath(SAVE_FILE))
    if not os.path.isfile(save_file):
        print('Save file not found. Let\'s make a new one, buddy')
        game = GameTree()
    else:
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

    if args.action == 'reply':
        if not len(args.args) == 2:
            print('There should be `choose1` and `choose2. The second will be choosed')
            exit(-1)
        game.add_user_reply(args.args[0], args.args[1])

    game.visualize()
    # game.save_tree(save_file)
    game.save_visualization('./vis1')
