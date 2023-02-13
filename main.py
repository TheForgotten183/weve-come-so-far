@namespace
class SpriteKind:
    Banner = SpriteKind.create()
    GenderSelection = SpriteKind.create()
    Null = SpriteKind.create()
    Hitbox = SpriteKind.create()
    Interactive = SpriteKind.create()
    logo = SpriteKind.create()
    strongenemy = SpriteKind.create()
    strongenemy2 = SpriteKind.create()
@namespace
class StatusBarKind:
    EnemyHealth2 = StatusBarKind.create()

def on_on_overlap(sprite, otherSprite):
    global EnemyLimit
    if controller.A.is_pressed():
        otherSprite.ay = 0
        otherSprite.destroy(effects.spray, 100)
        EnemyLimit += 1
        music.knock.play()
        info.change_score_by(1)
sprites.on_overlap(SpriteKind.Hitbox, SpriteKind.enemy, on_on_overlap)

def CharacterSize():
    scaling.scale_to_pixels(Character,
        20,
        ScaleDirection.HORIZONTALLY,
        ScaleAnchor.MIDDLE)
    scaling.scale_to_pixels(Character, 24, ScaleDirection.VERTICALLY, ScaleAnchor.MIDDLE)
def StopLookingAtTheCode():
    global WarriorBanner, ArcherBanner, MonkBanner, WizardBanner
    WizardBanner.destroy()
    WarriorBanner.destroy()
    ArcherBanner.destroy()
    MonkBanner.destroy()
    WarriorBanner = sprites.create(assets.image("""
        WarriorBanner
    """), SpriteKind.Banner)
    WarriorBanner.set_position(82, 60)
    ArcherBanner = sprites.create(assets.image("""
        ArcherBanner
    """), SpriteKind.Banner)
    ArcherBanner.set_position(113, 60)
    MonkBanner = sprites.create(assets.image("""
        MonkBanner
    """), SpriteKind.Banner)
    MonkBanner.set_position(144, 60)
    WizardBanner = sprites.create(assets.image("""
        WizardBanner
    """), SpriteKind.player)
    WizardBanner.set_position(51, 60)

def on_b_pressed():
    global Screen, WarriorBanner, ArcherBanner, MonkBanner, WizardBanner, strayminer, canShoot, EnemyLimit
    if Screen == 2:
        scene.set_background_image(assets.image("""
            ClassSelect_Background
        """))
        Female.destroy()
        Male.destroy()
        Screen = 1
        Preview.destroy()
        WarriorBanner = sprites.create(assets.image("""
            WarriorBanner
        """), SpriteKind.Banner)
        WarriorBanner.set_position(82, 60)
        ArcherBanner = sprites.create(assets.image("""
            ArcherBanner
        """), SpriteKind.Banner)
        ArcherBanner.set_position(113, 60)
        MonkBanner = sprites.create(assets.image("""
            MonkBanner
        """), SpriteKind.Banner)
        MonkBanner.set_position(144, 60)
        WizardBanner = sprites.create(assets.image("""
            WizardBanner
        """), SpriteKind.player)
        WizardBanner.set_position(51, 60)
    elif Screen == -1:
        shoot()
    elif Screen == 0:
        shoot()
    elif Screen == 3:
        if canTalk == 1:
            if game.ask("Do you want to continue", "the campaign?"):
                NothingToSeeHere()
                scene.set_background_image(assets.image("""
                    Nighttime
                """))
                tiles.set_tilemap(tilemap("""
                    level3
                """))
                strayminer = sprites.create(assets.image("""
                    StrayMiner
                """), SpriteKind.Null)
                strayminer.set_position(1492, 473)
                Screen = 4
                TalkButton.destroy()
                canShoot = 1
                firstlevel()
            elif game.ask("Do you want to try", "endless mode?"):
                NothingToSeeHere()
                scene.set_background_image(assets.image("""
                    Sunset
                """))
                tiles.set_tilemap(tilemap("""
                    Campaign1
                """))
                Screen = -1
                TalkButton.destroy()
                EnemyLimit = 16
                Character.set_position(32, 208)
                makeHealth()
                canShoot = 1
                makeHitbox()
    elif Screen == 4:
        shoot()
        if canTalk == 1:
            if info.score() < 7:
                game.splash("Clear the other enemies,", "then we'll talk")
                Character.set_position(160, 472)
            else:
                if game.ask("Hi! Follow me to the", "caves, we're safer there!"):
                    dos()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def warriorpew():
    global PewPew
    if LastButtonPressed == 1:
        PewPew = sprites.create(assets.image("""
            WarriorAxeR
        """), SpriteKind.projectile)
    else:
        PewPew = sprites.create(assets.image("""
            WarriorAxeL
        """), SpriteKind.projectile)
