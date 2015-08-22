label menu_gifts_actions:
    $item=hero.Items(choose.choice)
    $ gifted = True 

    if item.Name=="ball_dress" and hermi.Items.Count(item.Name)==0:
        show screen  blktone
        with d3
        m "(Я чувствую, что не будет обратного пути после того, как я дам ей это платье...)"
        m "(Я готов сделать это?)"
        hide screen blktone
        menu:
            "\"Да, вполне...\"":
                jump giving_thre_dress #27_final_events.rpy
            "\"Нет, не готов...\"":
                jump hermione_main_menu


    jump expression "giving_"+item.Name



label giving_xxxsmallskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1
#    $ have_xxxsmallskirt = False # Turns TRUE when you have the skirt in your possession.
#    $ gave_xxxsmallskirt = True #Turns True when Hermione has the xxxsmallskirt.
    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xxxsmallskirt")
    $hermi.WrdSetAddNew("xxxsmallskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали нано-юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
    
### DRESS CODE ###
label mini_on:
    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Это мини юбка?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        


    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )
                                                                                                                                                                                                                          #HERMIONE
    
    
    $herView.data().setStyleKey( 'skirt', 'short' )
    #$ herView.data().addSkirt( CharacterExItem( herView.mClothesFolder, "skirt_short.png", G_Z_SKIRT ) )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
                                                                                                                                                                                                                     #HERMIONE
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
    
label mini_off:
    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "Я рада, что вы попросили меня об этом. "
        $herView.hideQQ()
        $herView.addFaceName( "body_03.png")
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_01.png", pos )
        her "С удовольствием, сэр."

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_13.png", pos )
        her "Хорошо..."
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_28.png", pos )
        her "Опять эта скукотища?"
    
    
    #$ herView.data().addSkirt( CharacterExItem( herView.mClothesFolder, "skirt_normal.png", G_Z_SKIRT ) )
    $herView.data().setStyleKey( 'skirt', 'default' )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump hermione_main_menu
   
    
    
label badge_put:
    $herView.hideQQ()

    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Конечно, сэр..."
    
    #$ herView.data().addItemKey( G_N_BADGE, CharacterExItem( herView.mClothesFolder, "badge.png", G_Z_DRESS + 1, 'dress' ) )
    $herView.data().addItem( 'item_badge' )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump hermione_main_menu
    
    
label badge_take:
    $herView.hideQQ()
    
    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Как пожелаете, сэр..."

    $ herView.data().delItem( 'item_badge' )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump hermione_main_menu
    
    
### FISHNETS ###
label nets_put:
    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_11.png", pos )
        her "Ажурные чулки...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Вы, должно быть, не серьезно, сэр!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "С радостью..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, хорошо..."
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Я не из таких девушек, сэр..."
        her "Попытайте удачу с одной из \"Слизеринских\" шлюх..."
        menu:
            m "..."
            "\"Просто надень это!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это врядли соответствует форме студента Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, раз так..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Ажурные чулки?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Я не уверена насчет этого, сэр..."
        menu:
            m "..."
            "\"Просто надень их!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, Ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        

    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Если вы настаиваете, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )
                                                                                                                                                                                                                          #HERMIONE
    
     
    #$ herView.data().addItemKey( G_N_NETS, CharacterExItem( herView.mClothesFolder, "nets.png", G_Z_LEGS + 1, 'legs' ) )
    $herView.data().addItem( 'item_nets' )
    
    #$ legs_02 = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
    
label nets_take:
    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "Я рада, что вы приняли это решение, сэр."
        $herView.hideQQ()
        $herView.addFaceName( "body_03.png" )
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_01.png", pos )
        her "С удовольствием, сэр."

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_12.png", pos )
        her "Как пожелаете, сэр."
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_28.png", pos )
        her "Правда? Ой..."
    
    
    $ herView.data().delItem( 'item_nets' )
    #$ legs_02 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
       
label giving_lubricant: # JAR OF Анальный лубрикант.
    $herView.hideQ( d5 )                                                                                                                                                                                                           #HERMIONE
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 6
        $herView.showQ( "body_02.png", pos, d5 )                                                                                                                                                                                         #HERMIONE
        her "Я не знаю, что это..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "Но мне кажется, что эта банка полна чего-то мерзкого и противного..."
        her "Нет, спасибо, сэр."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
        $herView.addFaceName( "body_03.png" )
       
        
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 2
        $herView.showQ( "body_73.png", pos, d5 )                                                                                                                                                                                                                      #HERMIONE
        her "Хм..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Мне кажется, я знаю, что это такое..."
        her "Но почему вы даете что-то подобное вашей ученице, сэр?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Нет, спасибо."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
   
        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #$ anal_lube -= 1
        $herView.showQ( "body_118.png", pos, d5 )
        her "Анальный лубрикант?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Эм...ну...я знаю девочку..."
        her "То есть, не знаю, она подруга моей подруги..."
        her "Да, я передам это ей..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/09.png" # Анальный лубрикант
        show screen gift
        with d3
        ">Вы даете банку Гермионе..."
        hide screen gift
        with d3
        $herView.hideshowQQ( "body_186.png", pos )
        her "Тем не менее, я думаю, вы не должны дарить такие подарки вашим ученикам, сэр."
        $herView.hideQQ()
        call no_change #Message: Hermione's mood did not change.
        $herView.hideshowQQ( "body_79.png ", pos);
        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #$ anal_lube -= 1
        $ hermi.liking +=5
        $herView.showQ( "body_124.png", pos, d5 )
        her "Анальный лубрикант, сэр?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "Я знаю пару девушек, которые могли бы сделать что-нибудь с этим."
        $herView.hideshowQQ( "body_128.png", pos )
        her "Спасибо, что присматриваете за нами, сэр."
        $herView.hideQQ()
        call happy #Message that says that Hermione's mood has improved.
 
    $ pos = POS_370
    $herView.showQQ( None, pos )    
    jump hermione_main_menu
        
        
        
        
label giving_condoms: # A PACK OF CONDOMS
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 6
        $herView.showQ( "body_18.png", pos, d5 )
        her "Презервативы?!"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Сэр, я даже не знаю, что с этим делать..."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
        $herView.addFaceName( "body_03.png" )
        
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.showQ( "body_07.png", pos, d5 )
        her "...Презервативы?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Эм... Является ли это частью какой-то новой обучающей программы Хогвартса? Вроде сексуального развитие или вроде того?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Нет, сэр ... Мне кажется, что неправильно принимать этот подарок от вас..."
        $herView.hideQQ()
        call no_change 
   
        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #$ condoms -= 1
        $ hermi.liking += 3
        $herView.showQ( "body_03.png", pos, d5 )
        her "Пачка презервативов?"
        her "Сэр, как мне использовать их?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Ну, я приму их, только потому, что невежливо отказываться от подарка..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">Вы даете Гермионе пачку презервативов..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_29.png" )
        

        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #$ anal_lube -= 1
        $ hermi.liking +=4
        $herView.showQ( "body_08.png", pos, d5 )
        her "Пачка презервативов?"
        $herView.hideshowQQ( "body_128.png", pos )
        her "Я ценю вашу заботу, сэр. Спасибо."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">Вы даете пачку презервативов Гермионе..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_45.png" )
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
     
