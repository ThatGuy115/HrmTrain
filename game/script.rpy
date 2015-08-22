# тут инитим всякую фигню для персонажей и xml загрузки
init python:

    # create all stuff for hermione character
    WTXmlLinker.prepareCharacterResources( 'hermione', 
        '00_ex_characters', '00_ex_characters/00_hermione', '00_ex_characters/00_hermione' )
    WTXmlLinker.prepareCharacterResources( 'daphne', 
        '00_ex_characters', '00_ex_characters/01_daphne', '00_ex_characters/01_daphne' )
    WTXmlLinker.prepareCharacterResources( 'snape', 
        '00_ex_characters', '00_ex_characters/02_snape', '00_ex_characters/02_snape' )
    WTXmlLinker.prepareCharacterResources( 'luna', 
        '00_ex_characters', '00_ex_characters/03_luna', '00_ex_characters/03_luna' )
    WTXmlLinker.prepareCharacterResources( 'phoenix', 
        '00_ex_characters', '00_ex_characters/04_phoenix', '00_ex_characters/04_phoenix' )


init:
    # Scenario initialization
    python:
        global arr
        global entries

    $arr=dict()
    $entries=[]

    python:
        global this
        this=This()
        global wtevent
        global screens
        screens=ScreenCollection()
        global choose
        choose=None
        global time
        time=Time()
        global music
        music=Music()

# Подключение модуля отладки 
    python:
        global debug
    $debug=Debug(-1) # Если 0 - ничего не происходит, иначе сбрасывает значения перемнных в файл debug.txt
    $debug.SaveHeader()

    python:
# Описание предметов
        itemDefaults=[
        ("candy", "Чупа-чупс", 20, "03_hp/18_store/11.png", 
            "Чупа-чупс. Взрослая конфета для детей или детская конфета для взрослых?", "gifts", None ),
        ("chocolate", "Шоколад", 40, "03_hp/18_store/12.png", 
            "Рецепт этого восхитительного молочного шоколада держится в секрете. (По слухам, он содержит сушеных фей).", "gifts", None ),
        ("owl", "Плюшевая сова", 35, "03_hp/18_store/22.png", 
            "Игрушечная сова, набитая перьями настоящей совы. Она такая мягкая!", "gifts", None ),
        ("beer", "Сливочное пиво", 50, "03_hp/18_store/21.png", 
            "Девушки не могут устоять перед этим вкусом. Поэтому всегда пользуются большим спросом среди мальчиков. \n {size=-4}. Предупреждение: употребление алкоголя не допускается несовершеннолетними, без присмотра взрослых {/size}", "gifts", None ),
        ("mag1", "Обучающий журнал", 30, "03_hp/18_store/17.png", 
            "Образовательный журнал. \nВерный спутник каждого изгоя.", "gifts", None ),
        ("mag2", "Женский журнал", 45, "03_hp/18_store/18.png", 
            "Женский журнал. \nВсе крутые девчонки читают их.", "gifts", None ),
        ("mag3", "Журнал для взрослых", 60, "03_hp/18_store/19.png", 
            "Ваш парень превращается в хорошего мальчика? \nВаш муж больше не использует вас по назначению?\nВсе, что вы ждали о отношениях, любви и сексе. В основном о сексе.", "gifts", None ),
        ("mag4", "Порно журнал", 80, "03_hp/18_store/20.png", 
            "Дайте их своей девушке, чтобы проверить ее, своей жене, чтобы постыдить ее и вашей дочери, чтобы избежать \"разговоров\".", "gifts", None ),
        ("condoms", "Упаковка презервативов", 50, "03_hp/18_store/10.png", 
            "\"Презервативы Розовый единорог\". \nПокажите всем однорогое существо!\n{size=-4}Может содержать слюну реального единорога.{/size}", "gifts", None ),
        ("perfume", "Духи", 150, "03_hp/18_store/33.png", 
            "Духи \"В добрые руки\" источают невыразимый аромат и даются только в добрые руки.", "gifts", None ),
        ("vibrator", "Вибратор", 55, "03_hp/18_store/13.png", 
            "Великолепный, волшебный усиленный вибратор изготовлен из лозы дерева, с ядром жилы дракона.", "gifts", None ),
        ("lubricant", "Банка лубриканта", 60, "03_hp/18_store/09.png", 
            "Банка анальной смазки. Купите это любимому человеку - покажите, что вы заботитесь о нем/ней.", "gifts", None ),
        ("ballgag", "Кляп и наручники", 70, "03_hp/18_store/15.png", 
            "Кляп и манжеты, превратите свою вторую половинку в вашего сокамерника.", "gifts", None ),
        ("plug", "Анальная пробка", 85, "03_hp/18_store/16.png", 
            "Анальные пробки украшены настоящими хвостами. \nРазные размеры, чтобы удовлетворить экспертов, практиков и начинающих.", "gifts", None ),
        ("strapon", "Страпон \"Фестрал\"", 200, "03_hp/18_store/14.png", 
            "Cтрапон \"Фестрал\".\nКогда вы его увидите - потеряете дар речи.", "gifts", None ),
        ("krum", "Постер Виктора Крама", 0, "03_hp/18_store/26.png", 
            "Мастер по квиддичу, Виктор был выбран, чтобы играть за национальную сборную Болгарии по квиддичу. Несмотря на то, что он все еще ходит в школу, он по праву считается одним из лучших игроков в мире.", "cupboard", None ),
        ("lingerie", "Сексуальное нижнее белье", 0, "03_hp/18_store/24.png", 
            "Сексуальное нижнее белье \"Добрая Фея\". В постели она станет подобна императрице или сестрам Саббат.", "cupboard", None ),
        ("broom", "Леди Спид Стик-2000", 0, "03_hp/18_store/25.png", 
            "\"Леди Спид Стик-2000\", элегантный способ передвижения для страстных ведьм. Торговой маркой гарантируется полное удовлетворение от эффекта. Закажите одну штуку для вашей ведьмы, и она больше не будет использовать ее скучную старую метлу!", "cupboard", None ),
        ("sexdoll", "Секс-кукла \"Джуанна\"", 0, "03_hp/18_store/23.png", 
            "Секс-кукла \"Джуанна\"... Очень реалистичная. Выглядит почти как настоящий человек под каким-то заклинанием.", "cupboard", None ),
        ("shortskirt", "Школьная средняя юбка (40 см)", 200, "03_hp/18_store/07.png", 
            "Школьная средняя юбка. Знаметно улучшает оценки.", "gears_skirt", None ),
        ("xshortskirt", "Школьная короткая юбка (35 см)", 300, "03_hp/18_store/07.png", 
            "Школьная короткая юбка. Значительно улучшает оценки.", "gears_skirt", None ),
        ("xxshortskirt", "Школьная игривая юбка (30 см)", 500, "03_hp/18_store/07.png", 
            "Школьная игривая юбка. Для игр и игрищ. Сильно улучшаяет оценки.", "gears_skirt", None ),
        ("xsmallskirt", "Школьная мини-юбка (25 см)", 1000, "03_hp/18_store/07.png", 
            "Школьная мини-юбка. Резко улучшает оценки. Повышает рейтинг игры до 12+.", "gears_skirt", None ),
        ("xxsmallskirt", "Школьная микро-юбка (20 см)", 2000, "03_hp/18_store/07.png", 
            "Школьная микро-юбка. Фантастически улучшает оценки. Повышает рейтинг игры до 16+.", "gears_skirt", None ),
        ("xxxsmallskirt", "Школьная нано-юбка (10 см)", 0, "03_hp/18_store/07.png", 
            "Школьная нано-юбка. Заставляет всех забыть про оценки. В том числе и учителей. Повышает рейтинг игры до 35+.", "gears_skirt", None ),
        ("skirt_cheerleader", "Юбка болельщицы Гриффиндора", 500, "03_hp/18_store/07.png", 
            "Юбка болельщицы Гриффиндора. Настоящая. Остерегайтесь подделок.", "gears_skirt", None ),
        ("skirt_business", "Миниюбка бизнес-леди", 1000, "03_hp/18_store/07.png", 
            "Миниюбка бизнес-леди. Чем меньше прикрыты ноги, тем выгоднее условия контракта.", "gears_skirt", None ),
        ("skimpyshirt", "Школьная рубашка-минитопик", 1500, "03_hp/18_store/07.png", 
            "Школьная рубашка-минитопик. Будит в окружающих зверя. Если точнее - мартовского кота.", "gears_shirt", None ),
        ("shirt_cheerleader", "Кофта болельщицы Гриффиндора", 300, "03_hp/18_store/07.png", 
            "Кофта болельщицы Гриффиндора. Стимулирует игроков сильнее играть, а болельщиков сильнее болеть.", "gears_shirt", None ), 
        ("shirt_business", "Белая рубашка в деловом стиле", 300, "03_hp/18_store/07.png", 
            "Белая рубашка в деловом стиле. Цвет непорочности для порочных.", "gears_shirt", None ), 
        ("ball_dress", "Бальное платье", 500, "03_hp/18_store/01.png", 
            "Роскошное вечернее платье для особых случаев", "gears_dress", None ),
        ("badge", "Значок \"А.В.Н.Э.\"", 100, "03_hp/18_store/29.png", 
            "Значок \"А.В.Н.Э.\". Симулируй заботу...", "gears_other", None ),
        ("nets", "Ажурные чулки", 200, "03_hp/18_store/30.png", 
            "Ажурные чулки. Вопреки распространенному мнению, они не были изобретены рыбаком.", "gears_stockings", None ),
        ("tights", "Колготки", 100, "03_hp/18_store/30.png", 
            "Колготки. Не кантовать.", "gears_stockings", None ),
        ("wine", "Вино Дамблдора", 0, "03_hp/18_store/27.png", 
            "Бутылка из тайника профессора Дамблдора...", "cupboard", None ),
        ("potions", "Неизвестное зелье", 0, "03_hp/18_store/32.png", 
            "Какое-то зелье...", "cupboard", None ),
        ("dress", "Школьная рубашка с жилеткой", 0, "03_hp/18_store/01.png", 
            "Школьная рубашка с жилеткой", "gears_shirt", None ),
        ("standart2", "Школьная рубашка без жилетки", 0, "03_hp/18_store/01.png", 
            "Школьная рубашка без жилетки", "gears_shirt", None ),
        ("standart3", "Школьная рубашка без жилетки и галстука", 0, "03_hp/18_store/01.png", 
            "Школьная рубашка без жилетки и галстука", "gears_shirt", None ),
        ("standart4", "Школьная рубашка, расстегнутая сверху", 0, "03_hp/18_store/01.png", 
            "Школьная рубашка, расстегнутая сверху", "gears_shirt", None ),
        ("standart5", "Школьная рубашка, расстегнутая сверху и снизу", 0, "03_hp/18_store/01.png", 
            "Школьная рубашка, расстегнутая сверху и снизу", "gears_shirt", None ),
        ("panties", "Скромные белые трусики", 0, "03_hp/18_store/01.png", 
            "Скромные белые трусики", "gears_panties", None ),
        ("skirt", "Школьная длинная юбка (50см)", 0, "03_hp/18_store/01.png", 
            "Школьная длинная юбка.", "gears_skirt", None ),
        ("scroll", "Священный свиток", 300, "03_hp/18_store/31.png", 
            "Священный свиток содержит тайные знания...", "scroll", None), # {"pic":"03_hp/19_extras/xx.png"} )
        ("hair_wavy_black", "Обычная прическа (брюнетка)", 0, "03_hp/18_store/01.png", 
            "Обычная прическа (брюнетка)", "gears_hair", None ),
        ("hair_wavy_blonde", "Обычная прическа (блондинка)", 0, "03_hp/18_store/01.png", 
            "Обычная прическа (блондинка)", "gears_hair", None ),
        ("hair_wavy_red", "Обычная прическа (рыжая)", 0, "03_hp/18_store/01.png", 
            "Обычная прическа (рыжая)", "gears_hair", None ),
        ("hair_basic", "Обычная прическа (каштанка)", 0, "03_hp/18_store/01.png", 
            "Обычная прическа (каштанка)", "gears_hair", None ),
        ("hair_parade", "Прическа для выпускного", 0, "03_hp/18_store/01.png", 
            "Прическа для выпускного", "gears_hair", None ),
        ("hair_set", "Средства для волос \"Ведьмодница 2000\"", 500, "03_hp/18_store/07.png", 
            "Волшебный набор для ухода за волосами. И пусть ваш избранник потеряется в пышных локонах.", "gears_other", None ),

        ]

#        ("hair_ponytail_brown", "Хвостик (каштанка)", 0, "03_hp/18_store/01.png", 
#            "Хвостик (каштанка)", "gears_hair", None ),
#        ("hair_updo_black", "Пышная укладка (брюнетка)", 0, "03_hp/18_store/01.png", 
#            "Пышная укладка (брюнетка).", "gears_hair", None ),
#        ("hair_updo_brown", "Пышная укладка (каштанка)", 0, "03_hp/18_store/01.png", 
#            "Пышная укладка (каштанка)", "gears_hair", None ),
#        ("hair_wacky_black", "Буйная прическа (брюнетка)", 0, "03_hp/18_store/01.png", 
#            "Буйная прическа (брюнетка)", "gears_hair", None ),
#        ("hair_wacky_blonde", "Буйная прическа (блондинка)", 0, "03_hp/18_store/01.png", 
#            "Буйная прическа (блондинка)", "gears_hair", None ),
#        ("hair_wacky_red", "Буйная прическа (рыжая)", 0, "03_hp/18_store/01.png", 
#            "Буйная прическа (рыжая)", "gears_hair", None ),
#        ("hair_wavy_combed_brown", "Собранные волосы (каштанка)", 0, "03_hp/18_store/01.png", 
#            "Собранные волосы (каштанка)", "gears_hair", None ),

        
        

# Заполнение массива предметов
        itemList=[]
        for t in itemDefaults:
            (s, _caption, _price, _img, _description, _block, _constVals)=t
            SetArrayValue(s, "caption", _caption) 
            SetArrayValue(s, "price", _price) 
            SetArrayValue(s, "description", _description) 
            SetArrayValue(s, "img", _img) 
            SetArrayValue(s, "block", _block)
            if _constVals!=None:
                for o in _constVals:
                    SetArrayValue(s, o, _constVals[o]) 
            
            itemList.append(RegEntry(Item(s, 0)))

# Инициализация коллекций предметов
        global itsDAHR
        itsDAHR=RegEntry(ItemCollection("DAHR",{"gears":1, "gifts":3, "scroll":13, "gears_shirt":1, "gears_skirt":1, "gears_stockings":1, "gears_other":1, "gears_dress":1}))

        global itsOWL
        itsOWL=RegEntry(ItemCollection("OWL"))

# Инициализация персон
        global hero
        hero=RegEntry(Person("hero", "Джинн", 
            defVals={"perfumeused": 0})           
            )

        global hermi
        hermi=RegEntry(Person("hermione", "Гермиона", CharacterExData(WTXmlLinker.getLinkerKey_hermione()),
            defVals={"pos": POS_410, "pos2": gMakePos( 390, 340 ), 
                "SCUKO_presented":False, "incomePercent":0, "pointsPerDaphneVisit":0},
                constVals={"pos_door": gMakePos( 410, 0 ), "pos_doorleft": gMakePos( 370, 0 )}))        
        SetArrayValue("chibihermione", "door", [610,250])
        SetArrayValue("chibihermione", "center", [400,250])
        
        global daphne
        daphne=RegEntry(Person("daphne", "Дафна", CharacterExData( WTXmlLinker.getLinkerKey_daphne()), 
            defVals={"pos": POS_140, "pos2": gMakePos( 340, 420 ), 
                "visitInterval":1}, 
            constVals={"pos_door": gMakePos( 460, -60 ), "pos_center": POS_140}))
        SetArrayValue("chibidaphne", "door", [610,220])
        SetArrayValue("chibidaphne", "center", [370,220])

        global snape
        snape=RegEntry(Person("snape", "Северус Снейп", CharacterExData(WTXmlLinker.getLinkerKey_snape()),
            defVals={"pos": POS_140, "pos2": gMakePos( 340, 430 )}, 
            constVals={"pos_door": gMakePos( 350, 0 ), "pos_doorleft": gMakePos( 300, 0 ), "pos_center": POS_140}))
        SetArrayValue("chibisnape", "door", [610,210])
        SetArrayValue("chibisnape", "center", [360,210])
        
        global luna
        luna=RegEntry(Person("luna", "Луна", CharacterExData( WTXmlLinker.getLinkerKey_luna()), 
            defVals={"pos": POS_320, "pos2": gMakePos( 340, 420 )}, 
            constVals={"pos_door": gMakePos( 460, -60 ), "pos_center": POS_140}))
        SetArrayValue("chibiluna", "door", [610,220])
        SetArrayValue("chibiluna", "center", [370,220])
        
        global phoenix
        phoenix=RegEntry(Person("phoenix", "Феникс", CharacterExData( WTXmlLinker.getLinkerKey_phoenix()), 
            defVals={"pos": POS_610f, "pos2": gMakePos( 340, 420 )}, 
            constVals={"pos_door": gMakePos( 460, -60 ), "pos_center": POS_140}))
        SetArrayValue("chibiphoenix", "door", [610,220])
        SetArrayValue("chibiphoenix", "center", [370,220])



