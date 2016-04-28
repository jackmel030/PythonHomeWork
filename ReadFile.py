import string


class ReadFile:

    def __init__(self, file_address: string, file_type: string):
        self.file_address = file_address
        self.file_type = file_type

    def get_reading_file(self):
        read_words = []
        file_content = open(self.file_address, 'r')
        while True:
            words = file_content.readline().strip('\n').split(' ')
            if words[0] == '':
                break  # 讀到檔尾
            else:
                read_words.append(words)
        file_content.close()
        return read_words

    @staticmethod
    def show(words):
        for texts_index in range(len(words)):
            if words[texts_index] == 'None':
                print('')
            else:
                print(words[texts_index])


rd = ReadFile('testfile.txt', 'UTF-8')
rd.show(rd.get_reading_file())

