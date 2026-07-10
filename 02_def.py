# 함수 이름: bmi_check
# 매개변수: weight (몸무게, kg), height (키, m)
# 할 일: BMI를 계산해서 return
# 공식: BMI = 몸무게 / (키 * 키)

weight = 80
height = 1.8
def bmi_check(weight, height):
    BMI = weight / (height*height)
    return BMI
print(bmi_check(weight, height))
