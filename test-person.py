'''
I use the "person" class... and print using that.
'''
from person import person

#
# Main
#
if __name__ == '__main__':
    # Create a person named "Guido".
    guido_name = {'f': 'Guido', 'last': 'van Rossum'}
    guido = person(guido_name)

    # Add to Guido's bio.
    guido.add_to_bio('1956: Born in the Netherlands')
    guido.add_to_bio('1982: Earned M.S. Degree from University of Amsterdam')
    guido.add_to_bio('1986: Wrote a glob() routine')
    guido.add_to_bio('1989: Started writing python')
    guido.add_to_bio('2012: Started working for Dropbox')

    # Create a person named "Kim" for Guido to marry.
    kim_name = {'f': 'Kim', 'last': 'Knapp'}
    kim = person(kim_name)
    guido.change_spouse(kim)

    # Print everything you know about Guido.
    print guido.to_string()

