# How can you make this more scalable and reusable later?

def armstrong_it(num):
    breakdown = [int(d) for d in str(num)]
    mathed = 0
    for number in breakdown:
        mathed = mathed + number ** len(breakdown)
    return mathed


def find_armstrong_numbers(numbers):
    mathed = list(map(lambda item: armstrong_it(item), numbers))
    answer = []
    for i in range(len(numbers)):
        if i == mathed[i]:
            answer.append(i)
    return answer
