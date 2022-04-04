# 15-Puzzle-Solver
> Tugas Kecil Mata Kuliah IF2211 Strategi Algoritma ITB.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Program yang dapat menyelesaikan persoalan 15-Puzzle dengan menggunakan Algoritma Branch and Bound. Program menerima input puzzle berupa file .txt yang berisi matriks representasi puzzle. Apabila instansiasi Puzzle tidak dapat diselesaikan, program akan mengeluarkan output "Puzzle tidak dapat di Solve".

## Technologies Used
- Python 3
- NumPy Python library

## Features
- 15-Puzzle-Solver
- Step by step solution CLI visualization
- Node generated, Program runtime, KURANG(I) function

## Usage
- Pastikan sudah melakukan install Python 3 serta library NumPy 
- Lakukan clone pada repository ini
- Masuk ke directory tempat repository ini disimpan
- Jalankan program dengan menggunakan _command_
```
python ./src/main.py
```
- Masukkan input dengan menggunakan command line, dapat memilih antara randomly generated puzzle atau masukkan dari file teks
- Output berupa posisi awal, fungsi KURANG(I) akan keluar, program akan mengeluarkan output "Puzzle tidak dapat di Solve" apabila instansiasi tidak dapat diselesaikan dan akan mengeluarkan output berupa matriks posisi awal sampai akhir, waktu eksekusi, node yang dibangkitkan, step solusi apabila instansiasi dapat diselesaikan
- Apabila ingin mencoba instansiasi 15-puzzle lain, silahkan tambahkan puzzle pada folder test. Ubin kosong pada puzzle direpresentasikan dengan angka "0" dan ikuti format penulisan pada .txt yang sudah ada

## Acknowledgements
- Terima kasih kepada seluruh dosen pengajar dan asisten mata kuliah IF2211 Strategi Algoritma

## Contact
Created by:
- [@dhikaarta](https://github.com/dhikaarta)

