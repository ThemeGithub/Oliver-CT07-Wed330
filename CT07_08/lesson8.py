Anson = ["a", "b", "c"]
Baron = ["a", "c", "e"]
common = []
for i in Anson:
    if i in Baron:
        common.append(i)
for i in common:
    print(i)