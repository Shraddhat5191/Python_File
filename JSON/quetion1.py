import json
s='{"Name":"Ram";}'
print(s["Name"])
s=json.dumps(s)
print(json.loads(s))
# print(s)
# import json
# shraddha={
#     "name":"shraddha",
#     "age":20,
# }
# # s=json.dumps(s)
# print(json.loads(shraddha))

