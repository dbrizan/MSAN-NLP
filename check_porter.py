'''
This script checks the Porter Stemmer, as implemented in NLTK.
'''


def read_file(file_name):
    input = []
    with open(file_name) as f:
        content = f.readlines()
        for line in content:
            input.append(line.strip())
    return input


if __name__ == "__main__":
    from nltk.stem.porter import PorterStemmer

    stemmer = PorterStemmer()

    vocs = read_file('voc.txt')
    outputs = read_file('output.txt')
    instances_checked = 0
    instances_incorrect = 0

    for voc, output in zip(vocs, outputs):
        stemmed_word = stemmer.stem(voc)
        instances_checked += 1
        if stemmed_word != output:
            print '[X]', voc, '--> got', stemmed_word, '(expected', output + ')'
            instances_incorrect += 1
        # else:
            # print '[ ]', voc, '-->', output
    print 'Accuracy:', str(round(float(instances_checked - instances_incorrect) / float(instances_checked), 4) * 100) + '%'
