label menu_reading_book:

    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block and e._status>=0: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Книга: "+e._caption+" - "+("{image=check_08.png}" if e.IsDone() else ""), 
                    "reading_book_done" if e.IsDone() else "menu_reading_book_2", e.Name)

    $ choose.Show("books_list")

    label menu_reading_book_2:
        $ the_gift = wtevent._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3

        "\"[wtevent._caption]\"" "[wtevent._description]"#" Вы хотите прочитать ее?"
        menu:
            "- Читать книгу -":
# Проверяем, что освоены предыдущие ступени навыка:
### DR'S NEWSPAPER ooo ###
                if wtevent.GetValue("block")=="books_newsp":
                    if wtevent.Name=="nsp_newsp_book_p02a" and nsp_genie_writer < 1:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p02b" and nsp_genie_writer < 2:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p03a" and nsp_genie_writer < 3:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p03b" and nsp_genie_writer < 4:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p04" and nsp_genie_writer < 5:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p05a" and nsp_genie_writer < 6:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p05b" and nsp_genie_writer < 7:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p06a" and nsp_genie_writer < 8:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p06b" and nsp_genie_writer < 9:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                    
                if wtevent.GetValue("block")=="books_newsp2":
                    if wtevent.Name == "nsp_newsp_book_typo1" and (nsp_genie_typographic < 0 or nsp_genie_typographic_exp < 2):
                        m "Слишком мало опыта, нужно не менее двух публикаций с типографическим набором предыдущего уровня."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo2" and (nsp_genie_typographic < 1 or nsp_genie_typographic_exp < 2):
                        m "Слишком мало опыта, нужно не менее двух публикаций с типографическим набором предыдущего уровня."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo3" and (nsp_genie_typographic < 2 or nsp_genie_typographic_exp < 2):
                        m "Слишком мало опыта, нужно не менее двух публикаций с типографическим набором предыдущего уровня."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo4" and (nsp_genie_typographic < 3 or nsp_genie_typographic_exp < 2):
                        m "Слишком мало опыта, нужно не менее двух публикаций с типографическим набором предыдущего уровня."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo5" and (nsp_genie_typographic < 4 or nsp_genie_typographic_exp < 2):
                        m "Слишком мало опыта, нужно не менее двух публикаций с типографическим набором предыдущего уровня."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo6" and (nsp_genie_typographic < 5 or nsp_genie_typographic_exp < 2):
                        m "Слишком мало опыта, нужно не менее двух публикаций с типографическим набором предыдущего уровня."
                        hide screen gift
                        jump books_list
                        
                if wtevent.GetValue("block")=="books_newsp2":
                    if wtevent.Name == "nsp_newsp_book_photo2" and (nsp_genie_photocamera < 1 or nsp_genie_photocamera_exp < 3):
                        m "Слишком мало опыта, нужно провести не менее трех фотосессий с фотоаппаратом предыдущего типа."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_photo3" and (nsp_genie_photocamera < 2 or nsp_genie_photocamera_exp < 3):
                        m "Слишком мало опыта, нужно провести не менее трех фотосессий с фотоаппаратом предыдущего типа."
                        hide screen gift
                        jump books_list

                    if wtevent.Name == "nsp_newsp_book_photo4" and (nsp_genie_photocamera < 3 or nsp_genie_photocamera_exp < 3):
                        m "Слишком мало опыта, нужно провести не менее трех фотосессий с фотоаппаратом предыдущего типа."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_video" and (nsp_genie_photocamera < 4 or nsp_genie_sphere_ruby_level_eff < 1 or nsp_genie_sphere_diamond_level_eff < 1 or nsp_genie_sphere_sapphire_level_eff < 3):
                        m "Для освоения навыков из этой книги вам понадобится владение всеми видами фотоаппаратов, хрустальный шар, сапфир 3 уровня, рубин и алмаз."
                        hide screen gift
                        jump books_list
                        
############

                if wtevent.GetValue("block")=="books_edu":
                    if wtevent.prevInList.GetValue("block")!=wtevent.GetValue("block") or wtevent.prevInList.IsDone():
                        jump reading_book_xx
                    else:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                else:
                    if wtevent.Name=="book_05_b" and not this.book_05.IsDone():
                        m "Есть странные люди, которые приступают к книге со второй ее части. Но я не из таких."
                        jump expression _label
                    else:
                        jump reading_book_xx #"reading_book_01"
            "- Ничего -":
                hide screen gift
                jump expression _label #books_on_improvement

    label reading_book_done:
        $ the_gift = wtevent._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        "\"[wtevent._caption]\"" "[wtevent._description]."


# Отдельная обработка для Вайфу - ее нужно читать несколько раз                                
        if wtevent.Name=="book_07":
            if waifu_book_completed:
                m "Я не думаю, что повторное чтение этой книги даст мне хоть что-то."
                hide screen gift
                jump fiction_books

            if dear_waifu_completed_once:
                if book_07_units == 0:
                    m "Не думаю, что повторное чтение этой книги даст мне хоть что-то. Прочесть ее просто ради удовольствия?"
                    menu:
                        "- Читать книгу снова -":
                            hide screen gift
                            jump reading_book_xx
                        "- Ничего -":
                            hide screen gift
                            jump fiction_books
                else:
                    m "Я уже закончил ее, но решил прочесть еще раз ради удовольствия..."
                    hide screen gift
                    jump reading_book_xx
        else:
            m "Я уже закончил ее. "
            if wtevent._block=="books_edu" and wtevent._conclusion!="":
                m "Она дала мне новый навык: [wtevent._conclusion]"
            else:
                m "[wtevent._conclusion]"

            if wtevent.Name=="book_04":
                g4 "Я обуздал свой дух!"
                g9 "Мой дух - моя сучка!"

        hide screen gift
        jump expression _label

