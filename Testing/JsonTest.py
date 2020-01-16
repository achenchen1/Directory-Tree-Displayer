import json

with open('test.json', 'r') as j_file:
	json_dict = json.load(j_file)

for entry in json_dict:
	print(entry)

print("\n")
print(type(json_dict["championPatch"][0]))
patch_champs = {}

for x in json_dict["championPatch"]:
	try:
		patch_champs[x["rank"]].append(x["champion"])
	except KeyError:
		patch_champs[x["rank"]] = [x["champion"]]

counter = 0
for x in range(0, 200):
	try:
		for y in patch_champs[x]:
			counter += 1
			print(x, y)
	except KeyError:
		pass
print(len(json_dict["championPatch"]), counter)
