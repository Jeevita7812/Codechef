for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    max = 0
    max_pairs = 0
    total_pairs = 0
    for s in range(n):
        for j in range(n):
            if s < j:
                total_pairs += 1
                if max < (lst[s] + lst[j]):
                    max_pairs = 0
                    max = lst[s] + lst[j]
                    max_pairs += 1
                elif max == (lst[s] + lst[j]):
                    max_pairs += 1
    print(format((max_pairs / total_pairs),'.8f'))
