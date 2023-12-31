# bibtex-pruner
When a bibTeX file exported by Zotero contains too many unnecessary fields
当Zotero导出的bibTeX文件包含了太多不需要的字段

简体中文 | English

## 使用场景

在命令行中运行文件或直接传入bibtex文本（或考虑从剪贴板中读取并写回）

## 适用场景

**GB/T 7714—2015** 标准及使用此标准的LaTeX库：
* https://github.com/zepinglee/gbt7714-bibtex-style

## 同类工具

* bibtex-clean: [GitHub(CangyuanLi/bibtex_fields)](https://github.com/CangyuanLi/bibtex_fields), [PyPi(bibtex-clean)](https://pypi.org/project/bibtex-clean/)

## 附加功能

* 如果不是Zotero导出的而又需要处理帽子字符大小写，本工具可以帮您把帽子字符暴力修改为大写（参见[zepinglee/gbt7714-bibtex-style - 不能处理西文姓氏中含如é到É的大小写转换(#145)](https://github.com/zepinglee/gbt7714-bibtex-style/issues/145)）
* 不知道之前有没有在公开场合表达过，但是确实有想处理citation key的想法，不过似乎果然better bibtex已经实现了这个了 https://retorque.re/zotero-better-bibtex/citing/
