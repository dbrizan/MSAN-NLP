def read_file(filename):
    with open(filename) as f:
        contents = f.readlines()
    text = ''
    for line in contents:
        text += line.strip()
    return text


def read_all_files(directory):
    import os
    document = []
    file_list = os.listdir(directory)
    # print file_list
    for filename in file_list:
        # print os.path.join(directory, filename)
        document.append(read_file(os.path.join(directory, filename)))
    # print 'Got', len(document), 'documents.'
    return document


def clean(doc):
    from nltk.corpus import stopwords
    from nltk.stem.wordnet import WordNetLemmatizer
    import string

    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()

    stop_free = " ".join([i for i in doc.lower().split() if i not in stop]).decode('ascii', 'ignore')
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
    # return punc_free


def get_topics(corpus):
    import gensim
    from gensim import corpora

    dictionary = corpora.Dictionary(corpus)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]
    Lda = gensim.models.ldamodel.LdaModel

    # Running and Trainign LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

    print(ldamodel.print_topics(num_topics=3, num_words=3))


if __name__ == '__main__':
    import sys

    # doc = read_file(sys.argv[1])
    # print doc
    document = read_all_files(sys.argv[1])
    normalised = []
    for d in document:
        normalised.append(clean(d).split())
    print normalised[1]
    get_topics(normalised)

