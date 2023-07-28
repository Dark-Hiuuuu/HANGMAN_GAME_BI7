import os
import pygame
import random
import time
from word_guess import *
from ctypes import windll

# ------------------------- Function -------------------------
def check_win():
    for letter in word_guess:
        if letter not in guessed and letter not in hidden_letters:
            return False
    return True

# hàm kiểm tra thua 
def check_lose():
    return wrong_guesses_parts >= len(image_list)

# hàm reset game
def reset_game():
    global word_guess, guessed, hidden_letters, random_positions, wrong_guesses_parts, win_streak, lose_streak
    word_guess = choose_word()
    guessed = []
    hidden_letters = list("-" * len(word_guess))
    random_positions = random.sample(
        range(len(word_guess)), 2
    )  # Lấy ngẫu nhiên 2 vị trí trong từ cần đoán
    for pos in random_positions:
        hidden_letters[pos] = word_guess[pos]
    reset_buttons()
    wrong_guesses_parts = -1

# hàm chọn từ cần đoán từ list từ có sẵn
def choose_word():
    return random.choice(word_list)

# hàm dùng để hiển thị kí tự chữ cái khi ấn vào chữ cái từ các nút trong màn hình
def draw():
    display_word = ""
    for i in range(len(word_guess)):
        if word_guess[i] in guessed or i in random_positions:
            display_word += word_guess[i] + " "
        else:
            display_word += hidden_letters[i] + " "
    text = word_guess_font.render(display_word, 1, BLACK)
    screen.blit(text, (50, 600))

# hàm reset nút khi chuyển sang từ đoán mới 
def reset_buttons():
    global buttons
    buttons = []
    for letter in range(26):
        row = letter // 5
        col = letter % 5
        button_x = start_x + (button_width + button_padding_x) * col
        button_y = start_y + (button_height + button_padding_y) * row
        letter_button = pygame.Rect(button_x, button_y, button_width, button_height)
        buttons.append(letter_button)
def reset_timer():
    global start_time
    start_time = pygame.time.get_ticks()

# ------------------------ End Function -----------------------

# Add these variables at the beginning of the script
timer_duration = 120000
start_time = pygame.time.get_ticks()
windll.shcore.SetProcessDpiAwareness(1)
pygame.init()

width = 1000
height = 850
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Hangman game!") 

# load icon và hình ảnh itb chính trong game 
icon_window = pygame.image.load("images\LogoITB.png")
image_main_itb = pygame.image.load("images\MainScreen\ITB.png")
itb_main_logo = pygame.image.load('images\PlaygameScreen\ITB.png')

# set icon lên màn hình 
pygame.display.set_icon(icon_window)
background_color = (255, 255, 255)
BLACK = (0, 0, 0)

# list từ cần đoán
word_list = word_guess_list

word_guess = choose_word() #để chọn một từ ngẫu nhiên từ danh sách word_list và gán giá trị từ đó cho biến word_guess. Biến word_guess sẽ chứa từ cần đoán trong trò chơi
guessed = []    #Trong danh sách này, các chữ cái mà người chơi đã đoán đúng sẽ được thêm vào.
word_guess_font = pygame.font.SysFont("Italic", 50) # cỡ chữ và phông chữ của từ cần đoán 
# thêm ảnh nhân vật vô list image_list
image_list = []
image_folder = r"images\PlaygameScreen\Man"
for filename in os.listdir(image_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)
        image_surface = pygame.image.load(image_path)
        image_list.append(image_surface)


# set vị trí cho các phần thân của nhân vật 
image_positions = [
    (5, 513),  # chân trụ
    (69.17, 165),  # trụ
    (233.21, 391.46),  # tay trái
    (325, 391.46),  # tay phải
    (254.49, 391.46),  # thân
    (254.48, 424),  # chân
    (235.52, 304.05),  # đầu
    (276.94, 189.76),  # dây treo
]


#  vẽ các phần hình người dựa trên số lần đoán sai 
wrong_guesses_parts = -1
letter_images = []
for letter in range(26):
    letter_image = pygame.image.load(
        f"images\PlaygameScreen\Alphabet\{chr(ord('A') + letter)}.png"
    )
    letter_images.append(letter_image)

# tính toán vị trí cho nút bấm
button_width = 60
button_height = 60
button_padding_x = int(3.5 * (width / 100))
button_padding_y = int(3.5 * (height / 100))
start_x = width - ((button_width + button_padding_x) * 5) - 20
start_y = (height - (button_height + button_padding_y) * 5) // 2

