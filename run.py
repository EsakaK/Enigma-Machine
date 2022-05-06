import argparse
from parts.EnigmaMachine import EnigmaMachine

parser = argparse.ArgumentParser()
parser.add_argument('--key', type=str, default='AAA')
parser.add_argument('--encoding', type=int, default=1)
parser.add_argument('--file_path', type=str, default='./text/demo.txt')
parser.add_argument('--save_path', type=str, default='./text/res.txt')
args = parser.parse_args()


def read_file(file_path):
    with open(file_path, mode='r') as f:
        content = f.read()
    return content


def write_file(save_path, content):
    with (open(save_path, mode='w')) as f:
        f.write(content)
    return True


machine = EnigmaMachine(args.key)
x_sentence = read_file(args.file_path)
y_sentence = machine.coding(x_sentence,args.encoding)
write_file(save_path=args.save_path,content=y_sentence)