label desk:
    $ menu_x = 0.5 
    $ nsp_genie_sphere_video_txt = ""

    menu:
### DR'S NEWSPAPER ooo ###

        "- Искать приложение к каталогу -" if nsp_pre_snape == 5 and nsp_pre_dahre == 0:
            $ nsp_pre_dahre = 1
            m "Вы обнаружили дополнительный каталог книг для печатного дела."
            jump day_main_menu
            
        "- Искать другие приложения к каталогу -" if nsp_newspaper_menu == 4:
            $ nsp_newspaper_menu = 5
            m "Вы обнаружили дополнительный каталог дополнительных средств для печатного дела."
            jump day_main_menu
            
        "- Попытаться починить хрустальный шар -" if nsp_newspaper_menu >= 9 and nsp_newspaper_menu < 15:
            
            if nsp_newspaper_menu == 9 :
                ">Вы внимательно осмотрели шар со всех сторон. На вид он кажется сделан из тусклого стекла, которое почти не пропускаяет свет."
                ">Никаких подсказок. В такой ситуации можно прибегнуть к внутреннему зрению джина."
                ">На это ушло много времени, но вам удалось обнаружить особую магическую ауру шара."
            elif nsp_newspaper_menu == 10 :
                ">После долгой медитации вы обнаружили, что аура шара чужда этому месту. возможно даже..."
                ">Нет, лучше это все-таки проверить."
            elif nsp_newspaper_menu == 11 :
                ">Новое исследование подтвердило вашу догадку. Этот предмет не из мира Хогвартса."
            elif nsp_newspaper_menu == 12 :
                ">Потраченное время все-таки принесло плоды. Вам удалось уловить отблески солнца, играющие на бескрайних песках."
                ">Сухость воздуха и остроту колючек. Чары и месть, отвагу и честь..."
                ">Этот хрустальный шар был сделан в мире Аграбы, в вашем родном мире !"
                ">Вот почему он работает не как шар для предсказаний ! В Аграбе правила магии совсем иные !"
                ">Теперь нет сомнений, что вы сможете его починить."
            elif nsp_newspaper_menu == 13 :
                ">Вы потратили много времени на попытки призвать свою космическую силу."
                $hero (g4,"Ыыыыыыыть.")
                $hero (g4,"Аргх!")
                $hero (g4,"Ааааать.")
                $hero (g4,"Ух.")
                ">И так в течение нескольких часов..."
                ">Безрезультатно."
            elif nsp_newspaper_menu == 14 :
                $hero (m,"Почему же все бесполезно ?")
                $hero ("Конечно я никогда не был по-настоящему {size=+4}всесильным{/size}, но это уже слишком.")
                $hero ("А ведь что-то могло бы задать моей магии необходимый импульс.")
                $hero (g6,"Хм.")
                $hero (g6,"Раньше лучшим стимулом было выполнение какого-нибудь желания.")
                $hero (g7,"Итак, Джин, сконцентрируйся. Снейп желает фотографии из самых укромных мест, и единственное средство - работающий шар.")
                $hero (g4,"Ну же ! Напрягись ! Ыыыыыы.")
                ">Кажется, у вас начало получаться !"
                $hero (g4,"Аргх !")
                $hero (g8,"Фу-ух !")
                ">На столе перед вами лежит целый хрстальный шар. Слабое свечение исходит изнутри"
                ">Теперь вы способны легко понять, как он устроен, и составляете небольшую инструкцию."
                $hero (m,"Наконец-то !")
                $ nsp_genie_sphere = True
                
            $ nsp_newspaper_menu += 1
            
            if daytime:
                jump night_start
            else: 
                jump day_start  

###
        "- Осмотреть -" if not desk_examined:
            $ desk_examined = True
            m "Обычный стол..."
#===TG MODS START===

            m "Хм... это календарь?"
            $ renpy.say(m, "И если я прочел это правильно.....\n\nIt's........... \"%s %d, %s\"?" % (month_info[cal_month][5], cal_day, week_info[day_of_date((cal_month, cal_day))][1]))
            m "Что бы это ни значило......"
            m "Но, похоже кто-то рисовал на нем."
            m "Может быть стоит его немного изучить...."

            # Let's say Dumblegenie learns of the Hogsmeade dates from Dumbledore previously marking them down on the
            # in the calendar.
            $ known_dates['hogsmeade_weekends'] = True

            # Further, let's then allow those dates to show up by adding them to the places they need to go.
            $ dates_list = important_dates['hogsmeade_weekends']
            $ add_cal_notes(dates_list, 'hogsmeade_weekends')

            show screen cal_button_flash
            pause(1.5)
            hide screen cal_button_flash

#===TG MODS STOP===

            jump day_main_menu

