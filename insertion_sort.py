import random
import time

def insertion_sort(A, N):
    """
    Procedure to sort the array A using Insertion Sort.

    Parameters:
        A: list of integers (the sales data of products)
        N: integer (number of elements in A)

    Returns:
        None (the list A will be sorted in-place in ascending order)
    """
    # Starting the sorting process
    pass_idx = 1
    while pass_idx <= N - 1:
        i = pass_idx
        temp = A[pass_idx]
        while i > 0 and temp < A[i - 1]:
            A[i] = A[i - 1]
            i -= 1
        A[i] = temp
        pass_idx += 1

# Program utama untuk menyortir produk best seller tahunan
def main():
    # Data penjualan produk tahunan (1000 produk dengan nilai acak antara 1 dan 1000)
    produk = [random.randint(1, 1000) for _ in range(10000)]
    N = len(produk)

    print("Data produk sebelum disortir:", produk)

    # Mengukur waktu eksekusi
    start_time = time.time()

    # Menjalankan algoritma Insertion Sort
    insertion_sort(produk, N)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Data produk setelah disortir:", produk)
    print(f"Waktu eksekusi untuk menyortir 1000 produk: {execution_time:.6f} detik")

# Menjalankan program utama
if __name__ == "__main__":
    main()
