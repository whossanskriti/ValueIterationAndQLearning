

class nested_dictionary:
    def __init__(self):
        outsideDict = { "inside1" : {"fruit":"strawberry","bird":"pigeon"}
        }
        print(outsideDict["inside1"])

def main():
    dict = nested_dictionary()

if __name__ == "__main__":
    main()