# thêm chức năng cho nút 
buttons = []
for letter in range(26):
    row = letter // 5
    col = letter % 5
    button_x = start_x + (button_width + button_padding_x) * col
    button_y = start_y + (button_height + button_padding_y) * row
    letter_button = pygame.Rect(button_x, button_y, button_width, button_height)
    buttons.append(letter_button)

# chọn ra bất kì 2 kí tự trong từ để hiện thị cho người chơi
hidden_letters = list("-" * len(word_guess))
random_positions = random.sample(range(len(word_guess)), 2)  

# Lấy ngẫu nhiên 2 vị trí trong từ cần đoán
for pos in random_positions:
    hidden_letters[pos] = word_guess[pos]

# biến kiểm tra thắng và thua
win_streak = 0
lose_streak = 0

# biến dùng để cập nhật số lần thắng số lần thua lên màn hình
win_guess = 0 
lose_guess = 0 

# hàm kiểm tra thắng 
running = True
mouse_clicked = False

font_timer = pygame.font.SysFont("Italic", 65)


while running:
    draw()
    screen.blit(image_main_itb, (297, 53))   
    screen.fill(background_color)
    screen.blit(image_main_itb,(515,40))
    
    # vẽ lên màn hình số từ đoán đúng x``
    correct_text = word_guess_font.render(f"CORRECT: {win_guess}", 20, (0, 0, 0))
    screen.blit(correct_text, (150, 800))
    # vẽ lên màn hình số từ đoán sai
    wrong_text = word_guess_font.render(f"INCORRECT: {lose_guess}", 20, (0, 0, 0))
    screen.blit(wrong_text, (550, 800))

    display_word = ""  # Tạo biến display_word để hiển thị từ
    for i in range(len(word_guess)):
        if word_guess[i] in guessed or i in random_positions:
            display_word += word_guess[i] + " "
        else:
            display_word += hidden_letters[i] + " "
    text = word_guess_font.render(display_word, 1, BLACK)
    screen.blit(text, (75, 600))
        # vẽ hình itb, và background lên màn hình  

    for i in range(wrong_guesses_parts +1):
        screen.blit(image_list[i], image_positions[i])
        
# vẽ bảng chữ cái lên màn hình 
    for letter in range(26):
        pygame.draw.rect(screen, (0, 0, 0), buttons[letter])
        if buttons[letter].width > 0 and buttons[letter].height > 0:
            screen.blit(letter_images[letter], buttons[letter].topleft)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_clicked = False
                mouse_pos = pygame.mouse.get_pos()
                for letter in range(26):
                    if (
                        buttons[letter].collidepoint(mouse_pos)
                        and buttons[letter].width > 0
                        and buttons[letter].height > 0
                    ):
                        buttons[letter] = pygame.Rect(0, 0, 0, 0)
                        guessed.append(chr(ord("A") + letter))
                        if chr(ord("A") + letter) in word_guess:
                            for i in range(len(word_guess)):
                                if word_guess[i] == chr(ord("A") + letter):
                                    hidden_letters[i] = chr(ord("A") + letter)
                            if check_win():
                                win_streak += 1
                                win_guess += 1
                                pygame.time.delay(1000)  # Chờ  giây
                                reset_game()
                                reset_timer()
                        else:
                            wrong_guesses_parts += 1
                            if wrong_guesses_parts == 7:
                                screen.blit(image_list[7], image_positions[7])
                                pygame.display.flip()
                                pygame.time.delay(1000)  # Chờ  giây
                                lose_streak += 1
                                lose_guess += 1
                                pygame.time.delay(1000)  # Chờ  giây
                                reset_game()
                                reset_timer()
    
    if win_streak == 5:
        win_img = pygame.image.load("images\Win.png")
        screen.blit(win_img, ((208, 255)))
        pygame.display.flip()
        break

    if lose_streak == 3:
        lose_img = pygame.image.load("images\Game-Over.png")
        screen.blit(lose_img, ((208, 255)))
        pygame.display.update()
        break

        # Check the elapsed time since the game started
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(timer_duration - elapsed_time, 0)  # Calculate the remaining time

    # Convert milliseconds to minutes and seconds
    minutes = remaining_time // 60000
    seconds = (remaining_time % 60000) // 1000

    # Format the timer text
    timer_text = f"Time: {minutes:02}:{seconds:02}"

    # Render the timer text
    timer_surface = font_timer.render(timer_text, True, BLACK)
    screen.blit(timer_surface, (100, 60))  # Adjust the position to your preference


    if elapsed_time >= timer_duration:
        reset_game()
        reset_timer()  # Reset the timer for the new word
        lose_streak += 1
        lose_guess += 1

    pygame.display.update()
pygame.time.delay(5000)
pygame.quit()