## DR'S DEBUG TEST           
        "- Тест 1 -" if False :
            $ menu_x = 0.2 #Menu is moved to the left side.
            $ pos = POS_410
                
            $ hermi.whoring = 24
            
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ hermione_chibi_xpos = 400 #Near the desk.
            $ hermione_chibi_ypos = 250 #Добавил, т.к. без этого иногда падает игра.
            show screen hermione_02 #Hermione stands still.
            show screen bld1
            with d3
            
            $ nsp_germiona_kviddich_1_statimg = "New"
            $ nsp_germiona_kviddich_1_photo = "dis"
            $ nsp_event_kviddich_1 = 0
            $ cur_level = 1
            call nsp_event_kviddich_1
            jump hermione_goout
            
        "- Тест 2 -" if False :
        
            $ menu_x = 0.2 #Menu is moved to the left side.
            $ pos = POS_410
                
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ hermione_chibi_xpos = 400 #Near the desk.
            $ hermione_chibi_ypos = 250 #Добавил, т.к. без этого иногда падает игра.
            show screen hermione_02 #Hermione stands still.
            show screen bld1
            with d3
            $ hermi.whoring = 24       
            #$ hermi.WrdSetAddNew("xxxsmallskirt")
            #$ hermi.WrdDress("xxxsmallskirt")
            #$ hermi.WrdSetUnlock("skimpyshirt")
            #$ hermi.WrdSetDress("skimpyshirt")
            #$ hermi.WrdAddNew("badge")
            #$ hermi.WrdDress("badge")   
            #$ hermi.WrdSetMain()
            #$ hermi.WrdSpermDried()
            
            #$ hermi.WrdMenuRun ("new")
            
            #$ hermi.WrdSetUnlock(hermi.wrd_choose)
            #$ hermi.WrdSetDress(hermi.wrd_choose)

            #$ hermi.WrdMenuMainRun ()            
            
            jump hermione_approaching
#            jump hermione_goout            
            
        "- Тест 3 -" if False :

            $ hermi.whoring = 24
            $ cataloug_found = True
            $ persistent.game_complete = True
            #if persistent.endings is None:
            #    $ persistent.endings = set()
            #$ persistent.endings.update({1})
            #python :
            #    achieve.SetAchievement(const_ACH_WRD_HERMIONA_SHIRT_BUSINESS)
            #    achieve.UpdatePersistent()
            call the_oddities
            jump desk
            
        "- Тест 4 -" if False :

            $ hermi.whoring = 24
            $ cataloug_found = True
            call daphne_main_menu
            jump desk
            
        "- Тест 5 -" if False :
        
            $ menu_x = 0.2 #Menu is moved to the left side.
            $ pos = POS_410
                
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ hermione_chibi_xpos = 400 #Near the desk.
            $ hermione_chibi_ypos = 250 #Добавил, т.к. без этого иногда падает игра.
            show screen hermione_02 #Hermione stands still.
            show screen bld1                                  
            with d3
            $ hermi.whoring = 24                 
            
            jump new_request_02
#            jump hermione_goout 

        "- Тест 7 -" if False:
            $luna.LoadDefItemSets()
            $luna.Visibility("body+", False)
            $luna("~00 right red emb// Привет !")
            $luna.Visibility()
            jump desk
            
        "- Тест 8 -" if False:
            $phoenix.LoadDefItemSets()
            $phoenix.Visibility("body+", False)
            $phoenix("~a a def o// Привет !")
            $phoenix.body.data().addItem( 'item_pose_back_open' )
            $phoenix("Я ухожу.")
            $phoenix.body.data().delPose()
            $phoenix.body.data().addItem( 'item_pose_back_closed' )
            $phoenix(".........")
            $phoenix.body.data().delPose()  
            $phoenix.Visibility()
            jump desk
            
### DR'S NEWSPAPER ooo ###

        "- Писать статьи для газеты -" if nsp_newspaper_articles < 8 and nsp_newspaper_menu > 0 and nsp_newspaper_ready == False and nsp_newspaper_published == False:
            jump nsp_articles_work
        "{color=#858585}- Писать статьи для газеты -{/color}" if nsp_newspaper_articles >= 8 and nsp_newspaper_menu > 0 and nsp_newspaper_published == False:
            m "Я уже приготовил достаточно материала, газета готова к публикации."
            jump desk
        "{color=#858585}- Писать статьи для газеты -{/color}" if nsp_newspaper_ready == True and nsp_newspaper_menu > 0 and nsp_newspaper_published == False:
            m "Я уже приготовил достаточно материала, газета готова к публикации."
            jump desk
        "{color=#858585}- Писать статьи для газеты -{/color}" if nsp_newspaper_menu > 0 and nsp_newspaper_published == True:
            m "Газета была недавно опубликована. Перед продолжением работы нужно прочитать отзыв из министерства."
            jump desk
            
###   
            
        "- Делать бумажную работу -" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}- Делать бумажную работу -{/color}" if finished_report >= 6 and not got_paycheck:
            m "Я уже завершил шесть отчетов на этой неделе."
            jump desk
        "{color=#858585}- Делать бумажную работу -{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "Сначала мне нужно получить оплату."
            jump desk

        "- Книжная коллекция -" if not day == 1 and cataloug_found: 
            label books_list:
                $choose=None
                menu:
### DR'S NEWSPAPER ooo ###

                    "- Книги о газетном деле -" if nsp_pre_dahre >= 1:
                        label books_on_newspaper:
                            $_label="books_on_newspaper"
                            $_block="books_newsp"
                            jump menu_reading_book
                            
                    "- Мануалы инструментов для газетного дела -" if nsp_newspaper_menu >= 5:
                        label manuals_on_newspaper:
                            $_label="manuals_on_newspaper"
                            $_block="books_newsp2"
                            jump menu_reading_book
                            
