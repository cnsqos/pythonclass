import random
import time


SUITS = ['♠', '♦', '♥', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def create_deck():
    deck = [[suit, rank] for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def cpu_card(deck):
    return deck.pop()



def calculate_score(hand):
    score = 0
    ace_count = 0
    for suit, rank in hand:
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(rank)
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score


# ===== 카드 출력 =====
def format_hand(hand, hide_first=False):
    if hide_first:
        return "??, " + ", ".join([f"{suit}{rank}" for suit , rank in hand[1:]])
    else:
        return ", ".join([f"{suit}{rank}" for suit, rank in hand])

def show_hand(name, hand, hide_first=False):
    print(f"\n{name}: {format_hand(hand, hide_first)}")



def play_blackjack():
    deck = create_deck()
    player_hand = [cpu_card(deck), cpu_card(deck)]
    computer_hand = [cpu_card(deck), cpu_card(deck)]

    show_hand("플레이어", player_hand)
    show_hand("컴퓨터", computer_hand, hide_first=True)



    # ===== 플레이어 턴 =====
    while True:
        player_score = calculate_score(player_hand)
        print(f"\n플레이어 점수: {player_score}")

        if player_score > 21:
            time.sleep(1.2)
            print(f"컴퓨터 점수: {calculate_score(computer_hand)}")
            print("\n플레이어 버스트ㅋㅋ 패배!!")
            return "lose"

        choice = input("hit(1) / stay(2): ").strip()
        if choice == '1':
            player_hand.append(cpu_card(deck))
            show_hand("플레이어", player_hand)
        elif choice == '2':
            break
        else:
            print("1 또는 2만 입력하세요.")


    # ===== 컴퓨터 턴 =====
    time.sleep(1.2)
    print("\n컴퓨터 턴!")
    time.sleep(1.2)
    show_hand("컴퓨터", computer_hand)
    while calculate_score(computer_hand) < 17:
        time.sleep(1.2)  # 카드 뽑을 때 1.4초 지연
        computer_hand.append(cpu_card(deck))
        show_hand("컴퓨터", computer_hand)

    time.sleep(1.2)
    computer_score = calculate_score(computer_hand)
    print(f"\n컴퓨터 점수: {computer_score}")



    # ===== 승패 판정 =====
    time.sleep(1.2)
    player_score = calculate_score(player_hand)
    if computer_score > 21:
        time.sleep(1.2)
        print("\n컴퓨터 버스트ㅋㅋ 플레이어 승리^^!")
        return "win"
    elif player_score > computer_score:
        time.sleep(1.2)
        print("\n*플레이어 승리!")
        return "win"
    elif player_score < computer_score:
        time.sleep(1.2)
        print("\n*플레이어 패배!")
        return "lose"
    else:
        time.sleep(1.2)
        print("\n*무승부!")
        return "draw"
    

    # ===== 메인 루프: 플레이어/컴퓨터 배팅 + 재시작 =====
player_balance = 100
computer_balance = 100

while player_balance > 0 and computer_balance > 0:
    time.sleep(1.2)
    print(f"\n플레이어 보유 코인: {player_balance}")
    print(f"컴퓨터 보유 코인: {computer_balance}")

    # 플레이어 배팅 입력
    while True:
        try:
            time.sleep(1.2)
            player_bet = int(input("\n얼마를 베팅하시겠습니까? "))
            if 0 < player_bet <= player_balance:
                break
            else:
                print(f"1 이상 {player_balance} 이하로 입력하세요.")
        except:
            print("숫자만 입력하세요.")

    # 컴퓨터 배팅 
    time.sleep(1.2)  
    computer_bet = min(computer_balance, random.randint(1, 20))
    time.sleep(1.2)
    print(f"\n컴퓨터가 {computer_bet} 코인을 베팅했습니다.")
    time.sleep(1.2)

    # 게임 시작
    result = play_blackjack()


    # 배팅 결과 반영
    if result == "win":  
        player_balance += player_bet + computer_bet
        computer_balance -=computer_bet + (player_bet/2)
        time.sleep(1.2)
        print(f"\n<승리> : [플레이어 +{player_bet + computer_bet}/ 컴퓨터 -{computer_bet + (player_bet/2)}]")
    elif result == "lose":  
        player_balance -=player_bet + (computer_bet/2)
        computer_balance += computer_bet + player_bet
        time.sleep(1.2)
        print(f"\n<패배> : [플레이어 -{player_bet + (computer_bet/2)}/ 컴퓨터 +{computer_bet + player_bet}]")
    else: 
        time.sleep(1.2) 
        print("\n<무승부> 코인 변동 없음: ")

    time.sleep(1.2)
    print(f"\n**현재 코인** - [플레이어: {player_balance}/ 컴퓨터: {computer_balance}]")


    # 게임 종료 조건
    if player_balance <= 0:
        time.sleep(1.4)
        print("\n플레이어 코인 바닥! 게임 종료")
        break
    if computer_balance <= 0:
        time.sleep(1.4)
        print("\n컴퓨터 코인 바닥! 플레이어 승리!")
        break

    again = input("\n다시 하시겠습니까? (y/n): ").strip().lower()
    if again != 'y':
        print("게임 종료!")
        break

    