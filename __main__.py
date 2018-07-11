"""import a small or large array of repeating vals"""
from src.recursive_repeater import repeater_tail_recurse as repeater

Vals = [1, 2, 3, 4, 1, 2, 3]

def main(vals):
    """entry point for application. takes an array of ints"""
    print("This should be 1 -> " + str(repeater(vals)))

if __name__ == "__main__":
    main(Vals)