def monkpew():
    global PewPew
    if LastButtonPressed == 1:
        PewPew = sprites.create(assets.image("""
            MonkStar
        """), SpriteKind.projectile)
    else:
        PewPew = sprites.create(assets.image("""
            MonkStar
        """), SpriteKind.projectile)

def on_a_pressed():
    global Screen, Female, Male, canShoot
    if Screen == 1:
        Screen = 2
        scene.set_background_image(assets.image("""
            GenderSelect_Background
        """))
        WizardBanner.destroy()
        WarriorBanner.destroy()
        ArcherBanner.destroy()
        MonkBanner.destroy()
        Female = sprites.create(assets.image("""
                FemaleSelection
            """),
            SpriteKind.GenderSelection)
        Male = sprites.create(assets.image("""
                MaleSelection
            """),
            SpriteKind.GenderSelection)
        Female.set_position(130, 60)
        Male.set_position(80, 60)
    elif Screen == 2:
        canShoot = 1
        Screen = 0
        Male.destroy()
        Female.destroy()
        Preview.destroy()
        scene.set_background_image(assets.image("""
            Then theres this
        """))
        tiles.set_tilemap(tilemap("""
            level1
        """))
        WhatYouLookingAt()
        Character.ay = 500
        controller.move_sprite(Character, 100, 0)
        CharacterSize()
        makeHealth()
    elif Screen != -1 and (Screen != 0 and (Screen != 1 and Screen != 2)):
        if Character.is_hitting_tile(CollisionDirection.BOTTOM):
            Character.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global LastButtonPressed, ClassSelected, GenderSelected, Female, Male
    LastButtonPressed = -1
    if Screen == 1:
        music.thump.play()
        if ClassSelected == 1:
            ClassSelected = 0
        else:
            if ClassSelected == 2:
                ClassSelected = 1
            else:
                if ClassSelected == 3:
                    ClassSelected = 2
                else:
                    if ClassSelected == 4:
                        ClassSelected = 3
        pause(100)
        BroSeriously()
    else:
        if Screen == 2:
            music.thump.play()
            if GenderSelected == 1:
                GenderSelected = 0
                Female.destroy()
                Male.destroy()
                Female = sprites.create(assets.image("""
                        FemaleSelection
                    """),
                    SpriteKind.GenderSelection)
                Male = sprites.create(assets.image("""
                        MaleSelection
                    """),
                    SpriteKind.GenderSelection)
                Male.set_position(80, 60)
                Female.set_position(130, 60)
                GetGoodLol()
            else:
                if GenderSelected == 2:
                    GenderSelected = 1
                    Female.destroy()
                    Male.destroy()
                    Female = sprites.create(assets.image("""
                            FemaleSelection
                        """),
                        SpriteKind.GenderSelection)
                    Male = sprites.create(assets.image("""
                            MaleSelected
                        """),
                        SpriteKind.GenderSelection)
                    Male.set_position(80, 60)
                    Female.set_position(130, 60)
                    GetGoodLol()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_zero(status):
    info.change_score_by(1)
    statusbar3.sprite_attached_to().destroy()
statusbars.on_zero(StatusBarKind.EnemyHealth2, on_on_zero)

def wizardpew():
    global PewPew
    if LastButtonPressed == 1:
        PewPew = sprites.create(assets.image("""
                WizardFireBallR
            """),
            SpriteKind.projectile)
    else:
        PewPew = sprites.create(assets.image("""
                WizardFireBallL
            """),
            SpriteKind.projectile)
def dos():
    global Screen, FarmerGirl, Butler, Queen, Princess
    strayminer.destroy()
    TalkButton.destroy()
    tiles.set_tilemap(tilemap("""
        level9
    """))
    Screen = 5
    FarmerGirl = sprites.create(assets.image("""
        FarmerGirl
    """), SpriteKind.Null)
    FarmerGirl.set_position(1197, 473)
    Butler = sprites.create(assets.image("""
        Butler
    """), SpriteKind.Null)
    Butler.set_position(820, 475)
    Queen = sprites.create(assets.image("""
        Queen
    """), SpriteKind.Null)
    Queen.set_position(750, 233)
    Princess = sprites.create(assets.image("""
        Princess
    """), SpriteKind.player)
    Princess.set_position(1097, 314)

def on_countdown_end():
    global canShoot
    canShoot = 1
info.on_countdown_end(on_countdown_end)

def on_on_zero2(status2):
    info.change_score_by(1)
    statusbar2.sprite_attached_to().destroy()
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero2)

def makeHealth():
    global statusbar
    statusbar = statusbars.create(10, 2, StatusBarKind.health)
    statusbar.value = 100
    statusbar.attach_to_sprite(Character, 3, 0)

def on_on_overlap2(sprite2, otherSprite2):
    statusbar.value += -5.5
    otherSprite2.vx = -2.25 * otherSprite2.vx
    if controller.A.is_pressed():
        music.knock.play()
        statusbar3.value += -0.5
sprites.on_overlap(SpriteKind.player, SpriteKind.strongenemy2, on_on_overlap2)

def on_on_zero3(status3):
    game.over(False, effects.star_field)
statusbars.on_zero(StatusBarKind.health, on_on_zero3)

def on_right_pressed():
    global LastButtonPressed, ClassSelected, GenderSelected, Female, Male
    LastButtonPressed = 1
    if Screen == 1:
        music.thump.play()
        if ClassSelected == 0:
            ClassSelected = 1
        else:
            if ClassSelected == 1:
                ClassSelected = 2
            else:
                if ClassSelected == 2:
                    ClassSelected = 3
                else:
                    if ClassSelected == 3:
                        ClassSelected = 4
        pause(100)
        BroSeriously()
    else:
        if Screen == 2:
            music.thump.play()
            if GenderSelected == 0:
                GenderSelected = 1
                Female.destroy()
                Male.destroy()
                Female = sprites.create(assets.image("""
                        FemaleSelection
                    """),
                    SpriteKind.GenderSelection)
                Male = sprites.create(assets.image("""
                        MaleSelected
                    """),
                    SpriteKind.GenderSelection)
                Male.set_position(80, 60)
                Female.set_position(130, 60)
                GetGoodLol()
            else:
                if GenderSelected == 1:
                    GenderSelected = 2
                    Female.destroy()
                    Male.destroy()
                    Male = sprites.create(assets.image("""
                            MaleSelection
                        """),
                        SpriteKind.GenderSelection)
                    Female = sprites.create(assets.image("""
                            FemaleSelected
                        """),
                        SpriteKind.GenderSelection)
                    Male.set_position(80, 60)
                    Female.set_position(130, 60)
                    GetGoodLol()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def GetGoodLol():
    global Preview, CurrentlySelected
    if CurrentlySelected == 0:
        if ClassSelected == 1:
            if GenderSelected == 1:
                Preview = sprites.create(assets.image("""
                    WizardMale2
                """), SpriteKind.Null)
                Preview.set_position(30, 60)
                CurrentlySelected = 1
            elif GenderSelected == 2:
                Preview = sprites.create(assets.image("""
                    WizardFemale2
                """), SpriteKind.Null)
                Preview.set_position(30, 60)
                CurrentlySelected = 1
        else:
            if ClassSelected == 2:
                if GenderSelected == 1:
                    Preview = sprites.create(assets.image("""
                        WarriorMale2
                    """), SpriteKind.Null)
                    Preview.set_position(30, 60)
                    CurrentlySelected = 1
                elif GenderSelected == 2:
                    Preview = sprites.create(assets.image("""
                        WarriorFemale2
                    """), SpriteKind.Null)
                    Preview.set_position(30, 60)
                    CurrentlySelected = 1
            else:
                if ClassSelected == 3:
                    if GenderSelected == 1:
                        Preview = sprites.create(assets.image("""
                            ArcherMale2
                        """), SpriteKind.Null)
                        Preview.set_position(30, 60)
                        CurrentlySelected = 1
                    elif GenderSelected == 2:
                        Preview = sprites.create(assets.image("""
                            ArcherFemale2
                        """), SpriteKind.Null)
                        Preview.set_position(30, 60)
                        CurrentlySelected = 1
                else:
                    if ClassSelected == 4:
                        if GenderSelected == 1:
                            Preview = sprites.create(assets.image("""
                                MonkMale2
                            """), SpriteKind.Null)
                            Preview.set_position(30, 60)
                            CurrentlySelected = 1
                        elif GenderSelected == 2:
                            Preview = sprites.create(assets.image("""
                                MonkFemale2
                            """), SpriteKind.Null)
                            Preview.set_position(30, 60)
                            CurrentlySelected = 1
    elif CurrentlySelected == 1:
        if ClassSelected == 1:
            if GenderSelected == 1:
                Preview.destroy()
                Preview = sprites.create(assets.image("""
                    WizardMale2
                """), SpriteKind.Null)
                Preview.set_position(30, 60)
                CurrentlySelected = 1
            else:
                Preview.destroy()
                Preview = sprites.create(assets.image("""
                    WizardFemale2
                """), SpriteKind.Null)
                Preview.set_position(30, 60)
                CurrentlySelected = 1
        else:
            if ClassSelected == 2:
                if GenderSelected == 1:
                    Preview.destroy()
                    Preview = sprites.create(assets.image("""
                        WarriorMale2
                    """), SpriteKind.Null)
                    Preview.set_position(30, 60)
                    CurrentlySelected = 1
                else:
                    Preview.destroy()
                    Preview = sprites.create(assets.image("""
                        WarriorFemale2
                    """), SpriteKind.Null)
                    Preview.set_position(30, 60)
                    CurrentlySelected = 1
            else:
                if ClassSelected == 3:
                    if GenderSelected == 1:
                        Preview.destroy()
                        Preview = sprites.create(assets.image("""
                            ArcherMale2
                        """), SpriteKind.Null)
                        Preview.set_position(30, 60)
                        CurrentlySelected = 1
                    else:
                        Preview.destroy()
                        Preview = sprites.create(assets.image("""
                            ArcherFemale2
                        """), SpriteKind.Null)
                        Preview.set_position(30, 60)
                        CurrentlySelected = 1
                else:
                    if ClassSelected == 4:
                        if GenderSelected == 1:
                            Preview.destroy()
                            Preview = sprites.create(assets.image("""
                                MonkMale2
                            """), SpriteKind.Null)
                            Preview.set_position(30, 60)
                            CurrentlySelected = 1
                        else:
                            Preview.destroy()
                            Preview = sprites.create(assets.image("""
                                MonkFemale2
                            """), SpriteKind.Null)
                            Preview.set_position(30, 60)
                            CurrentlySelected = 1
def firstlevel():
    global badguy1, badguy2, badguy3, badguy4, badguy5, badguy6, badguy7, statusbar2, statusbar3
    makeHealth()
    badguy1 = sprites.create(assets.image("""
        DemonMale1
    """), SpriteKind.enemy)
    badguy1.set_position(640, 472)
    badguy2 = sprites.create(assets.image("""
        DemonMale1
    """), SpriteKind.enemy)
    badguy2.set_position(656, 472)
    badguy3 = sprites.create(assets.image("""
        DemonFemale1
    """), SpriteKind.enemy)
    badguy3.set_position(672, 472)
    badguy4 = sprites.create(assets.image("""
        DemonFemale1
    """), SpriteKind.enemy)
    badguy4.set_position(688, 472)
    badguy5 = sprites.create(assets.image("""
        DemonMale1
    """), SpriteKind.enemy)
    badguy5.set_position(704, 472)
    badguy6 = sprites.create(assets.image("""
            DemonFemale1
        """),
        SpriteKind.strongenemy)
    badguy7 = sprites.create(assets.image("""
            DemonFemale1
        """),
        SpriteKind.strongenemy2)
    badguy6.set_position(1652, 100)
    badguy7.set_position(1620, 100)
    statusbar2 = statusbars.create(10, 2, StatusBarKind.enemy_health)
    statusbar3 = statusbars.create(10, 2, StatusBarKind.EnemyHealth2)
    statusbar2.max = 2
    statusbar3.max = 2
    statusbar2.attach_to_sprite(badguy6, 2, 0)
    statusbar3.attach_to_sprite(badguy7, 2, 0)
    badguy1.ay = 9999
    badguy2.ay = 9999
    badguy3.ay = 9999
    badguy4.ay = 9999
    badguy5.ay = 9999
    badguy6.ay = 9999
    badguy7.ay = 9999
    pause(2000)
    badguy1.follow(Character, 75)
    badguy2.follow(Character, 75)
    badguy3.follow(Character, 75)
    badguy4.follow(Character, 75)
    badguy5.follow(Character, 75)
    pause(500)
    badguy6.follow(Character, 76)
    badguy7.follow(Character, 76)

def on_on_overlap3(sprite3, otherSprite3):
    global EnemyLimit
    sprite3.destroy()
    EnemyLimit += 1
    music.knock.play()
    statusbar2.value += -1
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.strongenemy,
    on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    statusbar.value += -5.5
    otherSprite4.vx = -2.25 * otherSprite4.vx
    if controller.A.is_pressed():
        music.knock.play()
        statusbar2.value += -0.5
sprites.on_overlap(SpriteKind.player, SpriteKind.strongenemy, on_on_overlap4)

def shoot():
    global canShoot
    if canShoot == 1:
        if characterSelected == 1:
            wizardpew()
        elif characterSelected == 2:
            wizardpew()
        elif characterSelected == 3:
            warriorpew()
        elif characterSelected == 4:
            warriorpew()
        elif characterSelected == 5:
            archerpew()
        elif characterSelected == 6:
            archerpew()
        elif characterSelected == 7:
            monkpew()
        elif characterSelected == 8:
            monkpew()
        PewPew.set_position(Character.x, Character.y)
        PewPew.vx = LastButtonPressed * 500
        canShoot = 0
        info.start_countdown(1)
        pause(500)
        PewPew.destroy()
def makeHitbox():
    global MeleeHitbox
    MeleeHitbox = sprites.create(assets.image("""
        MeleeHitbox
    """), SpriteKind.Hitbox)
    MeleeHitbox.follow(Character, 500)
def BroSeriously():
    if ClassSelected == 0:
        StopLookingAtTheCode()
    else:
        if ClassSelected == 1:
            StopLookingAtTheCode()
            animation.run_image_animation(WizardBanner,
                assets.animation("""
                    WizardBannerSelect
                """),
                165,
                True)
        else:
            if ClassSelected == 2:
                StopLookingAtTheCode()
                animation.run_image_animation(WarriorBanner,
                    assets.animation("""
                        WarriorBannerSelect
                    """),
                    165,
                    True)
            else:
                if ClassSelected == 3:
                    StopLookingAtTheCode()
                    animation.run_image_animation(ArcherBanner,
                        assets.animation("""
                            ArcherBannerSelect
                        """),
                        165,
                        True)
                else:
                    if ClassSelected == 4:
                        StopLookingAtTheCode()
                        animation.run_image_animation(MonkBanner,
                            assets.animation("""
                                MonkBannerSelect
                            """),
                            165,
                            True)
def MakingCodeShort():
    global badguyGender
    badguyGender = randint(0, 3)
    makeEnemy()
def makeEnemy():
    global badguy, EnemyLimit
    if EnemyLimit > 0:
        if badguyGender < 3:
            badguy = sprites.create(assets.image("""
                DemonMale1
            """), SpriteKind.enemy)
            badguy.set_position(randint(32, 1510), 0)
            badguy.ay = 9999
            badguy.follow(Character, 60)
            EnemyLimit += -1
        elif badguyGender == 3:
            badguy = sprites.create(assets.image("""
                DemonFemale1
            """), SpriteKind.enemy)
            badguy.set_position(randint(32, 1504), 48)
            badguy.ay = 9999
            badguy.follow(Character, 60)
            EnemyLimit += -1
def archerpew():
    global PewPew
    if LastButtonPressed == 1:
        PewPew = sprites.create(assets.image("""
                ArcherArrowR
            """),
            SpriteKind.projectile)
    else:
        PewPew = sprites.create(assets.image("""
                ArcherArrowL
            """),
            SpriteKind.projectile)

def on_on_overlap5(sprite5, otherSprite5):
    global EnemyLimit
    sprite5.destroy()
    EnemyLimit += 1
    music.knock.play()
    statusbar3.value += -1
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.strongenemy2,
    on_on_overlap5)

def Direction():
    if LastButtonPressed == -1:
        if characterSelected == 1:
            Character.set_image(assets.image("""
                WizardMale0
            """))
        elif characterSelected == 2:
            Character.set_image(assets.image("""
                WizardFemale0
            """))
        elif characterSelected == 3:
            Character.set_image(assets.image("""
                WarriorMale0
            """))
        elif characterSelected == 4:
            Character.set_image(assets.image("""
                WarriorFemale0
            """))
        elif characterSelected == 5:
            Character.set_image(assets.image("""
                ArcherMale0
            """))
        elif characterSelected == 6:
            Character.set_image(assets.image("""
                ArcherFemale0
            """))
        elif characterSelected == 7:
            Character.set_image(assets.image("""
                MonkMale0
            """))
        elif characterSelected == 8:
            Character.set_image(assets.image("""
                MonkFemale0
            """))
    elif LastButtonPressed == 1:
        if characterSelected == 1:
            Character.set_image(assets.image("""
                WizardMale2
            """))
        elif characterSelected == 2:
            Character.set_image(assets.image("""
                WizardFemale2
            """))
        elif characterSelected == 3:
            Character.set_image(assets.image("""
                WarriorMale2
            """))
        elif characterSelected == 4:
            Character.set_image(assets.image("""
                WarriorFemale2
            """))
        elif characterSelected == 5:
            Character.set_image(assets.image("""
                ArcherMale2
            """))
        elif characterSelected == 6:
            Character.set_image(assets.image("""
                ArcherFemale2
            """))
        elif characterSelected == 7:
            Character.set_image(assets.image("""
                MonkMale2
            """))
        elif characterSelected == 8:
            Character.set_image(assets.image("""
                MonkFemale2
            """))

def on_on_overlap6(sprite6, otherSprite6):
    global EnemyLimit
    otherSprite6.destroy(effects.spray, 200)
    sprite6.destroy()
    EnemyLimit += 1
    music.knock.play()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap6)

def NothingToSeeHere():
    global canTalk
    OldMan.destroy()
    Character.set_position(0, 0)
    canTalk = 0
def WhatYouLookingAt():
    global Character
    if characterSelected == 1:
        Character = sprites.create(assets.image("""
            WizardMale2
        """), SpriteKind.player)
        makeHitbox()
    else:
        if characterSelected == 2:
            Character = sprites.create(assets.image("""
                WizardFemale2
            """), SpriteKind.player)
            makeHitbox()
        else:
            if characterSelected == 3:
                Character = sprites.create(assets.image("""
                    WarriorMale2
                """), SpriteKind.player)
                makeHitbox()
            else:
                if characterSelected == 4:
                    Character = sprites.create(assets.image("""
                        WarriorFemale2
                    """), SpriteKind.player)
                    makeHitbox()
                else:
                    if characterSelected == 5:
                        Character = sprites.create(assets.image("""
                            ArcherMale2
                        """), SpriteKind.player)
                        makeHitbox()
                    else:
                        if characterSelected == 6:
                            Character = sprites.create(assets.image("""
                                ArcherFemale2
                            """), SpriteKind.player)
                            makeHitbox()
                        else:
                            if characterSelected == 7:
                                Character = sprites.create(assets.image("""
                                    MonkMale2
                                """), SpriteKind.player)
                                makeHitbox()
                            else:
                                if characterSelected == 8:
                                    Character = sprites.create(assets.image("""
                                        MonkFemale2
                                    """), SpriteKind.player)
                                    makeHitbox()

def on_on_overlap7(sprite7, otherSprite7):
    statusbar.value += -4.5
    otherSprite7.vx = -2.25 * otherSprite7.vx
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap7)

game_logo: Sprite = None
OldMan: Sprite = None
badguy: Sprite = None
badguyGender = 0
MeleeHitbox: Sprite = None
characterSelected = 0
badguy7: Sprite = None
badguy6: Sprite = None
badguy5: Sprite = None
badguy4: Sprite = None
badguy3: Sprite = None
badguy2: Sprite = None
badguy1: Sprite = None
statusbar: StatusBarSprite = None
statusbar2: StatusBarSprite = None
Princess: Sprite = None
Queen: Sprite = None
Butler: Sprite = None
FarmerGirl: Sprite = None
statusbar3: StatusBarSprite = None
PewPew: Sprite = None
LastButtonPressed = 0
canShoot = 0
TalkButton: Sprite = None
strayminer: Sprite = None
canTalk = 0
Preview: Sprite = None
Male: Sprite = None
Female: Sprite = None
Character: Sprite = None
EnemyLimit = 0
WizardBanner: Sprite = None
MonkBanner: Sprite = None
ArcherBanner: Sprite = None
WarriorBanner: Sprite = None
CurrentlySelected = 0
Screen = 0
ClassSelected = 0
GenderSelected = 0
GenderSelected = 0
ClassSelected = 0
Screen = 1
CurrentlySelected = 0
scene.set_background_image(assets.image("""
    ClassSelect_Background
"""))
WarriorBanner = sprites.create(assets.image("""
    WarriorBanner
"""), SpriteKind.Banner)
WarriorBanner.set_position(82, 60)
ArcherBanner = sprites.create(assets.image("""
    ArcherBanner
"""), SpriteKind.Banner)
ArcherBanner.set_position(113, 60)
MonkBanner = sprites.create(assets.image("""
    MonkBanner
"""), SpriteKind.Banner)
MonkBanner.set_position(144, 60)
WizardBanner = sprites.create(assets.image("""
    WizardBanner
"""), SpriteKind.player)
WizardBanner.set_position(51, 60)
EnemyLimit = 7

def on_on_update():
    global Screen
    if Screen == 0:
        if info.score() == 10:
            Screen = -2
            
            def on_start_cutscene():
                global game_logo, Screen, OldMan, canShoot
                scene.set_background_image(assets.image("""
                    and an eternally black void
                """))
                tiles.set_tilemap(tilemap("""
                    logotilemap
                """))
                game_logo = sprites.create(assets.image("""
                    logo
                """), SpriteKind.logo)
                scene.camera_follow_sprite(game_logo)
                pause(2000)
                scene.center_camera_at(game_logo.x, game_logo.y)
                story.sprite_move_to_location(game_logo, game_logo.x, game_logo.y - 18, 20)
                story.print_dialog("The Cheese Nerds",
                    100,
                    100,
                    50,
                    150,
                    2,
                    15,
                    story.TextSpeed.NORMAL)
                pause(500)
                game_logo.destroy()
                Screen = 3
                tiles.set_tilemap(tilemap("""
                    level2
                """))
                MeleeHitbox.destroy()
                badguy.destroy()
                statusbar.destroy()
                Character.set_position(16, 420)
                CharacterSize()
                OldMan = sprites.create(assets.image("""
                    Old_Man
                """), SpriteKind.Null)
                OldMan.set_position(1292, 444)
                canShoot = 0
                info.set_score(0)
            story.start_cutscene(on_start_cutscene)
            
game.on_update(on_on_update)

