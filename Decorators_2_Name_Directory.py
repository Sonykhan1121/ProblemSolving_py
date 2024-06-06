import operator

def person_lister(func):
    def wrapper(people):
        people.sort(key=lambda x: int(x[2]))
        # print(people)
        result = [func(person) for person in people ]
        # print(result)
        return result
    return wrapper

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    # print(people)
    print(*name_format(people), sep='\n')