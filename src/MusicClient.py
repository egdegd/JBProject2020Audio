from pydub import AudioSegment


def join(*args):
    file_out = args[0]
    sound = AudioSegment.empty()
    for file in args[1:]:
        sound += AudioSegment.from_mp3(file)
    sound.export(file_out)


def split_all_file(*args):
    file_in = args[0]
    sound = AudioSegment.from_file(file_in)
    intervals = args[1:]
    cur_interval = 0
    for interval in intervals:
        new_sound = sound[cur_interval:int(interval)]
        new_sound.export(f'split_from_{cur_interval}_to_{interval}')
        cur_interval = int(interval)
    new_sound = sound[cur_interval:]
    new_sound.export(f'split_from_{cur_interval}')


def cut_interval(*args):
    print(args)
    file_in, file_out, interval_start, interval_finish = args
    print(file_in, file_out, interval_start, interval_finish)
    sound = AudioSegment.from_file(file_in)
    cut_sound = sound[int(interval_start):int(interval_finish)]
    cut_sound.export(file_out)


def reverse(*args):
    file_in, file_out = args
    sound = AudioSegment.from_file(file_in)
    reverse_sound = AudioSegment.reverse(sound)
    reverse_sound.export(file_out)


def help():
    print('join <output file> <list of input file>\n'
          'split_all_file <input file> <list of points in ms>\n'
          'cut_interval <input file> <output file> <start of interval in ms> <finish of interval in ms>\n'
          'reverse <input file> <output file>\n'
          'exit')


class Client:
    def __init__(self):
        self.running = True
        self.commands = {
            "help": help,
            "join": join,
            "split_all_file": split_all_file,
            "cut_interval": cut_interval,
            "reverse": reverse,
            "exit": self.exit
        }

    def run(self):
        while self.running:
            cmd = input().split(" ")
            self.commands[cmd[0]](*cmd[1:])

    def exit(self):
        self.running = False


def main():
    client = Client()
    client.run()


if __name__ == "__main__":
    main()
