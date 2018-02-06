import re


class Dart():

    def spliter(self, s1):

        return num_score, exp_score, award_score

    def score_cal(self, i, score, exp, award=None):
        pass


data = ['1S2D*3T', "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]

for i in data:
    a = re.findall('\\d{1,2}', i)
    b = re.findall('[A-Z]{1}', i)
    c = re.findall('[*#]{1,3}', i)
    # print(list(map(lambda x: int(x), a)))
    # print(b)
    # print(c)
    # print()
dart = Dart()

for score in data:
    num_score, exp_score, award_score = dart.spliter(score)
    for i in range(len(num_score)):
        dart.score_cal(num_score[i], exp_score[i], award_score[i])
