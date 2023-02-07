def calculate_bmi(height, weight):
    bmi = weight / (height/100)**2
    return bmi

height = float(input("請輸入您的身高(cm)："))
weight = float(input("請輸入您的體重(kg)："))
bmi = calculate_bmi(height, weight)

print("您的BMI值為：%.2f" % bmi)
