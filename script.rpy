

define narrator = Character(None)
define p = Character("Пётр", color="#9bd5ff")
define a = Character("Акари", color="#ffb3c7")
define s = Character("Сэнсэй", color="#ffd166")
define stranger = Character("Прохожий", color="#c7d2fe")

define gui.main_menu_background = "images/menu/main_menu_sakura.jpg"

# Переменные прогресса.
default jp_score = 0
default jp_total = 0
default akari_trust = 0
default confidence = 0

# -------------------------
# Шрифты.
# Файл шрифта нужно положить сюда:
# game/fonts/NotoSansJP-Regular.ttf
# -------------------------
define gui.text_font = "fonts/NotoSansJP-Regular.ttf"
define gui.name_text_font = "fonts/NotoSansJP-Regular.ttf"
define gui.interface_text_font = "fonts/NotoSansJP-Regular.ttf"
define gui.button_text_font = "fonts/NotoSansJP-Regular.ttf"
define gui.choice_button_text_font = "fonts/NotoSansJP-Regular.ttf"

init python:
    style.default.font = "fonts/NotoSansJP-Regular.ttf"
    style.say_dialogue.font = "fonts/NotoSansJP-Regular.ttf"
    style.say_label.font = "fonts/NotoSansJP-Regular.ttf"
    style.button_text.font = "fonts/NotoSansJP-Regular.ttf"
    style.choice_button_text.font = "fonts/NotoSansJP-Regular.ttf"
    style.interface_text.font = "fonts/NotoSansJP-Regular.ttf"

# -------------------------
# Фоны и CG.
# Файлы нужно положить в:
# game/images/bg/
# game/images/cg/
# -------------------------
image bg airport_arrival = "images/bg/bg_airport_arrival.jpg"
image bg airport_turnstiles = "images/bg/bg_airport_turnstiles.jpg"
image bg dorm_exterior_night = "images/bg/bg_dorm_exterior_night.jpg"

image cg airport_akari_intro = "images/cg/cg_airport_akari_intro.jpg"
image cg bus_stop_akari = "images/cg/cg_bus_stop_akari.jpg"
image cg bus_interior_akari = "images/cg/cg_bus_interior_akari.jpg"
image cg dorm_exterior_sensei = "images/cg/cg_dorm_exterior_sensei.jpg"

# Старые текстовые спрайты оставлены как запасной вариант.
image akari neutral = Text("Акари", size=72, color="#ffb3c7", outlines=[(2, "#000000", 0, 0)])
image akari smile = Text("Акари :)", size=72, color="#ffb3c7", outlines=[(2, "#000000", 0, 0)])
image sensei fox = Text("🦊\nСэнсэй", size=54, color="#ffd166", text_align=0.5, outlines=[(2, "#000000", 0, 0)])

transform left_center:
    xalign 0.25
    yalign 0.82

transform right_center:
    xalign 0.75
    yalign 0.82

screen learning_hud():
    frame:
        xalign 0.02
        yalign 0.04
        background "#00000088"
        padding (12, 8)
        vbox:
            spacing 2
            text "Японский: [jp_score]/[jp_total]" size 22 color "#ffffff"
            text "Уверенность: [confidence]" size 18 color "#d1d5db"

label start:
    $ jp_score = 0
    $ jp_total = 0
    $ akari_trust = 0
    $ confidence = 0

    show screen learning_hud

    jump chapter_1_start


label add_correct:
    $ jp_score += 1
    $ jp_total += 1
    return


label add_wrong:
    $ jp_total += 1
    return


