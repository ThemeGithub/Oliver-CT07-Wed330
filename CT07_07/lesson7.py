name = ["name", 12345678, "Co-"]
student = ["student", 87654321, "Curriculum"]
person = ["person", 91827364, "Activities"]

people = []
people.append(name)
people.append(student)
people.append(person)
for i in people:
    print("name: " + i[0] + " number: " + str(i[1]) + " cca: " + i[2])