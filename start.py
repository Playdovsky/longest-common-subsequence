from lcs import Lcs
from diff import Diff

class Start:
    def __init__(self):
        self.menu()
    
    def menu(self):
        try:
            while True:
                print("\nPlease select option")
                print("1. Longest Commong Subsequence\n2. Compare files\n3. Exit\n")
                option = int(input())
                print()

                match option:
                    case 1:
                        n = input("Enter first string: ")
                        m = input("Enter second string: ")
                        lcs = Lcs(n, m)
                    case 2:
                        file1 = input("Enter path to first file: ")
                        file2 = input("Enter path to second file: ")
                        diff = Diff(file1, file2)
                    case 3:
                        exit()
                    case _:
                        print("Please select valid option from the list\n")
                        self.menu()
        except ValueError:
            print("Please select valid option from the list\n")
            self.menu()
        except FileNotFoundError:
            print("File could not be found. Please check paths and try again\n")
            self.menu()
        except Exception as e:
            print(f"An error occured: {e}\n")
            self.menu()

self_start = Start()