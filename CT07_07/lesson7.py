# name = ["name", 12345678, "Co-"]
# student = ["student", 87654321, "Curriculum"]
# person = ["person", 91827364, "Activities"]

# people = []
# people.append(name)
# people.append(student)
# people.append(person)
# for i in people:
#     print("name: " + i[0] + " number: " + str(i[1]) + " cca: " + i[2])

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]

# print(list1 + list2)


# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# print(sorted(list1 + list2))

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3
# print(fruits[:index])

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# print(fruits[:len(fruits) // 2])
# print(fruits[len(fruits) // 2:])

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# unique = []
# for i in list1:
#     if not i in list2:
#         unique.append(i)
# for i in list2:
#     if not i in list1:
#         unique.append(i)
# print(unique)

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list = list1 + list2
# for i in range(len(list)):
#     if list[i] % 2 == 0:
#         print(list[i])


# nested_list = [[1, 2], [3, 4], [5, 6]]
# list = []
# for i in nested_list:
#     for j in i:
#         list.append(j)
# print(list)

students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3


# temp = []
# groups = []
# for i in range(len(students)):
#     temp.append(students[i])
#     if (i + 1) % size == 0:
#         groups.append(temp)
#         temp = []
# print(groups)

groups = []
for i in range(0, len(students), size):
    groups.append(students[i:i + size])
print(groups)