import jieba

# 分词
filePath='/Users/xuyizhou/Desktop/corpus.txt'
fileSegWordDonePath ='/Users/xuyizhou/Desktop/corpusSegDone.txt'
# read the file by line
fileTrainRead = []
#fileTestRead = []
with open(filePath) as fileTrainRaw:
    for line in fileTrainRaw:
        fileTrainRead.append(line)
# define this function to print a list with Chinese
def PrintListChinese(list):
    for i in range(len(list)):
        print(list[i]),
# segment word with jieba
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][:],cut_all=False)))])
    if i % 1000 == 0 :
        print(i)

# to test the segment result
#PrintListChinese(fileTrainSeg[10])

# save the result
with open(fileSegWordDonePath,'w') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(str(fileTrainSeg[i][0]))