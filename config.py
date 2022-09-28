def GetConfig():
    settings = dict()
    with open("CHANGEME.ini", encoding='UTF-8') as fhand:
        for line in fhand:
            if line[0] == "~":
                continue
            line = line.strip()
            key, val = line.split("=")
            if val == "true":
                settings[key] = True
            elif val == "false":
                settings[key] = False
            elif key == "wordsearch":
                settings[key] = val.split(",")
            elif key == "limit":
                settings[key] = int(val)
            else:
                settings[key] = val
    
    return settings

