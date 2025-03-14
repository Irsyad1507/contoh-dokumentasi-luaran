def writeValue(text: str):
    global saveCode
    save_idx = 0
    for l in range(len(text)):
        char = text[save_idx]
        if char in "|\\":
            saveCode = str(saveCode) + "\\"
        saveCode = str(saveCode) + char
        save_idx += 1
    saveCode = str(saveCode) + "|"

def readValue():
    global save_idx
    value = ""
    while True:
        try:
            char = saveCode[save_idx]
        except IndexError:
            char = ""
        save_idx += 1
        if (char == "|"):
            break
        if char == "\\":
            try:
                char = saveCode[save_idx]
            except IndexError:
                char = ""
            save_idx += 1 
        value = str(value) + char
    return value

if __name__ == '__main__':
    saveCode = ""
    save_idx = 0
    writeValue("Hello")
    writeValue("Fellow :\\ Pythons")
    writeValue("123")
    print(saveCode)

    for j in range(4):
        print(readValue())