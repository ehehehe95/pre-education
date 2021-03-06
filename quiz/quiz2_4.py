'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''
class Card:

    def __init__(self):
        self.balance=0

    def charge(self,amount):
        self.balance += amount
        self.print()

    def consume(self,amount,place):
        if place=="영화관":
            amount=amount*0.8
        if amount > self.balance :
            print("잔액이 부족합니다.")
            return
        self.balance -= amount
        print("{}에서 {}원 사용했습니다".format(place, amount))

    def print(self):
        print("잔액이 %d원 입니다" % self.balance)

class Multi_card(Card):
    def consume(self,amount,place):
        if place=="영화관":
            amount=amount*0.8
        elif place=='마트' or place=='교통':
            amount=amount*0.9
        if amount > self.balance :
            print("잔액이 부족합니다.")
            return
        self.balance -= amount
        print("{}에서 {}원 사용했습니다".format(place, amount))

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

