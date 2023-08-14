import argparse
import re
import os
# Anki Add on: Customize Keyboard Shortcuts
# https://ankiweb.net/shared/info/24411424
# wps formulua: =C6&"<hr>"&D6

#separator:tab
#html:true
#tags column:2

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', help='file name')
    args = parser.parse_args()
    lnlist = []
    with open(args.file, "r", encoding="utf-8") as f:
        for ln in f:
            new_text = re.sub(r'\{\{c\d*::', '{{c1::', ln)
            left = new_text.find("{{c1::")
            right = new_text.find("}}")

            old_cloze = new_text[left:right]
            new_cloze = old_cloze.replace(" ","}} {{c1::")
            finish_cloze = new_text.replace(old_cloze,new_cloze)
            lnlist.append(finish_cloze)
    for ln in lnlist:
        print(ln,end="")
    abspath, basename = os.path.split(args.file)
    filepath = os.path.join(abspath,"finished_" + basename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#tags column:2\n")
        for ln in lnlist:
            f.write(ln)

if __name__ == '__main__':
    _main()