from ir_system import ir_system

if __name__ == "__main__":
    ir = ir_system()

    # Finding a set of documents is an art. For our toy example, let's use two:
    ir.read_file('ir-doc01.txt')
    ir.read_file('ir-doc05.txt')

    # The I/O should be its own class. For our toy example, let's use:
    search_term = raw_input('Search for: ')
    docs = ir.get_documents_matching(search_term)
    if docs is not None:
        print search_term, 'found in', docs
    else:
        print search_term, 'not found.'

