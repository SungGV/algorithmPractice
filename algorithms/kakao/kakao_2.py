from re import findall, match, search


class Dart():

    score = [1] * 3
    prev_award = None

    # def spliter(self, s):

    #     return num_score, other_score

    def score_cal(self, i, num_score, expo, award=None):
        self.prev_award = award
        if expo == 'T':
            self.score[i] = num_score * num_score * num_score
        elif expo == 'D':
            self.score[i] = num_score * num_score
        else:
            self.score[i] = num_score

        if award:
            if award == '#':
                self.score[i] *= -1
            elif award == "*":
                self.score[i] *= 2
                if self.prev_award == '#':
                    self.score[i - 1] *= -2
                elif i != 0:
                    self.score[i - 1] *= 2

        self.score[i] = self.score[i]
        print(self.score[i])


dart = Dart()
a = ['1S2D*3T', "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]

# other_score = [('S', ''), ('D', '*'), ('T', '')]
# num_score = [1, 2, 3]

# other_score = [('D', ''), ('S', '#'), ('S', '')]
# num_score = [1, 2, 10]

# other_score = [('D', ''), ('S', ''), ('T', '')]
# num_score = [1, 2, 0]

# other_score = [('S', '*'), ('T', '*'), ('S', '')]
# num_score = [1, 2, 3]

# other_score = [('D', '#'), ('S', '*'), ('S', '')]
# num_score = [1, 2, 3]

# other_score = [('T', ''), ('D', ''), ('D', '#')]
# num_score = [1, 2, 3]

other_score = [('D', ''), ('S', ''), ('T', '*')]
num_score = [1, 2, 3]

# for i in a:
# num_score, other_score = dart.spliter(i)
for i in range(len(num_score)):
    dart.score_cal(i, num_score[i], other_score[i][0], other_score[i][1])
    dart.prev_award = 0
print('total', sum(dart.score))
