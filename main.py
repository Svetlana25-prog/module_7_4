class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        self.all_words = {}
        for file_name in self.file_names:

            with open(file_name, 'r', encoding='utf-8') as f:
                words = f.read().replace('\n','').lower().split()

                words_new = []
                for word in words:
                    word_new_str = ''
                    for char in word:
                        if not char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            word_new_str += char
                    words_new.append(word_new_str)
                self.all_words[file_name] = words
        return self.all_words

    def find(self, word):
        dict_ews = {}
        for file_name_one in self.file_names:
            list_words_n = self.all_words[file_name_one]
            count = 1

            for l in list_words_n:
                if word.lower() == l:
                    dict_ews[file_name_one] = count
                    break
                count += 1
        return dict_ews

    def count(self, word):
        dict_ews = {}
        for file_name_one in self.file_names:
            list_words_n = self.all_words[file_name_one]
            count = 1

            for l in list_words_n:
                if word.lower() == l:

                    count += 1
            dict_ews[file_name_one] = count
        return dict_ews



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего




