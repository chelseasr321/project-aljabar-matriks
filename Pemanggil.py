import chelsea047

matriks = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

hasil = chelsea047.determinan3x3(matriks)

print("Matriks:")
for baris in matriks:
    print(baris)

print("\nDeterminan =", hasil)
