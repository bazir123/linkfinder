import re
with open("link_finder.txt", "r", encoding="utf8") as fileobjects:
    text = fileobjects.read()


    output = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', text)

    out_str = "\n".join(output)

    
    for l in output:
        if 'https' in l:
            with open('link.txt', 'a+', encoding="utf8") as f:
                         f.writelines(l + '\n')