# Создание объектов ивентов 
# По сути - Описание сценария от начала до открытия покупки сексуальных услуг
        this.Where({"DAY"})     .AddStep("event_01",                 ready= lambda e: day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined )
        this.Where({"NIGHT"})   .AddStep("event_02",                 ready= lambda e: day == 1 )
        this                    .AddStep("event_03",                 ready= lambda e: day == 2 )
        this                    .AddStep("event_05",                 ready= lambda e: day == 4 )
        this                    .AddStep("event_07:snape_summon",    ready= lambda e: day == 5 )
        this.Where({"DAY"})     .AddStep("event_08",                 ready= lambda e: day >= 8 )
        this.Where({"SNAPE"})   .AddStep("special_date_with_snape")
        this.Where({"DAY"})     .AddStep("event_08_02",              ready= lambda e: e.prev.prev.IsAgo(2) ) 
        this                    .AddStep("event_08_03",              ready = lambda e: e.prev.IsAgo(2) )
        this                    .AddStep("event_09",                 ready = lambda e: e.prev.IsAgo(2) )
        this.Where({"SNAPE"})   .AddStep("special_date_with_snape_02")
        this.Where({"NIGHT"})   .AddStep("event_11",                 ready = lambda e: e.prev.IsAgo(2))
        this                    .AddStep("event_12",                 ready = lambda e: e.prev.IsAgo(2))
        this                    .AddStep("event_13",                 ready = lambda e: e.prev.IsAgo(2))
        this.Where({"DAY"})     .AddStep("event_14:her_summon")
        this.Where({"CHITCHAT"}).AddStep("chitchat_event_01",        ready = lambda e: e.prev.IsAgo(2))
        this.Where({"NIGHT"})   .AddStep("event_15:her_wants_buy",   ready = lambda e: e.prev.IsAgo(7))


        li={"01":"\"Поговори со мной\"", "02": "\"Отличные трусики!\"", "04":"\"Полапать грудь!\"", "05":"Полапать попку!", "08":"\"Покажи их мне!\"", 
            "11":"\"Станцуй для меня!\"", "12":"\"Дай мне потрогать их!\"", "16":"\"Потрогай меня!\"", "22":"\"Соси его!\"", "29":"\"Давай займемся сексом!\"", "31":"\"Время для анала!\""}
        for s in li:
            this.AddEvent("new_request_"+s+"::"+li[s], points={"private"}, defVals={"heartCount": 0}) 

