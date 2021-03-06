import numpy as np
import copy

class Puzzle :
    def __init__(self, matrix = [], parents = [], gcost = 0, fcost = 0) :
        if(len(matrix) == 0) :
            self.randomPuzzleGenerator()
        else :
            self.matrix = np.array(matrix)
        self.parents = parents
        self.kosong = []
        self.fCost = fcost
        self.gCost = gcost
        self.findEmpty()

    def __lt__(self,other) :
        if(self.findcost() == other.findcost()) :
            return self.fCost >= other.fCost
        return self.findcost() <= other.findcost()

    def __str__ (self) :
        newpuzzle = (np.reshape(self.matrix,16)).tolist()
        asStr = ''
        for i in range (16) :
            asStr += f"{newpuzzle[i]}"
        return asStr

    def randomPuzzleGenerator(self) :
        self.matrix = np.arange(0,16)
        np.random.shuffle(self.matrix)
        self.matrix = np.reshape(self.matrix,(4,4))

    def setGcost(self, newGcost) :
        self.gCost = newGcost

    def ispuzzleValid(self) :
        if(self.matrix.shape != (4,4)) :
            return False
        newpuzzle = np.sort(np.reshape(self.matrix,16))
        for i in range(16) :
            if(i != newpuzzle[i]) :
                return False
        return True

    def checkKurangIndividual(self,number) :
        count = 0
        newpuzzle = (np.reshape(self.matrix,16)).tolist()
        if(number == 16) :
            foundIndex = self.kosong[0] * 4 + self.kosong[1]
        else :
            foundIndex = newpuzzle.index(number)
            
        for i in range(foundIndex,16) :
            if(newpuzzle[i] < number and newpuzzle[i] != 0) :
                count += 1
        return count
        

    def checkKurang(self) :
        #implementasi Kurang[i]
        count = 0
        newpuzzle = np.reshape(self.matrix,16)
        for i in range (15) :
            if(newpuzzle[i] != 0) :
                for j in range(i+1,16) :
                    if(newpuzzle[j] < newpuzzle[i] and newpuzzle[j] != 0) :
                        count += 1
            else :
                for j in range(i+1,16) :
                    count += 1
        return count

    def checkEmpty(self) :
        #mengecek apakah kosong ada di daerah arsir atau tidak
        newpuzzle = (np.reshape(self.matrix,16))
        newpuzzle = newpuzzle.tolist()
        index = newpuzzle.index(0)
        if(index in {0,2,5,7,8,10,13,15}):
            return 0
        elif(index in {1,3,4,6,9,11,12,14}) :
            return 1

    def isReachable(self) :
        return (self.checkEmpty() + self.checkKurang()) % 2 == 0

    def findEmpty(self) :
        newpuzzle = (np.reshape(self.matrix,16)).tolist()
        index = newpuzzle.index(0)
        self.kosong = [index//4 , index % 4]

    def countGCost(self) :
        cost = 0
        pembanding = np.arange(1,17)
        newpuzzle = (np.reshape(self.matrix,16))
        for i in range(0,16) :
            if(newpuzzle[i] != 0 and newpuzzle[i] != pembanding[i]) :
                cost += 1
        return cost

    def findcost(self) :
        return self.fCost + self.gCost
    
    def checkAvailableMove(self) :
        availableMoves = []
        if(self.kosong[0] != 0) :
            availableMoves.append("up")
        if(self.kosong[1] != 3) :
            availableMoves.append("right")
        if(self.kosong[0] != 3) :
            availableMoves.append("down")
        if(self.kosong[1] != 0) :
            availableMoves.append("left")
        return availableMoves

    #Fungsi gerakin puzzle
    def moveUp(self) :
        copy = np.ndarray.copy(self.matrix)
        i,j = self.kosong[0], self.kosong[1]

        indexBefore = ((i-1) * 4) + j
        indexAfter = i*4 + j
        gcostafter = self.gCost
        if(copy[i-1][j] == indexBefore + 1) :
            gcostafter += 1
        elif(copy[i-1][j]  == indexAfter + 1) :
            gcostafter -= 1
        
        newFcost = self.fCost + 1
        copy[i][j], copy[i-1][j] =  copy[i-1][j], copy[i][j]
        child = Puzzle(copy, self.parents + ["up"], gcostafter, newFcost)
        return child
    def moveDown(self) :
        copy = np.ndarray.copy(self.matrix)
        i,j = self.kosong[0], self.kosong[1]

        indexBefore = ((i+1) * 4) + j
        indexAfter = i*4 + j
        gcostafter = self.gCost    
        if(copy[i+1][j] == indexBefore + 1) :
            gcostafter += 1
        elif(copy[i+1][j] == indexAfter + 1) :
            gcostafter -= 1

        copy[i][j], copy[i+1][j] =  copy[i+1][j], copy[i][j]
        newFcost = self.fCost + 1
        child = Puzzle(copy, self.parents + ["down"], gcostafter, newFcost)
        return child
    def moveLeft(self) :
        copy = np.ndarray.copy(self.matrix)
        i,j = self.kosong[0], self.kosong[1]
        gcostafter = self.gCost
        indexBefore = (i * 4) + (j - 1)
        indexAfter = i*4 + j

        if(copy[i][j-1] == indexBefore + 1) :
            gcostafter += 1
        elif(copy[i][j-1] == indexAfter + 1) :
            gcostafter -= 1

        newFcost = self.fCost + 1
        copy[i][j], copy[i][j-1] =  copy[i][j-1], copy[i][j]
        child = Puzzle(copy, self.parents + ["left"], gcostafter, newFcost)
        
        return child
    def moveRight(self) :
        copy = np.ndarray.copy(self.matrix)
        i,j = self.kosong[0], self.kosong[1]
        gcostafter = self.gCost
        indexBefore = (i * 4) + (j+1)
        indexAfter = i*4 + j

        if(copy[i][j+1] == indexBefore + 1) :
            gcostafter += 1
        elif(copy[i][j+1] == indexAfter + 1) :
            gcostafter -= 1

        copy[i][j], copy[i][j+1] =  copy[i][j+1], copy[i][j]
        newFcost = self.fCost + 1
        child = Puzzle(copy, self.parents + ["right"], gcostafter, newFcost)
        return child
    
    def isSolved(self) :
        return self.gCost == 0
    
    def stepSoFar(self,solution) :
        copied = copy.deepcopy(self)
        print("\nPosisi Awal : ")
        self.printMatrix()
        print("")
        i = 1
        for move in solution :
            print("=" * 35)
            if(move == "up") :
                print(f"Step ke - {i} : UP, Puzzle Menjadi :")
                copied = copied.moveUp()
            if(move == "down") :
                print(f"Step ke - {i} : DOWN, Puzzle Menjadi :")
                copied = copied.moveDown()
            if(move == "right") :
                print(f"Step ke - {i} : RIGHT, Puzzle Menjadi :")
                copied = copied.moveRight()
            if(move == "left") :
                print(f"Step ke - {i} : LEFT, Puzzle Menjadi :")
                copied = copied.moveLeft()
            if(i == len(solution)) :
                print("Posisi Akhir, Puzzle Solved ")
            copied.printMatrix()
            i += 1

    def printMatrix(self) :
        print("???????????????????????????????????????????????????")
        for i in range(4):
            for j in range(4):
                print("??? ",end="")
                if(self.matrix[i][j] == 0) :
                    print(" ", end= "")
                else :
                    print(self.matrix[i][j], end="")
                if(self.matrix[i][j] < 10):
                    print(" ", end="")
            print("???")
            if(i != 3):
                print("???????????????????????????????????????????????????")
        print("???????????????????????????????????????????????????")