#Inspired by https://github.com/florian/diff-tool
from termcolor import colored

class Diff():
    def __init__(self, file1, file2):
        self.show_diff(file1, file2)
        
    def read_files(self, file1, file2):
        with open(file1, 'r') as f1:
            content1 = f1.readlines()
        
        with open(file2, 'r') as f2:
            content2 = f2.readlines()

        return self.differences(content1, content2)

    def differences(self, content1, content2):
        results = []
        i = len(content1)
        j = len(content2)

        matrix = self.calculate(content1, content2)

        while i != 0 or j != 0:
            if i == 0:
                results.append(('addition', content2[j - 1]))
                j -= 1
            elif j == 0:
                results.append(('removal', content1[i - 1]))
                i -= 1
            elif content1[i - 1] == content2[j - 1]:
                results.append(('unchanged', content1[i - 1]))
                i -= 1
                j -= 1
            elif matrix[i - 1][j] <= matrix[i][j - 1]:
                results.append(('addition', content2[j - 1]))
                j -= 1
            else:
                results.append(('removal', content1[i - 1]))
                i -= 1
        
        return list(reversed(results))
    
    def calculate(self, n, m):
        i = 0
        j = 0
        matrix = []
        
        while i < len(n) + 1:
            matrix.append([])
            while j < len(m) + 1:
                matrix[i].append(0)
                j += 1
            j = 0
            i += 1

        i = 0
        j = 0

        while i < len(n) + 1:
            while j < len(m) + 1:
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif n[i - 1] == m[j - 1]:
                    matrix[i][j] = 1 + matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
                j += 1
            j = 0
            i += 1
        
        return matrix
    
    def show_diff(self, file1, file2):
        results = self.read_files(file1, file2)
        print(f"\n{file1}  ==>  {file2}\n")

        for change_type, line in results:
            if change_type == 'addition':
                print(colored('+ ' + line.rstrip(), 'green'))
            elif change_type == 'removal':
                print(colored('- ' + line.rstrip(), 'red'))
            else:
                print(colored('= ' + line.rstrip(), 'white'))
        
        print()
        