# Отчеты Гермионы о публичных ивентах (за исключением 30_a, он - днем). Публичные ивенты состоят из 2-х частей. Днем - задание (обычный вызов из пункта меню) и отчет вечером 
# Можно избавиться и от десятка переменных первоначальной версии, а прогресс хранить в специальном поле объекта Event, но это приведет к довольно серьезной правке кода, что чревато ошибками. 
# Так что только убираем флажки можно/нельзя выполнять, а прогресс пусть остается во внешних переменных, как был
        tu=["02_b", "02_c", "03", "10", "15", "20", "23", "24", "30"]
        for s in tu:
            s="new_request_"+s
            # 3-й ивент добавляем здесь, он должен по порядку идти перед завершающим
            if s=="new_request_03": 
                this.AddEvent(s+"::\"Вор трусиков\"", points={"private"}, defVals={"heartCount": 0})
            else:
                this.AddEvent(s, points={"public"}) 
            s+="_complete"
            this.Where({"NIGHT"}, s).AddStep(s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 


# Следующее событие (первый раз трахнуться с одноклассниками) НЕ помещено в главный сценарий. 
# Т.е. может быть не выполнено никогда, а последующие в списке события все равно могут выполняться
# Однако в списке событий предшествует последующим - сделано для того, чтобы если событие может выполняться, оно имело приоритет перед оставшимися
# Если флаг request_30_a установить (устанавливается при вызове request_30 ветка 1), запустится разово 
        this.Where({"DAY"},"new_request_30_complete_a").AddStep("new_request_30_complete_a", ready = lambda e: request_30_a) 
# Аналогичное событие, которое может никогда не произойти - Герми уловила запах духов        
        this.Where({"HERMIENTER"},"giving_perfume").AddStep("giving_perfume", ready = lambda e: hero._perfumeused==time.stamp) 

        this.Where({"DAY"})     .AddStep("want_to_rule",             ready = lambda e: hermi.whoring >= 15) # Запустится, как только whoring превысит значение
        this                    .AddStep("against_the_rule",         ready = lambda e: e.prev.IsAgo(2)) # Через два дня
        this                    .AddStep("crying_about_dress",       ready = lambda e: hermi.whoring >= 18 and e.prev.IsAgo(5)) # Через 5 дней и при соответствующем уровне развращенности
        this                    .AddStep("sorry_about_hesterics") 

        this.Where({})          .AddStep("giving_thre_dress")
        this.Where({"NIGHT"})   .AddStep("good_bye_snape",           ready = lambda e: e.prev.IsAgo(2)) 

# КОНЕЦ ГЛАВНОГО СЦЕНАРИЯ

### DR'S NEWSPAPER ooo ###

        tu=["rights_1","rights_2","rights_3","rights_4","rights_5","magls_1","magls_2","magls_3","magls_4","magls_5","kviddich_1","kviddich_2","kviddich_3","kviddich_4","kviddich_5","kviddich_6"]
        for s in tu:
            s="nsp_event_"+s
            this.AddEvent(s) 
            s+="_complete"
            this.Where({"NIGHT"}, s).AddStep(s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 
            
#        tu=["sex_1","sex_2","sex_3","sex_4","sex_5","maniac_1","maniac_2","maniac_3","nude_1","nude_2","nude_3","nude_4","nude_5"]
#        for s in tu:
#            s="nsp_event_"+s
#            this.AddEvent(s) 
#            s+="_complete" 
#            this.Where({"NIGHT"}, s).AddStep(s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 
            
        tu=["forest_1"]
        for s in tu:
            s="nsp_event_"+s
            this.AddEvent(s) 
            s+="_complete"
            this.Where({"DAY"}, s).AddStep(s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 
            
        tu=["forest_2","studio_1","studio_2","studio_3","studio_4","studio_5","studio_6"]
        for s in tu:
            s="nsp_event_"+s
            this.AddEvent(s) 
            s+="_complete"
            this.Where({"NIGHT"}, s).AddStep(s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 

###

# ВЕТКА ДАФНЫ
# Ветка включается при вызове Снейпа ночью после того, как отработает ивент со Cнейпом, где он хвалится как трахает студенток
        this.Where({"SNAPE"},"daphne").AddStep("daphne_pre_01",        ready = lambda e: snape_events >= 6) 
        this.Where({"DAY"},"daphne").AddStep("daphne_pre_02",        ready = lambda e: e.prev.IsAgo(2)) 
        this.Where({"SNAPE", "CHITCHAT"},"daphne").AddStep("daphne_pre_03") 
        this.Where({"MAIL"},"daphne").AddStep("daphne_pre_04",        ready = lambda e: e.prev.IsAgo(3)) 
        this.Where({"SNAPE", "CHITCHAT"},"daphne").AddStep("daphne_pre_05") 
        this.Where({"MAIL"},"daphne_pre_06").AddStep("daphne_pre_06", ready = lambda e: e.prevInList.IsAgo(2)) 
        this.Where({"HERMICHAT"},"daphne").AddStep("daphne_pre_07",   ready = lambda e: e._start2+2<=day)
# Будет стартовать через день, пока не завершится daphne_pre_finish
        this.Where({"DAY"},"daphne").AddStep("daphne_pre_finish",     ready = lambda e: (e.prev.prevInList.IsFinished() and e.prev.IsAgo(2) and e._start2+2<=day), done=lambda e: e._finishCount>=4, constVals={"members":{"daphne"}}) 

        this.AddEvent("daphne_approaching", constVals={"members":{"daphne"}}) # Это просто для счетчика вызывалась ли Дафна сегодня (ну и для отладки может помочь)

# Поскольку точка "DAPHENTER" предваряет вызов меню и ивентов ниже, никаких дополнительных условий в ивентах меню не требуется
        this.Where({"DAPHENTER"},"dap_interlude_02").AddStep("dap_interlude_02", ready=lambda e: this.dap_request_02._finishCount>=1,constVals={"members":{"daphne"}})

        li={"05":["\"Научите меня\"","#(Перейдем непосредственно к тренеровке...)"]}
        for s in li:
                this.AddEvent("dap_request_"+s+"::"+li[s][0], points={"daphne_private"}, constVals={"eventPlan":li[s][1], "members":{"daphne"}}, defVals={"heartCount": 0}) 

        li={"04":["\"Больше откровенности\"","#(Полагаю алкоголь раскрепостит её...)"]}
        for s in li:
                this.AddEvent("dap_request_"+s+"::"+li[s][0], points={"daphne_private"}, constVals={"eventPlan":li[s][1], "members":{"daphne"}}, defVals={"heartCount": 0}) 

        li={"03":["\"Популярность\"","#(Пора занять её чем-то новым...)"]}
        for s in li:
            __s="dap_request_"+s
            this.AddEvent(__s+"::"+li[s][0], points={"daphne_public"}, constVals={"eventPlan":li[s][1], "members":{"daphne"}})
            __s+="_complete"
            this.Where({"NIGHT"}, __s).AddStep(__s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 

        li={"02":["\"Покажись!\"","#(Становится жарковато. Предложу ей что-нибудь снять...)"]}
        for s in li:
                this.AddEvent("dap_request_"+s+"::"+li[s][0], points={"daphne_private"}, constVals={"eventPlan":li[s][1], "members":{"daphne"}}, defVals={"heartCount": 0}) 

        li={"01":["\"Расскажи о девушках\"","#(Я расспрошу ее о ее подружках...)"]}
        for s in li:
            __s="dap_request_"+s
            this.AddEvent(__s+"::"+li[s][0], points={"daphne_public"}, constVals={"eventPlan":li[s][1], "members":{"daphne"}})
            __s+="_complete"
            this.Where({"NIGHT"}, __s).AddStep(__s,  done = lambda e: e._finishCount>=e.prevInList._finishCount) 




# Книги. Полный цикл от покупки в магазине Дахра до прочтения, до получения бонусов

#  Внимание!!! Порядок кортежей внутри списка менять следует с осторожностью. 
# Лоика обработки в дальнейшем предполагает, что группы книг по каждому навыку следуют в порядке от минимального к максимальному
# и группы разделены книгами другой направленности  (другой block)
        tu=[
        
            ("book_01::\"Медная книга духа\"",            80, "03_hp/18_store/08.png", "Эта книга описывает элементарные приемы, позволяющие улучшить свою концентрацию.",
                "шанс 1 к 6, что я завершу дополнительную главу при чтении книг и во время работы с отчетом."),
            ("book_02::\"Бронзовая книга духа\"",         160, "03_hp/18_store/08.png", "Эта книга описывает базовые приемы, позволяющие улучшить свою концентрацию.",
                "шанс 1 к 4, что я завершу дополнительную главу при чтении книг и во время работы с отчетом."),
            ("book_03::\"Серебрянная книга духа\"",       250, "03_hp/18_store/08.png", "Эта книга описывает продвинутые приемы, позволяющие улучшить свою концентрацию.",
                "шанс 1 к 2, что я завершу дополнительную главу при чтении книг и во время работы с отчетом. "),
            ("book_04::\"Золотая книга духа\"",          300, "03_hp/18_store/08.png", "Эта книга описывает экспертные приемы, позволяющие улучшить свою концентрацию.",
                "я всегда буду завершать дополнительную главу как при чтении книг, так и при работе с отчетами."),

            ("book_05::\"Сказ о Галадриэле. Книга I.\"", 200, "03_hp/18_store/04.png", "Эта книга рассказывает историю эльфийской принцессы, которая бросает вызов традициям своего народа и выбирает оковы для ее собственной судьбы. Или все не так?",
                "В результате мое воображение улучшилось."),          
            ("book_05_b::\"Сказ о Галадриэле. Книга II.\"",250, "03_hp/18_store/05.png", "Эта книга рассказывает историю эльфийской принцессы, которая бросает вызов традициям своего народа и выбирает оковы для ее собственной судьбы. Или все не так?",
                "В результате мое воображение улучшилось."),

            ("book_08::\"Скорочтение для чайников\"",     50, "03_hp/18_store/08.png", "Эта книга содержит несколько базовых методов, которые помогут вам улучшить навык скорочтения.",
                "небольшой шанс прочесть дополнительную главу, во время чтения."),
            ("book_09::\"Скорочтение для любителей\"",    90, "03_hp/18_store/08.png", "Эта книга содержит несколько продвинутых методов, которые помогут вам улучшить навык скорочтения.",
                "большой шанс закончить дополнительную главу, во время чтения."),
            ("book_10::\"Скорочтение для экспертов\"",    150, "03_hp/18_store/08.png", "Эта книга содержит несколько экспертных методов, которые помогут вам улучшить навык скорочтения.",
                "всегда заканчивать дополнительную главу во время чтения"),
            ("book_06::\"Игра Кресел\"",                 100, "03_hp/18_store/02.png", "Эпический рассказ о предательстве, убийствах и изнасилованиях, а затем еще несколько убийств, немного больше предательства и еще больше изнасилований.",
                "В результате мое воображение улучшилось.\nНо больше я не стану читать эту хрень!"),
            ("book_07::\"Моя дорогая вайфу\"",           300, "03_hp/18_store/03.png", "Переживите славные дни в вашей школе. Ваша сводная сестра Ши, учительница Мисс Стивенс или таинственная девушка из библиотеки? Кто станет вашей окончательной \"вайфу\"?",
                ""),
            ("book_12::\"Скорописание для чайников\"",    30, "03_hp/18_store/08.png", "Эта книга содержит несколько элементарных методов, которые позволят вам быстрее писать.",
                "шанс 1 к 6, что я завершу дополнительную главу, во время работы с отчетом. "),
            ("book_13::\"Скорописание для начинающих\"",  90, "03_hp/18_store/08.png", "Эта книга содержит несколько базовых методов, которые позволят вам быстрее писать.",
                "шанс 1 к 4, что я завершу дополнительную главу, во время работы с отчетом. "),
            ("book_14::\"Скорописание для любителей\"",  100, "03_hp/18_store/08.png", "Эта книга содержит несколько начальных методов, которые позволят вам быстрее писать.",
                "шанс 1 к 2, что я завершу дополнительную главу, во время работы с отчетом."),
            ("book_15::\"Скорописание для продвинутых\"",130, "03_hp/18_store/08.png", "Эта книга содержит несколько продвинутых методов, которые позволят вам быстрее писать.",
                "Теперь я настоящий мастер скорописания..."),
           ]

        for t in tu:
            (_sFullName, _price, _img, _description, _conclusion)=t
            if _img=="03_hp/18_store/08.png":
                _block="books_edu"
            else:
                _block="books_fict"

            lam=lambda e:e._status>=e._units
            if "book_07" in _sFullName: # У Вайфу морочливая обработка оставляю первоначальную на исходных флажках
                lam = lambda e: dear_waifu_completed_once
            wtevent=this.AddEvent(_sFullName,  
                ready= lambda e: GetStoreValue(e.Name, "status")>=0, done=lam , 
                defVals={"status": -2},
                constVals={"img": _img, "description":_description, "block":_block, "price":_price, "conclusion":_conclusion, "units": 10 if _block=="books_edu" else 20} )

#### DR'S NEWSPAPER ooo ###
# Товары для газеты

        tu=[("nsp_newsp_book_pre::\"Самоучитель газетного дела\"",           100, "08_newspaper_scenario/books/prebook.png", "Эта книга описывает элементарные основы оформления и публикации газеты.",
                "Теперь я могу издавать собственную газету."),
                ]

        for t in tu:
            (_sFullName, _price, _img, _description, _conclusion)=t
            _block="books_newsp"

            lam=lambda e:e._status>=e._units
            wtevent=this.AddEvent(_sFullName,  
                ready= lambda e: GetStoreValue(e.Name, "status")>=0, done=lam , 
                defVals={"status": -2},
                constVals={"img": _img, "description":_description, "block":_block, "price":_price, "conclusion":_conclusion, "units": 10} )
                
        

#######
#### DR'S NEWSPAPER ooo ###
# Товары для газеты
    python:

#        tu=[("nsp_newsp_book_p01::\"Журналистика для любителей\"",           120, "08_newspaper_scenario/books/Book_p1.png", "Эта книга описывает основы журналистики.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p02a::\"Журналистика для продвинутых. Том 1\"",           200, "08_newspaper_scenario/books/Book_p2a.png", "Эта книга описывает принципы журналистики.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p02b::\"Журналистика для продвинутых. Том 2\"",           300, "08_newspaper_scenario/books/Book_p2b.png", "Эта книга описывает принципы журналистики.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p03a::\"Журналистика для экспертов. Том 1\"",           500, "08_newspaper_scenario/books/Book_p3a.png", "Эта книга описывает секреты журналистики.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p03b::\"Журналистика для экспертов. Том 2\"",           600, "08_newspaper_scenario/books/Book_p3b.png", "Эта книга описывает секреты журналистики.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
               
#            ("nsp_newsp_book_p04::\"Стань писателем для любителей.\"",           300, "08_newspaper_scenario/books/Book_p4.png", "Эта книга описывает основы писательского ремесла.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p05a::\"Стань писателем для продвинутых. Том 1\"",           600, "08_newspaper_scenario/books/Book_p5a.png", "Эта книга описывает принципы писательского ремесла.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p05b::\"Стань писателем для продвинутых. Том 2\"",           800, "08_newspaper_scenario/books/Book_p5b.png", "Эта книга описывает принципы писательского ремесла.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p06a::\"Стань писателем для экспертов. Том 1\"",           1200, "08_newspaper_scenario/books/Book_p6a.png", "Эта книга описывает секреты писательского ремесла.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
#            ("nsp_newsp_book_p06b::\"Стань писателем для экспертов. Том 2\"",           1500, "08_newspaper_scenario/books/Book_p6b.png", "Эта книга описывает секреты писательского ремесла.",
#                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
#                ]

        tu=[("nsp_newsp_book_p01::\"Журналистика для любителей\"",           120, "08_newspaper_scenario/books/book.png", "Эта книга описывает основы журналистики.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p02a::\"Журналистика для продвинутых. Том 1\"",           200, "08_newspaper_scenario/books/book.png", "Эта книга описывает принципы журналистики.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p02b::\"Журналистика для продвинутых. Том 2\"",           300, "08_newspaper_scenario/books/book.png", "Эта книга описывает принципы журналистики.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p03a::\"Журналистика для экспертов. Том 1\"",           500, "08_newspaper_scenario/books/book.png", "Эта книга описывает секреты журналистики.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p03b::\"Журналистика для экспертов. Том 2\"",           600, "08_newspaper_scenario/books/book.png", "Эта книга описывает секреты журналистики.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
               
            ("nsp_newsp_book_p04::\"Стань писателем для любителей.\"",           300, "08_newspaper_scenario/books/book.png", "Эта книга описывает основы писательского ремесла.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p05a::\"Стань писателем для продвинутых. Том 1\"",           600, "08_newspaper_scenario/books/book.png", "Эта книга описывает принципы писательского ремесла.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p05b::\"Стань писателем для продвинутых. Том 2\"",           800, "08_newspaper_scenario/books/book.png", "Эта книга описывает принципы писательского ремесла.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p06a::\"Стань писателем для экспертов. Том 1\"",           1200, "08_newspaper_scenario/books/book.png", "Эта книга описывает секреты писательского ремесла.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                
            ("nsp_newsp_book_p06b::\"Стань писателем для экспертов. Том 2\"",           1500, "08_newspaper_scenario/books/book.png", "Эта книга описывает секреты писательского ремесла.",
                "Книга повысила мастерство написания статей. Кроме того, благодаря ей доступны новые журналистские задания."),
                ]

        for t in tu:
            (_sFullName, _price, _img, _description, _conclusion)=t
            _block="books_newsp"

            lam=lambda e:e._status>=e._units
            wtevent=this.AddEvent(_sFullName,  
                ready= lambda e: GetStoreValue(e.Name, "status")>=0, done=lam , 
                defVals={"status": -2},
                constVals={"img": _img, "description":_description, "block":_block, "price":_price, "conclusion":_conclusion, "units": 10} )
                
        tu=[("nsp_newsp_book_typo1::\"Типографический набор для любителей\"",           90, "08_newspaper_scenario/upd/Typo1.png", "Прилагающееся к типографическому набору руководство содержит все необходимое.",
                "Благодаря прочитанному руководству вы можете использовать \"Типографический набор для любителей\"."),
                
            ("nsp_newsp_book_typo2::\"Типографический набор для продвинутых\"",           200, "08_newspaper_scenario/upd/Typo2.png", "Прилагающееся к типографическому набору руководство содержит все необходимое.",
                "Благодаря прочитанному руководству вы можете использовать \"Типографический набор для продвинутых\"."),
                
            ("nsp_newsp_book_typo3::\"Типографический набор для профессионалов\"",           400, "08_newspaper_scenario/upd/Typo3.png", "Прилагающееся к типографическому набору руководство содержит все необходимое.",
                "Благодаря прочитанному руководству вы можете использовать \"Типографический набор для профессионалов\"."),
                
            ("nsp_newsp_book_typo4::\"Типографический набор для малых редакций\"",           800, "08_newspaper_scenario/upd/Typo4.png", "Прилагающееся к типографическому набору руководство содержит все необходимое.",
                "Благодаря прочитанному руководству вы можете использовать \"Типографический набор для малых редакций\"."),
                
            ("nsp_newsp_book_typo5::\"Типографический набор для средних редакций\"",          1500, "08_newspaper_scenario/upd/Typo5.png", "Прилагающееся к типографическому набору руководство содержит все необходимое.",
                "Благодаря прочитанному руководству вы можете использовать \"Типографический набор для средних редакций\"."),
               
            ("nsp_newsp_book_typo6::\"Типографический набор для больших редакций\"",          3000, "08_newspaper_scenario/upd/Typo6.png", "Прилагающееся к типографическому набору руководство содержит все необходимое.",
                "Благодаря прочитанному руководству вы можете использовать \"Типографический набор для больших редакций\"."),
                ]

        for t in tu:
            (_sFullName, _price, _img, _description, _conclusion)=t
            _block="books_newsp2"

            lam=lambda e:e._status>=e._units
            wtevent=this.AddEvent(_sFullName,  
                ready= lambda e: GetStoreValue(e.Name, "status")>=0, done=lam , 
                defVals={"status": -2},
                constVals={"img": _img, "description":_description, "block":_block, "price":_price, "conclusion":_conclusion, "units": 3} )
                
        tu=[("nsp_newsp_book_photo1::Фотоаппарат \"Гелиофотус 2\"",          250, "08_newspaper_scenario/photo/photo1.png", "Старинный фотоаппарат, способный делать вяло движущиеся черно-белые фотографии.",
                "Благодаря прочитанному руководству вы можете использовать \"Гелиофотус 2\"."),
                
            ("nsp_newsp_book_photo2::Фотоаппарат \"Обскура Магика 60\"",           500, "08_newspaper_scenario/photo/photo2.png", "Невзрачный фотоаппарат, содержащий в качестве основного элемента волшебную серебрянную пластину. Позволяет делать цветные фотографии средней активности.",
                "Благодаря прочитанному руководству вы можете использовать \"Обскура Магика 60\"."),
                
            ("nsp_newsp_book_photo3::Фотоаппарат \"Паномагик а777\"",           1000, "08_newspaper_scenario/photo/photo3.png", "Обработанный пылью фей фотоаппарат, напоминающий магловский ультразум. Способен делать активные 3д-фотографии.",
                "Благодаря прочитанному руководству вы можете использовать \"Паномагик а777\"."),
                
            ("nsp_newsp_book_photo4::Фотоаппарат \"Моменто Мемориус 2000\"",           2500, "08_newspaper_scenario/photo/photo4.png", "Мощнейший фотоаппарат, слабо светящийся в темноте. Сделанные им фото по-настоящему живут и способны даже выглядывать из кадра.",
                "Благодаря прочитанному руководству вы можете использовать \"Моменто Мемориус 2000\"."),

                ]

        for t in tu:
            (_sFullName, _price, _img, _description, _conclusion)=t
            _block="books_newsp2"

            lam=lambda e:e._status>=e._units
            wtevent=this.AddEvent(_sFullName,  
                ready= lambda e: GetStoreValue(e.Name, "status")>=0, done=lam , 
                defVals={"status": -2},
                constVals={"img": _img, "description":_description, "block":_block, "price":_price, "conclusion":_conclusion, "units": 2} )
                
        tu=[("nsp_newsp_book_video::Книга \"Я и мой шар\"",         5000, "08_newspaper_scenario/sphere/Book_sphere.png", "Книга о секретах использования полученного в хрустальном шаре изображения для газеты.",
                "Благодаря прочитанной книге вы можете помещать в газету видеоролики, показанные хрустальным шаром."),

                ]

        for t in tu:
            (_sFullName, _price, _img, _description, _conclusion)=t
            _block="books_newsp2"

            lam=lambda e:e._status>=e._units
            wtevent=this.AddEvent(_sFullName,  
                ready= lambda e: GetStoreValue(e.Name, "status")>=0, done=lam , 
                defVals={"status": -2},
                constVals={"img": _img, "description":_description, "block":_block, "price":_price, "conclusion":_conclusion, "units": 10} )

####### 


# Создает переменные одноименные с названиями ивентов. В результате к ивентам можно получить доступ не this("event_01") а this.event_01 
# Разница между вызовами: в первом случае происходит присваивание ивента переменной event. Во втором случае запоминания не происходит
        for e in this.List:
            exec("this."+e.Name+"=this.GetCall('"+e.Name+"')")
 
# Константы лямбы, используются в меню предметов при определении их доступности
        fn0=lambda o: True
        fn3=lambda o: hermi.whoring>=3


    call daphne_images_init

# Включить обработку перехода по меткам (label). 
    $onLabelExecute=lambda s: OnLabelExecute(s)


#    $renpy.game.onJumpExecute=lambda name, target,expression: OnJumpExecute(name, target,expression)
    



    
    $ commentaries = False # In the GALLERY turns commentaries ON and OFF. 
    
    image title2 = "title2.jpg"
    
    ### Disposable flags ###
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    $ d_flag_05 = False
    $ d_flag_06 = False
    $ d_flag_07 = False
    $ d_flag_08 = False
    $ d_flag_09 = False
    
    $ d_points = 0
    
    
    
    $ renpy.music.register_channel("bg_sounds", "sfx", True)
    $ renpy.music.register_channel("weather", "sfx", True)

    # Define some new transitions here.
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbulb2 = Fade(1, 0.5, 1, color='#fff')
    $ flashbb = Fade(0.2, 0.0, 0.8, color='#000')
    $ flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
    $ kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')
    
    #NVLE STUFF
    $ nvle = Character(color="#000", what_color="#ffffff", kind=nvl)
    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve
    
    $ layout.ARE_YOU_SURE = _("Вы уверены?")
    $ layout.DELETE_SAVE = _("Вы уверены, что хотите удалить сохранение?")
    $ layout.OVERWRITE_SAVE = _("Вы уверены, что хотите перезаписать это сохранение?")
    $ layout.LOADING = _("После загрузки вы потеряете весь текущий прогресс.\nВы уверены, что хотите сделать это?")
    $ layout.QUIT = _("Вы уверены, что хотите выйти?")
    $ layout.MAIN_MENU = _("Вы уверены, что хотите выйти в главное меню?\nЭто приведет к утере текущего прогресса.")
    $ layout.SLOW_SKIP = _("Вы уверены, что хотите начать пропуск текста?")
    $ layout.FAST_SKIP_UNSEEN = _("Вы уверены, что хотите пропустить следующий выбор?")
    $ layout.FAST_SKIP_SEEN = _("Вы уверены, что хотите пропустить следующий диалог или выбор?")
    #$ config.language = 'russian'
    
    # $ config.keymap['hide_windows'].remove('mouseup_2')
    # $ config.keymap['hide_windows'].remove('h')
    # $ config.keymap['hide_windows'].remove('joy_hide')
    
#define m = Character(None, window_left_padding=200, image="mage", color="#402313", ctc="ctc3", ctc_position="fixed")

###### Felix Locking ######

    $ felixblock = False

####################

label splashscreen:
    $ renpy.pause(0)
    scene black 
    with Pause(0.9)
    $ renpy.play('sounds/start.mp3')
    show image "logo/logo07.jpg" 
    pause 1
    with dissolve
    with Pause(2.0)
    
    scene black 
    with dissolve
    with Pause(1.0)

    return     
   
    
###TRANSITIONS###########
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)

###HARRY POTTER CHARACTERS###
image ch_hem 01 = "03_hp/animation/h_walk_01.png"




image bld2 = "slavem/bld2.png" 
image bld = "slavem/bld.png" 
image bg lp = "lpotion/lpfinal00.jpg"
image bg meadow = "meadow.jpg"
image bg magic = "meadowmagic.jpg"
image magic = "magic1.png"
image magic2 = "magic2.png"
image magic3 = "magic3.png"
image magic4 = "magic4.png"
image magic5 = "magic5.png"
image white = "white.jpg"
image tension = "quest01/fight.png"
image ctc3 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2, xpos=0.97, ypos=0.929, xanchor=1.0, yanchor=1.0)
image ctc4 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2, xpos=0.99, ypos=0.995, xanchor=0.8, yanchor=1.0)
image ctc7 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2,)
image whitefade = "whitefade.png"
image ariel1 = "ariel1.png"
image arielmad = "arielmad1.png"
image arielscream = "arielscream.png"
image asilent = "arielsilent.png"
image asulky = "arielsulky.png"
image threetits = "threetits/threetits01.png"
image threenormal = "threetits/threetits02.png"
image threetitsmad = "threetits/baretitsmad.png"
image threetitsmad2 = "threetits/baretitsmad2.png"
image slave02 = "slave/slave02.png"
image slave03 = "slave/slave03.png"
image slave04 = "slave/slave04.png"
image slave06 = "slave/slave01_04.png"
image threetitsmad4 = "threetits/baretitsmad4.png"
image blkfade = "blackfade.png"
image blk50 = im.Alpha("blackfade.png", 0.5) 







    #$#$# DAPHNE ANIMATIONS #$#$#

image dap_fap:
    "03_hp/24_daphne/dap_fap_a1.png"
    pause 0.8
    "03_hp/24_daphne/dap_fap_a1.png"
    pause 0.8
    "03_hp/24_daphne/dap_fap_a3.png"
    pause 0.8
    "03_hp/24_daphne/dap_fap_a4.png"
    pause 0.8
    "03_hp/24_daphne/dap_fap_a5.png"
    pause 0.8
    "03_hp/24_daphne/dap_fap_a6.png"
    pause 0.8
    restart

image dap_look_a1:
    "03_hp/24_daphne/dap_title_a1.png"

image dap_look_a2:
    "03_hp/24_daphne/dap_title_a2.png"

    ### INTRO MOVIE ANIMATIONS ###

image titleMain = "03_hp/23_title/01.png"

transform title_anim_fire:
    xpos 137 ypos 0 xanchor 0.5 yanchor 0.0
    "03_hp/23_title/title_fire_01.png"
    pause.1
    "03_hp/23_title/title_fire_02.png"
    pause.1
    "03_hp/23_title/title_fire_03.png"
    pause.1
    "03_hp/23_title/title_fire_04.png"
    pause.1
    "03_hp/23_title/title_fire_05.png"
    pause.1
    "03_hp/23_title/title_fire_06.png"
    pause.1
    "03_hp/23_title/title_fire_07.png"
    pause.1
    "03_hp/23_title/title_fire_08.png"
    pause.1
    "03_hp/23_title/title_fire_09.png"
    pause.1
    "03_hp/23_title/title_fire_10.png"
    pause.1
    "03_hp/23_title/title_fire_11.png"
    pause.1
    "03_hp/23_title/title_fire_12.png"
    pause.1
    "03_hp/23_title/title_fire_13.png"
    pause.1
    "03_hp/23_title/title_fire_14.png"
    pause.1
    repeat

transform title_anim_eyes:
    xpos 252 ypos 135 xanchor 0.5 yanchor 0.5
    "03_hp/23_title/title_eyes_1.png"
    pause 4.8
    "03_hp/23_title/title_eyes_1.png"
    pause 0.1    
    "03_hp/23_title/title_eyes_2.png"
    pause.1
    "03_hp/23_title/title_eyes_3.png"
    pause.1
    "03_hp/23_title/title_eyes_2.png"
    pause.1
    "03_hp/23_title/title_eyes_1.png"
    pause 0.8

### second circle
    "03_hp/23_title/title_eyes_1.png"
    pause 4.8
    "03_hp/23_title/title_eyes_1.png"
    pause 0.1 
    "03_hp/23_title/title_eyes_2.png"
    pause.1
    "03_hp/23_title/title_eyes_3.png"
    pause.1
    "03_hp/23_title/title_eyes_2b.png"
    pause.1
    "03_hp/23_title/title_eyes_1b.png"
    pause 0.8

### third circle
    "03_hp/23_title/title_eyes_1b.png"
    pause 1.2
    "03_hp/23_title/title_eyes_1b.png"
    pause 0.1 
    "03_hp/23_title/title_eyes_2b.png"
    pause.1
    "03_hp/23_title/title_eyes_3b.png"
    pause.1
    "03_hp/23_title/title_eyes_2.png"
    pause.1
    "03_hp/23_title/title_eyes_1.png"
    pause 0.8
    repeat

image intro_01:
    "03_hp/20_intro/01_01.png"
    pause 1
    "03_hp/20_intro/01_02.png"
    pause 1
    repeat

image intro_02:
    "03_hp/20_intro/02_01.png"
    pause 1
    "03_hp/20_intro/02_02.png"
    pause 1
    "03_hp/20_intro/02_01.png"
    pause 1
    "03_hp/20_intro/02_02.png"
    pause 1
    "03_hp/20_intro/02_03.png"
    pause.08
    "03_hp/20_intro/02_02.png"
    pause.08
    "03_hp/20_intro/02_03.png"
    pause.08
    repeat

image intro_03:
    "03_hp/20_intro/03_01.png"
    pause 1
    "03_hp/20_intro/03_02.png"
    pause 1
    repeat
    
image intro_04:
    "03_hp/20_intro/04_01.png"
    pause 1
    "03_hp/20_intro/04_02.png"
    pause 1
    repeat

image intro_05:
    "03_hp/20_intro/05_01.png"
    pause 1
    "03_hp/20_intro/05_02.png"
    pause 1
    repeat

image intro_06:
    "03_hp/20_intro/06_01.png"
    pause 1
    "03_hp/20_intro/06_02.png"
    pause 1
    repeat

###HARRY POTTER ANIMATIONS###

### BROKEN GLASS ###
image glass: # Animation that shows a broken glass effect when the duel starts.
    "03_hp/21_fight/01.png"
    pause 1.3
    "03_hp/21_fight/02.png"
    pause.3
    "03_hp/21_fight/03.png"
    pause.3
    "03_hp/21_fight/04.png"
    pause.3
    "03_hp/21_fight/05.png"
    pause.3
    "03_hp/21_fight/06.png"
    pause.3
    "03_hp/21_fight/07.png"



image ch_hem walk_01:
    "03_hp/animation/h_walk_01.png"
    pause.08
    "03_hp/animation/h_walk_02.png"
    pause.08
    "03_hp/animation/h_walk_03.png"
    pause.08
    "03_hp/animation/h_walk_02.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause.08
    "03_hp/animation/h_walk_04.png"
    pause.08
    "03_hp/animation/h_walk_05.png"
    pause.08
    "03_hp/animation/h_walk_04.png"
    pause.08
    repeat
    
image ch_hem robe: # Hermione chibi. Wearing a robe.
    "03_hp/animation/01.png"
    pause.08
    "03_hp/animation/02.png"
    pause.08
    "03_hp/animation/03.png"
    pause.08
    "03_hp/animation/04.png"
    pause.08
    "03_hp/animation/05.png"
    pause.08
    "03_hp/animation/06.png"
    pause.08
    "03_hp/animation/07.png"
    pause.08
    "03_hp/animation/08.png"
    pause.08
    repeat

image ch_hem robe_f: # Hermione chibi. Wearing a robe.
    im.Flip("03_hp/animation/01.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/02.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/03.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/04.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/05.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/06.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/07.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/08.png", horizontal=True)
    pause.08
    repeat
    
image ch_hem walk_01_f: #GErmione walking animation. Facing right.
    im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_02.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_02.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_04.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_05.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_04.png", horizontal=True)
    pause.08
    repeat    

    
image ch_hem run_f:
    "03_hp/animation/h_run_01f.png"
    pause.07
    "03_hp/animation/h_run_02f.png"
    pause.07
    "03_hp/animation/h_run_03f.png"
    pause.07
    "03_hp/animation/h_run_02f.png"
    pause.07
    "03_hp/animation/h_run_01f.png"
    pause.07
    "03_hp/animation/h_run_04f.png"
    pause.07
    "03_hp/animation/h_run_05f.png"
    pause.07
    "03_hp/animation/h_run_04f.png"
    pause.07
    repeat
    
    
image ch_hem blink:
    "03_hp/animation/h_walk_01.png"
    pause 2
    "03_hp/animation/h_walk_06.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause 5
    "03_hp/animation/h_walk_06.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause.08
    "03_hp/animation/h_walk_06.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause 3
    repeat

    
image snape_walk_01: #Default Snape walk animation. 
    "03_hp/09_snape_ani/snape_02.png"
    pause.18
    "03_hp/09_snape_ani/snape_03.png"
    pause.18
    "03_hp/09_snape_ani/snape_02.png"
    pause.18
    "03_hp/09_snape_ani/snape_05.png"
    pause.18
    repeat

image snape_walk_01_f: #Default Snape walk animation. 
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)     
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_03.png", horizontal=True)     
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)     
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_05.png", horizontal=True)     
    pause.18
    repeat
    
image genie_walk_ani: #Default Genie walk animation. 
    "03_hp/05_props/walk_01.png"
    pause.18   
    "03_hp/05_props/walk_02.png"
    pause.18 
    "03_hp/05_props/walk_03.png"
    pause.18 
    "03_hp/05_props/walk_04.png"
    pause.18 
    repeat
    
    
    
image rum:
    "03_hp/animation/rum_01.png"
    pause.3 
    "03_hp/animation/rum_02.png"
    pause.3  
    "03_hp/animation/rum_03.png"
    pause.3 
    "03_hp/animation/rum_04.png"
    pause 1 
    "03_hp/animation/rum_03.png"
    pause.3 
    "03_hp/animation/rum_02.png"
    pause.3 
    repeat
    
    

### Harry Potter DUEL ANIMATIONS ###

image smoke:
    "03_hp/08_animation_02/smoke_01.png"
    pause.1
    "03_hp/08_animation_02/smoke_02.png"
    pause.1
    "03_hp/08_animation_02/smoke_03.png"
    pause.1
    "03_hp/08_animation_02/smoke_04.png"
    pause.1

image ch_sna duel_01:
    "03_hp/04_duel/snape_01.png"
    pause.1
    "03_hp/04_duel/snape_02.png"
    pause.1
    "03_hp/04_duel/snape_03.png"
    pause.1
    "03_hp/04_duel/snape_02.png"
    pause.1
    repeat

image ch_gen duel_01:
    "03_hp/04_duel/gen_01.png"
    pause.1
    "03_hp/04_duel/gen_02.png"
    pause.1
    "03_hp/04_duel/gen_03.png"
    pause.1
    "03_hp/04_duel/gen_02.png"
    pause.1
    repeat
    
image ch_gen guard:
    "03_hp/04_duel/guard_01.png"
    pause.1
    "03_hp/04_duel/guard_02.png"
    pause.1
    "03_hp/04_duel/guard_03.png"
    pause.1
    "03_hp/04_duel/guard_02.png"
    pause.1
    repeat
    
image ch_gen barb:
    "03_hp/04_duel/barb_01.png"
    pause.15
    "03_hp/04_duel/barb_02.png"
    pause.15
    repeat


image ch_sna defend:
    "03_hp/04_duel/snape_defend_01.png"
    pause.1
    "03_hp/04_duel/snape_defend_02.png"
    pause.1
    "03_hp/04_duel/snape_defend_03.png"
    pause.1
    "03_hp/04_duel/snape_defend_02.png"
    pause.1
    repeat

image snape_attack:
    "03_hp/04_duel/sna_attack_01.png"
    pause.08
    "03_hp/04_duel/sna_attack_02.png"
    pause.08
    "03_hp/04_duel/sna_attack_03.png"
    pause.08
    "03_hp/04_duel/sna_attack_04.png"
    pause.08
    "03_hp/04_duel/sna_attack_05.png"
    pause.08
    "03_hp/04_duel/sna_attack_06.png"
    pause.08
    "03_hp/04_duel/sna_attack_07.png"
    pause.08
    "03_hp/04_duel/sna_attack_08.png"
    pause.08
    "03_hp/04_duel/sna_attack_09.png"
    pause.08
    "03_hp/04_duel/sna_attack_10.png"
    pause.08
    repeat

image snape_attack_guard:
    "03_hp/04_duel/sna_attack_guard_01.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_02.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_03.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_04.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_05.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_06.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_07.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_08.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_09.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_10.png"
    pause.08
    repeat
    
image snape_attack_guard: # CREDITS VERSION, with a longer pause.
    "03_hp/04_duel/sna_attack_guard_01.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_02.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_03.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_04.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_05.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_06.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_07.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_08.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_09.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_10.png"
    pause.5
    repeat
    
image genie_attack:
    "03_hp/04_duel/genie_attack_01.png"
    pause.15  
    "03_hp/04_duel/genie_attack_02.png"
    pause.15
    "03_hp/04_duel/genie_attack_01.png"
    pause.15
    "03_hp/04_duel/genie_attack_02.png"
    pause.15
    "03_hp/04_duel/genie_attack_01.png"
    pause.15 
    "03_hp/04_duel/genie_attack_02.png"
    pause.15
    "03_hp/04_duel/genie_attack_03.png"
    pause.15
    "03_hp/04_duel/genie_attack_04.png"
    pause.15
    "03_hp/04_duel/genie_attack_05.png"
    pause.15
    "03_hp/04_duel/genie_attack_06.png"
    pause.15
    "03_hp/04_duel/genie_attack_07.png"
    pause.15
    "03_hp/04_duel/genie_attack_08.png"
    pause.15
    "03_hp/04_duel/genie_attack_09.png"
    pause.15
    "03_hp/04_duel/genie_attack_10.png"
    pause.15
    "03_hp/04_duel/genie_attack_11.png"
    pause.15
    "03_hp/04_duel/genie_attack_12.png"
    pause.15 
    "03_hp/04_duel/genie_attack_13.png"
    pause.15
    "03_hp/04_duel/genie_attack_14.png"
    pause.15
    "03_hp/04_duel/genie_attack_15.png"
    pause.15
    "03_hp/04_duel/genie_attack_14.png"
    pause.15
    "03_hp/04_duel/genie_attack_15.png"
    pause.15 
    repeat
    
    
image snape_defend: #Snape is in defense stance. Barbarian throws axes at him.
    "03_hp/04_duel/sna_block_01.png"
    pause.15  
    "03_hp/04_duel/sna_block_02.png"
    pause.15
    "03_hp/04_duel/sna_block_01.png"
    pause.15
    "03_hp/04_duel/sna_block_02.png"
    pause.15
    "03_hp/04_duel/sna_block_01.png"
    pause.15 
    "03_hp/04_duel/sna_block_02.png"
    pause.15
    "03_hp/04_duel/sna_block_03.png"
    pause.15
    "03_hp/04_duel/sna_block_04.png"
    pause.15
    "03_hp/04_duel/sna_block_05.png"
    pause.15
    "03_hp/04_duel/sna_block_06.png"
    pause.15
    "03_hp/04_duel/sna_block_07.png"
    pause.15
    "03_hp/04_duel/sna_block_08.png"
    pause.15
    "03_hp/04_duel/sna_block_09.png"
    pause.15
    "03_hp/04_duel/sna_block_10.png"
    pause.15
    "03_hp/04_duel/sna_block_11.png"
    pause.15
    "03_hp/04_duel/sna_block_12.png"
    pause.15 
    "03_hp/04_duel/sna_block_13.png"
    pause.15
    repeat


image pentogram:
    "03_hp/04_duel/pen_05.png"
    pause.1
    "03_hp/04_duel/pen_04.png"
    pause.1
    "03_hp/04_duel/pen_03.png"
    pause.1
    "03_hp/04_duel/pen_02.png"
    pause.1
    "03_hp/04_duel/pen_01.png"
    pause.1
    "03_hp/04_duel/pen_02.png"
    pause.1
    "03_hp/04_duel/pen_03.png"
    pause.1
    "03_hp/04_duel/pen_04.png"
    pause.1
    "03_hp/04_duel/pen_05.png"
    pause.1
    repeat

image hand: #Hand appears. 
    "03_hp/04_duel/hand_01.png"
    pause.1  
    "03_hp/04_duel/hand_02.png"
    pause.1
    "03_hp/04_duel/hand_03.png"
    pause.1
    "03_hp/04_duel/hand_04.png"
    pause.1
    "03_hp/04_duel/hand_05.png"
    pause.1 
    "03_hp/04_duel/hand_06.png"
    pause.1
    "03_hp/04_duel/hand_07.png"
    pause.1
    "03_hp/04_duel/hand_08.png"
    pause.1
    "03_hp/04_duel/hand_09.png"
    pause.1
    "03_hp/04_duel/hand_10.png"
    pause.1
    "03_hp/04_duel/hand_11.png"
    pause.1
    "03_hp/04_duel/hand_12.png"
    pause.1
    "03_hp/04_duel/hand_13.png"
    pause.1
    "03_hp/04_duel/hand_14.png"
    pause.1
    "03_hp/04_duel/hand_15.png"
    pause.1
    "03_hp/04_duel/hand_16.png"
    pause.1
    repeat

image hand_genie: #Hand attacks Genie. 
    "03_hp/04_duel/hand_genie_01.png"
    pause.1
    "03_hp/04_duel/hand_genie_02.png"
    pause.1
    "03_hp/04_duel/hand_genie_03.png"
    pause.1
    "03_hp/04_duel/hand_genie_04.png"
    pause.1
    "03_hp/04_duel/hand_genie_05.png"
    pause.1
    "03_hp/04_duel/hand_genie_06.png"
    pause.1
    "03_hp/04_duel/hand_genie_07.png"
    pause.1
    "03_hp/04_duel/hand_genie_08.png"
    pause.1
    "03_hp/04_duel/hand_genie_09.png"
    pause.1
    "03_hp/04_duel/hand_genie_10.png"
    pause.1
    "03_hp/04_duel/hand_genie_11.png"
    pause.1
    "03_hp/04_duel/hand_genie_12.png"
    pause.1
    "03_hp/04_duel/hand_genie_13.png"
    pause.1


image hand_guard: #Hand attacks the guard. 
    "03_hp/04_duel/hand_guard_01.png"
    pause.1
    "03_hp/04_duel/hand_guard_02.png"
    pause.1
    "03_hp/04_duel/hand_guard_03.png"
    pause.1
    "03_hp/04_duel/hand_guard_04.png"
    pause.1
    "03_hp/04_duel/hand_guard_05.png"
    pause.1
    "03_hp/04_duel/hand_guard_06.png"
    pause.1
    "03_hp/04_duel/hand_guard_07.png"
    pause.1
    "03_hp/04_duel/hand_guard_08.png"
    pause.1
    "03_hp/04_duel/hand_guard_09.png"
    pause.1
    "03_hp/04_duel/hand_guard_10.png"
    pause.1
    "03_hp/04_duel/hand_guard_11.png"
    pause.1
    "03_hp/04_duel/hand_guard_12.png"
    pause.1
    "03_hp/04_duel/hand_guard_13.png"
    pause.1
    "03_hp/04_duel/hand_guard_14.png"
    pause.1
    "03_hp/04_duel/hand_guard_11.png"
    pause.1
    "03_hp/04_duel/hand_guard_12.png"
    pause.1
    "03_hp/04_duel/hand_guard_13.png"
    pause.1

### DAMAGE ###

image minus_50: 
    "03_hp/14_damage/50_01.png"
    pause.2
    "03_hp/14_damage/50_02.png"
    pause.2
    "03_hp/14_damage/50_03.png"
    pause.2
    "03_hp/14_damage/50_04.png"
    pause.2
    "03_hp/14_damage/50_05.png"
    pause.2
    "03_hp/14_damage/50_06.png"
    pause.2
    "03_hp/14_damage/50_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2
    
    
image minus_100: #Hand attacks the guard. 
    "03_hp/14_damage/100_01.png"
    pause.2
    "03_hp/14_damage/100_02.png"
    pause.2
    "03_hp/14_damage/100_03.png"
    pause.2
    "03_hp/14_damage/100_04.png"
    pause.2
    "03_hp/14_damage/100_05.png"
    pause.2
    "03_hp/14_damage/100_06.png"
    pause.2
    "03_hp/14_damage/100_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2
    
image minus_300: 
    "03_hp/14_damage/300_01.png"
    pause.2
    "03_hp/14_damage/300_02.png"
    pause.2
    "03_hp/14_damage/300_03.png"
    pause.2
    "03_hp/14_damage/300_04.png"
    pause.2
    "03_hp/14_damage/300_05.png"
    pause.2
    "03_hp/14_damage/300_06.png"
    pause.2
    "03_hp/14_damage/300_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2   
    
image plus_300: 
    "03_hp/14_damage/plus_300_01.png"
    pause.2
    "03_hp/14_damage/plus_300_02.png"
    pause.2
    "03_hp/14_damage/plus_300_03.png"
    pause.2
    "03_hp/14_damage/plus_300_04.png"
    pause.2
    "03_hp/14_damage/plus_300_05.png"
    pause.2
    "03_hp/14_damage/plus_300_06.png"
    pause.2
    "03_hp/14_damage/plus_300_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2   


image minus_400: #Hand attacks the guard. 
    "03_hp/14_damage/400_01.png"
    pause.2
    "03_hp/14_damage/400_02.png"
    pause.2
    "03_hp/14_damage/400_03.png"
    pause.2
    "03_hp/14_damage/400_04.png"
    pause.2
    "03_hp/14_damage/400_05.png"
    pause.2
    "03_hp/14_damage/400_06.png"
    pause.2
    "03_hp/14_damage/400_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2

image minus_500: #Hand attacks the guard. 
    "03_hp/14_damage/500_01.png"
    pause.2
    "03_hp/14_damage/500_02.png"
    pause.2
    "03_hp/14_damage/500_03.png"
    pause.2
    "03_hp/14_damage/500_04.png"
    pause.2
    "03_hp/14_damage/500_05.png"
    pause.2
    "03_hp/14_damage/500_06.png"
    pause.2
    "03_hp/14_damage/500_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2


image minus_0: #Hand attacks the guard. 
    "03_hp/14_damage/0_01.png"
    pause.2
    "03_hp/14_damage/0_02.png"
    pause.2
    "03_hp/14_damage/0_03.png"
    pause.2
    "03_hp/14_damage/0_04.png"
    pause.2
    "03_hp/14_damage/0_05.png"
    pause.2
    "03_hp/14_damage/0_06.png"
    pause.2
    "03_hp/14_damage/0_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2



### HARRY POTTER EMOTICONS ANIMATIONS ###

image newanimation2 = Animation("03_hp/05_props/12_genie_01.png", 0.25,
                            "03_hp/05_props/11_genie_02.png", 0.25)



image newanimation:
    "03_hp/05_props/12_genie_01.png"
    pause.1
    "03_hp/05_props/12_genie_02.png"
    pause.1
    "03_hp/05_props/12_genie_03.png"
    pause.1
    "03_hp/05_props/12_genie_02.png"
    pause.1
    "03_hp/05_props/12_genie_01.png"
    pause 5
    "03_hp/05_props/12_genie_01.png"
    pause.15
    "03_hp/05_props/12_genie_04.png"
    pause.15
    "03_hp/05_props/12_genie_01.png"
    pause.15
    "03_hp/05_props/12_genie_04.png"
    pause.15
    "03_hp/05_props/12_genie_01.png"
    pause 6
    repeat
    
image exclaim_01: #Exclamation mark.
    "03_hp/06_emo/exlaim_01.png"
    pause.1
    "03_hp/06_emo/exlaim_02.png"
    pause.1
    "03_hp/06_emo/exlaim_03.png"
    pause.1
    "03_hp/06_emo/exlaim_04.png"
    pause.1
    "03_hp/06_emo/exlaim_03.png"
    pause 2
    "03_hp/06_emo/exlaim_05.png"
    pause.08
    "03_hp/06_emo/exlaim_06.png"
    pause.08
    "03_hp/06_emo/exlaim_07.png"

image sad_01: #SAD SMILEY USED WHEN PETTING PHOENIX.
    "03_hp/06_emo/exlaim_01.png"
    pause.1
    "03_hp/06_emo/sad_01.png"
    pause.1   
    "03_hp/06_emo/sad_02.png"
    pause.1  
    "03_hp/06_emo/sad_03.png"
    pause 1  
    "03_hp/06_emo/sad_04.png"
    pause.1 
    "03_hp/06_emo/sad_03.png"
    pause.1  
    "03_hp/06_emo/sad_04.png"
    pause.1 
    "03_hp/06_emo/sad_03.png"
    pause 3
    "03_hp/06_emo/sad_02.png"
    pause.1 
    "03_hp/06_emo/sad_01.png"
    pause.1 
    "03_hp/06_emo/exlaim_07.png"
    
image hoot: #OWL'S "HOOT!".
    "03_hp/06_emo/hoot_01.png"
    pause.07
    "03_hp/06_emo/hoot_02.png"
    pause.07
    "03_hp/06_emo/hoot_03.png"
    pause.07
    "03_hp/06_emo/hoot_04.png"
    pause.07
    "03_hp/06_emo/hoot_05.png"
    pause.07
    "03_hp/06_emo/hoot_06.png"
    pause.07
    "03_hp/06_emo/hoot_07.png"
    pause 3
    "03_hp/06_emo/exlaim_07.png"
  
image notes: #A bunch of notes poping out with a "win" sound effect.
    "03_hp/08_animation_02/notes_01.png"   
    pause.08
    "03_hp/08_animation_02/notes_02.png"   
    pause.08
    "03_hp/08_animation_02/notes_03.png"   
    pause.08
    "03_hp/08_animation_02/notes_04.png"   
    pause.08
    "03_hp/08_animation_02/notes_05.png"   
    pause.08
    "03_hp/08_animation_02/notes_06.png"   
    pause.08
    "03_hp/08_animation_02/notes_07.png"   
    pause.08
    "03_hp/08_animation_02/notes_08.png"   
    pause.08
    "03_hp/08_animation_02/notes_09.png"   
    pause.08
    
image thought: #Thinking emotion over a chibi.
    "03_hp/06_emo/thought_02.png"
    pause.5    
    "03_hp/06_emo/thought_01.png"
    pause.5  
    repeat
    


  
  
### ADDING HOUSE POINTS ###
image ass_03_points:
    "03_hp/11_misc/03_points.png"
    pause 3
    "03_hp/11_misc/03_points_75.png"
    pause.08
    "03_hp/11_misc/03_points_50.png"
    pause.08
    "03_hp/11_misc/03_points_25.png"
    pause.08
    "03_hp/11_misc/points_00.png"

image what_01_points:
    "03_hp/11_misc/01_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/01_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/01_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/01_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/01_points.png", 0.0)

