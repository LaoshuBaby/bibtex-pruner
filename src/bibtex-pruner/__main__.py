# remove all url/file/snapshot before latex build, every zotero extrace should run once.

link_black_list = ["kns.cnki.net", "wanfangdata.com.cn", "github.com"]

def main():
    bib_file = open("ref.bib", "r", encoding="utf-8")
    bib = bib_file.readlines()

    def new_bib_func(bib):
        new_bib = []
        for line in bib:
            flag_exist = True
            for domain in link_black_list:
                if domain in line:
                    flag_exist = False
            if flag_exist == True:
                new_bib.append(line)
        
        return "\n".join(new_bib)
    
    bib_file.close()
    bib_file = open("ref.bib", "w", encoding="utf-8")
    bib_file.writelines(new_bib_func(bib))
    bib_file.close()


if __name__ == "__main__":
    main()