###
                    "- Обучающие книги -":
                        label books_on_improvement:
                            $_label="books_on_improvement"
                            $_block="books_edu"
                            jump menu_reading_book

                    "- Фантастика -":
                        label fiction_books:
                            $_label="fiction_books"
                            $_block="books_fict"
                            jump menu_reading_book

                    "- Ничего -":
                        jump desk

        "- Продолжить чтение -" if currentBook!=None:
            $wtevent=this(currentBook)
            jump reading_book_xx 
          
        
                    
                    
                    
        #"- The muggle oddities -" if have_catalogue: #Real thing
        "- Приблуды Дахра -" if cataloug_found: 
            if order_placed or package_is_here:
                show screen bld1
                with d3
                dahr "Пожалуйста, потерпите чуть-чуть. Сова уже в пути."
                hide screen bld1
                with d3
                jump desk
            else:
                 jump the_oddities
        
        
        

        # "- Подрочить на трусики Гермионы -" if request_03: #True when Hermione has no panties on.
        #     jump jerk_off
        "- Передернуть -" if not day < 5:
            jump jerk_off 
        "- Дремать -" if daytime and not day == 1:
            jump night_start
        "- Спать -" if not daytime and not day == 1:
            jump day_start
            
### DR'S NEWSPAPER ooo ###

        "- Газета -" if nsp_newspaper_menu >= 2 and cataloug_found: 
            label nsp_newspaper_list:
                $choose=None
                menu:

                    "- Публикация газеты -" if nsp_newspaper_ready == True:
                        label nsp_newspaper_publication:

                            $choose=None
                            menu:

                                "- Да -":
                                    $ nsp_newspaper_ready = False 
                                    $ nsp_newspaper_qual = (10 * (1 + nsp_genie_writer) * (1 + nsp_genie_typographic)) + (5 * nsp_genie_photocamera)
                                    $ nsp_newspaper_qual_last = nsp_newspaper_qual
                                    $ nsp_newspaper_cur_money = int((nsp_newspaper_qual + (nsp_newspaper_bonus_point/10) ) * (0.7 + (one_of_ten * 0.06) ))
                                    
                                    $ nsp_newspaper_published = True
                                    $ nsp_genie_typographic_exp += 1
                                    
                                    ">Вы поставили на свежий выпуск газеты магический штамп и лист исчез с тихим шуршанием, чтобы спустя мгновение возникнуть на стенде главного холла вместо прежнего."
                                    
                                    $ nsp_newspaper_bonus_point_last = nsp_newspaper_bonus_point
                                    $ nsp_newspaper_bonus_text = "нет"
                                    $ nsp_newspaper_bonus_point = 0
                                    
                                    if nsp_newspaper_menu == 7 :
                                        $ nsp_newspaper_menu = 8
                                    
                                    call screen main_menu_01
                            
                                "- Ничего -":
                                    jump desk
                                    
                    "{color=#858585}- Публикация газеты -{/color}" if nsp_newspaper_ready == False:
                         ">Недостаточно материала, нужно написать больше статей."
                         jump desk
                
                    "- Параметры газеты -" if nsp_newspaper_menu >= 4:
                        jump newsp_stats_00


                    "- Ничего -":
                        jump desk
                        
        "- Хрустальный шар -" if nsp_genie_sphere :
                
            $choose=None
            if nsp_genie_sphere_video :
                $ nsp_genie_sphere_video_txt = "\nВозможен перенос видео в газету"
            else :
                $ nsp_genie_sphere_video_txt = ""

            menu:
            
                "Уровень владения: [nsp_genie_sphere_level]\nСила сапфира [nsp_genie_sphere_sapphire_level_eff]\nСила рубина [nsp_genie_sphere_ruby_level_eff]\nСила алмаза [nsp_genie_sphere_diamond_level_eff][nsp_genie_sphere_video_txt]"
                
                "- Инструкции -":
                
                    call bigtext(["Инструкция к Хрустальному Шару.\n\nШар позволяет получать изображение на расстоянии. К сожалению, для вызова и поддержания данной магии необходимо "
                    "специальное простое заклинание со стороны другого волшебника. Иначе говоря, подсмотреть за кем-то вряд ли получится.\n\nКроме того, нужны три фокусных камня: сапфир, рубин и алмаз.\n\n"
                    "Сапфир отвечает за интенсивность связи. В зависимости от уровня он обеспечивает: 1 - разговор, 2 - слышимость звуков вокруг другого, 3 - изображение головы, 4 - изображение тела, 5 - полную картину.\n\n",
                    "Рубин отвечает за время четкого фокуса (влияет на возможности любой записи изображения): 1 - 30 секунд в день, 2 - 1 минута, 3 - 2 минуты, "
                    "4 - 5 минут, 5 - 10 минут.\n\nАлмаз отвечает за дальность действия шара: 1 - только комната, 2 - главное здание Хогвартса, 3 - основная территория Хогвартса, "
                    "4 - все окрестности Хогвартса (Запретный лес, Хогсмид), 5 - неограничено.\n\nКроме того, недостаточный навык владения шаром будет ограничивать силу камня.\n\n",
                    "Навык будет постепенно расти за счет любого применения шара. Если параметры шара не позволяют проводить съемку, то после журналистского задания будет получена "
                    "только статья, которая принесет намного меньше популярности.\n\n"
                    "Для начала нужно купить любой сапфир и поговорить с Гермионой. В дальнейшем понадобятся сапфир не ниже 3 уровня, рубин и алмаз. Фотоъемка в студии не использует "
                    "шар. После приобретения рубина, алмаза, сапфира 3 уровня и наилучшего фотоаппарата появится новая возможность, не забудьте внимательно изучить доступные книги в инструментах для газеты.\n\n"])

                    jump desk
                
                "- Ничего -":
                    jump desk

