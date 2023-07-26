# f = open('input.txt','r')
#
# txt = [line for line in f]
#
# sav = open('output.txt','w')
# for line in range(0,len(txt)):
#     if line % 2 == 1:
#         sav.write(txt[line])
# sav.close()
#

ds = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be".split(' ')
# print(ds)
dic = {}

for k, v in enumerate(ds):
    if v in dic:
        dic[v] += 1
    else:
        dic[v] = 1

for k, v in dic.items():
    print(k, v)