from diff import Diff

class Start:
    def __init__(self):
        self.menu()
    
    def menu(self):
        try:
            while True:
                print("Please select option")
                print("1. Longest Commong Subsequence\n2. Exit")
                option = int(input())
                
                match option:
                    case 1:
                        n = input("Enter first string: ")
                        m = input("Enter second string: ")
                        diff = Diff(n, m)
                    case 2:
                        exit()
                    case _:
                        print("Please select valid option from the list\n")
                        self.menu()
        except ValueError:
            print("Please select valid option from the list")
            self.menu()
        except Exception as e:
            print(f"An error occured: {e}")
            self.menu()

self_start = Start()