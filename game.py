import pygame as pg

pg.init()
font_name = pg.font.match_font('ariel')
size = 18
W,H =600,600
win = pg.display.set_mode((W, H)) # размер и создание игрогого окна
name = ""
def draw_text(surf, text , x, y, size = size,color=(255,0,255)):
  font = pg.font.Font(font_name, size)
  text_surfase = font.render(text,True,color)
  text_rect = text_surfase.get_rect()
  text_rect.midtop = (x,y)
  surf.blit(text_surfase, text_rect)
def user_name(sufr,text,x,y,size):
  font = pg.font.Font(font_name, size)
  text_surfase = font.render(text,True,color=(255,0,255))
  text_rect = text_surfase.get_rect()
  text_rect.midtop = (x,y)
  surf.blit(text_surfase, text_rect)
while main_loop:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
    elif i.type == pg.KEYDOWN:
      if i.key == pg.K_BACKSPACE:
        name = name[: -1]
      elif i.key == pg.K_RETURN:
          main_loop = False
      else:
        name += i.unicode
  win.fill((255,255,255))
  draw_text(win, 'vvedite imya', W//2,H//2)
  draw_text(win,name, W//2, H//2 * 20)
  pg.display.update()

while 1:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
  win y in range(0,H, 10)
    for x in range(0, W, 30):
      pg.draw.line(win, (0,0,0), (0, y), (W, y))
      pg.draw.line(win, (0,0,0), (x, 0), (x, H))

    pg.display.update()