image what_02_points:
    "03_hp/11_misc/02_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/02_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/02_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/02_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/02_points.png", 0.0)
    
image what_03_points:
    "03_hp/11_misc/03_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/03_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/03_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/03_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/03_points.png", 0.0)
    
image what_04_points:   #<============================================== 4 POINTS
    "03_hp/11_misc/04.png"
    pause 3
    im.Alpha("03_hp/11_misc/04.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/04.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/04.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/04.png", 0.0)

image what_05_points: # <================================================ 5 POINTS
    "03_hp/11_misc/05_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/05_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/05_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/05_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/05_points.png", 0.0)
    
image what_06_points: # <================================================ 6 POINTS
    "03_hp/11_misc/06.png"
    pause 3
    im.Alpha("03_hp/11_misc/06.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/06.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/06.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/06.png", 0.0)
    
    
image what_07_points: # <================================================ 7 POINTS
    "03_hp/11_misc/07.png"
    pause 3
    im.Alpha("03_hp/11_misc/07.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/07.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/07.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/07.png", 0.0)
    
image what_08_points: # <================================================ 8 POINTS
    "03_hp/11_misc/08.png"
    pause 3
    im.Alpha("03_hp/11_misc/08.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/08.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/08.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/08.png", 0.0)
    
image what_09_points: # <================================================ 9 POINTS
    "03_hp/11_misc/09.png"
    pause 3
    im.Alpha("03_hp/11_misc/09.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/09.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/09.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/09.png", 0.0)
    
