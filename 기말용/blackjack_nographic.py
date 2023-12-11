import random




### (TASK1) 2~10,"Jack","Queen","King","Ace"를 하나의 리스트 (FACES) 로 만드시오
FACES = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
SUITS = [ "Clubs", "Diamonds", "Hearts", "Spades" ]







### (TASK2) :Card 클래스를 생성하시오 (생성자 부분을 작성하시오) (Card 객체가 그 속성으로 face와 suit를 갖도록)
### 예시 card1=Card("Jack","Diamonds") 일 때, card1.face이 "Jack"이고 card1.suit이 "Diamonds"가 되도록
class Card():
  def __init__(self,face,suit):
    self.face=face
    self.suit=suit

  def __str__(self):
    article = "a "
    if self.face in [8, "Ace"]:
      article = "an "
    return article + str(self.face) + " of " + self.suit

  def value(self):
    if type(self.face) == int:
      return self.face
    if self.face == "Ace":
      return 11
    return 10

### (TASK3) Deck 클래스를 생성하시오 (생성자 부분을 작성하시오) 
### Deck 객체는 모든 종류의 Card 객체를 포함하는 리스트를 cards 속성으로가져야 함
class Deck():

  def __init__(self):
    Data=[]
    for i in SUITS:
      for j in FACES:
          Data.append(Card(j,i))
    self.cards=Data
    random.shuffle(self.cards)  # 덱을 생성하면서 섞는 함수

  def draw(self): # 덱에서 카드를 한장 뽑는 함수
    return self.cards.pop()







### (TASK4) hand가 특정 카드 객체들의 리스트일 때, 그 모든 값을 합해서 반환하는 함수를 작성하시오 
### 예시 
# card1=Card(3,"Diamonds")
# card2=Card(5,"Spades")
# card3=Card("ACE","Hearts")
# hand=[card1, card2, card3]
# sum=hand_value(hand) 
# print(sum) --> 19
def hand_value(hand):
    sum=0
    for i in hand:
      sum+=i.value()
    return sum

def ask_yesno(prompt):
  while True :
    user_input = input(prompt)
    if user_input == "y" :
      return True
    elif user_input == "n" :
      return False
    else :
      print("I beg your pardon!")
      
def blackjack():
  deck = Deck()
  dealer = []
  player = []
  
  
  data1=deck.draw()
  player.append(data1)
  print(data1)
  print("You are dealt {}".format(data1))
  
  data2=deck.draw()
  dealer.append(data2)
  print("Dealer is dealt a hidden card")
  
  data3=deck.draw()
  player.append(data3)
  print("You are dealt {}".format(data3))
  
  data4=deck.draw()
  dealer.append(data4)
  print("Dealer is dealt {}".format(data4))
  
  sum=hand_value(player)
  print("Your total is {}".format(sum))
   
  ### (TASK5) 처음에 카드 받는 단계
  ### palyer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 (예시: "You are dealt a 6 of hearts")
  ### 그다음으로 카드를 뽑아서 dealer 리스트에 추가하시오. 다만 hidden 카드이므로 딜러가 히든 카드를 뽑았다고 프린트하시오 ("Dealer is dealt a hidden card")
  ### 그 다음은 다시 palyer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 ("You are dealt a 3 of Spades")
  ### 그 다음은 dealer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 ("Dealer is dealt a 3 of spades")
  ### 마지막으로 플레이어의 2장의 카드의 합을 프린트하시오 ("Your total is 9")
  
  while(sum<21):
    if ask_yesno("Would you like another card? (y/n)"):
      data5=deck.draw()
      player.append(data5)
      print("You are dealt {}".format(data5))
      sum=hand_value(player)
      print("Your total is {}".format(sum))
    else:
      print("The dealers's hidden card was {}".format(data2))
      break
  
  
  ### (TASK6) 플레이어가 이후에 카드를 받는 단계
  ### while문을 활용하여여 palyer 리스트 카드들의 value의 합이 21보다 작다면 새로운 카드를 뽑을지 물어보고 ("Would you like another card? (y/n) ")
  ### 뽑는다면,deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 (예시: "You are dealt an Ace of Clubs")
  ### 플레이어의 카드의 합을 프린트하시오 ("Your total is 19")
  ### 그렇지 않다면 이제 dealer의 hidden card가 어떤 카드인지 프린트하세요. ("The dealers's hidden card was a 10 of spades")
  
  
  if(sum>21):
    print("You Went over 21! You lost!")
    return -1
  
  delaerSum=hand_value(dealer)
  if delaerSum<=17:
    data6=deck.draw()
    dealer.append(data6)
    print("Dealer is dealt {}".format(data6))
    delaerSum=hand_value(dealer)
    print("The dealer's total is {}".format(delaerSum))
  ### (TASK7) 21을 넘는지 확인하고, 딜러가 카드를 받는 단계
  ### player 리스트안의 카드들의 합이 21을 넘는지 확인하고 넘었다면 "You went over 21! You lost!"를 프린트하고 -1을 반환하여 함수를 종료합니다.
  ### dealer 리스트 카드들의 합이 17을 넘지 않는다면 계속해서 카드를 추가하고 어떤 카드를 받았는지 출력하세요. ("Dealer is dealt a 5 of spades")
  ### 최종적으로 dealer 리스트 카드 합의 값을 프린트하세요. ("The dealer's total is 18")
  
  print("Your total is {}".format(sum))
  print("The dealer's total is {}".format(delaerSum))
  if delaerSum>21:
    print("Dealer went over 21! You win!")
    return 1
  if sum>delaerSum:
    print("You win!")
    return 1
  elif sum<delaerSum:
    print("You lose!")
    return -1
  else:
    print("You have a tie!")
    return 0
  ### (Task8) 승부를 결정 짓는 단계
  ### 먼저 player 리스트 카드의 합을 프린트하세요. ("Your total is 20") 
  ### dealer 리스트 카드의 합을 프린트하세요. ("The dealer's total is 18")
  ### dealer 리스트 카드 합이 21을 넘겼다면 , ("Dealer went over 21! You win!")을 출력하고 +1을 반환하여 함수를 종료하세요. 
  ### 마지막으로, player 리스트 카드 합이 더 크다면/적다면/동일하다면 ("You win!"/"You lose!"/"You have a tie!")를 프린트하고  각각 +1/-1/0을 반환하여 함수를 종료하세요.
  
  
   


def game_loop():
  print("Welcome to Blackjack!")   
  while True:
    blackjack()    
    if not ask_yesno("Play another round? (y/n) "):
      break    

game_loop()
