import os, sys

def get_md_list(path):
	mds = []
	for filepath, dirname, filenames in os.walk(path):
		for file in filenames:
			l = len(file.split('.'))
			if(l <= 0 or file.split('.')[l-1] != "md" or file.split('.')[0] == "index"):
				continue
			mds.append(file)
	return mds


def write_index(mds):
	with open("index.md", "w", encoding="utf-8") as f:
		f.write("---\n");
		f.write("title: LeetCode\n");
		f.write("date: 2019-08-10 00:08:44\n");
		f.write("type: \"LeetCode\"\n");
		f.write("layout: \"LeetCode\"\n");
		f.write("---\n");
		f.write("\n");
	for md in mds:
		print(md)
		with open(md, encoding='utf-8') as f:
			lines = f.readlines()
			with open("index.md", "a+", encoding="utf-8") as f:
				f.write("## %s\n" % md.split('.')[0])
				f.write("<details> <summary>%s</summary>\n\n" % "详解")
				for line in lines:
					f.write(line)
				f.write("</details>\n")
			

curPath = os.getcwd()

mds = get_md_list(curPath)


write_index(mds)