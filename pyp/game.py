import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 800, 400

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифти
FONT = pygame.font.Font(None, 36)

# Фреймрейт
FPS = 60

# Клас динозавра
class Dino:
    def __init__(self): 
        self.image = pygame.image.load("dino.png").convert_alpha()  # Завантаження та обробка зображення
        self.image = pygame.transform.scale(self.image, (50, 50))  # Масштабування зображення
        self.x, self.y = 100, HEIGHT - 100  # Початкова позиція
        self.is_jumping = False  # Чи в стрибку
        self.jump_speed = -15  # Швидкість стрибка
        self.gravity = 1  # Прискорення від гравітації
        self.velocity = 0  # Поточна швидкість

    def update(self):  # Оновлення стану динозавра
        if self.is_jumping:
            self.velocity += self.gravity  # Додавання гравітації до швидкості
            self.y += self.velocity  # Оновлення позиції
            if self.y >= HEIGHT - 100:  # Перевірка досягнення землі
                self.y = HEIGHT - 100  # Фіксація на землі
                self.is_jumping = False  # Завершення стрибка
                self.velocity = 0  # Скидання швидкості

    def jump(self):  # Стрибок
        if not self.is_jumping:  # Якщо не в стрибку
            self.is_jumping = True  # Включити стрибок
            self.velocity = self.jump_speed  # Початкова швидкість стрибка

    def draw(self, screen):  # Малювання динозавра
        screen.blit(self.image, (self.x, self.y))  # Відображення на екрані



# Клас перешкоди
class Obstacle:
    def __init__(self): 
        self.image = pygame.image.load("cactus.png").convert_alpha()  # Завантаження зображення
        self.image = pygame.transform.scale(self.image, (40, 60))  # Масштабування зображення
        self.x = WIDTH  # Початкова позиція по осі X
        self.y = HEIGHT - 100  # Позиція по осі Y
        self.speed = 7  # Швидкість руху перешкоди

    def update(self):  # Оновлення стану перешкоди
        self.x -= self.speed  # Рух вліво
        if self.x < -50:  # Переміщення за межі екрана
            self.x = WIDTH + random.randint(100, 300)  # Перезавантаження позиції

    def draw(self, screen):  # Малювання перешкоди
        screen.blit(self.image, (self.x, self.y))  # Відображення на екрані

    def collide(self, dino):  # Перевірка зіткнення
        dino_rect = pygame.Rect(dino.x, dino.y, 50, 50)  # Прямокутник динозавра
        obstacle_rect = pygame.Rect(self.x, self.y, 40, 60)  # Прямокутник перешкоди
        return dino_rect.colliderect(obstacle_rect)  # Перевірка перетину



# Клас гри
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chrome Dinosaur")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dino = Dino()
        self.obstacles = [Obstacle()]
        self.score = 0
        self.lives = 3
        self.start_ticks = pygame.time.get_ticks()  # Час початку гри

    def reset(self):
        self.dino = Dino()
        self.obstacles = [Obstacle()]
        self.score = 0
        self.lives = 3
        self.start_ticks = pygame.time.get_ticks()

    def start_screen(self):
        self.screen.fill(WHITE)
        title_text = FONT.render("Chrome Dinosaur", True, BLACK)
        start_text = FONT.render("Press SPACE to Start", True, BLACK)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))
        self.screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 10))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def game_over_screen(self):
        self.screen.fill(WHITE)
        game_over_text = FONT.render("Game Over!", True, BLACK)
        restart_text = FONT.render("Press SPACE to Restart", True, BLACK)
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000  # Час в секундах
        time_survived_text = FONT.render(f"Time Survived: {elapsed_time}s", True, BLACK)
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))
        self.screen.blit(time_survived_text, (WIDTH // 2 - time_survived_text.get_width() // 2, HEIGHT // 2 + 50))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.reset()
                    waiting = False

    def draw_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000  # Час в секундах
        timer_text = FONT.render(f"Time: {elapsed_time}s", True, BLACK)
        self.screen.blit(timer_text, (10, 10))

    def run(self):
        while self.running:
            self.screen.fill(WHITE)

            # Обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.dino.jump()

            # Оновлення
            self.dino.update()
            for obstacle in self.obstacles:
                obstacle.update()
                if obstacle.collide(self.dino):
                    self.lives -= 1
                    obstacle.x = -100
                    if self.lives <= 0:
                        self.game_over_screen()

            # Малювання динозавра
            self.dino.draw(self.screen)
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)


            # Малюємо таймер і лічильник життів
            self.draw_timer()

            # Лічильник життів
            lives_text = FONT.render(f"Lives: {self.lives}", True, BLACK)
            self.screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

            # Оновлення екрану
            pygame.display.update()

            # Обмеження фреймрейту
            self.clock.tick(FPS)

# Запуск гри
game = Game()
game.start_screen()
game.run()
pygame.quit()