label chapter_1_start:
    scene bg airport_arrival with fade

    "Глава 1. Первый день."
    "Огромное табло над головой мигает десятками строк."
    "Иероглифы, иероглифы, иероглифы — ни одного знакомого слова."
    "Люди обтекают тебя с двух сторон, как река камень."
    "В руке — смятый листок с адресом общежития, который ты не можешь прочитать."
    "В кармане — телефон, который отказывается ловить сеть."
    p "Так... с чего начать?"

    menu:
        "Так, спокойно. Наверняка здесь есть информационная стойка.":
            $ confidence += 1
            "Ты отыскиваешь взглядом информационную стойку."
            "Она действительно есть. Но чем ближе ты смотришь на вывески, тем сильнее понимаешь: без языка и сети ты всё равно застрял."
            "Ты так и не решаешься подойти."
        "Может, просто пойти за всеми? Куда-нибудь да выйду.":
            "Ты выбираешь самого уверенного на вид японца и осторожно идёшь следом."
            scene bg airport_turnstiles with dissolve
            "Но чем ближе выход, тем сильнее внутри поднимается паника."
            "Ты замедляешь шаг."
        "Надо найти хоть кого-то, кто говорит по-английски.":
            $ confidence += 1
            "Ты подходишь к нескольким людям и пытаешься заговорить на английском."
            "То ли твой английский звучит хуже, чем тебе казалось, то ли все слишком спешат."
            "Никого остановить не получается."

    "Именно в этот момент ты замечаешь девушку, которая смотрит на тебя с тёплой, немного понимающей улыбкой."

    jump chapter_1_scene_2


label chapter_1_scene_2:
    scene cg airport_akari_intro with dissolve

    a "Привет! Ты выглядишь так, будто только что с самолёта и уже успел потеряться. Я угадала?"
    p "..."

    menu:
        "Да, есть немного... А ты что, говоришь по-русски?":
            $ akari_trust += 1
            a "Да, говорю. Меня Акари зовут. А ты смелый — раз один приехал."
            a "Хочешь, покажу, как тут поздороваться?"
            a "Смотри: こんにちは — konnichiwa. Это значит «добрый день»."
        "こんにちは... а, точнее, здравствуйте!":
            call add_correct
            $ akari_trust += 2
            # Акари уже находится внутри CG.
            a "О, так ты уже хотя бы что-то знаешь, здорово!"
            a "Да, я говорю по-русски — отец из России."
            a "Меня Акари зовут. Давай помогу."
        "Просто кивнуть. Ты слишком растерян, чтобы говорить.":
            a "Да, говорю. Меня Акари зовут."
            a "Ничего, бывает. Первый день в другой стране — это не прогулка."
            a "Давай начнём с простого: こんにちは — konnichiwa. Это «добрый день»."

    a "Ну-ка, попробуй повторить."

    menu:
        "Конничива.":
            call add_correct
            $ confidence += 1
            # Акари уже находится внутри CG.
            a "Почти идеально! Kon-ni-chi-wa — четыре слога, видишь? Ты быстро схватываешь."
        "Коннитива.":
            call add_wrong
            a "Близко! Там в серединке не «ти», а «чи» — будто «чи-и-из» говоришь."
        "Коничива.":
            call add_wrong
            a "Близко! Но в начале звук «н» длиннее: kon-ni-chi-wa."

    a "Куда тебе нужно?"
    p "В школьное общежитие. Кажется. Если я правильно понял этот адрес."
    a "О, похоже, мне с тобой в одну школу! Пойдём, провожу."
    a "Заодно по дороге расскажу, что тут и как."

    jump chapter_1_scene_3


label chapter_1_scene_3:
    scene cg bus_stop_akari with fade

    "Акари останавливается у выхода и показывает куда-то вправо."
    "За стеклянными дверями шумит город — но уже не пугающе, а почти приветливо."
    "Ты чувствуешь огромную благодарность к девушке, которая потратила на тебя столько времени."
    a "Ну вот, автобус до общежития — каждые пятнадцать минут. Табличку с номером видишь? Это наш."

    menu:
        "Аригато... годзаймас тебе, Акари.":
            call add_wrong
            a "Почти! «Годзаймас» звучит так, будто ты уже выдохнул в конце."
            a "Надо «годзаймасу» — с лёгким «у» на конце."
        "Спасибо огромное, Акари. Ты меня реально спасла.":
            call add_wrong
            a "По-русски я и так знаю, что ты благодарен."
            a "А давай попробуем по-японски: arigatou gozaimasu. Это очень вежливое «большое спасибо»."
        "Аригато годзаймасу, Акари-сан!":
            call add_correct
            $ akari_trust += 1
            # Акари уже находится внутри CG.
            a "Ух ты, прямо всё правильно сказал! Очень вежливо. Я рада, что помогла."

    "Ты делаешь шаг назад и случайно задеваешь чемоданом чей-то велосипед."
    "Велосипед звякает, прохожий оборачивается."
    a "Ой, скажи sumimasen — это «извините»."

    menu:
        "Сумимасэн!":
            call add_correct
            $ confidence += 1
            stranger "..."
            "Прохожий кивает и спокойно улыбается."
            a "Отлично! Sumimasen — вообще суперполезное слово."
            a "Им можно и извиниться, и официанта позвать, и многое другое."
        "Простите!":
            call add_wrong
            "Прохожий растерянно смотрит на тебя."
            a "По-русски он не понимает, но ничего страшного."
            a "На будущее: sumimasen выручает почти в любой непонятной ситуации."
        "Промолчать.":
            call add_wrong
            "Ты замираешь. Акари быстро кланяется прохожему."
            a "Ничего, бывает. Просто запомни: sumimasen."

    "К остановке подъезжает автобус."
    a "Поехали. По дороге расскажу про школу."

    jump chapter_1_scene_4


