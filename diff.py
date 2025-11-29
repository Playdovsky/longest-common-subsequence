class Diff:
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
        
        print(f"\nLongest Common Subsequence = {matrix[len(n)][len(m)]}\n\n")