# Write data to center of file

Задача записать данные в середину файла, экономя память

```console
php index.0.php
```

```
length of input content = 6
filesize = 16
file 1.bin opened
CURSOR POSITION 0
CURSOR POSITION 8
read to var second half substr
CURSOR POSITION 0
CURSOR POSITION 14
6 bytes writed to file 1.bin 
8 bytes writed to file 1.bin 
file 1.bin closed
```

Естественно сохранять вторую часть строки в памяти дешевле чем читать всю строку в память, еще дешевле было бы перестановкой через fgetc, fwrite, перестановкой курсора. Надеюсь скоро запилю и такой вариант.

## Read file backward

```console
php index.1.php
```

```
filesize = 16
file 1.bin opened
CURSOR POSITION 15
F

CURSOR POSITION 14
E

CURSOR POSITION 13
D

CURSOR POSITION 12
C

CURSOR POSITION 11
B

CURSOR POSITION 10
A

CURSOR POSITION 9
9

CURSOR POSITION 8
8

CURSOR POSITION 7
7

CURSOR POSITION 6
6

CURSOR POSITION 5
5

CURSOR POSITION 4
4

CURSOR POSITION 3
3

CURSOR POSITION 2
2

CURSOR POSITION 1
1

CURSOR POSITION 0
0

file 1.bin closed
```