label giving_perfume: # perfume
    if hero._perfumeused!=time.stamp:
        $Say("> Вы собираетесь подарить Гермионе духи, но они чудесным образом не даются вам в руки.//"
            "> После нескольких безуспешных попыток схватить уворачивающийся флакончик, вы решаете отказаться от этой идеи, чтобы не выглядеть полным идиотом.")
    else:
        $hermi.Visibility("body+")
        $hermi("~body_15.png// Сэр... Этот запах...")
        $hero("Какой запах?")
        $hermi("~body_13.png// У вас в башне пахнет... совсем как... это мне напоминает времена, когда я была маленькой.")
        if hermi.Items("perfume")._count==0:
            $hero("Неужели?")
            $hermi("~body_75.png// Это же запах зубоврачебного кабинета!")
            $hero("Ох, бедное дитя, похоже, нелегко тебе приходилось.")
            $hermi("~body_06.png// Да нет же, сэр, мне нравится этот запах и эти воспоминания!")
            $hero("Эмм... Девочка, я знал, что ты немножко мазохистка, но чтобы настолько...")
            $hermi("~body_04.png// СЭР! Мои родители - стоматологи!")
            $hero("А!.. О!.. Ну, раз так, то...")
        else:
            $hero("Да, я вспомнил, это запах зубоврачебного кабинета.")
        menu:
            "\"Возьми эти духи в подарок\"":
                "> Вы дарите духи Гермионе."
                $hermi.Items.Receive(hero.Items,"perfume")
                $hermi("~body_01.png// Спасибо, сэр!")
                $hermi.IncValue("liking",9-hermi.whoring//3) # от 9 до 1 балла (падает с повышение развращенности), при этом отношение может стать положительным
                call happy #Message that says that Hermione's mood has improved.


            "\"Я рад, что тебе понравилось\"":
                pass
        $hermi.Visibility()

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu


     
     
### CANDY ###
label giving_candy: # CANDY.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) # $ candy -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Конфета?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) #$ candy -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "Конфета?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Конфеты для детей, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_29.png", pos )
        her "Спасибо вам..."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_06.png" )
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) #$ candy -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "Конфета?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Eм... Конечно, спасибо..."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_06.png" )
        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #$ candy -= 1
        $ hermi.liking +=5
        $herView.showQ( "body_06.png", pos, d5 )
        her "Конфета?"
        $herView.hideshowQQ( "body_46.png", pos )
        her "Умные девушки используют конфеты как \"игрушку\"."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_74.png", pos )
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_128.png" )
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
        
        
        

### CHOCOLATE ###
label giving_chocolate: # CHOCOLATE.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) 
        $herView.showQ( "body_01.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_03.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideshowQQ( "body_09.png", pos )
        her "Хм..."
        her "Тут что-то о феях..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Это шутка какая-то, не так ли?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_15.png", pos )
        her "Спасибо вам..."
        call happy #Message that says that Hermione's mood has improved.
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_03.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Мне просто нравится как она хрустит, сэр! Н-не вкус..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Эм... Конечно, спасибо..."
        call happy #Message that says that Hermione's mood has improved.
       
 
        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_06.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideshowQQ( "body_111.png", pos )
        her "Вы балуете меня, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_129.png", pos )
        her "Спасибо вам."
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        

    ### VIBRATOR ###
label giving_vibrator: # VIBRATOR.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 10
        $herView.showQ( "body_01.png", pos, d5 )
        her "Магическая палочка?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Нет, выглядит как--"
        her ".........?"
        $herView.hideshowQQ( "body_18.png", pos )
        her "!!!"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Профессор Дамблдор!"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Это неуместно!"
        call upset
        $herView.addFaceName( "body_120.png" )
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Это то, что я думаю?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "Сэр, позвольте напомнить вам о том, что я принадлежу факультету \"Гриффиндор\"."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Этот подарок подходит для \"Слизеринских\" шлюх, сэр."
        call upset

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_118.png", pos, d5 )
        her "Это...вибратор?"
        her "Дизайн..."
        her "Он напоминает мне мою палочку..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Это сделано на заказ для меня?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Это неуместно."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Но, тем не менее..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">Вы даете вибратор Гермионе..."
        hide screen gift
        with d3
        call no_change
        

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_11.png", pos, d5 )
        her "Это вибратор..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Это... вызывает во мне..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Грязные мысли, сэр"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">Вы даете вибратор Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_124.png", pos )
        her "Спасибо, сэр."
        $herView.hideQQ()
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
        ### STRAP-ON ###
label giving_strapon: # STRAP-ON.
    $herView.hideQ( d5 )
    $ pos = POS_140
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_18.png", pos, d5 )
        her "Что это?"
        $herView.hideshowQQ( "body_14.png", pos )
        her "Какой-то артефакт?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Так хорошо продуман..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Вы уверены, что мне стоит обладать этим?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_16.png", pos )
        her "Огромное спасибо, сэр. Я обещаю хорошо обращаться с ним."
        $herView.hideQQ()
        call happy
        $herView.addFaceName( "body_15.png" )
    
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 15
        $herView.showQ( "body_18.png", pos, d5 )
        her "!!!"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Это..."
        her "Оно не выглядит... по человечески..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "То есть..."
        $herView.hideshowQQ( "body_86.png", pos )
        her "Сэр, вам не стыдно?!"
        her "Дарить что-то вроде этого ученику?!"
        $herView.hideshowQQ( "body_87.png", pos )
        her ".................."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Пожалуйста, уберите это."
        $herView.hideQQ()
        call upset

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Эта штука..."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Это нормальный размер...для \"этого\"?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Я имею в виду..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "......................."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Это реквизит для какого-то розыгрыша?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Оно неплохо сделано "
        $herView.hideshowQQ( "body_33.png", pos )
        her "Я возьму его..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        call happy


    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 30
        $herView.showQ( "body_48.png", pos, d5 )
        her "Это... Это великолепно, сэр..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Он смоделирован по тому самому Фестралу?"
        $herView.hideshowQQ( "body_190.png", pos )
        her "Но эти существа невидимы..."
        $herView.hideshowQQ( "body_118.png", pos )
        her ".................."
        $herView.hideshowQQ( "body_123.png", pos )
        her "Захватывающе..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Все не так, как вы могли подумать, сэр..."
        $herView.hideshowQQ( "body_127.png", pos )
        her "Я просто любуюсь мастерством..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_129.png", pos )
        her "Спасибо вам за подарок, сэр."
        $herView.hideQQ()
        call happy

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
   
        ### BALL GAG ###
label giving_ballgag: # BALL GAG.
    $herView.hideQ( d5 )
    $ pos = POS_140
        
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Что это?"
        $herView.hideshowQQ( "body_141.png", pos )
        her "Выглядит как одна из игрушек для взрослых?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Какая женщина в здравом уме будет подвергать себя такому унижению?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "И что мне с этим сделать?"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Это очень обидно, сэр..."                                                                                                                                                                                                              
        call upset

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 5
        $herView.showQ( "body_186.png", pos, d5 )
        her "Сэр, вы не понимаете, насколько неправильно было бы для меня принять от вас такой подарок?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "И ведь я даже не представляю, что с этим делать..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "То есть, эти пушистые наручники, это просто..."
        her "И этот круглый кляп... Эм..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Сэр, пожалуйста..."
        her "Просто уберите это."
        call upset


    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 9
        $herView.showQ( "body_120.png", pos, d5 )
        her "Месяц назад я бы чувствовала себя оскорбленной, если бы получила такой подарок..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Но теперь я знаю, что некоторые девушки получают удовольствие от такого..."
        $herView.hideshowQQ( "body_117.png", pos )
        $herView.hideshowQQ( "body_120.png", pos )
        her "Уверяю вас, я не одна из таких, сэр."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Но я знаю девушку, которая знает девушку, которая в таких вещах, как ..."
        $herView.hideshowQQ( "body_188.png", pos )
        her "Да, я возьму это и отдам ей..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Вы даете кляп и наручники Гермионе..."
        hide screen gift
        with d3
        call happy

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_190.png", pos, d5 )
        her "Кляп и наручники?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Это совершенно неуместно, сэр." # :)
        $herView.hideshowQQ( "body_129.png", pos )
        her "Но, подарок это подарок, так?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Вы даете кляп и наручники Гермионе..."
        hide screen gift
        with d3
        call happy
        

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
        
        
        
        
        
        
        
        
  
      ### ANAL PLUGS ###
