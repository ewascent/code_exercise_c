"""import a small or large array of repeating vals"""
from src.recursive_repeater import repeater_recurse as repeater
from src.xml_parser import *

Vals = [1, 2, 3, 4, 1, 2, 3]

def main(vals):
    """entry point for application. takes an array of ints"""
    print("==Run the repeater code.== \n")
    print("This should be 1 -> " + str(repeater(vals)) + "\n")
    print("==Parse some XML== \n")
    getText(fetchData('http://slashdot.org/slashdot.rdf'))
    print("==Parse more XML== \n")
    print(xmlReader(fetchData('http://slashdot.org/slashdot.rdf'), 200, 200))

if __name__ == "__main__":
    main(Vals)
