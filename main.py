from puzzle import *
import numpy as np

print("SELAMAT DATANG DI 15-PUZZLE-SOLVER :D\n")
print("Terdapat 2 Pilihan untuk 15-Puzzle : ")
print("1. Randomly Generated Puzzle")
print("2. Puzzle from .txt file\n")
cc = int(input("Silahkan Masukkan pilihan anda : "))

if (cc == 1) :
    puzzle = Puzzle()   
if (cc == 2) :
    filename = "./" + input("input filename : ")
    with open(filename, 'r') as f :
        inputMatrix = [[int(num) for num in line.split(',')] for line in f]
    puzzle = Puzzle(inputMatrix, [])

puzzle.setGcost(puzzle.countGCost())
print("Matrix Awal :")
print(puzzle.matrix)
print("=" * 35)
print("Nilai untuk setiap fungsi Kurang (i) : ")
for i in range(1,17) :
    count = puzzle.checkKurangIndividual(i)
    print(f"i = {i} | Kurang {i} = {count}")
print("=" * 35)
print(f"Nilai untuk Σ Kurang(i) + X = {puzzle.checkKurang() + puzzle.checkEmpty()}")
if(not puzzle.isReachable()) :
    print("Puzzle tidak dapat di Solve\n")
else :
    print("Puzzle bisa di Solve\n")


    