label giving_plug: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 8
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Хм...?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Это что-то вроде затычек?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">Вы даете Гермионе анальную пробку..."
        hide screen gift
        with d3
        $herView.hideshowQQ( "body_185.png", pos )
        her "Спасибо, сэр."
        call happy


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 15
        $herView.showQ( "body_186.png", pos, d5 )
        her "Сэр, это какие-то игрушки для взрослых?"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Это что-то из штук для анального секса?"
        her "Сэр, я считаю, что это одно из оружий для угнетения и унижения женщин!"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Козел!"
        call upset

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.showQ( "body_120.png", pos, d5 )
        her "Да, я знаю девочку, которая..."
        $herView.hideshowQQ( "body_186.png", pos )
        her "Пользуется чем-то подобным..."
        her "Но не я, сэр."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Нет. Спасибо."
        call no_change

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Анальная пробка?"
        $herView.hideshowQQ( "body_117.png", pos )
        her "Я не пользуюсь таким..."
        $herView.hideshowQQ( "body_122.png", pos )
        her "Хотя она очень красива..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "....................."
        $herView.hideshowQQ( "body_121.png", pos )
        her "Ну, ладно. Я возьму ее, если вы настаиваете."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUGS.
        show screen gift
        with d3
        ">Вы даете Гермионе анальную пробку..."
        hide screen gift
        with d3
        $herView.showQQ( "body_127.png", pos )
        her "Но, конечно же, никогда не воспользуюсь..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "................"
        call happy
        

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
        
        
          ### EDUCATIONAL MAGAZINES ###
label giving_mag1: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "\"Популярные магические\" журналы?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр!"
        her "Я использую их для своих исследований!"
        call happy

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Временами я ищу в журналах информацию, которую не могу найти в книгах..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр!"
        her "Я использую их для своих исследований!"
        call happy

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 3 
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_02.png", pos, d5 )
        her "Ох..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Да, я читаю как можно больше журналов..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Особенно много в последнее время..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр!"
        call happy
     

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_10.png", pos, d5 )
        her "Эм..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "Если быть честной, журналы уже не особо привлекают меня..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Но я не против принять их от вас."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_13.png", pos )
        her "Спасибо вам."
        call no_change 

 
    $ pos = POS_370
    $herView.showQQ( None, pos  )
    jump hermione_main_menu    
        
        
        
        
        
              ### GIRLY MAGAZINES ###
label giving_mag2: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.showQ( "body_15.png", pos, d5 )
        her "Хм?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Это какие-то журналы для \"слизеринских\" девок, я полагаю."
        $herView.hideshowQQ( "body_16.png", pos )
        her "Я выше, этих глупых журналов, сэр."
        call no_change
        $herView.addFaceName( "body_01.png" )
        
        
      
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_04.png", pos, d5 )
        her "Я не читаю журналы такого рода..."
        $herView.hideshowQQ( "body_13.png", pos )
        her "................"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Но я могу попробовать, просто смеха ради..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Спасибо, сэр!"
        call happy
        $herView.addFaceName( "body_06.png" )

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15 
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_10.png", pos, d5 )
        her "Мне стыдно признаваться, но..."
        $herView.hideshowQQ( "body_24.png", pos )
        her "Последнее время мне действительно нравится читать подобное..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Спасибо, сэр."
        call happy
        $herView.addFaceName( "body_06.png" )
        

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_18.png", pos, d5 )
        her "Последний выпуск \"Девченок\"?!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Нет ничего лучше этого журнала!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Спасибо, сэр."
        call happy
        $herView.addFaceName( "body_06.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu        
        
        
        
                  ### Журналы для взрослых ###
label giving_mag3: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 7
        $herView.showQ( "body_02.png", pos, d5 )
        her "Это...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Журналы для взрослых, сэр?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Учитывая ваш высокий статус?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "Сэр, неужели вы не нашли более продуктивный способ провести свое время?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Я определенно не стану брать их..."
        call upset
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 3
        $herView.showQ( "body_05.png", pos, d5 )
        her "Журналы для взрослых?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Сэр, мне не интересно подобное."
        $herView.hideshowQQ( "body_47.png", pos )
        her "И это не очень уместный подарок для одного из ваших студентов."
        call upset
        $herView.addFaceName( "body_29.png" )


    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 8 
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_31.png", pos, d5 )
        her "Журналы для взрослых?"
        $herView.hideshowQQ( "body_34.png", pos )
        her "Сэр, мне кажется это не подходящий подарок для девушки моего возраста..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько журналов для взрослых..."
        hide screen gift
        with d3
        $herView.showQQ( "body_79.png", pos )
        her "Я уберу их подальше..."
        call happy
        $herView.addFaceName( "body_120.png" ) 


    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_75.png", pos, d5 )
        her "Новый выпуск \"Л.ю.б.в.и.\"!!!"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Э-э...я имела в виду - \"Журналы для взрослых?\""
        her "Это слегка опрометчиво..."
        $herView.hideshowQQ( "body_74.png", pos )
        her "Но я возьму их..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько журналов для взрослых..."
        hide screen gift
        with d3
        $herView.showQQ( "body_74.png", pos )
        her "Спасибо, сэр."
        call happy
       

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu            
        
        
        
        
        
                      ### PORN MAGAZINES ###
label giving_mag4: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 15
        $herView.showQ( "body_01.png", pos, d5 )                                                                                                                                                                                       #HERMIONE
        her "Хм... Что это?"
        $herView.hideshowQQ( "body_130.png", pos )
        her "Сэр, это порно журналы!"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Вам должно быть стыдно!"
        call upset
        


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 8
        $herView.showQ( "body_48.png", pos, d5 )
        her "Порно журналы?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Сэр, что мне с ними делать?"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Исследовать их?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Козел!"
        call upset
        $herView.addFaceName( "body_120.png" )
        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_31.png", pos, d5 )
        her "Это жесткое порно."
        $herView.hideshowQQ( "body_34.png", pos )
        her "Не очень подходящий подарок для девушки моих лет!"
        $herView.hideshowQQ( "body_118.png", pos )
        her ".............."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Но я возьму..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько порно-журналов..."
        hide screen gift
        with d3
        $herView.showQQ( "body_79.png", pos )
        her "И я выброшу их в мусорное ведро, где они и должны быть... как и девушки, которые любят такие вещи..."
        call no_change
        $herView.addFaceName( "body_120.png" )

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_48.png", pos, d5 )
        her "Порнография?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "................"
        $herView.hideshowQQ( "body_117.png", pos )
        her "Как женщины вообще могут такое делать?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "................."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Ладно, я возьму их..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Исключительно для научных целей, конечно же..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько порно-журналов..."
        hide screen gift
        with d3
        call happy
        $herView.addFaceName( "body_45.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
        
        
        
           
                      ### BUTTERBEER ###
label giving_beer: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 3
        $herView.showQ( "body_01.png", pos, d5 )
        her "Сливочное пиво?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Вы уверены насчет этого?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Оно содержит алкоголь..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо вам."
        call happy
        


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_11.png", pos, d5 )
        her "Сливочное пиво, сэр?"
        $herView.hideQQ()
        
        $herView.showQQ( "body_14.png", pos )
        her "Это будет наш маленький секрет..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Я большая поклонница этого безвредного напитка."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy
        

        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Сливочное пиво?"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Я выпью ее с девочками несколько позднее."
        call happy
        

    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_06.png", pos, d5 )
        her "Сливочное пиво...?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Я выпью ее с мальчишками несколько позднее."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Э-э... Я хотела сказать с девочками, да."
        call happy
        $herView.addFaceName( "body_01.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
            
        
        
        
        
        
                   ### PLUSH OWL ###
label giving_owl: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 7
        $herView.showQ( "body_01.png", pos, d5 )
        her "Плюшевая сова?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Так мило..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy
        
      

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_11.png", pos, d5 )
        her "Плюшевая сова?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Мне нравится!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Игрушка?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Игрушки для детей, сэр."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Но я возьму..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy
        
        
        
      
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 4
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_66.png", pos, d5 )
        her "Это что-то из игрушек для взрослых?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Где-то есть переключатель или кнопка..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "И ...оно вибрирует или как?"
        $herView.hideshowQQ( "body_190.png", pos )
        her "Ох...?"
        her "Так это действительно просто плюшевая сова?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Кошмар..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "То есть, спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.addFaceName( "body_01.png" )
        call happy

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
    
    
    
        
     ### SEX DOLL ###
label giving_sexdoll: 
    $herView.hideQ( d5 )
   
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 20
        $herView.showQ( "body_48.png", pos, d5 )
        her "Это..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "Секс-кукла?!"
        $herView.hideshowQQ( "body_32.png", pos )
        her "Профессор Дамблдор!!!"
        call upset
        $herView.addFaceName( "body_33.png" )

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 20
        $herView.showQ( "body_48.png", pos, d5 )
        her "Секс-кукла?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Это очень неприлично, для такого как вы..."
        call upset

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_118.png", pos, d5 )
        her "Секс-кукла..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Это немного неуместно..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Но может мы сможем использовать ее для розыгрышей или вроде того..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">Вы даете Гермионе секс-куклу..."
        hide screen gift
        with d3
        $herView.showQQ( "body_124.png", pos )
        her "Спасибо, сэр."
        call happy
        
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 30
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_73.png", pos, d5 )
        her "Секс-кукла Джуанна?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Я не сказала бы, что одобряю подобное..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Но знаю, что Гарри хотел бы такую..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">Вы даете Гермионе секс-куклу..."
        hide screen gift
        with d3
        $herView.showQQ( "body_188.png", pos )
        her "Спасибо, сэр."
        call happy
        

        
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
        
      ### SEXY LINGERIE ###
label giving_lingerie: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Нижнее белье?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Сэр, я не могу принять от вас такой подарок.."
        call upset
       
      

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.showQ( "body_118.png", pos, d5 )
        her "Сексуальное нижнее белье?"
        $herView.hideshowQQ( "body_117.png", pos )
        her "Вы ведь знаете, что я не могу принять этот подарок."
        $herView.hideshowQQ( "body_118.png", pos )
        her "(Хотя оно довольно милое)........."
        call no_change

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 7
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_124.png", pos, d5 )
        her "Сексуальное нижнее белье?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Сэр, это несколько неуместно..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">Вы даете Гермионе сексуальное нижнее белье..."
        hide screen gift
        with d3
        $herView.showQQ( "body_188.png", pos )
        her "Спасибо, сэр."
        call happy

        
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_124.png", pos, d5 )
        her "Сексуальное нижнее белье?"
        $herView.hideshowQQ( "body_123.png", pos )
        her "Как вам кажется, я могу стать похожей на одну из ведьм из тех журналов для взрослых?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Ох... То есть, спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">Вы даете Гермионе сексуальное нижнее белье..."
        hide screen gift
        with d3
        call happy
        

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
    ### BROOM ###
label giving_broom: 
    $herView.hideQ( d5 )
    
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Метла...?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Хм..."
        $herView.hideshowQQ( "body_07.png", pos )
        her "Что это за странные штуки на ней?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Выглядит как седло...?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_11.png", pos )
        her "Спасибо вам за подарок, сэр."
        $herView.addFaceName( "body_06.png" )
        call happy
       
      

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Метла...?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "Хм..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "Это какая-то секс-игрушка, не так ли?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Ну, неплохо сделано..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_120.png", pos )
        her "Спасибо, сэр."
        call happy
        
        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 30
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_118.png", pos, d5 )
        her "Метла...?"
        her "Хм..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Что это за седло...?"
        $herView.hideshowQQ( "body_127.png", pos )
        her "Ну, не важно."
        her "Отказываться от дорогого подарка было бы глупо..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_120.png", pos )
        her "Спасибо, сэр."
        call happy

    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 30
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_124.png", pos, d5 )
        her "Метла..."
        her "Хм..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Это седло, сэр..."
        $herView.hideshowQQ( "body_190.png", pos )
        her "Оно было разработано специально для меня, не так ли?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Я не уверена, неуместно это или разумно..."
        $herView.hideshowQQ( "body_129.png", pos )
        her "Но это идеальное инженерное решение..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_128.png", pos )
        her "Спасибо, сэр."
        call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
    ### KRUM POSTER ###
