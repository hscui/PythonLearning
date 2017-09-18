# coding=utf-8

h = input('请输入您的身高（m）：')
height = float(h)
w = input('请输入您的体重（kg）：')
weight = float(w)
bmi = weight / (height ** 2)
if weight<30:
    print('请输入成年人的体重！')
elif bmi < 18.5:
    print('您的体重过轻！')
elif bmi >= 18.5 and bmi < 25:
    print("您的体重正常！")
elif bmi >= 25 and bmi < 28:
    print("您的体重有点过重了！")
elif bmi >= 28 and bmi < 32:
    print("您过于肥胖了，需要减点肥了！")
else:
    print("您是严重肥胖，需要减肥了！！")