def on_forever():
    if Screen == 0:
        music.play_tone(330, music.beat(BeatFraction.HALF))
        music.play_tone(277, music.beat(BeatFraction.WHOLE))
        music.play_tone(277, music.beat(BeatFraction.HALF))
        music.play_tone(311, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.DOUBLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.DOUBLE))
        music.play_tone(294, music.beat(BeatFraction.DOUBLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.DOUBLE))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(311, music.beat(BeatFraction.DOUBLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(415, music.beat(BeatFraction.HALF))
        music.play_tone(415, music.beat(BeatFraction.HALF))
        music.play_tone(494, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.HALF))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(277, music.beat(BeatFraction.WHOLE))
        music.play_tone(311, music.beat(BeatFraction.WHOLE))
    elif Screen == 3:
        music.play_tone(587, music.beat(BeatFraction.HALF))
        music.play_tone(659, music.beat(BeatFraction.HALF))
        music.play_tone(587, music.beat(BeatFraction.HALF))
        music.play_tone(554, music.beat(BeatFraction.WHOLE))
        music.play_tone(494, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.DOUBLE))
        music.play_tone(880, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(659, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
        music.play_tone(494, music.beat(BeatFraction.HALF))
        music.play_tone(554, music.beat(BeatFraction.DOUBLE))
        music.play_tone(554, music.beat(BeatFraction.HALF))
        music.play_tone(659, music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.HALF))
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        music.play_tone(554, music.beat(BeatFraction.HALF))
        music.play_tone(392, music.beat(BeatFraction.DOUBLE))
        music.play_tone(880, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(659, music.beat(BeatFraction.HALF))
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
        music.play_tone(494, music.beat(BeatFraction.HALF))
        music.play_tone(554, music.beat(BeatFraction.WHOLE))
forever(on_forever)

def on_forever2():
    global canTalk, TalkButton
    if Screen == 3:
        badguy.set_flag(SpriteFlag.INVISIBLE, True)
        tiles.destroy_sprites_of_kind(SpriteKind.enemy)
        if abs(OldMan.x - Character.x) < 48 and canTalk == 0:
            canTalk = 1
            TalkButton = sprites.create(assets.image("""
                TalkButton
            """), SpriteKind.Interactive)
            TalkButton.set_position(OldMan.x, OldMan.y - 15)
    elif Screen == 4:
        if abs(strayminer.x - Character.x) < 48 and canTalk == 0 and abs(strayminer.y - Character.y) < 16:
            canTalk = 1
            TalkButton = sprites.create(assets.image("""
                TalkButton
            """), SpriteKind.Interactive)
            TalkButton.set_position(strayminer.x, strayminer.y - 15)
forever(on_forever2)

def on_forever3():
    if Screen != 1 and Screen != 2:
        Direction()
forever(on_forever3)

def on_forever4():
    if Screen == 0:
        pause(3500)
        MakingCodeShort()
    elif Screen == -1:
        pause(2000)
        MakingCodeShort()
forever(on_forever4)

def on_forever5():
    global canTalk
    if Screen == 3:
        if abs(OldMan.x - Character.x) >= 48 and canTalk == 1:
            canTalk = 0
            TalkButton.destroy()
    elif Screen == 4:
        if abs(strayminer.x - Character.x) >= 48 and canTalk == 1:
            canTalk = 0
            TalkButton.destroy()
forever(on_forever5)

def on_forever6():
    global characterSelected
    if Screen != 1 and (Screen != 2 and Screen != -2):
        scene.camera_follow_sprite(Character)
    if ClassSelected == 1 and GenderSelected == 1:
        characterSelected = 1
    else:
        if ClassSelected == 1 and GenderSelected == 2:
            characterSelected = 2
        else:
            if ClassSelected == 2 and GenderSelected == 1:
                characterSelected = 3
            else:
                if ClassSelected == 2 and GenderSelected == 2:
                    characterSelected = 4
                else:
                    if ClassSelected == 3 and GenderSelected == 1:
                        characterSelected = 5
                    else:
                        if ClassSelected == 3 and GenderSelected == 2:
                            characterSelected = 6
                        else:
                            if ClassSelected == 4 and GenderSelected == 1:
                                characterSelected = 7
                            else:
                                if ClassSelected == 4 and GenderSelected == 2:
                                    characterSelected = 8
forever(on_forever6)

def on_forever7():
    if ClassSelected == 0:
        animation.stop_animation(animation.AnimationTypes.ALL, WizardBanner)
        animation.stop_animation(animation.AnimationTypes.ALL, WarriorBanner)
        animation.stop_animation(animation.AnimationTypes.ALL, MonkBanner)
        animation.stop_animation(animation.AnimationTypes.ALL, ArcherBanner)
    else:
        if ClassSelected == 1:
            animation.stop_animation(animation.AnimationTypes.ALL, WarriorBanner)
            animation.stop_animation(animation.AnimationTypes.ALL, ArcherBanner)
            animation.stop_animation(animation.AnimationTypes.ALL, MonkBanner)
        else:
            if ClassSelected == 2:
                animation.stop_animation(animation.AnimationTypes.ALL, WizardBanner)
                animation.stop_animation(animation.AnimationTypes.ALL, ArcherBanner)
                animation.stop_animation(animation.AnimationTypes.ALL, MonkBanner)
            else:
                if ClassSelected == 3:
                    animation.stop_animation(animation.AnimationTypes.ALL, WizardBanner)
                    animation.stop_animation(animation.AnimationTypes.ALL, WarriorBanner)
                    animation.stop_animation(animation.AnimationTypes.ALL, MonkBanner)
                else:
                    if ClassSelected == 4:
                        animation.stop_animation(animation.AnimationTypes.ALL, WizardBanner)
                        animation.stop_animation(animation.AnimationTypes.ALL, WarriorBanner)
                        animation.stop_animation(animation.AnimationTypes.ALL, ArcherBanner)
forever(on_forever7)