label giving_krum: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.showQ( "body_73.png", pos, d5 )
        her "Постер Квиддича?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Что мне с ним делать, сэр?"
        $herView.hideshowQQ( "body_184.png", pos )
        her "Нет, спасибо."
        call no_change
        $herView.addFaceName( "body_71.png" )


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 1
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_73.png", pos, d5 )
        her "Постер по Квиддичу?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Хм..."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Мне кажется, я видела этого игрока пару раз..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Это тот студент из Дурмштранга?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        call happy
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_73.png", pos, d5 )
        her "Постер Виктора Крама, сэр?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Ну, я немного интересуюсь квиддичем..."
        $herView.hideshowQQ( "body_87.png", pos )
        her "Не понять, что девушки находят в этих перекачанных парнях..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        call happy
        
        
       
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 25
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_72.png", pos, d5 )
        her "Постер Виктора Крама?!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Спасибо, сэр!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_46.png", pos )
        her "Не могу дождаться, чтобы повесить его над своей кроватью!"
        $herView.hideshowQQ( "body_64.png", pos )
        her "Девченки обзавидуются..."
        call happy


    $ pos = POS_370
    jump hermione_main_menu                    
        
        
        
        
        
     ### S.P.E.W. BADGE ###
label giving_badge: 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #     
    $hermi.WrdSetAddNew("badge")
    $herView.showQ( "body_01.png", pos, d5 )
    her "Значок?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. BADGE.
    show screen gift
    with d3
    ">Вы даете значок Гермионе...\n>Значок \"А.В.Н.Э.\" был добавлен в гардероб Гермионы."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_06.png", pos )
    her "Спасибо, сэр."
    call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                    
            
        
label giving_hair_set : 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #     
    $herView.showQ( "body_01.png", pos, d5 )
    her "Ведьмодница ? Я ?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/07.png" 
    show screen gift
    with d3
    ">Вы даете Гермионе набор для волос. Теперь в гардеробе доступны различные прически."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_06.png", pos )
    her "Спасибо, сэр."
    call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    $hermi.WrdHairUnlock()
    jump hermione_main_menu    
    
    
        
    ### Ажурные чулки ###
label giving_nets: 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #      
    $hermi.WrdSetAddNew("nets")    
    $herView.showQ( "body_03.png", pos, d5 )
    her "Пара чулков?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">Вы даете Гермионе пару чулков...\n>Ажурные чулки добавлены в ее гардероб."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_04.png", pos )
    her "Спасибо, сэр."
    call happy
    
    $herView.addFaceName( "body_03.png" )

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                    
            
   
label giving_tights: 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #     
    $hermi.WrdSetAddNew("tights")     
    $herView.showQ( "body_03.png", pos, d5 )
    her "Колготки ?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">Вы даете Гермионе колготки..."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_04.png", pos )
    her "Спасибо, сэр."
    call happy
    
    $herView.addFaceName( "body_03.png" )

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu        
    
        
        
    label happy:
        $herView.hideQQ()