###
        "- Ничего -":
            call screen main_menu_01
            
            

 #===TG MODS START===

        "-Исследовать календарь-" if False and desk_examined and not day == 1 and False :
            menu:
                # This is when playing an old game, and the above event didn't happen (since the mod wasn't installed,
                # and the desk is now set to (forever) examined.)
                #
                # I might later turn this into a general function to refresh the calendar. Possibly allow purging of
                # data to make a clean slate. Possibly only to correct things.
                #
                # I'll do that kind of thing later, once more has been implemented.
                "-Перепроверить даты-" if desk_examined and not known_dates['hogsmeade_weekends']:
                    m "Перелистывая страницы........"
                    m "Кто-то.... явно любит все эти \"Хогсмид по выходным\"."
                    m "Кто-то пьянчуга, судя по ним."
                    $ known_dates['hogsmeade_weekends'] = True
                    $ dates_list = important_dates['hogsmeade_weekends']
                    $ add_cal_notes(dates_list, 'hogsmeade_weekends')
                    show screen cal_button_flash
                    pause(1.5)
                    hide screen cal_button_flash
                    if daytime:
                        jump day_main_menu
                    else:
                        jump night_main_menu

                "-Ничего-":
                    if daytime:
                        jump day_main_menu
                    else:
                        jump night_main_menu

#===TG MODS STOP===
    
  
            
            


    
### READING ###

label reading_book_xx:

### Plays sound effects appropriate for reading. 
# Music
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.


    if raining:
        ">Вы читаете книгу [wtevent._caption], слушая дождь, барабанящий по крыше вашей башни."
    else:
        ">Вы читаете книгу [wtevent._caption]..."
   
    call chap_finished_xx
    
    call chapter_check_book_xx #Checks if the chapter just finished was the last one.
    
