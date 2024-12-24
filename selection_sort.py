import random
import time

def selection_sort_descending(A, N):
    """
    Procedure to sort the array A using Selection Sort in descending order.

    Parameters:
        A: list of integers (the sales data of products)
        N: integer (number of elements in A)

    Returns:
        None (the list A will be sorted in-place in descending order)
    """
    pass_idx = 1
    while pass_idx <= N - 1:
        idx = pass_idx - 1
        i = pass_idx
        while i < N:
            if A[idx] < A[i]:
                idx = i
            i += 1
        temp = A[pass_idx - 1]
        A[pass_idx - 1] = A[idx]
        A[idx] = temp
        pass_idx += 1

# Program utama untuk menyortir produk best seller tahunan
def main():
    # Data penjualan produk tahunan (1000 produk dengan nilai acak antara 1 dan 1000)
    produk = [random.randint(1, 1000) for _ in range(10000)]
    N = len(produk)

    print("Data produk sebelum disortir:", produk)

    # Mengukur waktu eksekusi
    start_time = time.time()

    # Menjalankan algoritma Selection Sort (Descending)
    selection_sort_descending(produk, N)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Data produk setelah disortir secara descending:", produk)
    print(f"Waktu eksekusi untuk menyortir 1000 produk: {execution_time:.6f} detik")

# Menjalankan program utama
if __name__ == "__main__":
    main()