#        if mad <= 0:
#            $ mad = 0
        $Say([">Настроение Гермионы улучшено...\n>Гермиона {size=+5}огорчена вами{/size}...", 
              ">Настроение Гермионы улучшено...\n>Гермиона {size=+5}не злится{/size} на вас...",
              ">Настроение Гермионы улучшено...\n>Гермионе {size=+5}вы приятны{/size}..."][Sign(hermi.liking)+1])
        return



    label no_change:
        $herView.hideQQ()
        ">Настроение Гермионы не изменилось..."
        return
        
    label upset:
        $herView.hideQQ()
        ">Настроение Гермионы ухудшилось...\n>Гермиона {size=+5}злится{/size} на вас..."
        return
        
        
label giving_shortskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"shortskirt")  
    $hermi.WrdSetAddNew("shortskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали среднюю школьную юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu

    
label giving_xshortskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xshortskirt")  
    $hermi.WrdSetAddNew("xshortskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали короткую школьную юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
label giving_xxshortskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xxshortskirt")  
    $hermi.WrdSetAddNew("xxshortskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали игривую школьную юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
label giving_xsmallskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xsmallskirt")  
    $hermi.WrdSetAddNew("xsmallskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную мини-юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
label giving_xxsmallskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xxsmallskirt")  
    $hermi.WrdSetAddNew("xxsmallskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную микро-юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu    
  
    
label giving_skirt_cheerleader:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"skirt_cheerleader")  
    $hermi.WrdSetAddNew("skirt_cheerleader")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали юбку болельщицы Гриффиндора Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu 
    
    
label giving_skirt_business:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"skirt_business")  
    $hermi.WrdSetAddNew("skirt_business")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали миниюбку бизнес-леди Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu 
    
    
label giving_skimpyshirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"skimpyshirt")  
    $hermi.WrdSetAddNew("skimpyshirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную рубашку-минитопик Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Рубашка ? У нее какой-то странный размер."
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu   
    
label giving_shirt_business :
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"shirt_business")  
    $hermi.WrdSetAddNew("shirt_business")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали белую рубашку в деловом стиле Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Рубашка ?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu  
    
label giving_shirt_cheerleader :
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"shirt_cheerleader")  
    $hermi.WrdSetAddNew("shirt_cheerleader")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали кофту болельщицы Гриффиндора Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Кофта ?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu 
    
### DR'S Wardrobe

label wrd_badge_01_first_dress :
    $ wrd_new_items -= 1
    $ wrd_badge_01 = 1

    $herView.hideQQ()

    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Конечно, сэр..."
    ""
    
    jump wrd_badge_01_dress

    
label wrd_nets_first_dress :

    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_11.png", pos )
        her "Ажурные чулки...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Вы, должно быть, не серьезно, сэр!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "С радостью..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, хорошо..."
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Я не из таких девушек, сэр..."
        her "Попытайте удачу с одной из \"Слизеринских\" шлюх..."
        menu:
            m "..."
            "\"Просто надень это!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это врядли соответствует форме студента Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, раз так..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Ажурные чулки?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Я не уверена насчет этого, сэр..."
        menu:
            m "..."
            "\"Просто надень их!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, Ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        

    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Если вы настаиваете, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_nets = 1
    jump wrd_nets_dress
    
label wrd_tights_first_dress :

    $ pos = POS_370
    $herView.hideshowQQ( "body_02.png", pos )
    her "Колготки, сэр ?"
    her "Это довольно неожиданно."
    if hermi.whoring <= 12 and hermi.whoring >= 3 :
        her "(Интересно, в чем тут подвох ?)"
    $herView.hideshowQQ( "body_07.png", pos )
    her "Мне кажется, что они не относятся к обычной форме ученицы..."
    her "С другой стороны, тут нет ничего плохого."

    $ wrd_new_items -= 1
    $ wrd_tights = 1
    jump wrd_tights_dress

label wrd_shortskirt_first_dress :

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Это короткая юбка?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_shortskirt = 1
    jump wrd_shortskirt_dress

label wrd_xshortskirt_first_dress :

    if wrd_shortskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка еще короче прежней?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она еще короче..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_xshortskirt = 1
    jump wrd_xshortskirt_dress

    
label wrd_xxshortskirt_first_dress :

    if wrd_xshortskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка еще короче прежней?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 14
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она еще короче..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 7
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )


    $ wrd_new_items -= 1
    $ wrd_xxshortskirt = 1
    jump wrd_xxshortskirt_dress

    
label wrd_xsmallskirt_first_dress :

    if wrd_xxshortskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта мини-юбка совсем коротенькая!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее всем будут видны мои трусики !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"45 очков ?\"" :
                        $ gryffindor +=45
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Чувствую, что я еще пожалею об этом..."
                        her "(Нужно будет поменьше наклоняться.)"
                        $herView.hideQQ()
                        $ hermi.liking -= 16
                        call upset
                    
        
        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 12
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 21: # Lv 8+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )


    $ wrd_new_items -= 1
    $ wrd_xsmallskirt = 1
    jump wrd_xsmallskirt_dress

label wrd_xxsmallskirt_first_dress :

    if wrd_xsmallskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Да это и юбкой-то назвать нельзя!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это абсолютно неприемлимо !"
        $ hermi.liking -= 18
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()         
                $ hermi.liking -= 8
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 8
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта мини-юбка совсем крошечная!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее мои трусики будут видны из другого конца коридора!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"70 очков ?\"" :
                        $ gryffindor +=70
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Ох... Что же я делаю...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 20
                        call upset
                    
        
        

    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Как... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она короткая-прекороткая..."
        her "Я хочу сказать, у всего же должен быть предел !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это однозначно не соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 16
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                $ gryffindor +=50
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 21 : # Lv 8.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Но она же..."
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем, совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Как скажете, сэр"
            "\"Я дам тебе 50 очков.\"":
                $ gryffindor +=50
                $herView.hideshowQQ( "body_07.png", pos )
                her "Ох-хо-хо"
                $herView.hideshowQQ( "body_68.png", pos )
                her "Да, сэр."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Да, сэр"
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu


    $ wrd_new_items -= 1
    $ wrd_xxsmallskirt = 1
    jump wrd_xxsmallskirt_dress

label wrd_xxxsmallskirt_first_dress :

    if wrd_xxsmallskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Да это и юбкой-то назвать нельзя!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 11: # Lv 1-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этом клочке материи ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да им даже с доски не сотрешь !"
        her "Нет, это невозможно !"
        $ hermi.liking -= 25
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этом клочке материи ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 10
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 18 and hermi.whoring <= 23: # Lv 7-8
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка микроскопическая!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее мои трусики будут видны из другого здания!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"100 очков ?\"" :
                        $ gryffindor +=100
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 25
                        call upset
                    
        
        

    if hermi.whoring >= 24 : # Lv Max.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Как... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она микроскопическая"
        her "Я хочу сказать, у всего же должен быть предел !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это немыслимо для Хогвартса!"
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 20
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Мммммм"
                $herView.hideshowQQ( "body_08.png", pos )
                her "Мне трудно решиться..."
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"100 очков ?\"" :
                        $ gryffindor +=100
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Постараюсь смириться."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        call upset
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    $ wrd_new_items -= 1
    $ wrd_xxxsmallskirt = 1
    jump wrd_xxxsmallskirt_dress
    
label wrd_skirt_cheerleader_first_dress :

    if nsp_event_kviddich_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не болельщица, не люблю болельщиц и не вижу смысла одеваться как одна из них !"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка слишком короткая?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она слишком короткая !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_skirt_cheerleader = 1
    jump wrd_skirt_cheerleader_dress
    
label wrd_skirt_business_first_dress :

    if nsp_event_magls_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не магл, кто бы что ни говорил. Зачем давать лишний повод ?"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка недопустимо коротка !"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 14
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 7
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )


    $ wrd_new_items -= 1
    $ wrd_skirt_business = 1
    jump wrd_skirt_business_dress

label wrd_standart02_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 8:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует форме Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 10 очков.\"":
                $ gryffindor +=10
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 9:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart02 = 1
    jump wrd_standart02_dress

    
label wrd_standart03_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 11:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует форме Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 12:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart03 = 1
    jump wrd_standart03_dress

label wrd_standart04_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 14:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует правилам Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 15:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart04 = 1
    jump wrd_standart04_dress

label wrd_standart05_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 20:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Сэр ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Вы же это не серьезно ? Ведь все-таки тут школа."
        menu:
            m "..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "О, сэр."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я постараюсь к этому привыкнуть."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 21:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart05 = 1
    jump wrd_standart05_dress

label wrd_skimpyshirt_first_dress :

    if wrd_standart05 == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы шутите, сэр?!"
        her "Да это не рубашка, а сплошной разврат."
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить ей менее оьткровенные варианты.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 11: # Lv 1-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да ей даже с доски не сотрешь !"
        her "Нет, это невозможно !"
        $ hermi.liking -= 15
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7-8
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта рубашка слишком откровенная!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Мои буф... мою грудь будет видно всем !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"50 очков ?\"" :
                        $ gryffindor +=50
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 20
                        call upset
                    
        
        

    if hermi.whoring >= 21 and hermi.whoring <= 23: # Lv 7-8
        $herView.hideshowQQ( "body_15.png", pos )
        her "Эта рубашка такая открытая... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "И совсем маленькая!"
        her "Сэр, вы уверены, что мне нужно это делать ?"
        her "Мне кажется, это плохая идея..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, заставлять меня делать это недопустимо!"
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 15
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Мммммм"
                $herView.hideshowQQ( "body_08.png", pos )
                her "Мне трудно решиться..."
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"50 очков ?\"" :
                        $ gryffindor +=50
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Постараюсь смириться."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        call upset
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
                
    if hermi.whoring >= 24 : # Lv Max.                
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_skimpyshirt = 1
    jump wrd_skimpyshirt_dress
    
label wrd_shirt_cheerleader_first_dress :

    if nsp_event_kviddich_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не болельщица, не люблю болельщиц и не вижу смысла одеваться как одна из них !"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 17: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта кофта слишком открытая !"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она не полностью прикрывает мои буф... мою... мой бюст !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_shirt_cheerleader = 1
    jump wrd_shirt_cheerleader_dress
    
    
label wrd_shirt_business_first_dress :

    if nsp_event_magls_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не магл, кто бы что ни говорил. Зачем давать лишний повод ?"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu


    if hermi.whoring >= 0 and hermi.whoring <= 14:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует правилам Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 15:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_shirt_business = 1
    jump wrd_shirt_business_dress

    
label wrd_nobadge_dress :
    call wrd_badges_undress
    call wrd_dress_change
    jump hermione_main_menu

label wrd_badge_01_dress :
    call wrd_badges_undress
    $ wrd_badge_01 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_nonets_dress :
    call wrd_nets_undress
    call wrd_dress_change
    jump hermione_main_menu

label wrd_nets_dress :
    call wrd_nets_undress
    $ wrd_nets = 1
    call wrd_dress_change
    jump hermione_main_menu
    
label wrd_tights_dress :
    call wrd_nets_undress
    $ wrd_tights = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skirt_dress :
    call wrd_skirts_undress
    $ wrd_skirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_shortskirt_dress :
    call wrd_skirts_undress
    $ wrd_shortskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xshortskirt_dress :
    call wrd_skirts_undress
    $ wrd_xshortskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xxshortskirt_dress :
    call wrd_skirts_undress
    $ wrd_xxshortskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xsmallskirt_dress :
    call wrd_skirts_undress
    $ wrd_xsmallskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xxsmallskirt_dress :
    call wrd_skirts_undress
    $ wrd_xxsmallskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xxxsmallskirt_dress :
    call wrd_skirts_undress
    $ wrd_xxxsmallskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skirt_cheerleader_dress :
    call wrd_skirts_undress
    $ wrd_skirt_cheerleader = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skirt_business_dress :
    call wrd_skirts_undress
    $ wrd_skirt_business = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart01_dress :
    call wrd_shirts_undress
    $ wrd_standart01 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart02_dress :
    call wrd_shirts_undress
    $ wrd_standart02 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart03_dress :
    call wrd_shirts_undress
    $ wrd_standart03 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart04_dress :
    call wrd_shirts_undress
    $ wrd_standart04 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart05_dress :
    call wrd_shirts_undress
    $ wrd_standart05 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skimpyshirt_dress : 
    call wrd_shirts_undress
    $ wrd_skimpyshirt = 1  
    call wrd_dress_change 
    jump hermione_main_menu

label wrd_shirt_cheerleader_dress : 
    call wrd_shirts_undress
    $ wrd_shirt_cheerleader = 1  
    call wrd_dress_change
    jump hermione_main_menu

label wrd_shirt_business_dress : 
    call wrd_shirts_undress
    $ wrd_shirt_business = 1  
    call wrd_dress_change 
    jump hermione_main_menu       

    
label wrd_badges_undress :

    if wrd_badge_01 == 1 :
        $ wrd_badge_01 = 2
    return

label wrd_nets_undress :

    if wrd_nets == 1 :
        $ wrd_nets = 2
    if wrd_tights == 1 :
        $ wrd_tights = 2
    return

label wrd_skirts_undress :

    if wrd_skirt == 1 :
        $ wrd_skirt = 2
    if wrd_shortskirt == 1 :
        $ wrd_shortskirt = 2
    if wrd_xshortskirt == 1 :
        $ wrd_xshortskirt = 2
    if wrd_xxshortskirt == 1 :
        $ wrd_xxshortskirt = 2
    if wrd_xsmallskirt == 1 :
        $ wrd_xsmallskirt = 2
    if wrd_xxsmallskirt == 1 :
        $ wrd_xxsmallskirt = 2
    if wrd_xxxsmallskirt == 1 :
        $ wrd_xxxsmallskirt = 2
    if wrd_skirt_cheerleader == 1 :
        $ wrd_skirt_cheerleader = 2
    if wrd_skirt_business == 1 :
        $ wrd_skirt_business = 2
    return

label wrd_shirts_undress :
    if wrd_standart01 == 1 :
        $ wrd_standart01 = 2
    if wrd_standart02 == 1 :
        $ wrd_standart02 = 2
    if wrd_standart03 == 1 :
        $ wrd_standart03 = 2
    if wrd_standart04 == 1 :
        $ wrd_standart04 = 2
    if wrd_standart05 == 1 :
        $ wrd_standart05 = 2
    if wrd_skimpyshirt == 1 :
        $ wrd_skimpyshirt = 2
    if wrd_shirt_cheerleader == 1 :
        $ wrd_shirt_cheerleader = 2
    if wrd_shirt_business == 1 :
        $ wrd_shirt_business = 2
    return

label wrd_dress_undress :

    call wrd_dress_undress_skirts
    call wrd_dress_undress_shirts
    call wrd_dress_undress_stockings
    call wrd_dress_undress_badge

    return
    
