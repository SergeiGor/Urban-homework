class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = []
        for f_n in file_names:
            self.file_names.append(f_n)

    def get_all_words(self):
        self.all_words = {}
        for f_n in self.file_names:
            with (open(f_n, encoding="utf-8") as file):
                words = []
                for s in file:
                    words.extend(s.lower().replace('\n', '').replace(',', '').replace('.', '').replace('-', '').replace('=', '').replace('!', '').replace('?', '').split())
                    self.all_words.update({f_n: words})
        return self.all_words

    def find(self, word):
        self.find_dic = {}
        for k in self.get_all_words():
            find_c = 0
            for el in self.all_words[k]:
                    find_c += 1
                    if word.lower() == el:
                        self.find_dic.update({k: find_c})
                        break
        return self.find_dic

    def count(self, word):
        self.count_dic = {}
        for f_n, words in self.all_words.items():
            number_c = 0
            for word_n in self.all_words[f_n]:
                if word_n.lower() == word.lower():
                    number_c += 1
                self.count_dic.update({f_n: number_c})
        return self.count_dic



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего