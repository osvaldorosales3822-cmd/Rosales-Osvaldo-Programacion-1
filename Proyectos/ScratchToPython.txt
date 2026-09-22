#Movimiento jugador
player =  ("forgetmenot")  
player.x = 100
player.y = 100
while True:
    import keyboard # pyright: ignore[reportMissingModuleSource]
    if keyboard.press("up"):
        player.x = player.x + 5
        if keyboard.press("left"):
            player.x = player.x - 5
            if keyboard.press("right"):
                player.y = player.y + 5
                if keyboard.press("down"):
                    player.y = player.y - 5
#Manejo de sprite     

while true:
    import keyboard
    import turtle
    if player: keyboard.press("up")
    player.shape("disfraz1.gif")
    time.sleep(1)
    if player: keyboard.press("down")
    player.shape("disfraz2.gif")
    time.sleep(1)
    if player: keyboard.press("left")
    player.shape("disfraz3.gif")
    time.sleep(1)
    if player: keyboard.press("right")
    player.shape("disfraz4.gif")
    time.sleep(1)

def limitar_posicion(sprite):
    while True:
        if sprite.x > 230:
            sprite.x = 230
            
        if sprite.x < -230:
            sprite.x = -230
            
        if sprite.y > 170:
            sprite.y = 170
            
        if sprite.y < -170:
            sprite.y = -170