image what_10_points: # <================================================ 10 POINTS
    "03_hp/11_misc/10.png"
    pause 3
    im.Alpha("03_hp/11_misc/10.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/10.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/10.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/10.png", 0.0)
    
image what_11_points: # <================================================ 11 POINTS
    "03_hp/11_misc/11.png"
    pause 3
    im.Alpha("03_hp/11_misc/11.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/11.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/11.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/11.png", 0.0)
    
image what_12_points: # <================================================ 12 POINTS
    "03_hp/11_misc/12.png"
    pause 3
    im.Alpha("03_hp/11_misc/12.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/12.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/12.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/12.png", 0.0)
    
image what_13_points: # <================================================ 13 POINTS
    "03_hp/11_misc/13.png"
    pause 3
    im.Alpha("03_hp/11_misc/13.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/13.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/13.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/13.png", 0.0)
    
image what_14_points: # <================================================ 14 POINTS
    "03_hp/11_misc/14.png"
    pause 3
    im.Alpha("03_hp/11_misc/14.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/14.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/14.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/14.png", 0.0)
    
image what_15_points: # <================================================ 15 POINTS
    "03_hp/11_misc/15_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/15_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/15_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/15_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/15_points.png", 0.0)
    
image what_16_points: # <================================================ 16 POINTS
    "03_hp/11_misc/16.png"
    pause 3
    im.Alpha("03_hp/11_misc/16.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/16.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/16.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/16.png", 0.0)
    
image what_17_points: # <================================================ 17 POINTS
    "03_hp/11_misc/17.png"
    pause 3
    im.Alpha("03_hp/11_misc/17.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/17.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/17.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/17.png", 0.0)
    
image what_18_points: # <================================================ 18 POINTS
    "03_hp/11_misc/18.png"
    pause 3
    im.Alpha("03_hp/11_misc/18.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/18.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/18.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/18.png", 0.0)
    
