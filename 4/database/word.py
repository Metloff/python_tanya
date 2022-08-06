from asyncore import write

class Word:
    def __init__(self):
        self.dict = {}
        self.path = 'database/dictionary.txt'

    def load_data(self):
        try:
            reader = open(self.path, 'r')
            for line in reader:
                if len(line) == 0:
                    break

                words = line.split(":")
                self.dict[words[0].strip()] = words[1].strip()
        finally:
            reader.close()

    def get_translation(self, en_w):
        return self.dict.get(en_w, "")

    def write_translation(self, en_w, ru_w):
        if self.dict.get(en_w) == ru_w:
            return

        try:
            writer = open(self.path, 'a')
            writer.write(f"{en_w}:{ru_w}\n")
            self.dict[en_w] = ru_w
        finally:
            writer.close()