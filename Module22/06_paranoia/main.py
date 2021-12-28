
def alphavit_leter(id,line,step):
    leter_list = ""
    for leter in range(len(alphavit)):
        if alphavit[leter] == line[id] and leter + step < len(alphavit):
            leter_list += alphavit[leter + step]
        elif alphavit[leter] == line[id] and leter + step >= len(alphavit):
            leter_list += alphavit[0 + (step - (len(alphavit) - leter))]
    return "".join(leter_list)

alphavit = 'abcdefghijklmnopqrstvxyz'
text = open("text.txt",'r')
step = 1
for line in text.readlines():
    crypto_text = [alphavit_leter(id,line.lower(),step) for id in range(len(line))]
    cipher_text = open('cipher_text.txt','a')
    cipher_text.writelines([''.join(crypto_text),'\n'])
    cipher_text.close()
    step += 1



