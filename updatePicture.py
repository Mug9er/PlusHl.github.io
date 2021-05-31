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

curPath = os.getcwd()

postsPath = curPath + "/source/_posts/"

paths = get_img_url(postsPath)

newPaths = []

for path in paths:
	newPaths.append(path[54:])

paths = newPaths

jsonPath = curPath + "/source/_data/galleries.json"

jsonStr = ""

with open(jsonPath, encoding='utf-8') as f:
	jsonObj = json.load(f)
	jsonStr = str(jsonObj).replace("'", "\"").replace(r"\n", "")

with open(jsonPath, "w", encoding='utf-8') as f:
	jsonObj = json.loads(jsonStr)
	jsonObj[0]["photos"] = paths
	f.write(json.dumps(jsonObj, indent=4, ensure_ascii=False))



	
