import os, sys, shutil, json

def get_md_list(path):
	mds = []
	for filepath, dirname, filenames in os.walk(path):
		for file in filenames:
			l = len(file.split('.'))
			if(l <= 0 or file.split('.')[l-1] != "md" or file.split('.')[0] == "index"):
				continue
			mds.append(file)
	return mds
			

def move_mds(mds):
	for md in mds:
		shutil.move(md, "../_posts/%s" % md)


def move_back_mds(mds):
	for md in mds:
		shutil.move("../_posts/%s" % md, md)


def get_json_info(mds):
	json_list = []
	for md in mds:
		with open(md, encoding='utf-8') as f:
			lines = f.readlines()
			dict = {}
			for line in lines:
				l = len(line.split(":"))
				arr = line.split(":")
				if(l <= 0 or (arr[0] != "title" and arr[0] != "abbrlink")):
					continue	
				dict[arr[0]] = arr[1][1:-1]
			json_list.append(dict)
	return json_list


def write_json(content):
	with open("../_data/leetcodes.json", "w", encoding='utf-8') as f:
		f.write(json.dumps(content, indent=4, ensure_ascii=False))

if __name__ == "__main__":
	
	curPath = os.getcwd()

	mds = get_md_list(curPath)

	move_mds(mds)

	os.system("hexo g")

	move_back_mds(mds)

	jsonObj = get_json_info(mds)
	
	write_json(jsonObj)
