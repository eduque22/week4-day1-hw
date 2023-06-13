import re
with open('regex_test.txt') as rgx:
    name_patt = re.compile('[A-Z][a-z]* [A-Z]?[a-z]*?')
    info = rgx.readlines()
    print(info)

    def regex_names(info):
        for name in info:
            match = name_patt.search(name)
            if match:
                print(name)
            else:
                return None

print(regex_names(info))