#Проверка на концентрацию
    if concentration>0:
        if concentration == 1:
            $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
            if concentraton_check == 1:
                call concetrationg_reading
        if concentration == 2:
            $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
            if concentraton_check == 1:
                call concetrationg_reading
        if concentration == 3:
            $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
            if concentraton_check == 1:
                call concetrationg_reading
        if concentration == 4:                                                               #Golden book.
            call concetrationg_reading
        
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl>0:
        $ speed_dummies = Rand([60,30,10][s_reading_lvl-1]//turbo)  # Массив содержит размер интервала для расчета вероятности. Первая книга 10/60 шансов прочитать доп. главу, вторая 10/30, 3-я 10/20 . В режиме турбо интервал уменьшается вдвое
        if speed_dummies <= 10: #Success.
            ">Используя изученные вами методы скорочтения, вы рациональнее используете время и продолжаете читать."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">Осталось еще несколько глав."

#===#############################################       

    if raining:
        if not fire_in_fireplace:
            ">Дождь за окном успокаивает вас, и вы отлично себя чувствуете, читая..."
            ">Вы пытаетесь продолжить читать, но вскоре понимаете, что воздух в комнате слишком влажный."
        else:
            ">Дождь за окном успокаивает вас, и вы отлично себя чувствуете, читая..."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">Осталось еще несколько глав."

    ">Осталось еще несколько глав."       
    $currentBook=wtevent.Name

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start #pered_menu#
    else: 
        jump day_start
        
###### Concentration reading
label concetrationg_reading:
    ">Во время чтения вы идеально сконцентрированы, что позволяет вам прочитать дополнительную главу."
    call chap_finished_xx
    call chapter_check_book_xx
    return
label chap_finished_xx:
    if wtevent.Name=="book_05":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
         "Повествуется о Галадриэли - нежной и доброй эльфийской принцессе.",
         "Повествуется об отце Галадриэли - Короле Метисе и его друге детства - Мофоселисе.",
         "Король Метис объявляет о помолвке своей дочери, принцессы Галадриэль с канцлером Мофоселисом.",
         "Галадриэль отказывается выйти замуж за человека, который в три раза старше ее и которого, до этой поры, она считала своим дядей.",
         "Король Метис не слушает \"глупые\" жалобы дочери. Галадриэль решает бежать.",
         "Галадриэль удается покинуть королевские покои ночью ...",
         "Король Метис в ярости из-за побега дочери. Он решает лично возглавить поиски.",
         "Галадриэль едет на своей кобыле \"Белая голубка\" через лес. Принцесса наслаждается свободой... Вскоре она встречает всадника - весьма приятного человеческого дворянина...",
         "Галадриэль едет вместе с дворянином. Они обмениваются шутками, и он очень забавляет ее. Вдруг дворянин нападает на принцессу и сильным ударом лишает сознания!...",
         "Галадриэль приходит в себя. Она с ужасом чувствует, что дворянин входит в нее. Галадриэль зовет на помощь, но красавчик крепко держит ее и жестоко насилует.",
         "Галадриэль безуспешно пытается вырваться. И тут она замечает, что ее окружает полдюжины мужчин, которые злобно ухмыляются.",
         "После того, как дворянин заканчивает с Галадриэль, его люди пускают эльфийскую принцессу по кругу. Галадриэль плачет и умоляет их прекратить.",
         "Галадриэль приходит в себя в клетке на каком-то рынке. Ее руки связаны, ее благородные одежды разорваны в клочья, а волосы полны веток и сухой спермы.",
         "Жирный, богатый мужчина покупает Галадриэль и приводит ее в свой дом. Принцесса больше не плачет. Она счастлива выбраться из клетки.",
         "Галадриэль позволили принять ванну, после чего раб приносит ей чистую одежду и еду.",
         "Галадриэль начинает надеяться, что ее беды позади, но это не так. Вскоре она понимает, что это за место: бордель.",
         "Эльфийская принцесса вынуждена работать шлюхой. Она ненавидит свою новую жизнь, но у нее не остается выбора.",
         "Галадриэль быстро набирает популярность. Люди, Темные Эльфы и даже карлики, она раздвигает ноги для всех.",
         "Слава о молодой и красивой эльфийской шлюхе распространяется окрест. Галадриэль принимает свою новую жизнь в борделе.",
         "Но внезапно все резко меняется. Галадриэль узнает, что она беременна. - Конец первой книги -"
        ][wtevent._status-1]
        )


    if wtevent.Name=="book_05_b":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]",
        [   
         "Галадриэль беременна уже несколько месяцев. К удивлению принцессы, ее популярность растет, как будто в прямой зависимости от размера ее живота.",
         "Хотя Галадриэль и ведет себя, как послушная шлюха, на самом деле, она продумывает побег из борделя.",
         "Эльфийская принцесса-шлюха ничего не знает о жизни за стенами борделя. Но это не влияет на ее решимость спастись.",
         "Планирование побега из борделя занимает много времени, но в конце-концов Галадриэль удается бежать.",
         "Галадриэль теряется в огромном городе и вынуждена провести ночь на улице.",
         "На улицах трудно найти еду. Галадриэль борется со стаей бродячих собак, и одна из них кусает Галадриэль за руку.",
         "Беременная Галадриэль предлагает составить компанию  паре грязных бездомных мужчин в обмен на еду. С ними она проводит ночи.",
         "Галадриэль понимает, что ее жизнь в борделе была раем по сравнению с тем, что она имеет теперь. Она решает вернуться обратно.",
         "Владелец Галадриэль - жирный, богатый человек не наказывает Галадриэль за побег. Наоборот, он счастлив, что одна из его самых популярных девушек вернулась.",
         "Галадриэль снова в тепле и чистоте, ее хорошо кормят. Она рада, что вернулась и популярна, как никогда.",
         "Галадриэль обслуживает клиентов на протяжении всей беременности. Ребенок вот-вот родится...",
         "Богатый человек в маске заказывает Галадриэль на весь день. Лениво ублажая клиента, Галадриэль гадает кто бы это мог быть.",
         "Таинственный человек целый день развлекается с Галадриэль. Из наполненных грудей принцессы капает молоко, в то время, как человек трахает ее.",
         "Человек в маске кончает на лицо Галадриэль во второй раз за сегодня. Затем он решает снять маску и показать лицо.",
         "Галадриэль обнаруживает, что этот человек - ее отец, король Метис. Только тут и он понимает, что беременная шлюха, которую он трахал несколько часов - его дочь.",
        # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
         "Он обнимает свое потерявшее дар речи дитя. Глаза Галадриэль пусты. Сперма отца капает с ее лица...",
         "Галадриэль в ужасе кричит. К ее удивлению, она обнаруживает себя в королевских покоях, в своей постели.",
         "Проходит несколько минут, пока она понимает, что она никогда не была беременна. Все приключения - это лишь сон.",
         "Галадриэль бросается к отцу и обнимает его. Девушка пережила слишком многое в \"прошлой жизни\". Она счастлива и соглашается выйти замуж за канцлера Мофоселиса.",
         "{size=-1}Галадриэль стоит у алтаря. Она довольна и счастлива. Вдруг она замечает нечто, что наполняет ее сердце ужасом. На ее руке - шрам. Место укуса собаки. - Конец -{/size}"
        ][wtevent._status-1]
        )

    if wtevent.Name=="book_06":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
        "Семейство благородных северян.",
        "Королевская семья и король.",
        "Другое семейство.",
        "Инцест между братом и его сестрой-королевой.",
        "Покушение на ребенка. Он чудом выживает, но находится в коме.",
        "Другие персонажи.",
        "Одни персонажи строят козни против других.",
        "Короля отравили и он умирает. Еще несколько инцестов между братом и сестрой.",
        "Казнили некоторых персонажей, за которых вы болели.", # НЕ ПЕРЕВЕДЕНо
        "Появилось несколько новых персонажей.",
        "Некоторые женщины были изнасилованы и жестоко убиты.",
        "Еще несколько членов дворянской семьи северян безвременно почили.",
        "Еще больше женщин изнасилованы. Некоторым из них удается выжить. (Разумеется, чтобы их изнасиловали чуть позже).", 
        "Персонажи, которых вы ненавидите сталкиваются в эпической битве против персонажей, за которых вы болеете.",
        "Большинство персонажей, которых вы ненавидите пережили сражение. Все, за кого вы болели, мертвы.",
        "Еще несколько изнасилований и убийств... (Вас это уже не трогает...)", 
        "Новые персонажи появляются в истории. Вы, вроде, начинаете болеть за одного из них.",
        "Персонаж, за которого вы болеете, влюбляется в милую девушку.",
        "Персонаж, за которого вы болели, зверски убит. Его девушку насилуют и тоже убивают.",
        "Новая раса наполовину замороженной нежити включается в историю. Продолжение следует..."
        ][wtevent._status-1]
        )

    if wtevent.Name=="book_07":
        $ book_07_units +=1
        $wtevent._status=book_07_units
        call waifu

