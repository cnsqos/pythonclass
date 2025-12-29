import pygame, random, time, sys

pygame.init()
pygame.mixer.init()

# ===== 기본 설정 =====
WIDTH, HEIGHT = 1024, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎴 화려한 블랙잭 🎴")
CLOCK = pygame.time.Clock()
FPS = 60

# 색상
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,150,0)
RED   = (200,0,0)
YELLOW= (255,255,0)
BLUE  = (0,0,255)

# 폰트
FONT = pygame.font.SysFont('arial', 24)
BIG_FONT = pygame.font.SysFont('arial', 48)

# 이미지 & 사운드 로딩
CARD_BACK = pygame.image.load('images/back.png').convert_alpha()
SOUND_COIN = pygame.mixer.Sound('sounds/coin.wav')
SOUND_WIN  = pygame.mixer.Sound('sounds/win.wav')
SOUND_LOSE = pygame.mixer.Sound('sounds/lose.wav')

SUITS = ['S','D','H','C']
RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

CARD_IMAGES = {}
for suit in SUITS:
    for rank in RANKS:
        path = f'images/{rank}{suit}.png'
        CARD_IMAGES[f'{rank}{suit}'] = pygame.image.load(path).convert_alpha()

# ===== 버튼 클래스 =====
class Button:
    def __init__(self, x, y, w, h, text, color, hover_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.clicked = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(SCREEN, self.hover_color, self.rect)
            if clicked and not self.clicked:
                self.clicked = True
                return True
        else:
            pygame.draw.rect(SCREEN, self.color, self.rect)
        self.clicked = False
        text_surf = FONT.render(self.text, True, WHITE)
        SCREEN.blit(text_surf, (self.rect.x + self.rect.w//2 - text_surf.get_width()//2,
                                self.rect.y + self.rect.h//2 - text_surf.get_height()//2))
        return False

# ===== 카드 & 게임 로직 =====
def create_deck():
    deck = [f'{rank}{suit}' for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        rank = card[:-1]  # 마지막 글자는 무늬
        if rank in ['J','Q','K']:
            score += 10
        elif rank=='A':
            score += 11
            ace_count +=1
        else:
            score += int(rank)
    while score>21 and ace_count:
        score -=10
        ace_count -=1
    return score

# ===== 카드 화면 표시 =====
def draw_hand(hand, x, y, hidden=False):
    for i, card in enumerate(hand):
        if hidden and i==0:
            SCREEN.blit(CARD_BACK, (x+i*80, y))
        else:
            SCREEN.blit(CARD_IMAGES[card], (x+i*80, y))

# ===== 메시지 =====
def show_message(msg, color=YELLOW, y=250):
    text = BIG_FONT.render(msg, True, color)
    SCREEN.blit(text, (WIDTH//2 - text.get_width()//2, y))
    pygame.display.update()
    pygame.time.delay(1000)

# ===== 블랙잭 게임 진행 =====
def play_blackjack(player_balance, computer_balance):
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    player_bet = 10
    # 자동 배팅 (원하면 UI로 선택 가능)
    player_all_in = (player_bet==player_balance)
    computer_all_in = (player_bet==computer_balance)

    running = True
    player_turn = True
    hit_btn = Button(50,500,120,50,'HIT',BLUE,(0,100,255))
    stay_btn = Button(200,500,120,50,'STAY',RED,(255,50,50))
    while running:
        SCREEN.fill(GREEN)
        draw_hand(computer_hand, 150,50, hidden=player_turn)
        draw_hand(player_hand, 150,350)
        # 코인/배팅 표시
        SCREEN.blit(FONT.render(f'플레이어: {player_balance}  컴퓨터: {computer_balance}',True,WHITE),(600,10))
        SCREEN.blit(FONT.render(f'베팅: {player_bet}',True,WHITE),(600,40))

        # 버튼 클릭 처리
        if player_turn:
            if hit_btn.draw():
                player_hand.append(deck.pop())
                SOUND_COIN.play()
            if stay_btn.draw():
                player_turn=False
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not player_turn:
            break
        CLOCK.tick(FPS)

    # ===== 딜러 턴 =====
    while calculate_score(computer_hand)<17:
        computer_hand.append(deck.pop())
        SOUND_COIN.play()
        SCREEN.fill(GREEN)
        draw_hand(computer_hand,150,50)
        draw_hand(player_hand,150,350)
        pygame.display.update()
        pygame.time.delay(600)

    # ===== 승패 판단 =====
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    SCREEN.fill(GREEN)
    draw_hand(computer_hand,150,50)
    draw_hand(player_hand,150,350)
    pygame.display.update()
    pygame.time.delay(500)

    if player_score>21:
        show_message("버스트! 패배",RED)
        SOUND_LOSE.play()
        player_balance -= player_bet
        computer_balance += player_bet
    elif computer_score>21 or player_score>computer_score:
        show_message("승리!",YELLOW)
        SOUND_WIN.play()
        player_balance += player_bet
        computer_balance -= player_bet
    elif player_score<computer_score:
        show_message("패배...",RED)
        SOUND_LOSE.play()
        player_balance -= player_bet
        computer_balance += player_bet
    else:
        show_message("무승부",WHITE)

    pygame.time.delay(1000)
    return player_balance, computer_balance

# ===== 메인 루프 =====
def main():
    player_balance = 100
    computer_balance = 100

    while True:
        player_balance, computer_balance = play_blackjack(player_balance, computer_balance)

        # 종료 조건
        if player_balance<=0 or computer_balance<=0:
            SCREEN.fill(GREEN)
            if player_balance<=0:
                show_message("플레이어 코인 소진! 게임 종료",RED)
            else:
                show_message("컴퓨터 코인 소진! 승리!",YELLOW)
            pygame.time.delay(1500)

            # 재시작 선택
            SCREEN.fill(GREEN)
            show_message("재시작? HIT:1 / ESC: 종료",WHITE, y=250)
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_1:
                            player_balance=100
                            computer_balance=100
                            waiting=False
                        elif event.key==pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

if __name__=="__main__":
    main()