label wrd_dress_undress_skirts :

    $ herView.data().delItem( 'item_skirt' )
    $ herView.data().delItem( 'item_skirts_skirt02_short' )
    $ herView.data().delItem( 'item_skirts_skirt03_xshort' )
    $ herView.data().delItem( 'item_skirts_skirt04_xxshort' )
    $ herView.data().delItem( 'item_skirts_skirt05_xsmall' )
    $ herView.data().delItem( 'item_skirts_skirt06_xxsmall' )
    $ herView.data().delItem( 'item_skirts_skirt07_xxxsmall' )
    $ herView.data().delItem( 'item_skirts_skirt_business' )
    $ herView.data().delItem( 'item_skirts_cheerleader_gryffindor' )

    return
    
label wrd_dress_undress_shirts :

    $ herView.data().delItem( 'item_tits' )
    $ herView.data().delItem( 'item_tits_no' )

    $ herView.data().delItem( 'item_dress' )
    $ herView.data().delItem( 'item_shirts_standard02_untucked_tie' )
    $ herView.data().delItem( 'item_shirts_standard03_untucked' )
    $ herView.data().delItem( 'item_shirts_standard04_untucked_unbuttoned' )
    $ herView.data().delItem( 'item_shirts_standard05_untucked_unbuttoned_double' )
    $ herView.data().delItem( 'item_shirts_standard06_skimpy_tied' )
    $ herView.data().delItem( 'item_shirts_blouse_business' )
    $ herView.data().delItem( 'item_shirts_cheerleader_gryffindor' )

    return
    
label wrd_dress_undress_stockings :

    $ herView.data().delItem( 'item_nets' )
    $ herView.data().delItem( 'item_stockings_tights' )

    return
    
label wrd_dress_undress_badge :

    $ herView.data().delItem( 'item_badge' )

    return
    
label wrd_dress_change :

    $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
    call wrd_dress_change_silent

    $herView.hideshowQQ( "body_01.png", pos )
    
    pause.5
    $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
    $screens.Show("ctc").Pause().Hide("ctc")
    
    return
    
label wrd_dress_change_silent :
    
    call wrd_dress_undress
    
    if wrd_tits == 1 :
        $ herView.data().addItem( 'item_tits' )
    if wrd_tits_no == 1 :
        $ herView.data().addItem( 'item_tits_no' )   
    
    if wrd_badge_01 == 1 :
        $ herView.data().addItem( 'item_badge' )
        
    if wrd_nets == 1 :
        $ herView.data().addItem( 'item_nets' )
    if wrd_tights == 1 :
        $ herView.data().addItem( 'item_stockings_tights' )

    if wrd_skirt == 1 :
        $ herView.data().addItem( 'item_skirt' )
    if wrd_shortskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt02_short' )
    if wrd_xshortskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt03_xshort' )
    if wrd_xxshortskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt04_xxshort' )
    if wrd_xsmallskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt05_xsmall' )
    if wrd_xxsmallskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt06_xxsmall' )
    if wrd_xxxsmallskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt07_xxxsmall' )
    if wrd_skirt_business == 1 :
        $ herView.data().addItem( 'item_skirts_skirt_business' )
    if wrd_skirt_cheerleader == 1 :
        $ herView.data().addItem( 'item_skirts_cheerleader_gryffindor' )
    
    if wrd_standart01 == 1 :
        $ herView.data().addItem( 'item_dress' )
    if wrd_standart02 == 1 :
        $ herView.data().addItem( 'item_shirts_standard02_untucked_tie' )
    if wrd_standart03 == 1 :
        $ herView.data().addItem( 'item_shirts_standard03_untucked' )
    if wrd_standart04 == 1 :
        $ herView.data().addItem( 'item_shirts_standard04_untucked_unbuttoned' )
    if wrd_standart05 == 1 :
        $ herView.data().addItem( 'item_shirts_standard05_untucked_unbuttoned_double' )
    if wrd_skimpyshirt == 1 :
        $ herView.data().addItem( 'item_shirts_standard06_skimpy_tied' )
    if wrd_shirt_business == 1 :
        $ herView.data().addItem( 'item_shirts_blouse_business' )
    if wrd_shirt_cheerleader == 1 :
        $ herView.data().addItem( 'item_shirts_cheerleader_gryffindor' )
    
    return

### New Wardrobe 2.0

label wrd_first_badge :
    $ wrd_new_items -= 1
    $ wrd_badge_01 = 1

    $herView.hideQQ()

    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Конечно, сэр..."
    ""
    
    $ hermi.WrdSetUnlock ("badge")
    $ hermi.WrdSetDress("badge")
    $ hermi.WrdSetMainBL ()

    return

    
label wrd_first_nets :

    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_11.png", pos )
        her "Ажурные чулки...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Вы, должно быть, не серьезно, сэр!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "С радостью..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, хорошо..."
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Я не из таких девушек, сэр..."
        her "Попытайте удачу с одной из \"Слизеринских\" шлюх..."
        menu:
            m "..."
            "\"Просто надень это!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это врядли соответствует форме студента Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, раз так..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Ажурные чулки?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Я не уверена насчет этого, сэр..."
        menu:
            m "..."
            "\"Просто надень их!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, Ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        

    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Если вы настаиваете, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("nets")
    $ hermi.WrdSetDress("nets")
    $ hermi.WrdSetMainBL ()

    return
    
label wrd_first_tights :

    $ pos = POS_370
    $herView.hideshowQQ( "body_02.png", pos )
    her "Колготки, сэр ?"
    her "Это довольно неожиданно."
    if hermi.whoring <= 12 and hermi.whoring >= 3 :
        her "(Интересно, в чем тут подвох ?)"
    $herView.hideshowQQ( "body_07.png", pos )
    her "Мне кажется, что они не относятся к обычной форме ученицы..."
    her "С другой стороны, тут нет ничего плохого."

    $ hermi.WrdSetUnlock ("tights")
    $ hermi.WrdSetDress("tights")
    $ hermi.WrdSetMainBL ()

    return

label wrd_first_shortskirt :

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Это короткая юбка?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("shortskirt")
    $ hermi.WrdSetDress("shortskirt")
    $ hermi.WrdSetMainBL ()

    return

label wrd_first_xshortskirt :

    if not hermi.WrdIsAdm("shortskirt") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка еще короче прежней?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она еще короче..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("xshortskirt")
    $ hermi.WrdSetDress("xshortskirt")
    $ hermi.WrdSetMainBL ()

    return

    
label wrd_first_xxshortskirt :

    if not hermi.WrdIsAdm("xshortskirt") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка еще короче прежней?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 14
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она еще короче..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 7
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("xxshortskirt")
    $ hermi.WrdSetDress("xxshortskirt")
    $ hermi.WrdSetMainBL ()

    return

    
label wrd_first_xsmallskirt :

    if not hermi.WrdIsAdm("xxshortskirt") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта мини-юбка совсем коротенькая!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее всем будут видны мои трусики !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"45 очков ?\"" :
                        $ gryffindor +=45
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Чувствую, что я еще пожалею об этом..."
                        her "(Нужно будет поменьше наклоняться.)"
                        $herView.hideQQ()
                        $ hermi.liking -= 16
                        call upset
                    
        
        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 12
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 21: # Lv 8+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("xsmallskirt")
    $ hermi.WrdSetDress("xsmallskirt")
    $ hermi.WrdSetMainBL ()

    return