### DR'S NEWSPAPER ooo ###
    if wtevent.Name=="nsp_newsp_book_pre":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
        "Во вводной главе говорится об истории появления и развития газет в мире магов.",
        "Вы изучаете основы написания газетных статей.",
        "Вы изучаете основы написания газетных статей.",
        "Вы изучаете основы написания газетных статей.",
        "Вы изучаете основы редактирования газет.",
        "Вы изучаете основы редактирования газет.",
        "Вы изучаете основы оформления газет.",
        "Вы изучаете основы оформления газет.",
        "Вы изучаете основы оформления газет.",
        "В заключительной главе приводится краткий перечень советов начинающему редактору.",
        ][wtevent._status-1]
        )

    if wtevent.Name in ["nsp_newsp_book_p01", "nsp_newsp_book_p02a", "nsp_newsp_book_p02b", "nsp_newsp_book_p03a", "nsp_newsp_book_p03b"]:
        $wtevent.IncValue("status", 1)  #+=1
            
    if wtevent.Name in ["nsp_newsp_book_p04", "nsp_newsp_book_p05a", "nsp_newsp_book_p05b", "nsp_newsp_book_p06a", "nsp_newsp_book_p06b"]:
        $wtevent.IncValue("status", 1)  #+=1

    if wtevent.Name in ["nsp_newsp_book_typo1", "nsp_newsp_book_typo2", "nsp_newsp_book_typo3", "nsp_newsp_book_typo4", "nsp_newsp_book_typo5", "nsp_newsp_book_typo6"]:
        $wtevent.IncValue("status", 1)  #+=1
            
    if wtevent.Name in ["nsp_newsp_book_photo1", "nsp_newsp_book_photo2", "nsp_newsp_book_photo3", "nsp_newsp_book_photo4"]:
        $wtevent.IncValue("status", 1)  #+=1
            
    if wtevent.Name=="nsp_newsp_book_video":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
        "Во вводной главе говорится об истории появления и развития прорицательства в мире магов. И только в конце вы сообразили, что это вообще вас не касается.",
        "Вы изучаете принципы компоновки видеокадра.",
        "Вы изучаете художественные правила видеомонтажа.",
        "Глава содержит в себе биографию автора. Безобразие.",
        "Вы изучаете заклинания для переноса информации из шара на бумагу.",
        "Вы продолжаете изучать заклинания для переноса информации из шара на бумагу.",
        "Внезапно, целая глава посвящена философским мыслям автора о жизни. Пожалуй, эти страницы стоит приберечь для борьбы с бессонницей.",
        "Вы продолжаете изучать заклинания для переноса информации из шара на бумагу. Кажется, начинает понемногу получаться.",
        "Вы завершаете изучать заклинания для переноса информации из шара на бумагу. Остается прочитать заключительную главу.",
        "Ну разумеется, в последней главе находится фотография автора и его благодарности жене, детям, домашним животным и маглам по соседству.",
        ][wtevent._status-1]
        )

###        
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    if wtevent._block=="books_edu": 
#        $wtevent._status=this.GetCall(wtevent.Name).SetValue("status", wtevent._status+1)  #wtevent.SetValue("status", wtevent._status+1)  #+=1
        $wtevent.IncValue("status", 1)    
    ">Вы закончили \"главу [wtevent._status]\" этой книги."
    return
    
###
label chapter_check_book_xx: #Checks if the chapter just finished was the last one.
    if (wtevent.IsDone() and wtevent.Name!="book_07") or (wtevent.Name=="book_07" and book_07_units == 20):#book_xx_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        $currentBook=None

        if wtevent.Name=="book_06":
            g4 "Что за херня! Я ненавижу человека, который это написал!"
            m "Впрочем, все эти изнасилования натолкнули меня на пару идей..."


        if wtevent.Name=="book_07":
            if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
                m "Вау! Отличная книга! Это было неплохо!"
                
                #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
                if not found_dahrs_ticket_once:
                    m "Хм...?"
                    m "Что это...? Закладка?"
                    $ the_gift = "03_hp/18_store/06.png" # The DAHR's ticket.
                    show screen gift
                    with d3
                    $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                    ">Вы нашли ваучер Дахра."
                    hide screen gift
                    with d3
                    m "Хм..."
                    $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                    $ waifu_book_completed = True
            elif shea_waifu and shea >= 8: 
                if not complited_shea_already: #Finished with Shea for the first time.
                    m "Неплохо. Я действительно готов заботиться о Ши ..."
                    g9 "Ну, о ней и ее анальной девственности..."
                    $ complited_shea_already = True
                else: #Finished with Shea for the second time.
                    m "Значит в конце я снова с Ши?"
                    m "Хм... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"
            elif victoria_waifu and victoria >= 7:
                if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                    m "Неплохо, неплохо. Госпожа Стивенс оказалась той еще шлюхой..."
                    $ complited_stevens_already = True
                else: #Finished with Shea for the second time.
                    m "Значит в конце я снова с госпожой Стивенс?"
                    m "Хм... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"
            elif leena_waifu and leena >= 8:
                if not complited_leena_already: #Finished with Leena for the first time.
                    g9 "Славненько! Обожаю хэппи энды!"
                    $ complited_leena_already = True
                else: #Finished with Shea for the second time.
                    m "Значит, в конце я снова со светленькой девахой?"
                    m "Хм... Может, в следующий раз попробовать выбирать другие варианты...?"

            else:
                m "Хм ... Конец очень разочаровал..."
                m "Может, я должен прочитать ее еще раз когда-нибудь..."
            
            $ book_07_units = 0 #RESTING THE BOOK FOR ANOTHER PLAYTHORUGH.
            $ shea = 0 #RESETING SHEA'S POINTS FOR THE NEXT PLAYTHOURGH.
            $ victoria = 0
            $ leena = 0

            if not dear_waifu_completed_once:
                $ dear_waifu_completed_once = True # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
                $ imagination +=1


        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        if wtevent._conclusion!="":
            if wtevent._block=="books_edu":
                m "Новый навык: [wtevent._conclusion]"
            else:
                m "[wtevent._conclusion]"

