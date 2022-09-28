import matplotlib.pyplot as plt

data = open("data.txt", 'r').readlines()


class Person:
    def __init__(self, name, gender, age, height):
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.height = float(height)

    def __str__(self):
        return self.name + " " + self.gender + " " + str(self.age) + " " + str(self.height)

    def dist(self, other):
        return abs(self.age - other.age) + 15 * abs(self.height - other.height)


class Dataset:
    def __init__(self, people):
        self.people = people


people = [None] * (len(data) - 1)

for i in range(1, len(data)):
    data_split = data[i].split()
    p = Person(data_split[0], data_split[1], data_split[2], data_split[3])
    people[i - 1] = p

n = len(people)
x = []
y = []
for i in range(n):
    p = people[i]
    x.append(p.age)
    y.append(15 * p.height)
plt.scatter(x, y)
plt.xlim(0, 110)
plt.ylim(0, 110)
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()


def compute_groups(people, centers):
    # one pass
    groups = [None] * len(people)
    for i in range(n):
        p = people[i]
        group = -1
        min_dist = 69420
        for c in centers:
            if c.dist(p) < min_dist:
                min_dist = c.dist(p)
                group = int(c.gender)
        groups[i] = group
    return groups


def print_results(people, groups):
    for i in range(len(people)):
        print(people[i].name + ": Group " + str(groups[i] + 1))


def recompute_centers(people, groups):
    n = len(people)
    centers = [None] * 4
    for i in range(4):
        centers[i] = Person("Group " + str(i + 1), i, 0, 0)
    center_count = [0] * 4

    for i in range(n):
        p = people[i]
        center = centers[groups[i]]
        center.age += p.age
        center.height += p.height
        center_count[groups[i]] += 1

    for i in range(4):
        center = centers[i]
        center.age /= center_count[i]
        center.height /= center_count[i]

    return centers


def print_centers(centers):
    for i in range(len(centers)):
        print(centers[i].name + ": AGE [" + str(centers[i].age) + "]   HEIGHT [" + str(centers[i].height) + "]")


center_indexes = [16, 9, 4, 14]
centers = [None] * 4
for i in range(4):
    index = center_indexes[i]
    centers[i] = Person("Group " + str(i + 1), i, people[index].age, people[index].height)

print("\nInitial Centers")
print_centers(centers)
print("\nPass #1")
groups = compute_groups(people, centers)
print_results(people, groups)
centers = recompute_centers(people, groups)
print_centers(centers)
print("\nPass #2")
groups = compute_groups(people, centers)
print_results(people, groups)
centers = recompute_centers(people, groups)
print_centers(centers)

'''
print("\nPass #3")
groups = compute_groups(people, centers)
print_results(people, groups)
centers = recompute_centers(people, groups)
print_centers(centers)
'''

n = len(people)
x = []
y = []
colors = []
for i in range(n):
    p = people[i]
    x.append(p.age)
    y.append(p.height)
    colors.append("cbgr"[groups[i]])
plt.scatter(x, y, c=colors)
plt.xlim(0, 50)
plt.ylim(0, 7)
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()
