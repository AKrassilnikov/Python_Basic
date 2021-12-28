
import zipfile,os
unzip = zipfile.ZipFile("voyna-i-mir.zip",'r')
file = unzip.extract('voyna-i-mir.txt')
voyna_i_mir = open('voyna-i-mir.txt','r',encoding='utf-8')
summ_leters = 0
for line in voyna_i_mir.readlines():
    summ_leters += len(line)
voyna_i_mir.close()
print("Всего символов: ",summ_leters)



