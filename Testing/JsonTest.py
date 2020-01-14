import json

with open('test.json', 'r') as j_file:
	json_dict = json.load(j_file)

for entry in json_dict:
	print(entry)

print("\n")
print(type(json_dict["players"][0]))
for x in json_dict["players"][0]:
	print(x)
	print(type(json_dict["players"][0][x]))
