import os, sys, json


def get_img_url(path):
	paths = []
	for filepath, dirname, filenames in os.walk(path):
		for file in filenames:
			last = len(file.split('.'))
			if(last <= 0 or file.split('.')[last-1] != "md"):
				pass
			with open(path+file) as f:
				lines = f.readlines();
			for p in lines:
				if(p[0:3] == "img"):
					if(p[4] == ' '):
						paths.append(p[5:-1])
					else:
						paths.append(p[4,-1])
	return paths

print(len(

curPath = os.getcwd()

postsPath = curPath + "/source/_posts/"

paths = get_img_url(postsPath)

for path in paths:
	

jsonPath = curPath + "/source/_data/galleries.json"

jsonStr = ""

with open(jsonPath) as f:
	jsonObj = json.load(f)
	jsonStr = str(jsonObj).replace("'", "\"").replace(r"\n", "")
	print(jsonStr)

with open(jsonPath, "w") as f:
	jsonObj = json.loads(jsonStr)
	print(jsonObj)	
	jsonObj[0]["photos"] = paths
	f.write(json.dumps(jsonObj, indent=4, ensure_ascii=False))



	