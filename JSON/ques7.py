import json
  
  
# the file to be converted to 
# json format
file= 'JSON/data.txt'
  
# dictionary where the lines from
# text will be stored
dict1 = {}
  
# creating dictionary
with open(file) as f:
  
    for s in f:
        key, description = s.strip().split(None, 1)
        dict1[key] = description.strip()
  
# creating json file
# the JSON file is named as test1
out_file = open("JSON/json_file.json", "w")
json.dump(dict1,out_file)
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()

# import json
# filename = 'JSON/data.txt'
# dict1 = {}
# with open(filename) as fh:
#     for line in fh:
#         command, description = line.strip().split(None, 1)
#         dict1[command] = description.strip()
# out_file = open("test1.json", "w")
# json.dump(dict1, out_file, indent = 7, sort_keys = False)
# out_file.close()

# file=open("data.txt","r")




