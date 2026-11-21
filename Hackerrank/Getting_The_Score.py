n = int(input())
scores = list(map(int, input().split()))

unique_scores = list(set(scores))
unique_scores.sort()

print(unique_scores[-2])