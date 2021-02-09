#FF D8 FF DB
#FF D8 FF E0 00 10 4A 46 49 46 00 01
#FF D8 FF EE
#FF D8 FF E1

def outputFile(key, encContents, outfile):
    print "[-] Generating output file.."
    with open(outfile, "w") as wf:
        for i in range(len(encContents)):
            wf.write(chr(ord(encContents[i]) ^ key[i % len(key)]))
    print "[-] DONE!\n"

def keyGen(magicArray, setarray, size):
    key = []
    for i in range(size):
        key.append(setarray[i] ^ magicArray[i])
    return key

set1 = [0xff, 0xd8, 0xff, 0xdb]
set2 = [0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10, 0x4a, 0x46, 0x49, 0x46, 0x00, 0x01]
set3 = [0xff, 0xd8, 0xff, 0xee]
set4 = [0xff, 0xd8, 0xff, 0xe1]

print "[-] Opening file.."
with open('my_magic_bytes.jpg.enc','rb') as rf:
    contents = rf.read()
    magic_array = []
    for i in range(12):
        magic_array.append(ord(contents[i]))

    print "\n*** Possible Keys *** "

    key1 = keyGen(magic_array, set1, 4)
    print "[-] Key 1 : ", " ".join(list(map(hex, key1))).replace("0x","")

    key2 = keyGen(magic_array, set2, 12)
    print "[-] Key 2 : ", " ".join(list(map(hex, key2))).replace("0x", "")

    key3 = keyGen(magic_array, set3, 4)
    print "[-] Key 3 : ", " ".join(list(map(hex, key3))).replace("0x", "")

    key4 = keyGen(magic_array, set4, 4)
    print "[-] Key 4 : ", " ".join(list(map(hex, key4))).replace("0x", ""), "\n"

    print "*** Generating output file for each key ***"

    print "[-] KEY 1"
    outputFile(key1, contents, "out1.dat")

    print "[-] KEY 2"
    outputFile(key2, contents, "out2.dat")

    print "[-] KEY 3"
    outputFile(key3, contents, "out3.dat")

    print "[-] KEY 4"
    outputFile(key4, contents, "out4.dat")
    print "** ENJOY !! **"
    print "|| Dont forget to run `file` command in each output file. ||\n"
