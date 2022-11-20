def generateSquare(n):
    if n%2!=0:
        magicSquare = [[0 for x in range(n)]
                       for y in range(n)] 
        i = n / 2
        j = n - 1
        num = 1
        while num <= (n * n): 
            if i == -1 and j == n: 
                j = n - 2
                i = 0
            else:  
                if j == n: 
                    j = 0    
                if i < 0: 
                    i = n - 1
            if magicSquare[int(i)][int(j)]:
                j = j - 2
                i = i + 1
                continue
            else: 
                magicSquare[int(i)][int(j)] = num 
                num = num + 1
            j = j + 1
            i = i - 1 
        print ("Number of row :", n)
        print("Number of columns :",n) 
        print ("Sum of each row or column or diagonal :",n * (n * n + 1) // 2, "\n") 
        for i in range(0, n): 
            for j in range(0, n): 
                print('%2d ' % (magicSquare[i][j]),end = '') 
                if j == n - 1:  
                    print()
    else:     
        arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]
        for i in range(0,n//4):
            for j in range(0,n//4):
                arr[i][j] = (n*n + 1) - arr[i][j];
        for i in range(0,n//4):
            for j in range(3 * (n//4),n):
                arr[i][j] = (n*n + 1) - arr[i][j];
        for i in range(3 * (n//4),n):
            for j in range(0,n//4):
                arr[i][j] = (n*n + 1) - arr[i][j];
        for i in range(3 * (n//4),n):
            for j in range(3 * (n//4),n):
                arr[i][j] = (n*n + 1) - arr[i][j];
        for i in range(n//4,3 * (n//4)):
            for j in range(n//4,3 * (n//4)):
                arr[i][j] = (n*n + 1) - arr[i][j];
        print ("Number of rows :", n)
        print("Number of columns :",n)
        print ("Sum of each row or column or diagonal :",n * (n * n + 1) // 2, "\n") 
        for i in range(n):
            for j in range(n):
                print ('%2d ' %(arr[i][j]),end=" ")
            print()


n=int(input("Dimension of the basket :"))
generateSquare(n)
