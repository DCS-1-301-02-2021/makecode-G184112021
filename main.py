scene.set_background_color(8)
spacePlane=sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . 1 . . . . . . . . . . .
    . . . . b b b f f f . . . . . .
    . . . c b b b b . . . . . . . .
    . . . c c b b b b . . . . . . .
    . 2 2 c b c b b b b . . 1 1 1 .
    2 4 4 c b b c b b b b b b b b f
    . 2 2 b b b b b b b b b b b . .
    . . . . b b b b b b . . . . . .
    . . . . b b b b b . . . . . . .
    . . . . b b b b . . . . . . . .
    . . . . b b b . . . . . . . . .
    . . . . b b f f f f . . . . . .
"""),SpriteKind.player)
info.set_life(3)
spacePlane.set_stay_in_screen(True)
controller.move_sprite(spacePlane, 200, 200)
def on_a_pressed():
    missile=sprites.create_projectile_from_sprite(
        img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            4 4 4 4 4 4 4 4 . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """),spacePlane, 200, 0)
controller.A.on_event(
    ControllerButtonEvent.PRESSED, on_a_pressed)
def on_update():
    body=sprites.create(assets.image("""body"""),
        SpriteKind.enemy)
    body.set_velocity(-100, randint(-30, 30))
    body.y=randint(0, scene.screen_height())
    body.left=scene.screen_width()
    body.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update)
def on_hit(sprite, othersprite):
    othersprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy,
    on_hit)
def on_crash(sprite, othersprite):
    othersprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy,
    on_crash)