

def LoadDataSet(address):
    Data = []
    with open(address) as txtData:
        lines = txtData.readlines()
        for line in lines:
            lineData = line.strip().split('\t')
            Data.append(lineData)
        return Data



def naiveBayesian(trainData, testData):

    m = len(trainData)
    pro_c = [0, 0]
    for i in range(m):
        # 计算p(ci)
        if trainData[i][-1] == '0':
            pro_c[0] += 1
        else:
            pro_c[1] += 1
    print(pro_c)
    one = pro_c[0] + 1
    two = pro_c[1] + 1
    problity = [one / (one + two), two / (one + two)]
    print('probability:', problity)
    # 计算p(年龄|否)
    p_age_0 = []
    count_A = 1
    count_B = 1
    count_C = 1
    pro_c_0 = pro_c[0] + 3
    for item in range(m):
        if trainData[item][-1] == '0':
            if trainData[item][0] == 'A':
                count_A += 1
            elif trainData[item][0] == 'B':
                count_B += 1
            elif trainData[item][0] == 'C':
                count_C += 1
    p_age_0.append(count_A / pro_c_0)
    p_age_0.append(count_B / pro_c_0)
    p_age_0.append(count_C / pro_c_0)
    print('p_age_0:', p_age_0)

    # 计算p(年龄|是)
    p_age_1 = []
    count_A = 1
    count_B = 1
    count_C = 1
    pro_c_1 = pro_c[1] + 3
    for item in range(m):
        if trainData[item][-1] == '1':
            if trainData[item][0] == 'A':
                count_A += 1
            if trainData[item][0] == 'B':
                count_B += 1
            if trainData[item][0] == 'C':
                count_C += 1
    p_age_1.append(count_A / pro_c_1)
    p_age_1.append(count_B / pro_c_1)
    p_age_1.append(count_C / pro_c_1)
    print('p_age_1:', p_age_1)

    # 计算p(收入|否)
    p_money_0 = []
    count_A = 1
    count_B = 1
    count_C = 1
    pro_c_0 = pro_c[0] + 3
    for item in range(m):
        if trainData[item][-1] == '0':
            if trainData[item][1] == 'low':
                count_A += 1
            elif trainData[item][1] == 'medium':
                count_B += 1
            elif trainData[item][1] == 'high':
                count_C += 1
    p_money_0.append(count_A / pro_c_0)
    p_money_0.append(count_B / pro_c_0)
    p_money_0.append(count_C / pro_c_0)
    print('p_money_0:', p_money_0)

    # 计算p(收入|是)
    p_money_1 = []
    count_A = 1
    count_B = 1
    count_C = 1
    pro_c_1 = pro_c[1] + 3
    for item in range(m):
        if trainData[item][-1] == '1':
            if trainData[item][1] == 'low':
                count_A += 1
            elif trainData[item][1] == 'medium':
                count_B += 1
            elif trainData[item][1] == 'high':
                count_C += 1
    p_money_1.append(count_A / pro_c_1)
    p_money_1.append(count_B / pro_c_1)
    p_money_1.append(count_C / pro_c_1)
    print('p_money_1:', p_money_1)

    # 计算p(学生|否)
    p_student_0 = []
    count_A = 1
    count_B = 1
    pro_c_0 = pro_c[0] + 2
    for item in range(m):
        if trainData[item][-1] == '0':
            if trainData[item][2] == 'no':
                count_A += 1
            elif trainData[item][2] == 'yes':
                count_B += 1
    p_student_0.append(count_A / pro_c_0)
    p_student_0.append(count_B / pro_c_0)
    print('p_student_0:', p_student_0)

    # 计算p(学生|是)
    p_student_1 = []
    count_A = 1
    count_B = 1
    pro_c_1 = pro_c[1] + 2
    for item in range(m):
        if trainData[item][-1] == '1':
            if trainData[item][2] == 'no':
                count_A += 1
            elif trainData[item][2] == 'yes':
                count_B += 1
    p_student_1.append(count_A / pro_c_1)
    p_student_1.append(count_B / pro_c_1)
    print('p_student_1:', p_student_1)

    # 计算p(信用等级|否)
    p_faith_0 = []
    count_A = 1     # fair
    count_B = 1     # excellent
    pro_c_0 = pro_c[0] + 2
    for item in range(m):
        if trainData[item][-1] == '0':
            if trainData[item][3] == 'fair':
                count_A += 1
            elif trainData[item][3] == 'excellent':
                count_B += 1
    p_faith_0.append(count_A / pro_c_0)
    p_faith_0.append(count_B / pro_c_0)
    print('p_faith_0:', p_faith_0)

    # 计算p(信用等级|是)
    p_faith_1 = []
    count_A = 1     # fair
    count_B = 1     # excellent
    pro_c_1 = pro_c[1] + 2
    for item in range(m):
        if trainData[item][-1] == '1':
            if trainData[item][3] == 'fair':
                count_A += 1
            elif trainData[item][3] == 'excellent':
                count_B += 1
    p_faith_1.append(count_A / pro_c_1)
    p_faith_1.append(count_B / pro_c_1)
    print('p_faith_1:', p_faith_1)

    pro_test_0 = problity[0] * p_age_0[2] * p_money_0[1] * p_student_0[0] * p_faith_0[0]
    pro_test_1 = problity[1] * p_age_1[2] * p_money_1[1] * p_student_1[0] * p_faith_1[0]

    return pro_test_0, pro_test_1





trainData = LoadDataSet('traindata.txt')
# print(trainData)
testData = LoadDataSet('testdata.txt')
print(testData)
pro_test_0, pro_test_1 = naiveBayesian(trainData, testData)

print('pro_test_0:', pro_test_0)
print('pro_test_1:', pro_test_1)



