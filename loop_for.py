# A for-loop is used for iterating over a list, a tuple, a dictionary, a set,
#  or a string sequence.


# Range is function: range(n): 0...n-1
numbers = []
for i in range(10):
    numbers.append(i)
print(f"numbers range(10): {numbers}")

# range(begin, end): begin..end-1: range(4,8) is 4, 5, 6, 7
numbers = []
for i in range(4, 10):
    numbers.append(i)
print(f"numbers range(4, 10): {numbers}")

# range(begin, end, step): range(10,20,2) is 10, 12, 14, 16, 18
numbers = []
for i in range(10, 20, 2):
    numbers.append(i)
print(f"numbers range(10,20,2): {numbers}")

# for loop: continue
odd, even = [], []
for i in range(10):
    if i % 2 == 0:
        even.append(i)
        continue
    odd.append(i)
print(f"Odd: {odd}")
print(f"Even: {even}")

# for loop: break
answer, non_answer = [], []
for i in range(40, 100):
    if i == 42:
        answer.append(i)
        break
    non_answer.append(i)
print(f"Answer to univers: {answer}")
print(f"Non-Answer to univers: {non_answer}")

# for loop: break-else, else - when loop finishes (not by break) by exhaustion
#  of the range list
answer, non_answer = [], []
for i in range(30, 41):
    if i == 42:
        break
    non_answer.append(i)
else:
    print(f"No answer found: {i}")
print(f"Answer to univers: {answer}")
print(f"Non-Answer to univers: {non_answer}")


# pass is a NOOP
def noop():
    pass
    return


noop()
print("pass done")
