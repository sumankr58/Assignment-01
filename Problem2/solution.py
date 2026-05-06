def min_operations(arr, k):
    remainder = arr[0] % k
    for num in arr:
        if num % k != remainder:
            return -1

    transformed = [(num - remainder) // k for num in arr]
    transformed.sort()

    median = transformed[len(transformed) // 2]

    operations = sum(abs(x - median) for x in transformed)

    return operations


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(min_operations(arr, k))
