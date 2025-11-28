class Start:
    def __init__(self):
        self.menu()
    
    def menu(self):
        try:
            while True:
                print("Please select option")
                print("1. Pass\n2. Exit")
                option = int(input())
                
                match option:
                    case 1:
                        pass
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