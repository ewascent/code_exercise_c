from repeater import repeater_tail_recurse as repeater

def main():
    """entry point for application"""
    vals = [1, 2, 3, 1, 2, 3]
    print("This should be 1 -> " + str(repeater(vals)))

if __name__ == "__main__":
    main()
