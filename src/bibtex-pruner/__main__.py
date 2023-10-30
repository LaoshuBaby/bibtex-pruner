rule_1 = ["title", "author", "journaltitle", "volume", "number", "pages", "langid"]
rule_2 = ["date", "eprint", "eprinttype", "issn", "doi", "keywords", "file"]
link_black_list = ["kns.cnki.net", "wanfangdata.com.cn", "github.com"]


def fliter_link(bib_line_list):
    # remove all url/file/snapshot before latex build
    new_bib = []
    for line in bib_line_list:
        flag_exist = True
        for domain in link_black_list:
            if domain in line:
                flag_exist = False
        if flag_exist == True:
            new_bib.append(line)

    return "\n".join(new_bib)


def fliter_doi():
    pass


def main(method="bibtexparser"):
    # READ
    bib_file = open("ref.bib", "r", encoding="utf-8")
    bib:str = bib_file.read()
    bib_file.close()
    # PROCESS
    if method=="perline":
        bib_text=fliter_link(bib.split("\n"))
        
    if method=="bibtexparser":
        import bibtexparser
        library = bibtexparser.parse_string(bib)
        print(library)
    # WRITE
    bib_file = open("ref.bib", "w", encoding="utf-8")
    bib_file.writelines(bib_text)
    bib_file.close()
    

if __name__ == "__main__":
    # TODO 添加支持自定义bib文件
    main()
