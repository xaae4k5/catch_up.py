from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Подводные догонялки')
#задай фон сцены
background = transform.scale(image.load('sea.jpg'), (700,500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('scum.png'), (180,90))
sprite2 = transform.scale(image.load('fish.png'), (180,90))

clock = time.Clock()
FPS = 40

game = True
x1, y1 = 100, 100
x2, y2 = 300, 300

while game:

    #проверка нажатия на кнопку выход
    for e in event.get():
        if e.type == QUIT:
            game = False

    key_pressed = key.get_pressed()
    if key_pressed[K_UP] and y1>5:
        y1 -= 5
    if key_pressed[K_DOWN] and y1<395:
        y1 += 5
    if key_pressed[K_LEFT] and x1>0:
        x1 -= 5
    if key_pressed[K_RIGHT] and x1<600:
        x1 += 5

    if key_pressed[K_w] and y2>5:
        y2 -= 5
    if key_pressed[K_s] and y2<395:
        y2 += 5
    if key_pressed[K_a] and x2>0:
        x2 -= 5
    if key_pressed[K_d] and x2<600:
        x2 += 5
    #отображение фона
    window.blit(background, (0,0))
    window.blit(sprite1, (x1,y1))
    window.blit(sprite2, (x2,y2))

    #обновление окна игры
    display.update()
    clock.tick(FPS)



#обработай событие «клик по кнопке "Закрыть окно"»