label wrd_first_xxsmallskirt :

    if not hermi.WrdIsAdm("xsmallskirt") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Да это и юбкой-то назвать нельзя!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это абсолютно неприемлимо !"
        $ hermi.liking -= 18
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()         
                $ hermi.liking -= 8
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 8
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта мини-юбка совсем крошечная!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее мои трусики... если они надеты... будут видны из другого конца коридора!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"70 очков ?\"" :
                        $ gryffindor +=70
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Ох... Что же я делаю...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 20
                        call upset
                    
        
        

    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Как... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она короткая-прекороткая..."
        her "Я хочу сказать, у всего же должен быть предел !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это однозначно не соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 16
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                $ gryffindor +=50
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 21 : # Lv 8.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Но она же..."
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем, совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Как скажете, сэр"
            "\"Я дам тебе 50 очков.\"":
                $ gryffindor +=50
                $herView.hideshowQQ( "body_07.png", pos )
                her "Ох-хо-хо"
                $herView.hideshowQQ( "body_68.png", pos )
                her "Да, сэр."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Да, сэр"
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    $ hermi.WrdSetUnlock ("xxsmallskirt")
    $ hermi.WrdSetDress("xxsmallskirt")
    $ hermi.WrdSetMainBL ()

    if wrd_nopanties_dialog == False and hermi.whoring >= 12 and (hermi.WrdIsWear("xxsmallskirt") or hermi.WrdIsWear("xxxsmallskirt")):
        m "Гермиона !!! Вау !"
        m "Ты не боишься так ходить по школе ?"
        
        $herView.hideshowQQ( "body_56.png", pos )
        her "..........."
        her "Я использую маскирующие чары, сэр."
        
        $ wrd_nopanties_dialog = True
    
    return

label wrd_first_xxxsmallskirt :

    if not hermi.WrdIsAdm("xxsmallskirt") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Да это и юбкой-то назвать нельзя!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 11: # Lv 1-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этом клочке материи ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да им даже с доски не сотрешь !"
        her "Нет, это невозможно !"
        $ hermi.liking -= 25
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этом клочке материи ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 10
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 18 and hermi.whoring <= 23: # Lv 7-8
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка микроскопическая!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее мои трусики... ну, если я их надену... будут видны из другого здания!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"100 очков ?\"" :
                        $ gryffindor +=100
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 25
                        call upset
                    
        
        

    if hermi.whoring >= 24 : # Lv Max.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Как... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она микроскопическая"
        her "Я хочу сказать, у всего же должен быть предел !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это немыслимо для Хогвартса!"
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 20
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Мммммм"
                $herView.hideshowQQ( "body_08.png", pos )
                her "Мне трудно решиться..."
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"100 очков ?\"" :
                        $ gryffindor +=100
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Постараюсь смириться."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        call upset
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    $ hermi.WrdSetUnlock ("xxxsmallskirt")
    $ hermi.WrdSetDress("xxxsmallskirt")
    $ hermi.WrdSetMainBL ()

    if wrd_nopanties_dialog == False and hermi.whoring >= 12 and (hermi.WrdIsWear("xxsmallskirt") or hermi.WrdIsWear("xxxsmallskirt")):
        m "Гермиона !!! Вау !"
        m "Ты не боишься так ходить по школе ?"
        
        $herView.hideshowQQ( "body_56.png", pos )
        her "..........."
        her "Я использую маскирующие чары, сэр."
        
        $wrd_nopanties_dialog = True
    
    return
    
label wrd_first_skirt_cheerleader :

    if nsp_event_kviddich_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не болельщица, не люблю болельщиц и не вижу смысла одеваться как одна из них !"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка слишком короткая?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она слишком короткая !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("skirt_cheerleader")
    $ hermi.WrdSetDress("skirt_cheerleader")
    $ hermi.WrdSetMainBL ()

    return
    
label wrd_first_skirt_business :

    if nsp_event_magls_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не магл, кто бы что ни говорил. Зачем давать лишний повод ?"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка недопустимо коротка !"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 14
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 7
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("skirt_business")
    $ hermi.WrdSetDress("skirt_business")
    $ hermi.WrdSetMainBL ()

    return

label wrd_first_standart2 :

    if hermi.whoring >= 0 and hermi.whoring <= 8:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует форме Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 10 очков.\"":
                $ gryffindor +=10
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 9:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("standart2")
    $ hermi.WrdSetDress("standart2")
    $ hermi.WrdSetMainBL ()
    $ hermi.WrdSetAddNew("standart3")

    return

    
label wrd_first_standart3 :

    if not hermi.WrdIsAdm("standart2") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы шутите, сэр?!"
        her "Да это не рубашка, а сплошной разврат."
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить ей менее оьткровенные варианты.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370
    
    if hermi.whoring >= 0 and hermi.whoring <= 11:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует форме Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 12:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("standart3")
    $ hermi.WrdSetDress("standart3")
    $ hermi.WrdSetMainBL ()
    $ hermi.WrdSetAddNew("standart4")

    return

label wrd_first_standart4 :

    if not hermi.WrdIsAdm("standart3") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы шутите, сэр?!"
        her "Да это не рубашка, а сплошной разврат."
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить ей менее оьткровенные варианты.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 14:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует правилам Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 15:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("standart4")
    $ hermi.WrdSetDress("standart4")
    $ hermi.WrdSetMainBL ()
    $ hermi.WrdSetAddNew("standart5")

    return

label wrd_first_standart5 :

    if not hermi.WrdIsAdm("standart4") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы шутите, сэр?!"
        her "Да это не рубашка, а сплошной разврат."
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить ей менее оьткровенные варианты.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370
    
    if hermi.whoring >= 0 and hermi.whoring <= 20:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Сэр ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Вы же это не серьезно ? Ведь все-таки тут школа."
        menu:
            m "..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "О, сэр."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я постараюсь к этому привыкнуть."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 21:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("standart5")
    $ hermi.WrdSetDress("standart5")
    $ hermi.WrdSetMainBL ()

    return

label wrd_first_skimpyshirt :

    if not hermi.WrdIsAdm("standart5") :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы шутите, сэр?!"
        her "Да это не рубашка, а сплошной разврат."
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить ей менее оьткровенные варианты.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 11: # Lv 1-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да ей даже с доски не сотрешь !"
        her "Нет, это невозможно !"
        $ hermi.liking -= 15
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7-8
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта рубашка слишком откровенная!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Мои буф... мою грудь будет видно всем !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"50 очков ?\"" :
                        $ gryffindor +=50
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 20
                        call upset
                    
        
        

    if hermi.whoring >= 21 and hermi.whoring <= 23: # Lv 7-8
        $herView.hideshowQQ( "body_15.png", pos )
        her "Эта рубашка такая открытая... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "И совсем маленькая!"
        her "Сэр, вы уверены, что мне нужно это делать ?"
        her "Мне кажется, это плохая идея..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, заставлять меня делать это недопустимо!"
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 15
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Мммммм"
                $herView.hideshowQQ( "body_08.png", pos )
                her "Мне трудно решиться..."
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"50 очков ?\"" :
                        $ gryffindor +=50
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Постараюсь смириться."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        call upset
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
                
    if hermi.whoring >= 24 : # Lv Max.                
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("skimpyshirt")
    $ hermi.WrdSetDress("skimpyshirt")
    $ hermi.WrdSetMainBL ()

    return
    
label wrd_first_shirt_cheerleader :

    if nsp_event_kviddich_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не болельщица, не люблю болельщиц и не вижу смысла одеваться как одна из них !"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 17: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта кофта слишком открытая !"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она не полностью прикрывает мои буф... мою... мой бюст !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("shirt_cheerleader")
    $ hermi.WrdSetDress("shirt_cheerleader")
    $ hermi.WrdSetMainBL ()

    return
    
    
label wrd_first_shirt_business :

    if nsp_event_magls_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не магл, кто бы что ни говорил. Зачем давать лишний повод ?"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu


    if hermi.whoring >= 0 and hermi.whoring <= 14:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует правилам Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 15:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ hermi.WrdSetUnlock ("shirt_business")
    $ hermi.WrdSetDress("shirt_business")
    $ hermi.WrdSetMainBL ()

    return
    
    