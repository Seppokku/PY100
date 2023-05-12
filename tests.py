guess = 'world'
solution = 'bleed'
answer = []
for k, v in zip(guess, solution):
    if k in solution and k == v:
        k = 'g'
        answer.append(k)
    elif k not in solution:# or guess_.count(k) > solution.count(v):
        k = 'b'
        answer.append(k)
    elif k in solution and guess.index(k) != solution.index(v) or guess.count(k) > solution.count(v):
        k = 'y'
        answer.append(k)


print(''.join(answer))
print('correct answer: byggg')