label chapter_1_scene_4:
    scene cg bus_interior_akari with fade

    "Автобус мягко покачивается."
    "За окном проплывают неоновые вывески, но ты смотришь на них уже без страха."
    "Акари, кажется, тоже расслабилась — она устала, но всё равно улыбается."
    a "Ну что, первый день уже почти позади."
    a "Давай проверим, что у тебя получилось запомнить?"
    a "Как поздороваться по-японски?"

    menu:
        "こんにちは — konnichiwa.":
            call add_correct
            a "Да! Вот это уже похоже на начало нормального разговора."
        "ありがとう — arigatou.":
            call add_wrong
            a "Это «спасибо». А приветствие — konnichiwa."
        "すみません — sumimasen.":
            call add_wrong
            a "Это «извините». А поздороваться можно: konnichiwa."

    a "Теперь — как сказать очень вежливое «большое спасибо»?"

    menu:
        "ありがとうございます — arigatou gozaimasu.":
            call add_correct
            # Акари уже находится внутри CG.
            a "Именно. Очень хорошо."
        "こんにちは — konnichiwa.":
            call add_wrong
            a "Это «добрый день». Спасибо — arigatou gozaimasu."
        "おやすみ — oyasumi.":
            call add_wrong
            a "Это «спокойной ночи». Пригодится позже, но не сейчас."

    a "И последнее. Что сказать, если случайно кого-то задел?"

    menu:
        "すみません — sumimasen.":
            call add_correct
            $ confidence += 1
            a "Правильно. Самое полезное слово дня."
        "はい — hai.":
            call add_wrong
            a "Hai — это «да». А извиниться можно словом sumimasen."
        "さようなら — sayounara.":
            call add_wrong
            a "Это прощание. Лучше сказать sumimasen."

    scene bg dorm_exterior_night with fade

    "Автобус подъезжает к общежитию."
    a "Вот мы и на месте."
    a "Завтра увидимся в школе. Отдохни."
    a "おやすみ — oyasumi. Спокойной ночи."

    scene cg dorm_exterior_sensei with dissolve

    s "Неплохо для первого дня, ученик."
    s "Целых три новых слова. Вот это да."
    s "Хотя надо же с чего-то начинать — подмечено было верно."
    s "Завтра будет больше. Отдыхай."

    p "..."
    p "Так. Ладно. Галлюцинации от стресса. Бывает."

    hide screen learning_hud
    jump chapter_1_summary


label chapter_1_summary:
    scene bg dorm_exterior_night with fade

    $ percent = 0
    if jp_total > 0:
        $ percent = int((jp_score * 100.0) / jp_total)

    "Итоги прототипа."
    "Правильных учебных ответов: [jp_score] из [jp_total]."
    "Результат: [percent]%%."

    if percent >= 80:
        "Акари явно впечатлена твоим первым днём."
    elif percent >= 50:
        "Ты ошибался, но старался. Для первого дня это уже победа."
    else:
        "Пока тяжело, но ты хотя бы начал. Япония никуда не убежит."

    "Конец первого концепта."
    "Следующий шаг: добавить Главу 2, реальные фоны, спрайты Акари/Петра/Сэнсэя и музыку."

    return
