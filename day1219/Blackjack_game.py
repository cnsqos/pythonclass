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

        if player_score == 21:
            time.sleep(1)
            print("\n🎉 블랙잭! 즉시 승리!!")
            return "blackjack"

        print(f"\n플레이어 점수: {player_score}")

        if player_score > 21:
            time.sleep(1)
            print(f"컴퓨터 점수: {calculate_score(computer_hand)}")
            print("\n<플레이어 버스트ㅋㅋ 패배!!>")
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
    time.sleep(1)
    print("\n컴퓨터 턴!")
    show_hand("컴퓨터", computer_hand)
    while calculate_score(computer_hand) < 17:
        time.sleep(1)
        computer_hand.append(cpu_card(deck))
        show_hand("컴퓨터", computer_hand)

    computer_score = calculate_score(computer_hand)
    print(f"\n컴퓨터 점수: {computer_score}")

    # ===== 승패 판정 =====
    player_score = calculate_score(player_hand)
    if computer_score > 21:
        print("\n<컴퓨터 버스트@@ 플레이어 승리^^!>")
        return "win"
    elif player_score > computer_score:
        print("\n<플레이어 승리^^>")
        return "win"
    elif player_score < computer_score:
        print("\n<플레이어 패배ㅠㅠ>")
        return "lose"
    else:
        print("\n<무승부>")
        return "draw"

# ===== 메인 루프 =====
def main_game():
    while True:  # 전체 게임 재시작 루프
        player_balance = 100
        computer_balance = 100
        win_streak = 0
        show_rules = True

        while player_balance > 0 and computer_balance > 0:
            time.sleep(1)

            if show_rules:
                print("\n===== 블랙잭 게임 시작! =====")
                print("규칙 안내:")
                print("1. 목표 점수는 21점을 넘지 않으면서 최대한 21에 가까운 점수입니다.")
                print("2. J, Q, K는 10점, A는 1점 또는 11점으로 계산됩니다.")
                print("3. 플레이어는 hit(1)으로 카드를 더 뽑거나 stay(2)로 턴을 종료할 수 있습니다.")
                print("4. 컴퓨터는 17점 이상이 될 때까지 자동으로 카드를 뽑습니다.")
                print("5. 배팅 금액을 입력하고 승패에 따라 코인이 증감합니다.")
                print("=============================================================\n")
                show_rules = False

            min_bet = min(10, player_balance)
            print(f"\n플레이어 보유 코인: {player_balance}")
            print(f"컴퓨터 보유 코인: {computer_balance}")

            # ===== 플레이어 배팅 =====
            if player_balance <= 10:
                player_bet = player_balance
                print(f"\n💥 플레이어 코인이 {player_balance}개뿐이라 자동 올인합니다! 💥")
            else:
                while True:
                    try:
                        player_bet = float(input("\n얼마를 베팅하시겠습니까? "))
                        if min_bet <= player_bet <= player_balance:
                            if player_bet == player_balance:
                                print(f"\n💥 플레이어 올인! 이번 판에 모든 코인 걸기! 💥")
                            break
                        else:
                            print(f"{min_bet} 이상 {player_balance} 이하로 입력하세요.")
                    except:
                        print("숫자만 입력하세요.")

            # ===== 컴퓨터 베팅 AI =====
            if computer_balance <= 10:
                computer_bet = computer_balance
                print(f"\n컴퓨터 코인이 {computer_balance}개뿐이라 자동 올인합니다!")
            else:
                if win_streak >= 2:
                    computer_bet = min(computer_balance, random.randint(30, 70))
                    print(f"\n⚡ 플레이어 연승 감지! 컴퓨터 공격적 베팅 ⚡")
                else:
                    if computer_balance > player_balance:
                        computer_bet = min(computer_balance, random.randint(20, 50))
                    else:
                        computer_bet = min(computer_balance, random.randint(10, 30))
            print(f"\n컴퓨터가 {computer_bet} 코인을 베팅했습니다.")
            time.sleep(1)

            player_all_in = (player_bet == player_balance)
            computer_all_in = (computer_bet == computer_balance)

            # ===== 게임 시작 =====
            result = play_blackjack()

            # ===== 결과 반영 =====
            streak_bonus = 0
            blackjack_bonus = 0

            if result == "blackjack":
                blackjack_bonus = player_bet * 1.0
                player_balance += player_bet + computer_bet + blackjack_bonus
                computer_balance -= computer_bet
                win_streak += 1
                print(f"\n🂡 블랙잭 보너스 +{blackjack_bonus} 코인!")
            elif result == "win":
                bonus = player_bet * 0.5 if player_all_in else 0
                if player_all_in:
                    print(f"\n🔥 올인 승리 보너스 +{bonus} 코인!")
                player_balance += player_bet + computer_bet + bonus
                computer_balance -= computer_bet + (player_bet / 2)
                win_streak += 1
            elif result == "lose":
                bonus = computer_bet * 0.5 if computer_all_in else 0
                if computer_all_in:
                    print(f"\n💀 컴퓨터 올인 승리 보너스 +{bonus} 코인!")
                player_balance -= player_bet + (computer_bet / 2)
                computer_balance += computer_bet + player_bet + bonus
                win_streak = 0
            else:
                win_streak = 0

            # ===== 연승 보너스 =====
            if win_streak >= 2:
                streak_bonus = win_streak * 10
                if win_streak >= 3:
                    streak_bonus *= 2
                player_balance += streak_bonus
                print(f"🔥 연승 보너스 +{streak_bonus} 코인! ({win_streak}연승)")

            player_balance = max(0, player_balance)
            computer_balance = max(0, computer_balance)

            print(f"\n**현재 코인** \n[플레이어: {player_balance}/ 컴퓨터: {computer_balance}]")

            # ===== 종료 조건 =====
            if player_balance <= 0:
                print("\n<플레이어 코인 소진! 게임 종료>")
                break
            if computer_balance <= 0:
                print("\n<컴퓨터 코인 소진! 플레이어 승리!>")
                break

            again = input("\n계속 진행 하시겠습니까? (yes : 1 /no : 2): ").strip().lower()
            if again != '1':
                print("게임 종료!")
                break

        # ===== 재시작 여부 =====
        restart = input("\n재시작하시겠습니까? (yes:1 / no:2): ").strip()
        if restart != '1':
            print("게임을 종료합니다.")
            break
        else:
            time.sleep(1)
            print("\n===== 테이블을 청소하는중.. =====\n")
            time.sleep(1)
            print("\n===== 코인을 분배하는중.. =====\n")
            time.sleep(1)
            print("\n===== 카드를 섞는중.. =====\n")
            time.sleep(1)
            print("\n===== 준비 완료 =====\n")
            time.sleep(1)

if __name__ == "__main__":
    main_game()