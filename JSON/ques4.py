import json
s={'4':5,'6':7,'1':3,'2':4}
# with open("shraddha.json","w") as a:
#     json.dump(s,a,sort_keys=True)

out_file=open("bye.json","w")
json.dump(s,out_file,sort_keys=True)
out_file.close()    
