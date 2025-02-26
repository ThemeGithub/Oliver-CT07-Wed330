name = ["name", 12345678, "Co-"]
student = ["student", 87654321, "Curriculum"]
person = ["person", 91827364, "Activities"]


people = [
    ["name", 12345678, "Co-"],
    ["student", 8765432, "Curriculum"],
    ["person", 91827364, "Activities"]
]

for i in people:
    print("name: " + i[0] + " number: " + str(i[1]) + " cca: " + i[2])