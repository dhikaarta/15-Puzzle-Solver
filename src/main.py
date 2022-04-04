from puzzle import *
import numpy as np
from queue import PriorityQueue
import timeit

print("SELAMAT DATANG DI 15-PUZZLE-SOLVER :D\n")
print("Terdapat 2 Pilihan untuk 15-Puzzle : ")
print("1. Randomly Generated Puzzle")
print("2. Puzzle from .txt file\n")
cc = int(input("Silahkan Masukkan pilihan anda : "))

if (cc == 1) :
    puzzle = Puzzle()   
if (cc == 2) :
    filename = "./Test/" + input("input filename : ")
    with open(filename, 'r') as f :
        inputMatrix = [[int(num) for num in line.split(' ')] for line in f]
    puzzle = Puzzle(inputMatrix, [])

start = timeit.default_timer()
puzzle.setGcost(puzzle.countGCost())

print("Matrix Awal :")
puzzle.printMatrix()
print("=" * 35)
print("Nilai untuk setiap fungsi Kurang (i) : \n")
for i in range(1,17) :
    count = puzzle.checkKurangIndividual(i)
    if(i < 10) :
        print(f"i = {i}  | Kurang {i} = {count}")
    else :
        print(f"i = {i} | Kurang {i} = {count}")
print("=" * 35)
print(f"Nilai untuk Σ Kurang(i) + X = {puzzle.checkKurang() + puzzle.checkEmpty()}")

if(not puzzle.isReachable()) :
    print("Puzzle tidak dapat di Solve\n")
else :

    visited = {}
    solutions = []
    matQueue = PriorityQueue()
    matQueue.put(puzzle)
    nodeVisited = 0

    while(not matQueue.empty()) :
        currentNode = matQueue.get()
        visited[str(currentNode)] = True

        if(currentNode.isSolved()) :
            solutions.append(currentNode.parents)
            stop = timeit.default_timer()
            break
        else :
            availableMoves = currentNode.checkAvailableMove()
            for move in availableMoves :
                if move == "up" :
                    new = currentNode.moveUp()
                    if(str(new) not in visited) :
                        nodeVisited += 1
                        matQueue.put(new)
                if move == "right" :
                    new = currentNode.moveRight()
                    if(str(new) not in visited) :
                        nodeVisited += 1
                        matQueue.put(new)
                if move == "down" :
                    new = currentNode.moveDown()
                    if(str(new) not in visited) :
                        nodeVisited += 1
                        matQueue.put(new)
                if move == "left" :
                    new = currentNode.moveLeft()
                    if(str(new) not in visited) :
                        nodeVisited += 1
                        matQueue.put(new)
    
    
    puzzle.stepSoFar(solutions[0])

    print("-" * 35)
    print(f"• Solusi yang didapat = {solutions}")
    print(f"• Banyak step = {len(currentNode.parents)} step")
    print(f"• Waktu Eksekusi : {stop - start} detik")
    print(f"• Node yang dibangkitkan : {nodeVisited} node")
    print("-" * 35)


    

