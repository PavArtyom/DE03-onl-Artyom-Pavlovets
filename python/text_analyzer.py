def analyze_file():
    direct_path = "/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/path.txt"
    direct_analysis = "/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/analysis.txt"
    with open(direct_path, "r+") as path, open(direct_analysis, "r+") as analysis:
        content = path.readlines()
        counter = 0
        for contain in content:
            words = contain.split()
            num_words = len(words)
            counter += num_words
            longest_word = max(words, key=len)
        analysis.write(str(len(content)) + ' - Количество строк' +'\n' + str(counter) + ' - Количество слов' +
                       '\n' + str(longest_word) + ' - Самое длинное слово' + '\n')
    return (f'Количество строк: {len(content)}, Количество слов: {counter}, '
                f'Самое длинное слово: {longest_word} ')



