# 아래 정보로 시작:
# fruits = ["사과", "바나나", "포도"]
# prices = [1500, 800, 3000]   # 개당 가격(원)

# 할 일:
# 1) 함수 이름: total_price
#    매개변수: price, count
#    기능: price * count 계산해서 return

# 2) 사과 2개, 바나나 5개, 포도 1개를 각각 샀을 때
#    각각 얼마인지 total_price 함수를 이용해서 계산하고
#    print()로 각각 출력해봐.
#    (예: "사과 2개 가격: ???" 이런 식으로)

fruits = ["사과", "바나나","포도"]
prices = [1500, 800, 3000]

def total_price(price, count):
    result = price * count
    return result

apple_price = total_price(1500, 2)
print(apple_price)
