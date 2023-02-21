#picoCTF "basic-mod1" decrypted the msg

#split the msg
msg = " 54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 ".split()
#print(msg)
#map it to mods
mods = [i for i in range(0,37)]
#print(mods)
#map it to each alphabet and number and _
chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
#print(chars)
#dictionary of em
d = {mods[i]:chars[i] for i in range (len(mods))}
#print (d)
#so here we mod the dict we made over 37. convert the msg to int since it strings, to get the flag, so we used end to make it easier and clearer to read
print("picoCTF{", end="")
for i in range(len(msg)):
    print(d[int(msg[i]) % 37], end="")
print("}")