# remove all url/file/snapshot before latex build, every zotero extrace should run once.

watch_list = ["kns.cnki.net", "wanfangdata.com.cn", "github.com"]
bib_file = open("ref.bib", "r", encoding="utf-8")
bib = bib_file.readlines()
new_bib = []
for line in bib:
    flag_exist = True
    for domain in watch_list:
        if domain in line:
            flag_exist = False
    if flag_exist == True:
        new_bib.append(line)
bib_file.close()
bib_file = open("ref.bib", "w", encoding="utf-8")
bib_file.writelines(new_bib)
bib_file.close()
