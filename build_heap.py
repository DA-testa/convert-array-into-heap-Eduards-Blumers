# python3

def heapify(data, n, i, swaps):

    smallest = i  
    l = 2 * i + 1 
    r = 2 * i + 2

    if l < n and data[l] < data[smallest]:
        smallest = l

    if r < n and data[r] < data[smallest]:
        smallest = r

    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
        heapify(data, n, smallest, swaps)


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps


def main():
    
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
