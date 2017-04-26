from person import person

#
# Main
#
if __name__ == '__main__':
    guido_name = {'f': 'Guido', 'last': 'van Rossum'}
    guido = person(guido_name)

    guido.add_to_bio('1956: Born in the Netherlands')
    guido.add_to_bio('1982: Earned M.S. Degree from University of Amsterdam')
    guido.add_to_bio('1986: Wrote a glob() routine')
    guido.add_to_bio('1989: Started writing python')
    guido.add_to_bio('2012: Started working for Dropbox')

    kim_name = {'f': 'Kim', 'last': 'Knapp'}
    kim = person(kim_name)
    guido.change_spouse(kim)

    print guido.to_string()