image what_19_points: # <================================================ 19 POINTS
    "03_hp/11_misc/19.png"
    pause 3
    im.Alpha("03_hp/11_misc/19.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.0)
    
image what_19_points: # <================================================ 19 POINTS
    "03_hp/11_misc/19.png"
    pause 3
    im.Alpha("03_hp/11_misc/19.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.0)
    
image what_20_points: # <================================================ 20 POINTS
    "03_hp/11_misc/20.png"
    pause 3
    im.Alpha("03_hp/11_misc/20.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/20.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/20.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/20.png", 0.0)
    
image what_21_points: # <================================================ 21 POINTS
    "03_hp/11_misc/21.png"
    pause 3
    im.Alpha("03_hp/11_misc/21.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/21.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/21.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/21.png", 0.0)
    
image what_22_points: # <================================================ 22 POINTS
    "03_hp/11_misc/20.png"
    pause 3
    im.Alpha("03_hp/11_misc/22.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/22.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/22.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/22.png", 0.0)
    
image what_23_points: # <================================================ 23 POINTS
    "03_hp/11_misc/23.png"
    pause 3
    im.Alpha("03_hp/11_misc/23.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/23.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/23.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/23.png", 0.0)
    
image what_24_points: # <================================================ 24 POINTS
    "03_hp/11_misc/24.png"
    pause 3
    im.Alpha("03_hp/11_misc/24.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/24.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/24.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/24.png", 0.0)
    
image what_25_points: # <================================================ 25 POINTS
    "03_hp/11_misc/25.png"
    pause 3
    im.Alpha("03_hp/11_misc/25.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/25.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/25.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/25.png", 0.0)
    
image what_26_points: # <================================================ 26 POINTS
    "03_hp/11_misc/26.png"
    pause 3
    im.Alpha("03_hp/11_misc/26.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/26.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/26.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/26.png", 0.0)
    
image what_27_points: # <================================================ 27 POINTS
    "03_hp/11_misc/27.png"
    pause 3
    im.Alpha("03_hp/11_misc/27.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/27.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/27.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/27.png", 0.0)
    
image what_28_points: # <================================================ 28 POINTS
    "03_hp/11_misc/28.png"
    pause 3
    im.Alpha("03_hp/11_misc/28.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/28.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/28.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/28.png", 0.0)
    
image what_29_points: # <================================================ 29 POINTS
    "03_hp/11_misc/20.png"
    pause 3
    im.Alpha("03_hp/11_misc/29.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/29.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/29.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/29.png", 0.0)
    
image what_30_points: # <================================================ 30 POINTS
    "03_hp/11_misc/30.png"
    pause 3
    im.Alpha("03_hp/11_misc/30.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/30.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/30.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/30.png", 0.0)
    
image what_31_points: # <================================================ 31 POINTS
    "03_hp/11_misc/31.png"
    pause 3
    im.Alpha("03_hp/11_misc/31.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/31.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/31.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/31.png", 0.0)
    
image what_32_points: # <================================================ 32 POINTS
    "03_hp/11_misc/32.png"
    pause 3
    im.Alpha("03_hp/11_misc/32.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/32.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/32.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/32.png", 0.0)
    
image what_33_points: # <================================================ 33 POINTS
    "03_hp/11_misc/33.png"
    pause 3
    im.Alpha("03_hp/11_misc/33.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/33.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/33.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/33.png", 0.0)
 
image what_34_points: # <================================================ 34 POINTS
    "03_hp/11_misc/34.png"
    pause 3
    im.Alpha("03_hp/11_misc/34.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/34.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/34.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/34.png", 0.0)
    
image what_35_points: # <================================================ 35 POINTS
    "03_hp/11_misc/35.png"
    pause 3
    im.Alpha("03_hp/11_misc/35.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/35.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/35.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/35.png", 0.0)
    
image what_36_points: # <================================================ 36 POINTS
    "03_hp/11_misc/36.png"
    pause 3
    im.Alpha("03_hp/11_misc/36.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/36.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/36.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/36.png", 0.0)
    
image what_37_points: # <================================================ 37 POINTS
    "03_hp/11_misc/37.png"
    pause 3
    im.Alpha("03_hp/11_misc/37.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/37.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/37.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/37.png", 0.0)
    
image what_38_points: # <================================================ 38 POINTS
    "03_hp/11_misc/38.png"
    pause 3
    im.Alpha("03_hp/11_misc/38.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/38.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/38.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/38.png", 0.0)
    
image what_39_points: # <================================================ 39 POINTS
    "03_hp/11_misc/39.png"
    pause 3
    im.Alpha("03_hp/11_misc/39.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/39.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/39.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/39.png", 0.0)
    
image what_40_points: # <================================================ 40 POINTS
    "03_hp/11_misc/40.png"
    pause 3
    im.Alpha("03_hp/11_misc/40.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/40.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/40.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/40.png", 0.0)
    
image what_41_points: # <================================================ 41 POINTS
    "03_hp/11_misc/41.png"
    pause 3
    im.Alpha("03_hp/11_misc/41.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/41.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/41.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/41.png", 0.0)
    
image what_42_points: # <================================================ 42 POINTS
    "03_hp/11_misc/42.png"
    pause 3
    im.Alpha("03_hp/11_misc/42.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/42.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/42.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/42.png", 0.0)
    
image what_43_points: # <================================================ 43 POINTS
    "03_hp/11_misc/43.png"
    pause 3
    im.Alpha("03_hp/11_misc/43.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/43.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/43.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/43.png", 0.0)
    
image what_44_points: # <================================================ 44 POINTS
    "03_hp/11_misc/44.png"
    pause 3
    im.Alpha("03_hp/11_misc/44.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/44.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/44.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/44.png", 0.0)
    
image what_45_points: # <================================================ 45 POINTS
    "03_hp/11_misc/45.png"
    pause 3
    im.Alpha("03_hp/11_misc/45.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/45.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/45.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/45.png", 0.0)
    
image what_46_points: # <================================================ 46 POINTS
    "03_hp/11_misc/46.png"
    pause 3
    im.Alpha("03_hp/11_misc/46.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/46.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/46.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/46.png", 0.0)
    
image what_47_points: # <================================================ 47 POINTS
    "03_hp/11_misc/47.png"
    pause 3
    im.Alpha("03_hp/11_misc/47.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/47.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/47.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/47.png", 0.0)
    
image what_48_points: # <================================================ 48 POINTS
    "03_hp/11_misc/48.png"
    pause 3
    im.Alpha("03_hp/11_misc/48.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/48.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/48.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/48.png", 0.0)
    
image what_49_points: # <================================================ 49 POINTS
    "03_hp/11_misc/49.png"
    pause 3
    im.Alpha("03_hp/11_misc/49.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/49.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/49.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/49.png", 0.0)
    
image what_50_points: # <================================================ 50 POINTS
    "03_hp/11_misc/50.png"
    pause 3
    im.Alpha("03_hp/11_misc/50.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/50.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/50.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/50.png", 0.0)
    
    
    
    

#############################################################    
image feather: #Falling feather.
    "03_hp/animation/pho_22.png"
    pause 10
    "03_hp/animation/pho_01.png"
    pause.15 
    "03_hp/animation/pho_02.png"
    pause.15
    "03_hp/animation/pho_03.png"
    pause.15 
    "03_hp/animation/pho_04.png"
    pause.15 
    "03_hp/animation/pho_05.png"
    pause.15 
    "03_hp/animation/pho_06.png"
    pause.15 
    "03_hp/animation/pho_07.png"
    pause.15 
    "03_hp/animation/pho_08.png"
    pause.15 
    "03_hp/animation/pho_09.png"
    pause.15 
    "03_hp/animation/pho_10.png"
    pause.15 
    "03_hp/animation/pho_11.png"
    pause.15 
    "03_hp/animation/pho_12.png"
    pause.15 
    "03_hp/animation/pho_13.png"
    pause.15 
    "03_hp/animation/pho_14.png"
    pause.15 
    "03_hp/animation/pho_15.png"
    pause.15 
    "03_hp/animation/pho_16.png"
    pause.15 
    "03_hp/animation/pho_17.png"
    pause.15 
    "03_hp/animation/pho_18.png"
    pause 10
    "03_hp/animation/pho_19.png"
    pause.1 
    "03_hp/animation/pho_20.png"
    pause.1 
    "03_hp/animation/pho_21.png"
    pause.1 
    "03_hp/animation/pho_22.png"
    pause 20
    repeat
  
    
image pho_01: #Phoenix idile animation
    "03_hp/animation/phoenix_01.png"  
    pause 2
    "03_hp/animation/phoenix_02.png"  
    pause.15
    "03_hp/animation/phoenix_03.png"  
    pause.15
    "03_hp/animation/phoenix_02.png"  
    pause.15
    "03_hp/animation/phoenix_01.png"  
    pause.15
    "03_hp/animation/phoenix_02.png"  
    pause.15
    "03_hp/animation/phoenix_03.png"  
    pause.15
    "03_hp/animation/phoenix_02.png"  
    pause.15
    "03_hp/animation/phoenix_01.png"  
    pause 10
    repeat
 
image paperwork_02: #Genie working behind his desk.
    "03_hp/animation/working_01.png"  
    pause.15 
    "03_hp/animation/working_02.png"  
    pause.15
    "03_hp/animation/working_01.png"  
    pause.15 
    "03_hp/animation/working_02.png"  
    pause.15
    "03_hp/animation/working_01.png"  
    pause.15 
    "03_hp/animation/working_02.png"  
    pause 1
    "03_hp/animation/working_03.png"
    pause.15
    "03_hp/animation/working_04.png"
    pause.15
    "03_hp/animation/working_05.png"
    pause.15
    "03_hp/animation/working_06.png"
    pause.15
    "03_hp/animation/working_05.png"
    pause.15
    "03_hp/animation/working_06.png"
    pause.15
    "03_hp/animation/working_05.png"
    pause.15
    "03_hp/animation/working_06.png"
    pause 1
    "03_hp/animation/working_07.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_09.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_07.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_09.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_03.png"
    pause.15
    "03_hp/animation/working_02.png"
    pause.15
    repeat
 
image reading: #Genie reading.
    im.Flip("03_hp/animation/reading_01.png", horizontal=True)  
    pause 2
    im.Flip("03_hp/animation/reading_06.png", horizontal=True)  
    pause.15 
    im.Flip("03_hp/animation/reading_05.png", horizontal=True)  
    pause.15
    im.Flip("03_hp/animation/reading_04.png", horizontal=True)  
    pause.15
    im.Flip("03_hp/animation/reading_03.png", horizontal=True)  
    pause.15
    im.Flip("03_hp/animation/reading_02.png", horizontal=True)  
    pause.15
    im.Flip("03_hp/animation/reading_01.png", horizontal=True)  
    pause 2
    repeat
    
    
image reading_near_fire: #Genie reading near the fireplace.
    "03_hp/animation/reading_01.png"
    pause 2
    "03_hp/animation/reading_06.png" 
    pause.15 
    "03_hp/animation/reading_05.png"  
    pause.15
    "03_hp/animation/reading_04.png"  
    pause.15
    "03_hp/animation/reading_03.png"
    pause.15
    "03_hp/animation/reading_02.png" 
    pause.15
    "03_hp/animation/reading_01.png"
    pause 2
    repeat
    
image genie_jerking_off: #Genie sitting behind his desk and jerking off...
    "03_hp/animation/jerking_off_01.png"
    pause.2
    "03_hp/animation/jerking_off_02.png"
    pause.2
    "03_hp/animation/jerking_off_03.png"
    pause.2
    "03_hp/animation/jerking_off_02.png"
    pause.2
    repeat
    
image genie_jerking_sperm_ani: #Sperm after jerking off.
    "03_hp/animation/jerking_sperm_01.png"
    pause.1
    "03_hp/animation/jerking_sperm_02.png"
    pause.1
    "03_hp/animation/jerking_sperm_03.png"
    pause.1
    "03_hp/animation/jerking_sperm_04.png"
    pause.1
    "03_hp/animation/jerking_sperm_05.png"
    pause.1
    "03_hp/animation/jerking_sperm_06.png"
    pause.1
    "03_hp/animation/jerking_sperm_07.png"
    pause.1
    "03_hp/animation/jerking_sperm_08.png"
    pause.1
    "03_hp/animation/jerking_sperm_09.png"
    pause.1
    "03_hp/animation/jerking_sperm_10.png"
    pause.1
    "03_hp/animation/jerking_sperm_11.png"
    pause 2
    repeat
 
### FAVORS ###
### GROPINGS ###
image groping_01: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "03_hp/animation/grope_01.png"
    pause.2
    "03_hp/animation/grope_02.png"
    pause.2
    "03_hp/animation/grope_03.png"
    pause.5
    "03_hp/animation/grope_02.png"
    pause.2
    "03_hp/animation/grope_01.png"
    pause.2
    repeat

image groping_02: #Genie groping Hermione under her skirt. Hermione's behind is facing Genie.
    "03_hp/animation/grope_b_01.png"
    pause.2
    "03_hp/animation/grope_b_02.png"
    pause.2
    "03_hp/animation/grope_b_03.png"
    pause.5
    "03_hp/animation/grope_b_02.png"
    pause.2
    "03_hp/animation/grope_b_01.png"
    pause.2
    repeat


image groping_01_blinking: #Animation of Hermione blinking her eyes.
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    "03_hp/animation/grope_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    repeat
    
image groping_02_blinking: #Animation of Hermione blinking her eyes.
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_b_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    "03_hp/animation/grope_b_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_b_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    repeat
    
### GROPING TITS FULLY CLOTHED ###
image groping_03_ani: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "03_hp/animation/molest_01.png"
    pause.2
    "03_hp/animation/molest_02.png"
    pause.2
    "03_hp/animation/molest_03.png"
    pause.2
    "03_hp/animation/molest_04.png"
    pause.2
    "03_hp/animation/molest_05.png"
    pause.2
    "03_hp/animation/molest_06.png"
    pause.2
    "03_hp/animation/molest_07.png"
    pause.2
    "03_hp/animation/molest_08.png"
    pause.2
    repeat
    
### GROPING NAKED TITS ###
image groping_naked_tits_ani: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "03_hp/animation/tit_molester_naked_01.png"
    pause.2
    "03_hp/animation/tit_molester_naked_02.png"
    pause.2
    "03_hp/animation/tit_molester_naked_03.png"
    pause.2
    "03_hp/animation/tit_molester_naked_04.png"
    pause.2
    "03_hp/animation/tit_molester_naked_05.png"
    pause.2
    "03_hp/animation/tit_molester_naked_06.png"
    pause.2
    "03_hp/animation/tit_molester_naked_07.png"
    pause.2
    "03_hp/animation/tit_molester_naked_08.png"
    pause.2
    repeat
    
    
### JERKING OFF ###
image jerking_off_ani: #Genie jerking off in front of topless Hermione.
    "03_hp/animation/07_jerking_off_01.png"
    pause.2
    "03_hp/animation/07_jerking_off_02.png"
    pause.2
    "03_hp/animation/07_jerking_off_03.png"
    pause.2
    "03_hp/animation/07_jerking_off_04.png"
    pause.2
    repeat
    
image jerking_off_02_ani: #Genie jerking off in front of dancing on a desk Hermione. (Difference is that the dick is aimed higher.)
    "03_hp/08_animation_02/06_jerking_01.png"
    pause.2
    "03_hp/08_animation_02/06_jerking_02.png"
    pause.2
    "03_hp/08_animation_02/06_jerking_03.png"
    pause.2
    "03_hp/08_animation_02/06_jerking_04.png"
    pause.2
    repeat

image jerking_off_03_ani: #SNape jerking off in front of dancing on a desk Hermione.
    "03_hp/08_animation_02/10_jerking_01.png"
    pause.2
    "03_hp/08_animation_02/10_jerking_02.png"
    pause.2
    "03_hp/08_animation_02/10_jerking_03.png"
    pause.2
    "03_hp/08_animation_02/10_jerking_04.png"
    pause.2
    repeat
    
### CUM ###
image jerking_off_cum_ani: #Sperm.
    "03_hp/animation/08_cum_01.png"
    pause.1
    "03_hp/animation/08_cum_02.png"
    pause.1
    "03_hp/animation/08_cum_03.png"
    pause.1
    "03_hp/animation/08_cum_04.png"
    pause.1
    "03_hp/animation/08_cum_05.png"
    pause.1
    "03_hp/animation/08_cum_06.png"
    pause.1
    "03_hp/animation/08_cum_07.png"
    pause.1
    "03_hp/animation/08_cum_08.png"
    pause.1
    "03_hp/animation/08_cum_09.png"
    pause.1
    "03_hp/animation/08_cum_10.png"
    pause.1
    "03_hp/animation/08_cum_11.png"
    pause.1
    "03_hp/animation/08_cum_12.png"
    pause.1
    "03_hp/animation/08_cum_13.png"
    pause 3
    "03_hp/animation/08_cum_14.png"
    pause.1
    "03_hp/animation/08_cum_15.png"
    pause.1
    "03_hp/animation/08_cum_16.png"
    pause.1
    repeat

### CUM_02 ###
image genie_cum_03: #Genie cuming on Hermione after she is done striping.
    "03_hp/08_animation_02/09_cum_01.png"
    pause.1
    "03_hp/08_animation_02/09_cum_02.png"
    pause.1
    "03_hp/08_animation_02/09_cum_03.png"
    pause.1
    "03_hp/08_animation_02/09_cum_04.png"
    pause.1
    "03_hp/08_animation_02/09_cum_05.png"
    pause.1
    "03_hp/08_animation_02/09_cum_06.png"
    pause.1
    "03_hp/08_animation_02/09_cum_07.png"
    pause.1
    "03_hp/08_animation_02/09_cum_08.png"
    pause.1
    "03_hp/08_animation_02/09_cum_09.png"
    pause.1
    "03_hp/08_animation_02/09_cum_10.png"
    pause.1
    "03_hp/08_animation_02/09_cum_11.png"
    pause.1
    "03_hp/08_animation_02/09_cum_12.png"
    pause.1
    "03_hp/08_animation_02/09_cum_13.png"
    pause.1
    "03_hp/08_animation_02/09_cum_14.png"
    pause.1
    "03_hp/08_animation_02/09_cum_15.png"
    pause.1
    "03_hp/08_animation_02/09_cum_16.png"
    pause.1
    "03_hp/08_animation_02/09_cum_17.png"
    pause.1
    "03_hp/08_animation_02/09_cum_18.png"
    pause 2
    "03_hp/08_animation_02/09_cum_19.png"
    pause.1
    "03_hp/08_animation_02/09_cum_20.png"
    pause.1
    "03_hp/08_animation_02/00.png"
    pause.5
    repeat

### CUM_03 ###
image snape_cum_01: #Snape cumming on Hermione after she is done striping.
    "03_hp/08_animation_02/11_cum_01.png"
    pause.1
    "03_hp/08_animation_02/11_cum_02.png"
    pause.1
    "03_hp/08_animation_02/11_cum_03.png"
    pause.1
    "03_hp/08_animation_02/11_cum_04.png"
    pause.1
    "03_hp/08_animation_02/11_cum_05.png"
    pause.1
    "03_hp/08_animation_02/11_cum_06.png"
    pause.1
    "03_hp/08_animation_02/11_cum_07.png"
    pause.1
    "03_hp/08_animation_02/11_cum_08.png"
    pause.1
    "03_hp/08_animation_02/11_cum_09.png"
    pause.1
    "03_hp/08_animation_02/11_cum_10.png"
    pause.1
    "03_hp/08_animation_02/11_cum_11.png"
    pause.1
    "03_hp/08_animation_02/11_cum_12.png"
    pause.1
    "03_hp/08_animation_02/11_cum_13.png"
    pause.1
    "03_hp/08_animation_02/11_cum_14.png"
    pause.1
    "03_hp/08_animation_02/11_cum_15.png"
    pause.1
    "03_hp/08_animation_02/11_cum_16.png"
    pause.1
    "03_hp/08_animation_02/11_cum_17.png"
    pause.1
    "03_hp/08_animation_02/11_cum_18.png"
    pause 2
    "03_hp/08_animation_02/11_cum_19.png"
    pause.1
    "03_hp/08_animation_02/11_cum_20.png"
    pause.1
    "03_hp/08_animation_02/00.png"
    pause.5
    repeat
    

    
### HERMIONE DANCING FULLY CLOTHED ###
image clothed_dance_ani:
    "03_hp/08_animation_02/01_dancing_01.png"
    pause.1
    "03_hp/08_animation_02/01_dancing_02.png"
    pause.1
    "03_hp/08_animation_02/01_dancing_03.png"
    pause.1
    "03_hp/08_animation_02/01_dancing_04.png"
    pause.1
    repeat


### HERMIONE DANCING NO VEST###
image no_vest_dance_ani:
    "03_hp/08_animation_02/02_no_vest_01.png"
    pause.1
    "03_hp/08_animation_02/02_no_vest_02.png"
    pause.1
    "03_hp/08_animation_02/02_no_vest_03.png"
    pause.1
    "03_hp/08_animation_02/02_no_vest_04.png"
    pause.1
    repeat
    
### HERMIONE DANCING NO SKIRT###
image no_skirt_dance_ani:
    "03_hp/08_animation_02/04_no_skirt_01.png"
    pause.1    
    "03_hp/08_animation_02/04_no_skirt_02.png"
    pause.1    
    "03_hp/08_animation_02/04_no_skirt_03.png"
    pause.1    
    "03_hp/08_animation_02/04_no_skirt_04.png"
    pause.1    
    repeat    
    
### HERMIONE DANCING NO SHIRT###
image no_shirt_dance_ani:
    "03_hp/08_animation_02/03_no_shirt_01.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_02.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_03.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_04.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_05.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_06.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_07.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_08.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_09.png"
    pause.1
    repeat
    
### HERMIONE DANCING NO PANTIES###
image no_panties_dance_ani:
    "03_hp/08_animation_02/07_dance_01.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_02.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_03.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_04.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_05.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_06.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_07.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_08.png"
    pause.1    
    "03_hp/08_animation_02/07_dance_09.png"
    pause.1    
    repeat
    
    
    
### HERMIONE DANCING NO SHIRT NO SKIRT###
image no_shirt_no_skirt_dance_ani:
    "03_hp/08_animation_02/05_panties_01.png"
    pause.1
    "03_hp/08_animation_02/05_panties_02.png"
    pause.1
    "03_hp/08_animation_02/05_panties_03.png"
    pause.1
    "03_hp/08_animation_02/05_panties_04.png"
    pause.1
    "03_hp/08_animation_02/05_panties_05.png"
    pause.1
    "03_hp/08_animation_02/05_panties_06.png"
    pause.1
    "03_hp/08_animation_02/05_panties_07.png"
    pause.1
    "03_hp/08_animation_02/05_panties_08.png"
    pause.1
    "03_hp/08_animation_02/05_panties_09.png"
    pause.1
    repeat
    
    
### HERMIONE GIVING GENIE A HANDJOB ###
image handjob_ani:
    "03_hp/08_animation_02/12_handjob_01.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_02.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_03.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_04.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_05.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_06.png"
    pause.1
    repeat
    
### HERMIONE GIVING A KISS TO GENIE'S COCK ###
image kiss_ani:
    "03_hp/08_animation_02/13_kiss_01.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_02.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_03.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_04.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_05.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_06.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_07.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_08.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_09.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_10.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_11.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_12.png"
    pause.1
    repeat
    
### HERMIONE HANDJOB CUMMING UNDER THE SHIRT ###
image undershirt_cum_ani:
    "03_hp/08_animation_02/14_finish_01.png"
    pause 1
    "03_hp/08_animation_02/14_finish_02.png"
    pause.1
    "03_hp/08_animation_02/14_finish_03.png"
    pause.1
    "03_hp/08_animation_02/14_finish_04.png"
    pause.1
    "03_hp/08_animation_02/14_finish_05.png"
    pause.1
    "03_hp/08_animation_02/14_finish_06.png"
    pause.1
    "03_hp/08_animation_02/14_finish_07.png"
    pause.1
    "03_hp/08_animation_02/14_finish_08.png"
    pause.1
    "03_hp/08_animation_02/14_finish_09.png"
    pause.1
    "03_hp/08_animation_02/14_finish_10.png"
    pause 2
    "03_hp/08_animation_02/14_finish_11.png"
    pause.1
    "03_hp/08_animation_02/14_finish_12.png"
    pause.1
    "03_hp/08_animation_02/14_finish_13.png"
    pause.1
    repeat
    
### HERMIONE HANDJOB CUMMING ON THE SHIRT ###
image on_shirt_cum_ani:
    "03_hp/08_animation_02/15_cum_00.png"
    pause.1
    "03_hp/08_animation_02/15_cum_01.png"
    pause.1
    "03_hp/08_animation_02/15_cum_02.png"
    pause.1
    "03_hp/08_animation_02/15_cum_03.png"
    pause.1
    "03_hp/08_animation_02/15_cum_04.png"
    pause.1
    "03_hp/08_animation_02/15_cum_05.png"
    pause.1
    "03_hp/08_animation_02/15_cum_06.png"
    pause.1
    "03_hp/08_animation_02/15_cum_07.png"
    pause.1
    "03_hp/08_animation_02/15_cum_08.png"
    pause.1
    "03_hp/08_animation_02/15_cum_09.png"
    pause.1
    "03_hp/08_animation_02/15_cum_10.png"
    pause.1
    "03_hp/08_animation_02/15_cum_11.png"
    pause.1
    "03_hp/08_animation_02/15_cum_12.png"
    pause.1
    "03_hp/08_animation_02/15_cum_13.png"
    pause.1
    "03_hp/08_animation_02/15_cum_14.png"
    pause.1
    "03_hp/08_animation_02/15_cum_15.png"
    pause.1
    "03_hp/08_animation_02/15_cum_16.png"
    pause.1
    "03_hp/08_animation_02/15_cum_17.png"
    pause.1
    "03_hp/08_animation_02/15_cum_18.png"
    pause.1
    "03_hp/08_animation_02/15_cum_19.png"
    pause.1
    "03_hp/08_animation_02/15_cum_20.png"
    pause.1
    "03_hp/08_animation_02/15_cum_21.png"
    pause 1
    "03_hp/08_animation_02/15_cum_22.png"
    pause.1
    "03_hp/08_animation_02/15_cum_21.png"
    pause.1
    "03_hp/08_animation_02/15_cum_22.png"
    pause .1
    "03_hp/08_animation_02/15_cum_21.png"
    pause 1
    "03_hp/08_animation_02/15_cum_23.png"
    pause.1
    "03_hp/08_animation_02/15_cum_24.png"
    pause.1
    "03_hp/08_animation_02/15_cum_25.png"
    pause.1
    "03_hp/08_animation_02/15_cum_00.png"
    pause.7
    repeat
    
    
### HERMIONE HANDJOB KISS DRINKING CUM FROM COCK ###
image kiss_cum_ani:
    "03_hp/08_animation_02/16_cum_01.png"
    pause.1
    "03_hp/08_animation_02/16_cum_02.png"
    pause.1
    "03_hp/08_animation_02/16_cum_03.png"
    pause.1
    "03_hp/08_animation_02/16_cum_04.png"
    pause.1
    "03_hp/08_animation_02/16_cum_05.png"
    pause.1
    "03_hp/08_animation_02/16_cum_06.png"
    pause.1
    "03_hp/08_animation_02/16_cum_07.png"
    pause.1
    repeat
    
    
### HERMIONE BLOWJOB ###
image blowjob_ani:
    "03_hp/08_animation_02/17_blow_01.png"
    pause.1
    "03_hp/08_animation_02/17_blow_02.png"
    pause.1
    "03_hp/08_animation_02/17_blow_03.png"
    pause.1
    "03_hp/08_animation_02/17_blow_04.png"
    pause.1
    "03_hp/08_animation_02/17_blow_05.png"
    pause.1
    "03_hp/08_animation_02/17_blow_06.png"
    pause.1
    "03_hp/08_animation_02/17_blow_07.png"
    pause.1
    "03_hp/08_animation_02/17_blow_08.png"
    pause.1
    "03_hp/08_animation_02/17_blow_09.png"
    pause.1
    "03_hp/08_animation_02/17_blow_10.png"
    pause.1
    "03_hp/08_animation_02/17_blow_11.png"
    pause.1
    "03_hp/08_animation_02/17_blow_12.png"
    pause.1
    repeat
    
### HERMIONE BLOWJOB NOT SUCKING ###
image hand_ani:
    "03_hp/08_animation_02/18_hand_01.png"
    pause 3  
    "03_hp/08_animation_02/18_hand_02.png"
    pause.1    
    "03_hp/08_animation_02/18_hand_03.png"
    pause.1    
    "03_hp/08_animation_02/18_hand_04.png"
    pause.1 
    repeat
    
### HERMIONE BLOWJOB CUM IN MOUTH ###
image cum_in_mouth_ani:
    "03_hp/08_animation_02/19_mouth_cum_01.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_02.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_03.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_04.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_05.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_06.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_07.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_08.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_09.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_10.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_11.png"
    pause 1
    "03_hp/08_animation_02/19_mouth_cum_12.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_13.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_14.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_15.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_16.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_17.png"
    pause 2
    "03_hp/08_animation_02/19_mouth_cum_18.png"
    pause.2
    "03_hp/08_animation_02/19_mouth_cum_01.png"
    pause 1
    repeat
    
### HERMIONE BLOWJOB CUM ON FACE ###
image cum_on_face_ani:
    "03_hp/08_animation_02/20_face_cum_01.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_02.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_03.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_04.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_05.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_06.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_07.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_08.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_09.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_10.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_11.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_12.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_13.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_14.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_15.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_16.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_17.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_18.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_19.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_20.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_21.png"
    pause.1    
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1   
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1   
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1  
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1 
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1 
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 2
    repeat

### HERMIONE CUM COVERED FACE BLINKING ###
image cum_on_face_blink_ani:
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1   
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1  
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1 
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1 
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1  
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 2
    repeat    
    
    
### HERMIONE SEX ###
image sex_ani:
    "03_hp/08_animation_02/21_sex_01.png"
    pause.1       
    "03_hp/08_animation_02/21_sex_02.png"
    pause.1    
    "03_hp/08_animation_02/21_sex_03.png"
    pause.1    
    "03_hp/08_animation_02/21_sex_04.png"
    pause.1    
    "03_hp/08_animation_02/21_sex_05.png"
    pause.1    
    "03_hp/08_animation_02/21_sex_06.png"
    pause.1    
    "03_hp/08_animation_02/21_sex_07.png"
    pause.1    
    repeat
    
### HERMIONE FAST SPEED SEX ###
image sex2_ani:
    "03_hp/08_animation_02/21_sex_01.png"
    pause.05      
    "03_hp/08_animation_02/21_sex_02.png"
    pause.05
    "03_hp/08_animation_02/21_sex_03.png"
    pause.05   
    "03_hp/08_animation_02/21_sex_04.png"
    pause.05    
    "03_hp/08_animation_02/21_sex_05.png"
    pause.05    
    "03_hp/08_animation_02/21_sex_06.png"
    pause.05    
    "03_hp/08_animation_02/21_sex_07.png"
    pause.05    
    repeat
    
    

### HERMIONE SEX LOW SPEED ###
image sex_slow_ani:
    "03_hp/08_animation_02/21_sex_01.png"
    pause.15       
    "03_hp/08_animation_02/21_sex_02.png"
    pause.15  
    "03_hp/08_animation_02/21_sex_03.png"
    pause.15    
    "03_hp/08_animation_02/21_sex_04.png"
    pause.15    
    "03_hp/08_animation_02/21_sex_05.png"
    pause.15    
    "03_hp/08_animation_02/21_sex_06.png"
    pause.15   
    "03_hp/08_animation_02/21_sex_07.png"
    pause.15  
    repeat
    
### HERMIONE SEX CUM OUTSIDE ###
image sex_cum_out_ani:
    "03_hp/08_animation_02/22_cum_01.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_02.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_03.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_04.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_05.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_06.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_07.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_08.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_09.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_10.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_11.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_12.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_13.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_14.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_15.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_16.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_17.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_18.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_19.png"
    pause 2     
    "03_hp/08_animation_02/22_cum_20.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_21.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_22.png"
    pause.1       
    "03_hp/08_animation_02/22_cum_23.png"
    pause.1    
    repeat
    
### HERMIONE SEX CUM OUTSIDE BLINKING###
image sex_cum_out_blink_ani:
    "03_hp/08_animation_02/22_cum_19.png"
    pause 1       
    "03_hp/08_animation_02/22_cum_24.png" #closed
    pause.1           
    "03_hp/08_animation_02/22_cum_19.png" 
    pause.1
    "03_hp/08_animation_02/22_cum_24.png" #closed
    pause.1           
    "03_hp/08_animation_02/22_cum_19.png" 
    pause 2
    "03_hp/08_animation_02/22_cum_24.png" #closed
    pause.1           
    "03_hp/08_animation_02/22_cum_19.png" 
    pause 2
    repeat
    

### HERMIONE SEX CUM INSIDE###
image sex_cum_in_ani:
    "03_hp/08_animation_02/23_cum_01.png"
    pause.1      
    "03_hp/08_animation_02/23_cum_02.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_03.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_04.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_05.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_06.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_07.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_08.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_09.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_10.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_11.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_12.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_13.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_14.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_15.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_16.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_17.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_18.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_19.png"
    pause 3   
    "03_hp/08_animation_02/23_cum_20.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_21.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_22.png"
    pause.1   
    "03_hp/08_animation_02/23_cum_23.png"
    pause.1   
    repeat
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    
    
    
    
### HANGING WITH SNAPE ###
image genie_jerking_sperm: #Genie and Snape sitting in front of fireplace...
    "03_hp/animation/hanging_with_snape_01.png"
    pause 2
    "03_hp/animation/hanging_with_snape_02.png"
    pause.2
    "03_hp/animation/hanging_with_snape_03.png"
    pause.2
    "03_hp/animation/hanging_with_snape_04.png"
    pause 1
    "03_hp/animation/hanging_with_snape_03.png"
    pause.2
    "03_hp/animation/hanging_with_snape_01.png"
    pause 3
    repeat
    
### Harry Potter Weather ###
image cloud_01: #Cloud behind the window.
    pause 2
    "03_hp/07_weather/01cloud_01.png"   
    pause 2 
    "03_hp/07_weather/01cloud_02.png"
    pause 2 
    "03_hp/07_weather/01cloud_03.png"
    pause 2 
    "03_hp/07_weather/01cloud_04.png" 
    pause 2 
    "03_hp/07_weather/01cloud_05.png"  
    pause 2 
    "03_hp/07_weather/01cloud_06.png"  
    pause 2 
    "03_hp/07_weather/01cloud_07.png"  
    pause 2 
    "03_hp/07_weather/01cloud_08.png"  
    pause 2 
    "03_hp/07_weather/01cloud_09.png"  
    pause 2 
    "03_hp/07_weather/01cloud_10.png"  
    pause 2 
    "03_hp/07_weather/01cloud_11.png"  
    pause 2 
    "03_hp/07_weather/01cloud_12.png"  
    pause 2 
    "03_hp/07_weather/01cloud_13.png"  
    pause 2 
    "03_hp/07_weather/01cloud_14.png"  
    pause 2 
    "03_hp/07_weather/01cloud_15.png"  
    pause 2 
    "03_hp/07_weather/01cloud_16.png"  
    pause 2 
    "03_hp/07_weather/01cloud_17.png"  
    pause 2 
    "03_hp/07_weather/01cloud_18.png"  
    pause 2 
    "03_hp/07_weather/01cloud_19.png"  
    pause 2 
    "03_hp/07_weather/01cloud_20.png"  
    pause 2 
    "03_hp/07_weather/01cloud_21.png"  
    pause 2 
    "03_hp/07_weather/01cloud_22.png" 
    pause 2 
    "03_hp/07_weather/01cloud_23.png"  
    pause 2 
    "03_hp/07_weather/01cloud_24.png"  
    pause 2 
    "03_hp/07_weather/01cloud_25.png"  
    pause 2 
    "03_hp/07_weather/01cloud_26.png"  
    pause 2 
    "03_hp/07_weather/01cloud_27.png"  
    pause 2 
    "03_hp/07_weather/01cloud_28.png"  
    pause 2 
    "03_hp/07_weather/01cloud_29.png"  
    pause 2 
    "03_hp/07_weather/01cloud_30.png"  
    pause 2 
    "03_hp/07_weather/01cloud_31.png"  
    pause 2 
    "03_hp/07_weather/01cloud_32.png"  
    pause 2
    "03_hp/07_weather/01cloud_01.png"   
    pause 9
    repeat
    
    
image rain: #Rain.
    "03_hp/07_weather/rain_01.png"   
    pause.1 
    "03_hp/07_weather/rain_02.png"   
    pause.1
    "03_hp/07_weather/rain_03.png"   
    pause.1
    repeat
    
    
image candle_fire: #Candle fire.
    "03_hp/05_props/fire_01.png"   
    pause.1 
    "03_hp/05_props/fire_02.png"   
    pause.1 
    "03_hp/05_props/fire_03.png"   
    pause.1 
    "03_hp/05_props/fire_04.png"   
    pause.1 
    "03_hp/05_props/fire_05.png"   
    pause.1 
    "03_hp/05_props/fire_06.png"   
    pause.1 
    "03_hp/05_props/fire_07.png"   
    pause.1 
    "03_hp/05_props/fire_08.png"   
    pause.1 
    "03_hp/05_props/fire_09.png"   
    pause.1 
    "03_hp/05_props/fire_10.png"   
    pause.1 
    repeat
    
image candle_fire_02: #Candle fire.
    "03_hp/05_props/fire_01.png"   
    pause.1 
    "03_hp/05_props/fire_04.png"   
    pause.1 
    "03_hp/05_props/fire_03.png"   
    pause.1 
    "03_hp/05_props/fire_02.png"   
    pause.1 
    "03_hp/05_props/fire_08.png"   
    pause.1 
    "03_hp/05_props/fire_06.png"   
    pause.1 
    "03_hp/05_props/fire_07.png"   
    pause.1 
    "03_hp/05_props/fire_05.png"   
    pause.1 
    "03_hp/05_props/fire_10.png"   
    pause.1 
    "03_hp/05_props/fire_09.png"   
    pause.1 
    repeat    
    
    
image lightening: #Lightening during rain behind the window.
    pause 20
    "03_hp/07_weather/lightining_01.png"   
    pause.1    
    "03_hp/07_weather/lightining_02.png"   
    pause.1 
    "03_hp/07_weather/lightining_03.png"   
    pause.1 
    "03_hp/07_weather/lightining_04.png"   
    pause.1 
    "03_hp/07_weather/lightining_05.png"   
    pause.1 
    "03_hp/07_weather/lightining_06.png"   
    pause.1 
    "03_hp/07_weather/lightining_05.png"   
    pause.1 
    "03_hp/07_weather/lightining_06.png"   
    pause.1 
    "03_hp/07_weather/lightining_05.png"   
    pause 20
    repeat
    

image fireplace_fire: #Fireplace fire.
    "03_hp/05_props/fireplace_fire_01.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_02.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_03.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_04.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_05.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_06.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_07.png"   
    pause.1
    "03_hp/05_props/fireplace_fire_08.png"   
    pause.1
    repeat
    
    
image feeding: #FEEDING THE PHOENIX.
    "03_hp/animation/feeding_01.png"   
    pause.5
    "03_hp/animation/feeding_02.png"   
    pause.1
    "03_hp/animation/feeding_03.png"   
    pause.1
    "03_hp/animation/feeding_04.png"   
    pause.1
    "03_hp/animation/feeding_05.png"   
    pause.5
    "03_hp/animation/feeding_03.png"   
    pause.1
    "03_hp/animation/feeding_02.png"   
    pause.1
    "03_hp/animation/feeding_01.png" 
    

image petting: #PETTING THE PHOENIX.
    "03_hp/animation/petting_01.png"   
    pause 1  
    "03_hp/animation/petting_02.png"   
    pause.1
    "03_hp/animation/petting_03.png"   
    pause.1
    "03_hp/animation/petting_04.png"   
    pause.1
    "03_hp/animation/petting_05.png"   
    pause.1
    "03_hp/animation/petting_06.png"   
    pause.2
    "03_hp/animation/petting_05.png"   
    pause.2
    "03_hp/animation/petting_06.png"   
    pause.2
    "03_hp/animation/petting_05.png"   
    pause.2
    "03_hp/animation/petting_06.png"   
    pause.2
    "03_hp/animation/petting_05.png"   
    pause.2
    "03_hp/animation/petting_04.png"   
    pause.1
    "03_hp/animation/petting_03.png"   
    pause.1
    "03_hp/animation/petting_02.png"   
    pause.1
    "03_hp/animation/petting_01.png"   
    pause.1
    


image owl_01: #OWL WITH ENVELOPE IN IT'S MOUTH, BLINKING.
    "03_hp/05_props/owl_01.png"   
    pause.1
    "03_hp/05_props/owl_02.png"   
    pause.1
    "03_hp/05_props/owl_03.png"   
    pause.15
    "03_hp/05_props/owl_02.png"   
    pause.1
    "03_hp/05_props/owl_01.png"   
    pause 7
    repeat

    
## ANIMATIONS



#############################################
    
image heal:
    "magic/heal01.png"
    pause.06
    "magic/heal02.png"
    pause.06
    "magic/heal03.png"
    pause.06
    "magic/heal04.png"
    pause.06
    "magic/heal05.png"
    pause.06
    "magic/heal06.png"
    pause.06
    "magic/heal07.png"
    pause.06
    "magic/heal08.png"
    pause.06    
    "magic/heal09.png"
    pause.06
    "magic/heal10.png"
    pause.06            
    "magic/heal11.png"
    pause.06
    "magic/heal12.png"
    pause.06
    "magic/heal13.png"
    pause.06
    "magic/heal14.png"
    pause.06    
    "magic/heal15.png"
    pause.06
    "magic/heal16.png"
    pause.06  
    "magic/heal17.png"
    pause.06
    "magic/heal18.png"
    pause.06 
    
image heal_02: # Smaller version of heal. 40% of the original size.
    "magic_02/heal01.png"
    pause.06
    "magic_02/heal02.png"
    pause.06
    "magic_02/heal03.png"
    pause.06
    "magic_02/heal04.png"
    pause.06
    "magic_02/heal05.png"
    pause.06
    "magic_02/heal06.png"
    pause.06
    "magic_02/heal07.png"
    pause.06
    "magic_02/heal08.png"
    pause.06    
    "magic_02/heal09.png"
    pause.06
    "magic_02/heal10.png"
    pause.06            
    "magic_02/heal11.png"
    pause.06
    "magic_02/heal12.png"
    pause.06
    "magic_02/heal13.png"
    pause.06
    "magic_02/heal14.png"
    pause.06    
    "magic_02/heal15.png"
    pause.06
    "magic_02/heal16.png"
    pause.06  
    "magic_02/heal17.png"
    pause.06
    "magic_02/heal18.png"
    pause.06     

    
### DR'S Newspaper ooo ###

image nsp_cheerleader_dance1_ani:
    "03_hp/08_animation_02/nsp01_cheerleader_01.png"
    pause.5    
    "03_hp/08_animation_02/nsp01_cheerleader_02.png"
    pause.5    
    "03_hp/08_animation_02/nsp01_cheerleader_03.png"
    pause.5    
    "03_hp/08_animation_02/nsp01_cheerleader_04.png"
    pause.5    
    repeat   
    
image nsp_cheerleader_dance2_ani:
    "03_hp/08_animation_02/nsp01_cheerleader_01.png"
    pause.3    
    "03_hp/08_animation_02/nsp01_cheerleader_02.png"
    pause.3    
    "03_hp/08_animation_02/nsp01_cheerleader_03.png"
    pause.3    
    "03_hp/08_animation_02/nsp01_cheerleader_04.png"
    pause.3    
    "03_hp/08_animation_02/nsp01_cheerleader_01.png"
    pause.5  
    "03_hp/08_animation_02/nsp01_cheerleader_05.png"
    pause.5  
    repeat 
    
image nsp_hermiona_panic_ani:
    "03_hp/animation/h_run_01.png"
    pause.07
    "03_hp/animation/h_run_02.png"
    pause.07
    "03_hp/animation/h_run_03.png"
    pause.07
    "03_hp/animation/h_run_04.png"
    pause.07
    "03_hp/animation/h_run_05.png"
    pause.07
    "03_hp/animation/h_run_01f.png"
    pause.07
    "03_hp/animation/h_run_02f.png"
    pause.07
    "03_hp/animation/h_run_03f.png"
    pause.07
    "03_hp/animation/h_run_04f.png"
    pause.07
    "03_hp/animation/h_run_05f.png"
    pause.07
    repeat
    
##########################SEX################


image side mage = "mage.png"
image side mage1 = "mage1.png"
image side mage2 = "mage2.png"
image side mage3 = "mage3.png"
image side mage4 = "mage4.png"
image side mage5 = "mage5.png"
image side mage6 = "mage6.png"
image side mage7 = "mage7.png"
image side mage8 = "mage8.png"
image side mage9 = "mage9.png"
image side mage10 = "mage10.png"
image side mage11 = "mage11.png"
image side aka1 = "aka.png"
image side aka2 = "aka2.png"
image side aka3 = "aka3.png"
image side aka4 = "aka4.png"
image side aka5 = "aka5.png"
image side aka6 = "aka6.png"
image side aka7 = "aka7.png"
image side dum1 = "dum_01.png"
image side dum2 = "dum_02.png"
image side dum3 = "dum_03.png"
image side dum4 = "dum_04.png"
image side dum5 = "dum_05.png"

define dahr = Character(None,
    color="#402313",
    window_left_padding=230,
    show_side_image=Image("03_hp/18_store/dahr.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")
    
## CHARACTERS 

define s = Character(None, color="#402313", ctc="ctc3", ctc_position="fixed")
define m = Character(None, window_left_padding=200, image="mage", color="#402313", ctc="ctc3", ctc_position="fixed")
define g1 = Character(None, window_left_padding=200, image="mage1", color="#402313", ctc="ctc3", ctc_position="fixed")
define g = Character(None, window_left_padding=300, image="mage2", color="#402313", ctc="ctc3", ctc_position="fixed")
define g2 = Character(None, window_left_padding=300, image="mage3", color="#402313", ctc="ctc3", ctc_position="fixed")
define g4 = Character(None, window_left_padding=200, image="mage4", color="#402313", ctc="ctc3", ctc_position="fixed")
define g5 = Character(None, window_left_padding=200, image="mage5", color="#402313", ctc="ctc3", ctc_position="fixed")
define g6 = Character(None, window_left_padding=200, image="mage6", color="#402313", ctc="ctc3", ctc_position="fixed")
define g7 = Character(None, window_left_padding=200, image="mage7", color="#402313", ctc="ctc3", ctc_position="fixed")
define g8 = Character(None, window_left_padding=200, image="mage8", color="#402313", ctc="ctc3", ctc_position="fixed")
define g9 = Character(None, window_left_padding=200, image="mage9", color="#402313", ctc="ctc3", ctc_position="fixed")
define g10 = Character(None, window_left_padding=200, image="mage10", color="#402313", ctc="ctc3", ctc_position="fixed")
define g11 = Character(None, window_left_padding=200, image="mage11", color="#402313", ctc="ctc3", ctc_position="fixed")
define a = Character(None, window_left_padding=220, image="aka", color="#402313", ctc="ctc3", ctc_position="fixed")
define a1 = Character(None, window_left_padding=220, image="aka1", color="#402313", ctc="ctc3", ctc_position="fixed")
define a2 = Character(None, window_left_padding=220, image="aka2", color="#402313", ctc="ctc3", ctc_position="fixed")
define a3 = Character(None, window_left_padding=220, image="aka3", color="#402313", ctc="ctc3", ctc_position="fixed")
define a4 = Character(None, window_left_padding=290, image="aka4", color="#402313", ctc="ctc3", ctc_position="fixed")
define a5 = Character(None, window_left_padding=220, image="aka5", color="#402313", ctc="ctc3", ctc_position="fixed")
define a6 = Character(None, window_left_padding=220, image="aka6", color="#402313", ctc="ctc3", ctc_position="fixed")
define a7 = Character(None, window_left_padding=220, image="aka7", color="#402313", ctc="ctc3", ctc_position="fixed")

define dum = Character(None, window_left_padding=240, image="dum1", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum2 = Character(None, window_left_padding=240, image="dum2", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum3 = Character(None, window_left_padding=240, image="dum3", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum4 = Character(None, window_left_padding=240, image="dum4", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum5 = Character(None, window_left_padding=240, image="dum5", color="#402313", ctc="ctc3", ctc_position="fixed")



define eslow = Character(None, color="#402313", what_slow_cps=20)
define centertext = Character(None,
                          what_size=20, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          what_outlines=[(3, "#000000", 2, 2), (3, "#ffffff", 0, 0)],
                          #Gives an outline
                          what_slow_cps=20 #Speed at which the text appears (slow)
                          )

init-2:
    ### MENU PLACEMENT ###
    $ menu_x = 0.5

    
    
    
    $ teleport = ImageDissolve("id_teleport.png", 1.0, 0)
   


    # Declare an nvl-version of eileen.
    $ nvle = Character(color="#000", what_color="#ffffff", kind=nvl)
    
    
    $ who = Character('Женский голос', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ whom = Character('Мужской голос', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr1 = Character('Кто-то из толпы', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr2 = Character('Другой голос из толпы', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr3 = Character('Женский голос', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr5 = Character('Толпа', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr6 = Character('Несколько голосов сразу', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ who2 = Character('???', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ g3 = Character('Genie', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ fem = Character('Студентка', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ mal = Character('Студент # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ mal2 = Character('Студент # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ ann = Character('Диктор', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sly1 = Character('Студент Слизерина', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sly2 = Character('Другой студент Слизерина', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ aa = Character('АКАБУР', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    
    
    
    $ elena_pts = 0
    
    ###HARRY POTTER CHARACTERS###
    $ translators = Character('Переводчик', color="#0089BE", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    #$ skaz = Character('Сказочник', color="#0000FF")
    #$ nyark = Character ('Nyarkohotep', color="FF0000")
    ### DR'S CODE ooo ###
    #$ dr = Character('Дрон', color="#00FF00")
    $ ach = Character('Достижение', color = "#888888")
    $ dev = Character('??????', color = "#0000FF")
    ###
    #$ felix = Character('Феликс', color="#7789CA")
    ###
    $ her = Character('Гермиона', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ her2 = Character('Гермиона', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    $ sna = Character('Северус Снейп', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sna2 = Character('Северус Снейп', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed")  #Text box used for "head only" speech. (Because it has padding).
    $ vol = Character('Лорд Волдеморт', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ l = Character('Лола', color="#402313", window_right_padding=230, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    
    $ lun = Character('Луна', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ pho = Character('Феникс', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
#    $ daph = Character('Дафна', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
#    $ daph2 = Character('Дафна', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Это текстовое окно, оно используется для головы(потому что имеет отступы)

#-----------------------___HEADS___---------------------------------#
    
init python:
  def conditional_portrait( status_var, filename_prefix, startIndex, endIndex, **kwargs ):
        args = []
        for s in range( startIndex, endIndex + 1 ):
            args.append( "%s == %d" % (status_var, s) )
            args.append( Image( "%s%02d.png" % ( filename_prefix, s ) ) )
        return ConditionSwitch( *args, **kwargs )    
    
    
### SNAPE HEAD ###
define sna_head_state = 1
define sna_head_main = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=conditional_portrait( "sna_head_state", "03_hp/12_snape_head/head_", 1, 26, xalign=1.0, yalign=0.0 ),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


### HERMIONE HEAD ###
define her_head_state = 1
define her_head_main = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=conditional_portrait( "her_head_state", "03_hp/15_hermione_head/", 1, 45, xalign=1.0, yalign=0.0 ),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed" )


## TRANSFORMATION



transform basicfade:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.5 alpha 0.0

transform basicfade2:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0
            
transform basicfade3:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 0.8 alpha 0.0 

transform basicfade4:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0 
            
            
            
label start:

# Если поставть флаг, более вменяемые сообщения о некоторых ошибках при сохранении. На саму игру не влияет
    init python:
         config.use_cpickle = False

    # Ending class initialization
    call Ending_constants
    call Achievement_constants
    python:
        global end
        global achieve
    $ end = Ending ()
    $ achieve = Achievement()

    # Создание elog должно стоять перед вызовами GetValue, так что лучше его сделать сразу после метки start
    call start_elog
    call after_load

    call main_ex_CharacterExItem_constants
    python:
        # it's the fucking magic - make custom class variable being saved by Ren'Py...
        # global keyword says to python that this variable will be global
        # and because it's defined after 'start' label - it'll be saved by Ren'Py, great!
        
        # main data of hermione
        global herData
        # full-sized view
        global herView
        # dialogue-face view
        global herViewHead  

    $herData = hermi.GetValue("vData")    
    $herView = hermi.body    
    $herViewHead = hermi.head   
        
    #$ herData = CharacterExData( WTXmlLinker.getHermioneLinkerKey() )
#    $ herData = CharacterExData( WTXmlLinker.getLinkerKey_hermione() )
#    $ herData.clearState()
    
#    $ herView = CharacterExView( 5, her, 'hermione' )
#    $ herView.attach( herData )
    
#    $ herViewHead = CharacterExView( 8, her2, 'hermione_head' )
#    $ herViewHead.pushScreenTag( 'head' )
#    $ herViewHead.attach( herData )

    # test new stuff! load all this with two sets - body and clothes!
#    $herView.data().addItemSet( 'hermione_body' )
#    $herView.data().addItemSet( 'hermione_start_clothes' )

    
    $ hermi.WrdInit()
    $ hermi.WrdSetMain()

    $ gold = 0
    $ turbo =1
    $ avogadro_law = False
    
    $ rum_times = 0 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    
    ### HERMIONE_MAIN SCREN FLAGS ###
    $ only_upper = False #When true, legs are not displayed in the hermione_main screen.
    $ autograph = False #Displays professor Lockhart's autograph on Hermione's leg.
    $ no_blinking = False #When True - blinking animation is not displayed. 
    $ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    $ legs_02 = False # Turns TRUE when xxxsmallskirt is activated.
    $ h_tears = False #Displays a layer with tears.
     
    $ current_payout = 0 #Used when haggling about price of th favor.
     
    $ snape_invated_to_watch = False #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
    $ invited_snape_once_already = False #In the "Dance for me" event, after you send Hermione to invite Snape to watch for the first time - turns TRUE.
    
    $ uni_sperm = False #Triggers universal sperm to show on hermione_main screen.
    $ days_without_an_event = 0 #Counts days since last (any) event took place.
    
    $ ask_me_once = False #Turns true after Hermione asks you about your true identity, during sex.
    
    $ tiara = False #When TRUE tiara is displayed on h_head2 and hermione_main screens.

#    $ public_whore_ending = False #If TRUE the game will end with "Public Whore Ending".
    
    $ p_level_02_active = False #When turns TRUE public favors of level 02 become available. 
    $ p_level_03_active = False #When turns TRUE public favors of level 03 become available. 
    $ p_level_04_active = False #When turns TRUE public favors of level 04 become available. 
    $ p_level_05_active = False #When turns TRUE public favors of level 05 become available. 
    $ p_level_06_active = False #When turns TRUE public favors of level 06 become available. 
    $ p_level_07_active = False #When turns TRUE public favors of level 07 become available. 


    $ lazy_aka_not_yet = True #In public events. Kiss a girl. Event level 03. Event # 3. "Lazy Akabur bug". Turns FALSE after that.
    $ sucked_off_ron = False #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
    $ suked_off_ron_and_har = False #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
    $ fucked_ron_and_har = False #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.



    
    
###HOUSE POINTS RELATED###
    $ snapes_support = 0 #Controls how much points is awarded to SLYTHERIN daily.
    


###HERMIONE STATS###
#    $ mad = 0 #Every day -1.

    
### JERKING OFF FLAGS ###
    $ request_03 = False #True when Hermione has no panties on.
    $ jerking_session = False
    $ have_cum_soaced_panties = False #TRUE when you have the panties in your possession (before you return them to Hermione).

    $ jerking_off_to_jasmine = False #Turns TRUE when Princess Jasmine has been chosen as a target for a jerk-off session.
    $ jerking_off_to_lara = False 
    $ cum_on_the_floor = False #TRUE when chosen to cum on the floor.
    $ cum_on_panties = False #True when choose to cum on Hermione's panties.


### EVENTS ###
    $ event08_happened = False #Turns TRUE after event_08 (Hermone visits first time).
    $ event09 = False #Turns TRUE when you let Hermione in during event_09. Otherwise she will keep coming every morning.
    $ event10 = False #Turns TRUE when you let Hermione in during event_10. Otherwise she will keep coming every morning.
    $ event11_happened = False #Turns TRUE after event_11
    $ event12_happened = False #Turns TRUE after event_12
    $ event13_happened = False #Turns TRUE after event_13
    $ event14_happened = False #Turns TRUE after event_14
    $ event15_happened = False #Turns TRUE after event_15
    $ event16_happened = False #Turns TRUE after event_16
    
    $ request_30_a = False #Turns true when hermione fails to show up after her "Fuck a classmate" favor. Runs an event next morning.
    
### 27_FINAL_EVENTS ###
#    $ event_chairman_happened = False #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
#    $ snape_against_chairman_hap = False # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
#    $ have_no_dress_hap = False #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
#    $ sorry_for_hesterics = False # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    

    $ slytherin = 180 #Shows amount of points the Slytherin house has.
    $ gryffindor = 53 #Shows amount of points the Gryffindor house has.
    $ hufflepuff = 25 #Shows amount of points the Hufflepuff house has.
    $ ravenclaw = 31 #Shows amount of points the Ravenclaw house has.



    
  

### MISC FLAGS ###

    $ lock_public_favors = False #Turns True if reached whoring level 05 while public 
    $ touched_by_boy = False #Turns true if sent Hermione to get touched by a boy at least once.
    
    $ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once a day. Turns back to False every night.
    $ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    

### STORE BOOKS AND ITEMS ###

#    $ bought_book_05_b = False #Affects 15_mail.rpy

    $ dear_waifu_completed_once = False # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
    $ found_dahrs_ticket_once = False # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
    $ vouchers = 0 #Shows the amount of DAHR's vouchers in your possession.
    
    

    
    $ searched = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ wine_not = False # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
    
    $ robeon = False # When true - Hermione is wearing a robe.
    
    $ sfmax = False # Turns TRUE when friendship with Snape been maxed out.
    
    $ badges = False # Turns layer with a badgge on and off in hermione_main screen.
    $ ba_01 = False # Desplays a badge in hermione_main screen.
    $ ne = False # Desplays a fishnets LAYER in hermione_main screen.
    $ ne_01 = False # Desplays the fishnets in hermione_main screen.
    
    $ flip = False # When TRUE Hermione's full size sprite is flipped.

    
    
    
   
    
    ### DUEL ###
    $ potions = 0 #Amount of healing potions Genie has in stock.
    
    $ tut_happened = False # Turns TRUE after you click the tutoring button and see the message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.
    
    $ cataloug_found = False # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
    
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ work_unlock2 = False # Unlocks the "Paperwork" button.
    
    $ bird_interact = 0 # Counts how many times you have interacted with the bird.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    ### XXXSMALLSKIRT ###
#    $ bought_skirt_already = False # Turns TRUE after you redeem the voucher and get the mini skirt.
#    $ bought_xxxsmallskirt = False #Affects 15_mail.rpy
#    $ have_xxxsmallskirt = False # Turns TRUE when you have the skirt in your possession.
#    $ gave_xxxsmallskirt = False #Turns True when Hermione has the xxxsmallskirt.
    
    $ dress_code = False # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    
    show image "blackfade.png"

#    menu:
#        "Тестировать чибиков?":
#            jump test_daphna
#        "Продолжить запуск":
#            pass

    if persistent.game_complete: # Offer for game+
        menu:
            "Новая игра +" ">Хотите перенести все золото и имущество из предыдущей игры?"
            "\"Да, пожалуйста.\"":
                $ gold = gold + persistent.gold
                ">Добавлено: [persistent.gold] галеонов."
                python:
                    if persistent.itemSet!=None:
                        for o in persistent.itemSet:
                            hero.Items.AddItem(o,persistent.itemSet[o])
                            renpy.say("",">Добавлено: \""+hero.Items(o)._caption+"\" ("+str(hero.Items(o)._count)+" шт.)")
                            
                
            "\"Не нужно.\"":
                pass

#    menu:         
#        "Отлаживать":
#            $ end.SetEndingValue(const_ENDING_PUBLIC_WHORE,2)
#            $ hermione_main_zorder = 5  
#            $ hermione_chibi_ypos = 250
#            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
#            $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
#            jump test
#    dev "Всем привет, и с новой версией \"Тренера Ведьмы\"!"
#    dev "Игра получилась объемная, и становится больше с каждым новым обновлением."
#    dev "И поэтому проходить ее каждый раз, чтобы добраться до нового контента может быть очень утомительным."
#    dev "Вы хотите включить \"Режим Авогадро\", чтобы получить кучу золота, очков Слизерина и послабления в некоторых других областях?"
#    m "Почему \"Авогадро\"?"
#    dev "..."
#    dev "... потому что звучит круто?"
#    m "У меня для тебя плохие новости..."
#    m "И вообще, игра еще не началась, а ты уже занимаешься самовставками, при том, что работы сделал с гулькин нос."
#    dev "Но я..."
#    m "И что с этим красным цветом на твоем нике?"
#    dev "Красный - цвет силы!"
#    m "..."
#    m "Я ухожу отсюда."
#    $ renpy.play('sounds/door.mp3')
#    dev "..."
#    dev "Чем плох красненький..?"
#    dev "*вздох* В общем, если надо, я могу намного облегчить ваше прохождение."
#    dev "Вы хотите воспользоваться этим эксплоитом, или в полной мере насладиться Гриндом?"
#    dev "Предупреждаю - возможны баги и несоответствия с сюжетом игры."
    
    menu:
        "Дай мне чит!":
            $ avogadro_law = True
            $ gold = gold + 10000
            $ slytherin = 3000
            ">Добавлена здоровая куча золота.\n>Слизерин находится в далеком отрыве от всех.\n>Поладить со Снейпом стало гораздо легче."
            
        "Нет, читеры должны гореть в аду!":
#            dev "..."
            dev "Ты - истинный самурай."
            pass
    menu:         
        "Вы желаете пропустить интро?"
        "Начать интро.":
            jump intro
        "Пропустить интро.":
            jump hp
        "Перейти сразу на утро после дуэли.":
            $this.event_05.SetValue("finish2",4)
            jump hp
    
   
label masterstart: 
    stop music fadeout 1
    $ renpy.music.set_volume(1.0, .5, channel=7)
   
    scene bg meadow
    show sylvie smile
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    show whitefade at basicfade, center
    show magic at basicfade, center
    show magic2 at basicfade2, center
    show magic3 at basicfade3, center
    show magic4 at basicfade4, center
    hide magic
    hide magic2
    hide magic3
    hide magic4
    hide whitefade
    show heal
    
label masterstart2: 
    stop music fadeout 1
    
    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7
    