# Изменения навыка по завершению книги (кроме Вайфу - book_07 в ней навык меняется отдельно)
# Можно было сделать через событие, но тогда получится более громоздко. Так что пока так:
        if wtevent.Name in ["book_01", "book_02", "book_03", "book_04"]:
            $ concentration += 1
        if wtevent.Name in ["book_05", "book_05_b", "book_06"]:     
            $ imagination +=1
        if wtevent.Name in ["book_08", "book_09", "book_10"]:
            $ s_reading_lvl +=1
        if wtevent.Name in ["book_12", "book_13", "book_14", "book_15"]:
            $ speedwriting += 1

### DR'S NEWSPAPER ooo ###

        if wtevent.Name=="nsp_newsp_book_pre" and nsp_newspaper_menu == 0:
            $ nsp_newspaper_menu = 1
            
        if wtevent.Name in ["nsp_newsp_book_p01", "nsp_newsp_book_p02a", "nsp_newsp_book_p02b", "nsp_newsp_book_p03a", "nsp_newsp_book_p03b"]:
            $ nsp_genie_writer += 1
            
        if wtevent.Name in ["nsp_newsp_book_p04", "nsp_newsp_book_p05a", "nsp_newsp_book_p05b", "nsp_newsp_book_p06a", "nsp_newsp_book_p06b"]:
            $ nsp_genie_writer += 1

        if wtevent.Name in ["nsp_newsp_book_typo1", "nsp_newsp_book_typo2", "nsp_newsp_book_typo3", "nsp_newsp_book_typo4", "nsp_newsp_book_typo5", "nsp_newsp_book_typo6"]:
            $ nsp_genie_typographic += 1
            $ nsp_genie_typographic_exp = 0
            
        if wtevent.Name in ["nsp_newsp_book_photo1", "nsp_newsp_book_photo2", "nsp_newsp_book_photo3", "nsp_newsp_book_photo4"]:
            $ nsp_genie_photocamera += 1
            $ nsp_genie_photocamera_exp = 0
            
        if wtevent.Name == "nsp_newsp_book_video" :
            $ nsp_genie_sphere_video = True
            
###
            
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
 

###
label fire_in: #Shows Genie reading a book near the fireplace.
    hide screen chair
    hide screen genie
    show screen reading_near_fire
    with Dissolve(0.3)
    return
###
label fire_out: #Shows Genie reading a book near the window.
    hide screen chair
    hide screen genie
    show screen reading
    with Dissolve(0.3)
    return
    
 
 
    
    
    
    
        
    
    
### PAPERWORK ###
label paperwork:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">Вы делаете отчет."
    
    call finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call f_moon_bonus
           
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 4:                                                               #Golden book.
        call concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call concentration_label
#    if concentration == 6:
#            call concentration_label
    ###==============================================================================================
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 4:
            call speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speedwriting == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
    
### 
label report_chapters_check:
    if report_chapters >= 7:
        ">Вы закончили отчет."
        $ report_chapters = 0
        $ finished_report += 1
        $ total_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Полнолуние сделало вас более продуктивным.\n>Вы закончили [report_chapters]-ю главу."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили [report_chapters]-ю главу."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Во время работы вы идеально сконцентрированы.\n>И заканчиваете дополнительную главу.\n>Вы закончили [report_chapters]-ю главу."
    return

    
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Вы используете свой навык скорописания.\n>И заканчиваете дополнительную главу.\n>Вы закончили [report_chapters]-ю главу."
    return

### DR'S NEWSPAPER ooo ###

label nsp_articles_work:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">Вы пишете статьи для газеты."
    
    call nsp_finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call nsp_f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call nsp_f_moon_bonus
           
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call nsp_concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call nsp_concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call nsp_concentration_label
    if concentration == 4:                                                               #Golden book.
        call nsp_concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call nsp_concentration_label
#    if concentration == 6:
#            call nsp_concentration_label
    ###==============================================================================================
    
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call nsp_speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call nsp_speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call nsp_speedwriting_label
    if speedwriting == 4:
            call nsp_speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call nsp_speedwriting_label
#    if speedwriting == 6:
#        call nsp_speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
###

### 
label nsp_report_chapters_check:
    if nsp_newspaper_articles >= 8:
        ">Вы закончили статью."
        $ nsp_newspaper_articles = 0
        $ nsp_newspaper_ready = True
        if nsp_newspaper_menu == 1:
            $ nsp_newspaper_menu = 2
    return
### FULL MOON BONUS ###
label nsp_f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ nsp_newspaper_articles += 1
    ">Полнолуние сделало вас более продуктивным.\n>Вы закончили [nsp_newspaper_articles]-ю статью."
    return
###
label nsp_finished_working_chapter:
    $ nsp_newspaper_articles += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили [nsp_newspaper_articles]-ю статью."
    return
### CONCENTRATION
label nsp_concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ nsp_newspaper_articles += 1
    ">Во время работы вы идеально сконцентрированы.\n>И заканчиваете дополнительную статью.\n>Вы закончили [nsp_newspaper_articles]-ю статью."
    return
### SPEEDWRITING
label nsp_speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ nsp_newspaper_articles += 1
    ">Вы используете свой навык скорописания.\n>И заканчиваете дополнительную статью.\n>Вы закончили [nsp_newspaper_articles]-ю статью."
    return
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Чтение книг не дает мне ничего."
    hide screen gift
    return
    
    
    
### READING A BOOK BLOCK ### Sends here to make sure that proper SFX is played during reading a book.
label reading_block:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    return
