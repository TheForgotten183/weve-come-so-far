namespace SpriteKind {
    export const Banner = SpriteKind.create()
    export const GenderSelection = SpriteKind.create()
    export const Null = SpriteKind.create()
    export const Hitbox = SpriteKind.create()
    export const Interactive = SpriteKind.create()
    export const logo = SpriteKind.create()
    export const strongenemy = SpriteKind.create()
    export const strongenemy2 = SpriteKind.create()
}
namespace StatusBarKind {
    export const EnemyHealth2 = StatusBarKind.create()
}
sprites.onOverlap(SpriteKind.Hitbox, SpriteKind.Enemy, function (sprite, otherSprite) {
    if (controller.A.isPressed()) {
        otherSprite.ay = 0
        otherSprite.destroy(effects.spray, 100)
        EnemyLimit += 1
        music.knock.play()
        info.changeScoreBy(1)
    }
})
function CharacterSize () {
    scaling.scaleToPixels(Character, 20, ScaleDirection.Horizontally, ScaleAnchor.Middle)
    scaling.scaleToPixels(Character, 24, ScaleDirection.Vertically, ScaleAnchor.Middle)
}
function StopLookingAtTheCode () {
    WizardBanner.destroy()
    WarriorBanner.destroy()
    ArcherBanner.destroy()
    MonkBanner.destroy()
    WarriorBanner = sprites.create(assets.image`WarriorBanner`, SpriteKind.Banner)
    WarriorBanner.setPosition(82, 60)
    ArcherBanner = sprites.create(assets.image`ArcherBanner`, SpriteKind.Banner)
    ArcherBanner.setPosition(113, 60)
    MonkBanner = sprites.create(assets.image`MonkBanner`, SpriteKind.Banner)
    MonkBanner.setPosition(144, 60)
    WizardBanner = sprites.create(assets.image`WizardBanner`, SpriteKind.Player)
    WizardBanner.setPosition(51, 60)
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Screen == 2) {
        scene.setBackgroundImage(assets.image`ClassSelect_Background`)
        Female.destroy()
        Male.destroy()
        Screen = 1
        Preview.destroy()
        WarriorBanner = sprites.create(assets.image`WarriorBanner`, SpriteKind.Banner)
        WarriorBanner.setPosition(82, 60)
        ArcherBanner = sprites.create(assets.image`ArcherBanner`, SpriteKind.Banner)
        ArcherBanner.setPosition(113, 60)
        MonkBanner = sprites.create(assets.image`MonkBanner`, SpriteKind.Banner)
        MonkBanner.setPosition(144, 60)
        WizardBanner = sprites.create(assets.image`WizardBanner`, SpriteKind.Player)
        WizardBanner.setPosition(51, 60)
    } else if (Screen == -1) {
        shoot()
    } else if (Screen == 0) {
        shoot()
    } else if (Screen == 3) {
        if (canTalk == 1) {
            if (game.ask("Do you want to continue", "the campaign?")) {
                NothingToSeeHere()
                scene.setBackgroundImage(assets.image`Nighttime`)
                tiles.setTilemap(tilemap`level3`)
                strayminer = sprites.create(assets.image`StrayMiner`, SpriteKind.Null)
                strayminer.setPosition(1492, 473)
                Screen = 4
                TalkButton.destroy()
                canShoot = 1
                firstlevel()
            } else if (game.ask("Do you want to try", "endless mode?")) {
                NothingToSeeHere()
                scene.setBackgroundImage(assets.image`Sunset`)
                tiles.setTilemap(tilemap`Campaign1`)
                Screen = -1
                TalkButton.destroy()
                EnemyLimit = 16
                Character.setPosition(32, 208)
                makeHealth()
                canShoot = 1
                makeHitbox()
            }
        }
    } else if (Screen == 4) {
        shoot()
        if (canTalk == 1) {
            if (info.score() < 7) {
                game.splash("Clear the other enemies,", "then we'll talk")
                Character.setPosition(160, 472)
            } else {
                if (game.ask("Hi! Follow me to the", "caves, we're safer there!")) {
                    dos()
                }
            }
        }
    }
})
function warriorpew () {
    if (LastButtonPressed == 1) {
        PewPew = sprites.create(assets.image`WarriorAxeR`, SpriteKind.Projectile)
    } else {
        PewPew = sprites.create(assets.image`WarriorAxeL`, SpriteKind.Projectile)
    }
}
function monkpew () {
    if (LastButtonPressed == 1) {
        PewPew = sprites.create(assets.image`MonkStar`, SpriteKind.Projectile)
    } else {
        PewPew = sprites.create(assets.image`MonkStar`, SpriteKind.Projectile)
    }
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Screen == 1) {
        Screen = 2
        scene.setBackgroundImage(assets.image`GenderSelect_Background`)
        WizardBanner.destroy()
        WarriorBanner.destroy()
        ArcherBanner.destroy()
        MonkBanner.destroy()
        Female = sprites.create(assets.image`FemaleSelection`, SpriteKind.GenderSelection)
        Male = sprites.create(assets.image`MaleSelection`, SpriteKind.GenderSelection)
        Female.setPosition(130, 60)
        Male.setPosition(80, 60)
    } else if (Screen == 2) {
        canShoot = 1
        Screen = 0
        Male.destroy()
        Female.destroy()
        Preview.destroy()
        scene.setBackgroundImage(assets.image`Then theres this`)
        tiles.setTilemap(tilemap`level1`)
        WhatYouLookingAt()
        Character.ay = 500
        controller.moveSprite(Character, 100, 0)
        CharacterSize()
        makeHealth()
    } else if (Screen != -1 && (Screen != 0 && (Screen != 1 && Screen != 2))) {
        if (Character.isHittingTile(CollisionDirection.Bottom)) {
            Character.vy = -200
        }
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    LastButtonPressed = -1
    if (Screen == 1) {
        music.thump.play()
        if (ClassSelected == 1) {
            ClassSelected = 0
        } else {
            if (ClassSelected == 2) {
                ClassSelected = 1
            } else {
                if (ClassSelected == 3) {
                    ClassSelected = 2
                } else {
                    if (ClassSelected == 4) {
                        ClassSelected = 3
                    }
                }
            }
        }
        pause(100)
        BroSeriously()
    } else {
        if (Screen == 2) {
            music.thump.play()
            if (GenderSelected == 1) {
                GenderSelected = 0
                Female.destroy()
                Male.destroy()
                Female = sprites.create(assets.image`FemaleSelection`, SpriteKind.GenderSelection)
                Male = sprites.create(assets.image`MaleSelection`, SpriteKind.GenderSelection)
                Male.setPosition(80, 60)
                Female.setPosition(130, 60)
                GetGoodLol()
            } else {
                if (GenderSelected == 2) {
                    GenderSelected = 1
                    Female.destroy()
                    Male.destroy()
                    Female = sprites.create(assets.image`FemaleSelection`, SpriteKind.GenderSelection)
                    Male = sprites.create(assets.image`MaleSelected`, SpriteKind.GenderSelection)
                    Male.setPosition(80, 60)
                    Female.setPosition(130, 60)
                    GetGoodLol()
                }
            }
        }
    }
})
statusbars.onZero(StatusBarKind.EnemyHealth2, function (status) {
    info.changeScoreBy(1)
    statusbar3.spriteAttachedTo().destroy()
})
function wizardpew () {
    if (LastButtonPressed == 1) {
        PewPew = sprites.create(assets.image`WizardFireBallR`, SpriteKind.Projectile)
    } else {
        PewPew = sprites.create(assets.image`WizardFireBallL`, SpriteKind.Projectile)
    }
}
function dos () {
    strayminer.destroy()
    TalkButton.destroy()
    tiles.setTilemap(tilemap`level9`)
    Screen = 5
    FarmerGirl = sprites.create(assets.image`FarmerGirl`, SpriteKind.Null)
    FarmerGirl.setPosition(1197, 473)
    Butler = sprites.create(assets.image`Butler`, SpriteKind.Null)
    Butler.setPosition(820, 475)
    Queen = sprites.create(assets.image`Queen`, SpriteKind.Null)
    Queen.setPosition(750, 233)
    Princess = sprites.create(assets.image`Princess`, SpriteKind.Player)
    Princess.setPosition(1097, 314)
}
info.onCountdownEnd(function () {
    canShoot = 1
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    info.changeScoreBy(1)
    statusbar2.spriteAttachedTo().destroy()
})
function makeHealth () {
    statusbar = statusbars.create(10, 2, StatusBarKind.Health)
    statusbar.value = 100
    statusbar.attachToSprite(Character, 3, 0)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.strongenemy2, function (sprite, otherSprite) {
    statusbar.value += -5.5
    otherSprite.vx = -2.25 * otherSprite.vx
    if (controller.A.isPressed()) {
        music.knock.play()
        statusbar3.value += -0.5
    }
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.over(false, effects.starField)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    LastButtonPressed = 1
    if (Screen == 1) {
        music.thump.play()
        if (ClassSelected == 0) {
            ClassSelected = 1
        } else {
            if (ClassSelected == 1) {
                ClassSelected = 2
            } else {
                if (ClassSelected == 2) {
                    ClassSelected = 3
                } else {
                    if (ClassSelected == 3) {
                        ClassSelected = 4
                    }
                }
            }
        }
        pause(100)
        BroSeriously()
    } else {
        if (Screen == 2) {
            music.thump.play()
            if (GenderSelected == 0) {
                GenderSelected = 1
                Female.destroy()
                Male.destroy()
                Female = sprites.create(assets.image`FemaleSelection`, SpriteKind.GenderSelection)
                Male = sprites.create(assets.image`MaleSelected`, SpriteKind.GenderSelection)
                Male.setPosition(80, 60)
                Female.setPosition(130, 60)
                GetGoodLol()
            } else {
                if (GenderSelected == 1) {
                    GenderSelected = 2
                    Female.destroy()
                    Male.destroy()
                    Male = sprites.create(assets.image`MaleSelection`, SpriteKind.GenderSelection)
                    Female = sprites.create(assets.image`FemaleSelected`, SpriteKind.GenderSelection)
                    Male.setPosition(80, 60)
                    Female.setPosition(130, 60)
                    GetGoodLol()
                }
            }
        }
    }
})
function GetGoodLol () {
    if (CurrentlySelected == 0) {
        if (ClassSelected == 1) {
            if (GenderSelected == 1) {
                Preview = sprites.create(assets.image`WizardMale2`, SpriteKind.Null)
                Preview.setPosition(30, 60)
                CurrentlySelected = 1
            } else if (GenderSelected == 2) {
                Preview = sprites.create(assets.image`WizardFemale2`, SpriteKind.Null)
                Preview.setPosition(30, 60)
                CurrentlySelected = 1
            }
        } else {
            if (ClassSelected == 2) {
                if (GenderSelected == 1) {
                    Preview = sprites.create(assets.image`WarriorMale2`, SpriteKind.Null)
                    Preview.setPosition(30, 60)
                    CurrentlySelected = 1
                } else if (GenderSelected == 2) {
                    Preview = sprites.create(assets.image`WarriorFemale2`, SpriteKind.Null)
                    Preview.setPosition(30, 60)
                    CurrentlySelected = 1
                }
            } else {
                if (ClassSelected == 3) {
                    if (GenderSelected == 1) {
                        Preview = sprites.create(assets.image`ArcherMale2`, SpriteKind.Null)
                        Preview.setPosition(30, 60)
                        CurrentlySelected = 1
                    } else if (GenderSelected == 2) {
                        Preview = sprites.create(assets.image`ArcherFemale2`, SpriteKind.Null)
                        Preview.setPosition(30, 60)
                        CurrentlySelected = 1
                    }
                } else {
                    if (ClassSelected == 4) {
                        if (GenderSelected == 1) {
                            Preview = sprites.create(assets.image`MonkMale2`, SpriteKind.Null)
                            Preview.setPosition(30, 60)
                            CurrentlySelected = 1
                        } else if (GenderSelected == 2) {
                            Preview = sprites.create(assets.image`MonkFemale2`, SpriteKind.Null)
                            Preview.setPosition(30, 60)
                            CurrentlySelected = 1
                        }
                    }
                }
            }
        }
    } else if (CurrentlySelected == 1) {
        if (ClassSelected == 1) {
            if (GenderSelected == 1) {
                Preview.destroy()
                Preview = sprites.create(assets.image`WizardMale2`, SpriteKind.Null)
                Preview.setPosition(30, 60)
                CurrentlySelected = 1
            } else {
                Preview.destroy()
                Preview = sprites.create(assets.image`WizardFemale2`, SpriteKind.Null)
                Preview.setPosition(30, 60)
                CurrentlySelected = 1
            }
        } else {
            if (ClassSelected == 2) {
                if (GenderSelected == 1) {
                    Preview.destroy()
                    Preview = sprites.create(assets.image`WarriorMale2`, SpriteKind.Null)
                    Preview.setPosition(30, 60)
                    CurrentlySelected = 1
                } else {
                    Preview.destroy()
                    Preview = sprites.create(assets.image`WarriorFemale2`, SpriteKind.Null)
                    Preview.setPosition(30, 60)
                    CurrentlySelected = 1
                }
            } else {
                if (ClassSelected == 3) {
                    if (GenderSelected == 1) {
                        Preview.destroy()
                        Preview = sprites.create(assets.image`ArcherMale2`, SpriteKind.Null)
                        Preview.setPosition(30, 60)
                        CurrentlySelected = 1
                    } else {
                        Preview.destroy()
                        Preview = sprites.create(assets.image`ArcherFemale2`, SpriteKind.Null)
                        Preview.setPosition(30, 60)
                        CurrentlySelected = 1
                    }
                } else {
                    if (ClassSelected == 4) {
                        if (GenderSelected == 1) {
                            Preview.destroy()
                            Preview = sprites.create(assets.image`MonkMale2`, SpriteKind.Null)
                            Preview.setPosition(30, 60)
                            CurrentlySelected = 1
                        } else {
                            Preview.destroy()
                            Preview = sprites.create(assets.image`MonkFemale2`, SpriteKind.Null)
                            Preview.setPosition(30, 60)
                            CurrentlySelected = 1
                        }
                    }
                }
            }
        }
    }
}
function firstlevel () {
    makeHealth()
    badguy1 = sprites.create(assets.image`DemonMale1`, SpriteKind.Enemy)
    badguy1.setPosition(640, 472)
    badguy2 = sprites.create(assets.image`DemonMale1`, SpriteKind.Enemy)
    badguy2.setPosition(656, 472)
    badguy3 = sprites.create(assets.image`DemonFemale1`, SpriteKind.Enemy)
    badguy3.setPosition(672, 472)
    badguy4 = sprites.create(assets.image`DemonFemale1`, SpriteKind.Enemy)
    badguy4.setPosition(688, 472)
    badguy5 = sprites.create(assets.image`DemonMale1`, SpriteKind.Enemy)
    badguy5.setPosition(704, 472)
    badguy6 = sprites.create(assets.image`DemonFemale1`, SpriteKind.strongenemy)
    badguy7 = sprites.create(assets.image`DemonFemale1`, SpriteKind.strongenemy2)
    badguy6.setPosition(1652, 100)
    badguy7.setPosition(1620, 100)
    statusbar2 = statusbars.create(10, 2, StatusBarKind.EnemyHealth)
    statusbar3 = statusbars.create(10, 2, StatusBarKind.EnemyHealth2)
    statusbar2.max = 2
    statusbar3.max = 2
    statusbar2.attachToSprite(badguy6, 2, 0)
    statusbar3.attachToSprite(badguy7, 2, 0)
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
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.strongenemy, function (sprite, otherSprite) {
    sprite.destroy()
    EnemyLimit += 1
    music.knock.play()
    statusbar2.value += -1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.strongenemy, function (sprite, otherSprite) {
    statusbar.value += -5.5
    otherSprite.vx = -2.25 * otherSprite.vx
    if (controller.A.isPressed()) {
        music.knock.play()
        statusbar2.value += -0.5
    }
})
function shoot () {
    if (canShoot == 1) {
        if (characterSelected == 1) {
            wizardpew()
        } else if (characterSelected == 2) {
            wizardpew()
        } else if (characterSelected == 3) {
            warriorpew()
        } else if (characterSelected == 4) {
            warriorpew()
        } else if (characterSelected == 5) {
            archerpew()
        } else if (characterSelected == 6) {
            archerpew()
        } else if (characterSelected == 7) {
            monkpew()
        } else if (characterSelected == 8) {
            monkpew()
        }
        PewPew.setPosition(Character.x, Character.y)
        PewPew.vx = LastButtonPressed * 500
        canShoot = 0
        info.startCountdown(1)
        pause(500)
        PewPew.destroy()
    }
}
function makeHitbox () {
    MeleeHitbox = sprites.create(assets.image`MeleeHitbox`, SpriteKind.Hitbox)
    MeleeHitbox.follow(Character, 500)
}
function BroSeriously () {
    if (ClassSelected == 0) {
        StopLookingAtTheCode()
    } else {
        if (ClassSelected == 1) {
            StopLookingAtTheCode()
            animation.runImageAnimation(
            WizardBanner,
            assets.animation`WizardBannerSelect`,
            165,
            true
            )
        } else {
            if (ClassSelected == 2) {
                StopLookingAtTheCode()
                animation.runImageAnimation(
                WarriorBanner,
                assets.animation`WarriorBannerSelect`,
                165,
                true
                )
            } else {
                if (ClassSelected == 3) {
                    StopLookingAtTheCode()
                    animation.runImageAnimation(
                    ArcherBanner,
                    assets.animation`ArcherBannerSelect`,
                    165,
                    true
                    )
                } else {
                    if (ClassSelected == 4) {
                        StopLookingAtTheCode()
                        animation.runImageAnimation(
                        MonkBanner,
                        assets.animation`MonkBannerSelect`,
                        165,
                        true
                        )
                    }
                }
            }
        }
    }
}
function MakingCodeShort () {
    badguyGender = randint(0, 3)
    makeEnemy()
}
function makeEnemy () {
    if (EnemyLimit > 0) {
        if (badguyGender < 3) {
            badguy = sprites.create(assets.image`DemonMale1`, SpriteKind.Enemy)
            badguy.setPosition(randint(32, 1510), 0)
            badguy.ay = 9999
            badguy.follow(Character, 60)
            EnemyLimit += -1
        } else if (badguyGender == 3) {
            badguy = sprites.create(assets.image`DemonFemale1`, SpriteKind.Enemy)
            badguy.setPosition(randint(32, 1504), 48)
            badguy.ay = 9999
            badguy.follow(Character, 60)
            EnemyLimit += -1
        }
    }
}
function archerpew () {
    if (LastButtonPressed == 1) {
        PewPew = sprites.create(assets.image`ArcherArrowR`, SpriteKind.Projectile)
    } else {
        PewPew = sprites.create(assets.image`ArcherArrowL`, SpriteKind.Projectile)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.strongenemy2, function (sprite, otherSprite) {
    sprite.destroy()
    EnemyLimit += 1
    music.knock.play()
    statusbar3.value += -1
})
function Direction () {
    if (LastButtonPressed == -1) {
        if (characterSelected == 1) {
            Character.setImage(assets.image`WizardMale0`)
        } else if (characterSelected == 2) {
            Character.setImage(assets.image`WizardFemale0`)
        } else if (characterSelected == 3) {
            Character.setImage(assets.image`WarriorMale0`)
        } else if (characterSelected == 4) {
            Character.setImage(assets.image`WarriorFemale0`)
        } else if (characterSelected == 5) {
            Character.setImage(assets.image`ArcherMale0`)
        } else if (characterSelected == 6) {
            Character.setImage(assets.image`ArcherFemale0`)
        } else if (characterSelected == 7) {
            Character.setImage(assets.image`MonkMale0`)
        } else if (characterSelected == 8) {
            Character.setImage(assets.image`MonkFemale0`)
        }
    } else if (LastButtonPressed == 1) {
        if (characterSelected == 1) {
            Character.setImage(assets.image`WizardMale2`)
        } else if (characterSelected == 2) {
            Character.setImage(assets.image`WizardFemale2`)
        } else if (characterSelected == 3) {
            Character.setImage(assets.image`WarriorMale2`)
        } else if (characterSelected == 4) {
            Character.setImage(assets.image`WarriorFemale2`)
        } else if (characterSelected == 5) {
            Character.setImage(assets.image`ArcherMale2`)
        } else if (characterSelected == 6) {
            Character.setImage(assets.image`ArcherFemale2`)
        } else if (characterSelected == 7) {
            Character.setImage(assets.image`MonkMale2`)
        } else if (characterSelected == 8) {
            Character.setImage(assets.image`MonkFemale2`)
        }
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.spray, 200)
    sprite.destroy()
    EnemyLimit += 1
    music.knock.play()
    info.changeScoreBy(1)
})
function NothingToSeeHere () {
    OldMan.destroy()
    Character.setPosition(0, 0)
    canTalk = 0
}
function WhatYouLookingAt () {
    if (characterSelected == 1) {
        Character = sprites.create(assets.image`WizardMale2`, SpriteKind.Player)
        makeHitbox()
    } else {
        if (characterSelected == 2) {
            Character = sprites.create(assets.image`WizardFemale2`, SpriteKind.Player)
            makeHitbox()
        } else {
            if (characterSelected == 3) {
                Character = sprites.create(assets.image`WarriorMale2`, SpriteKind.Player)
                makeHitbox()
            } else {
                if (characterSelected == 4) {
                    Character = sprites.create(assets.image`WarriorFemale2`, SpriteKind.Player)
                    makeHitbox()
                } else {
                    if (characterSelected == 5) {
                        Character = sprites.create(assets.image`ArcherMale2`, SpriteKind.Player)
                        makeHitbox()
                    } else {
                        if (characterSelected == 6) {
                            Character = sprites.create(assets.image`ArcherFemale2`, SpriteKind.Player)
                            makeHitbox()
                        } else {
                            if (characterSelected == 7) {
                                Character = sprites.create(assets.image`MonkMale2`, SpriteKind.Player)
                                makeHitbox()
                            } else {
                                if (characterSelected == 8) {
                                    Character = sprites.create(assets.image`MonkFemale2`, SpriteKind.Player)
                                    makeHitbox()
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    statusbar.value += -4.5
    otherSprite.vx = -2.25 * otherSprite.vx
})
let game_logo: Sprite = null
let OldMan: Sprite = null
let badguy: Sprite = null
let badguyGender = 0
let MeleeHitbox: Sprite = null
let characterSelected = 0
let badguy7: Sprite = null
let badguy6: Sprite = null
let badguy5: Sprite = null
let badguy4: Sprite = null
let badguy3: Sprite = null
let badguy2: Sprite = null
let badguy1: Sprite = null
let statusbar: StatusBarSprite = null
let statusbar2: StatusBarSprite = null
let Princess: Sprite = null
let Queen: Sprite = null
let Butler: Sprite = null
let FarmerGirl: Sprite = null
let statusbar3: StatusBarSprite = null
let PewPew: Sprite = null
let LastButtonPressed = 0
let canShoot = 0
let TalkButton: Sprite = null
let strayminer: Sprite = null
let canTalk = 0
let Preview: Sprite = null
let Male: Sprite = null
let Female: Sprite = null
let Character: Sprite = null
let EnemyLimit = 0
let WizardBanner: Sprite = null
let MonkBanner: Sprite = null
let ArcherBanner: Sprite = null
let WarriorBanner: Sprite = null
let CurrentlySelected = 0
let Screen = 0
let ClassSelected = 0
let GenderSelected = 0
GenderSelected = 0
ClassSelected = 0
Screen = 1
CurrentlySelected = 0
scene.setBackgroundImage(assets.image`ClassSelect_Background`)
WarriorBanner = sprites.create(assets.image`WarriorBanner`, SpriteKind.Banner)
WarriorBanner.setPosition(82, 60)
ArcherBanner = sprites.create(assets.image`ArcherBanner`, SpriteKind.Banner)
ArcherBanner.setPosition(113, 60)
MonkBanner = sprites.create(assets.image`MonkBanner`, SpriteKind.Banner)
MonkBanner.setPosition(144, 60)
WizardBanner = sprites.create(assets.image`WizardBanner`, SpriteKind.Player)
WizardBanner.setPosition(51, 60)
EnemyLimit = 7
game.onUpdate(function () {
    if (Screen == 0) {
        if (info.score() == 10) {
            Screen = -2
            story.startCutscene(function () {
                scene.setBackgroundImage(assets.image`and an eternally black void`)
                tiles.setTilemap(tilemap`logotilemap`)
                game_logo = sprites.create(assets.image`logo`, SpriteKind.logo)
                scene.cameraFollowSprite(game_logo)
                pause(2000)
                scene.centerCameraAt(game_logo.x, game_logo.y)
                story.spriteMoveToLocation(game_logo, game_logo.x, game_logo.y - 18, 20)
                story.printDialog("The Cheese Nerds", 100, 100, 50, 150, 2, 15, story.TextSpeed.Normal)
                pause(500)
                game_logo.destroy()
                Screen = 3
                tiles.setTilemap(tilemap`level2`)
                MeleeHitbox.destroy()
                badguy.destroy()
                statusbar.destroy()
                Character.setPosition(16, 420)
                CharacterSize()
                OldMan = sprites.create(assets.image`Old_Man`, SpriteKind.Null)
                OldMan.setPosition(1292, 444)
                canShoot = 0
                info.setScore(0)
            })
        }
    }
})
forever(function () {
    if (Screen == 0) {
        music.playTone(330, music.beat(BeatFraction.Half))
        music.playTone(277, music.beat(BeatFraction.Whole))
        music.playTone(277, music.beat(BeatFraction.Half))
        music.playTone(311, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(247, music.beat(BeatFraction.Whole))
        music.playTone(247, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(220, music.beat(BeatFraction.Double))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(233, music.beat(BeatFraction.Half))
        music.playTone(233, music.beat(BeatFraction.Half))
        music.playTone(247, music.beat(BeatFraction.Double))
        music.playTone(294, music.beat(BeatFraction.Double))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Double))
        music.playTone(294, music.beat(BeatFraction.Half))
        music.playTone(294, music.beat(BeatFraction.Half))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.playTone(311, music.beat(BeatFraction.Double))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(415, music.beat(BeatFraction.Half))
        music.playTone(415, music.beat(BeatFraction.Half))
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Half))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.playTone(277, music.beat(BeatFraction.Whole))
        music.playTone(311, music.beat(BeatFraction.Whole))
    } else if (Screen == 3) {
        music.playTone(587, music.beat(BeatFraction.Half))
        music.playTone(659, music.beat(BeatFraction.Half))
        music.playTone(587, music.beat(BeatFraction.Half))
        music.playTone(554, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Double))
        music.playTone(880, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(659, music.beat(BeatFraction.Half))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Half))
        music.playTone(554, music.beat(BeatFraction.Double))
        music.playTone(554, music.beat(BeatFraction.Half))
        music.playTone(659, music.beat(BeatFraction.Half))
        music.playTone(523, music.beat(BeatFraction.Half))
        music.playTone(784, music.beat(BeatFraction.Whole))
        music.playTone(554, music.beat(BeatFraction.Half))
        music.playTone(392, music.beat(BeatFraction.Double))
        music.playTone(880, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(659, music.beat(BeatFraction.Half))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Half))
        music.playTone(554, music.beat(BeatFraction.Whole))
    }
})
forever(function () {
    if (Screen == 3) {
        badguy.setFlag(SpriteFlag.Invisible, true)
        tiles.destroySpritesOfKind(SpriteKind.Enemy)
        if (Math.abs(OldMan.x - Character.x) < 48 && canTalk == 0) {
            canTalk = 1
            TalkButton = sprites.create(assets.image`TalkButton`, SpriteKind.Interactive)
            TalkButton.setPosition(OldMan.x, OldMan.y - 15)
        }
    } else if (Screen == 4) {
        if (Math.abs(strayminer.x - Character.x) < 48 && canTalk == 0 && Math.abs(strayminer.y - Character.y) < 16) {
            canTalk = 1
            TalkButton = sprites.create(assets.image`TalkButton`, SpriteKind.Interactive)
            TalkButton.setPosition(strayminer.x, strayminer.y - 15)
        }
    }
})
forever(function () {
    if (Screen != 1 && Screen != 2) {
        Direction()
    }
})
forever(function () {
    if (Screen == 0) {
        pause(3500)
        MakingCodeShort()
    } else if (Screen == -1) {
        pause(2000)
        MakingCodeShort()
    }
})
forever(function () {
    if (Screen == 3) {
        if (Math.abs(OldMan.x - Character.x) >= 48 && canTalk == 1) {
            canTalk = 0
            TalkButton.destroy()
        }
    } else if (Screen == 4) {
        if (Math.abs(strayminer.x - Character.x) >= 48 && canTalk == 1) {
            canTalk = 0
            TalkButton.destroy()
        }
    }
})
forever(function () {
    if (Screen != 1 && (Screen != 2 && Screen != -2)) {
        scene.cameraFollowSprite(Character)
    }
    if (ClassSelected == 1 && GenderSelected == 1) {
        characterSelected = 1
    } else {
        if (ClassSelected == 1 && GenderSelected == 2) {
            characterSelected = 2
        } else {
            if (ClassSelected == 2 && GenderSelected == 1) {
                characterSelected = 3
            } else {
                if (ClassSelected == 2 && GenderSelected == 2) {
                    characterSelected = 4
                } else {
                    if (ClassSelected == 3 && GenderSelected == 1) {
                        characterSelected = 5
                    } else {
                        if (ClassSelected == 3 && GenderSelected == 2) {
                            characterSelected = 6
                        } else {
                            if (ClassSelected == 4 && GenderSelected == 1) {
                                characterSelected = 7
                            } else {
                                if (ClassSelected == 4 && GenderSelected == 2) {
                                    characterSelected = 8
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
forever(function () {
    if (ClassSelected == 0) {
        animation.stopAnimation(animation.AnimationTypes.All, WizardBanner)
        animation.stopAnimation(animation.AnimationTypes.All, WarriorBanner)
        animation.stopAnimation(animation.AnimationTypes.All, MonkBanner)
        animation.stopAnimation(animation.AnimationTypes.All, ArcherBanner)
    } else {
        if (ClassSelected == 1) {
            animation.stopAnimation(animation.AnimationTypes.All, WarriorBanner)
            animation.stopAnimation(animation.AnimationTypes.All, ArcherBanner)
            animation.stopAnimation(animation.AnimationTypes.All, MonkBanner)
        } else {
            if (ClassSelected == 2) {
                animation.stopAnimation(animation.AnimationTypes.All, WizardBanner)
                animation.stopAnimation(animation.AnimationTypes.All, ArcherBanner)
                animation.stopAnimation(animation.AnimationTypes.All, MonkBanner)
            } else {
                if (ClassSelected == 3) {
                    animation.stopAnimation(animation.AnimationTypes.All, WizardBanner)
                    animation.stopAnimation(animation.AnimationTypes.All, WarriorBanner)
                    animation.stopAnimation(animation.AnimationTypes.All, MonkBanner)
                } else {
                    if (ClassSelected == 4) {
                        animation.stopAnimation(animation.AnimationTypes.All, WizardBanner)
                        animation.stopAnimation(animation.AnimationTypes.All, WarriorBanner)
                        animation.stopAnimation(animation.AnimationTypes.All, ArcherBanner)
                    }
                }
            }
        }
    }
})
