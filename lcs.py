class Lcs:
    def __init__(self, n, m):
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
        
        self.calculate(matrix, n, m)
    
    def calculate(self, matrix, n, m):
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
        
        self.display(matrix, n, m)
    
    def display(self, matrix, n, m):
        i = 0
        j = 0
        
        print()
        print("    " + " ".join(m))

        while i < len(n) + 1:
            row = ""
            if i == 0:
                row = "  "
            else:
                row = n[i - 1] + " "
            while j < len(m) + 1:
                row += str(matrix[i][j]) + " "
                j += 1
            print(row)
            j = 0
            i += 1
        
        print(f"\nLongest Common Subsequence\n| length = {matrix[len(n)][len(m)]}\n| string = {self.find_lcs_string(matrix, n, m)}\n")
    
    def find_lcs_string(self, matrix, n, m):
        i = len(n)
        j = len(m)
        lcs_string = ""
        
        while i > 0 and j > 0:
            if n[i - 1] == m[j - 1]:
                lcs_string = n[i - 1] + lcs_string
                i -= 1
                j -= 1
            elif matrix[i - 1][j] > matrix[i][j - 1]:
                i -= 1
            else:
                j -= 1
                
        return lcs_string