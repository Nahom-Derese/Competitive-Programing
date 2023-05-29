n = int(input())

# create a dictionary to store the players' scores
scores = {}

# loop over n rounds
for i in range(n):
    name, score = input().split()
    score = int(score)
    if name not in scores:
        scores[name] = 0
    scores[name] += score

# find the maximum score and the player(s) with that score
max_score = max(scores.values())
winners = [name for name, score in scores.items() if score == max_score]

# find the first player among the winners to reach the maximum score
winner = None
for name, score in zip(input().split(), map(int, input().split())):
    if name in winners and score >= max_score:
        winner = name
        break

# print the winner's name
print(winner)