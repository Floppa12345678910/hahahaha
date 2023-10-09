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
while 1:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
    elif i.type == pg.KEYDOWN:
      if i.key == pg.K_BACKSPACE:
        name = name[: -1]
      elif i.key == pg.K_RETURN:
          print(name)
      else:
        name += i.unicode
  win.fill((0,0,0))
  draw_text(win, 'vvedite imya', W//2,H//2)
  pg.display.update()
