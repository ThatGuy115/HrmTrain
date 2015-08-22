label nsp_theme_magls :

    $herView.hideshowQQ( "body_01.png", pos )
    g9 "(Попробую действовать творчески.)"
    m "Скажи, как по-твоему, справедливо ли обзывать тебя грязнокровкой ?"
    $herView.hideshowQQ( "body_72.png", pos )    
    her "Сэр !"
    her "Как вы можете говорить такое ?"
    her "У меня нет слов !"
    m "Успокойся ! Я не смеюсь над тобой."
    m "Мне просто нужно знать, готова ли ты что-то с этим сделать ?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "То есть вы не..."
    $herView.hideshowQQ( "body_16.png", pos )
    her "Да, сэр, конечно да."
    her "Но что я могу ?"
    $herView.hideshowQQ( "body_12.png", pos )
    her "Многие \"чистокровки\" убеждены, что маглы похожи на животных. А маглорожденные - на животных, одевших одежды волшебников."
    her "И никто из аристократов не захочет прислушаться к мнению неаристократов."
    m "У меня есть идея. Нужно снять с тебя одежды волшебников и..."
    $herView.hideshowQQ( "body_22.png", pos )
    her "Но сэр ! Как вы можете такое предлагать ? Это совершенно неприемлимо ! Это должно быть шуткой."
    her "Пожалуй мне лучше уйти."
    g6 "(Ну и ну, в этот раз я даже ничего такого не имел ввиду !)"
    m "Постой ! Я хотел сказать, что нужно одеть одежду маглов вместо обычной."
    $herView.hideshowQQ( "body_14.png", pos )
    her "Маглов, сэр ? Боюсь, я не понимаю."
    m "Я думаю, все проблемы расизма возникают из-за того, что потомственные маги плохо понимают маглов."
    m "И никто из них обычно не ходит на это, как его, магловодство... магловидение... магловедение !"
    m "Но если кто-то из учеников покажет им лучшие стороны магловской культуры..."
    $herView.hideshowQQ( "body_01.png", pos )
    
    return

label nsp_event_magls_1 :

    if cur_level == 1 :

        $herView.hideshowQQ( "body_01.png", pos )
    
        if nsp_event_magls_1 == 0 :  
        
            g9 "(Интересно, что подумает Дамблдор, если оставить ему на память женскую одежду в шкафу...)"
            g9 "Ты готова снять сегодня всю маговскую одежду и выйти на публику ?"
            $herView.hideshowQQ( "body_18.png", pos )
            her "Сэр ???"
            m "... В магловской одежде."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Опять вы меня разыграли."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Ну, если вы уверены, что это поможет улучшить отношения к маглорожденным..."
            her "Я готова попробовать."
            m "Отлично. Для начала надень-ка деловой наряд успешной магловки."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Магловки… Мне не нравится, как это звучит."
            her "Ладно, думаю ничего страшного тут нет."
            
            $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
            $hermi.WrdDress ("skirt_business")
            $hermi.WrdDress ("shirt_business")
            $hermi.WrdDress ("tights")
            $hermi.WrdNoOther()
            $hermi.WrdMain()
            $ herView.data().setStyleKey( 'shirt_business', 'closed' )
            hide screen hermione_02
            show screen nsp_hermione_business
            $herView.hideshowQQ( "body_01.png", pos )
            pause.5
            $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
            $screens.Show("ctc").Pause().Hide("ctc")
            
            m "И не забудь, что нужно выглядеть привлекательно."
            m "Мы хотим улучшить репутацию маглов, а не потерять последний шанс."
            m "Попробуй расстегнуть пару верхних пуговиц."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Да, сэр."
            $hermi.WrdMain()
            pause.5
            g9 "Вот, гораздо лучше."
            $herView.hideshowQQ( "body_12.png", pos )
            her "(Ну еще бы.)"

        else :
            m "Готова к маскараду ? Сегодня это деловой костюм."
            $herView.hideshowQQ( "body_15.png", pos )
            her "Всегда, сэр."
            
            $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
            $hermi.WrdDress ("skirt_business")
            $hermi.WrdDress ("shirt_business")
            $hermi.WrdDress ("tights")
            $hermi.WrdNoOther()
            $hermi.WrdMain()
            hide screen hermione_02
            show screen nsp_hermione_business
            pause.5
            $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
            $screens.Show("ctc").Pause().Hide("ctc")
            
            m "Отлично."
            g9 "На месте \"чистокровок\" я бы вду… то есть задумался."
            $herView.hideshowQQ( "body_06.png", pos )
            her "Спасибо, сэр."
        
        $herView.hideshowQQ( "body_01.png", pos )
        hide screen nsp_hermione_business
        $hermi.WrdSetMain()
        
    
    
    elif cur_level == 2 :
        ">текст преивента маглов 1-2"
    elif cur_level == 3 :
        ">текст преивента маглов 1-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 1-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 1-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маглах "
    $ nsp_genie_sphere_req = nsp_germiona_magls_1_photo
    
    if nsp_germiona_magls_1_statimg == "New" :
        $ cur_level = nsp_event_magls_1 + 1
    else :
        $ cur_level = nsp_event_magls_1

    if cur_level == 1 :
    
        hide screen hermione_02
        show screen nsp_hermione_business
        $hermi.WrdDress ("skirt_business")
        $hermi.WrdDress ("shirt_business")
        $hermi.WrdDress ("tights")
        $hermi.WrdNoOther()
        $hermi.WrdMain()
        $herView.hideshowQQ( "body_01.png", pos )
    
        her "А вот и я, сэр"
        m "Рассказывай."
        $herView.hideshowQQ( "body_04.png", pos )
        her "Как вы и просили, я весь день проходила в этом наряде."
        m "И тебе удалось улучшить отношение к маглам ?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Ой не знаю, профессор."
        her "Сегодня на меня гораздо чаще обращали внимание слизеринцы..."
        her "Так что, наверное, можно сказать, что мне удалось заинтересовать общественность."
        m "И в чем же проявлялось их внимание."
        $herView.hideshowQQ( "body_45.png", pos )
        her "Они… Они..."
        m "Они приставали к тебе ?"
        her "Нет, сэр. Они смотрели."
        m "Всего лишь смотрели ?"
        $herView.hideshowQQ( "body_52.png", pos )
        her "Они… Многие из них смотрели на меня с вожделением. Мне весь день было не по себе."
        her "Могу я уже переодеться в обычную одежду ?"
        m "Да, разумеется."

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $hermi.WrdSetMain()
        hide screen nsp_hermione_business
        show screen hermione_02
        $herView.hideshowQQ( "body_01.png", pos )
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")
            
        her "Надеюсь, что мне удалось помочь нашему общему делу."
        m "Не сомневайся."
        g9 "(Тебе определенно удалось помочь мне развеять скуку, маленькая шлюха.)"
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc
            
    elif cur_level == 2 :
        ">текст ивента маглов 1-2"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента маглов 1-3" 
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента маглов 1-4"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc
        
    elif cur_level == 5 :
        ">текст ивента маглов 1-5"
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_magls_2 :

    if cur_level == 1 :
        ">текст преивента маглов 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента маглов 2-2"
        
    elif cur_level == 3 :
        ">текст преивента маглов 2-3"
        
    elif cur_level == 4 :
        ">текст преивента маглов 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента маглов 2-5" 
        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маглах "
    $ nsp_genie_sphere_req = nsp_germiona_magls_2_photo
    
    if nsp_germiona_magls_2_statimg == "New" :
        $ cur_level = nsp_event_magls_2 + 1
    else :
        $ cur_level = nsp_event_magls_2

    if cur_level == 1 :
        ">текст ивента маглов 2-1"  
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc       

    elif cur_level == 2 :
        ">текст ивента маглов 2-2"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента маглов 2-3"   
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента маглов 2-4"            
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента маглов 2-5" 
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_magls_3 :

    if cur_level == 1 :
        ">текст преивента маглов 3-1"
    elif cur_level == 2 :
        ">текст преивента маглов 3-2"
    elif cur_level == 3 :
        ">текст преивента маглов 3-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 3-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 3-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маглах "
    $ nsp_genie_sphere_req = nsp_germiona_magls_3_photo
    
    if nsp_germiona_magls_3_statimg == "New" :
        $ cur_level = nsp_event_magls_3 + 1
    else :
        $ cur_level = nsp_event_magls_3

    if cur_level == 1 :
        ">текст ивента маглов 3-1"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента маглов 3-2"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc
        
    elif cur_level == 3 :
        ">текст ивента маглов 3-3" 
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_magls_3 = cur_level 
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc 
        
    elif cur_level == 4 :
        ">текст ивента маглов 3-4" 
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента маглов 3-5"  
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc
            

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_magls_4 :

    if cur_level == 1 :
        ">текст преивента маглов 4-1"
    elif cur_level == 2 :
        ">текст преивента маглов 4-2"
    elif cur_level == 3 :
        ">текст преивента маглов 4-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 4-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 4-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маглах "
    $ nsp_genie_sphere_req = nsp_germiona_magls_4_photo
    
    if nsp_germiona_magls_4_statimg == "New" :
        $ cur_level = nsp_event_magls_4 + 1
    else :
        $ cur_level = nsp_event_magls_4
        
    if cur_level == 1 :
        ">текст ивента маглов 4-1"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента маглов 4-2"
        
        if nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 55 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 55

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента маглов 4-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента маглов 4-4"  
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента маглов 4-5"  
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 150

        call nsp_bonus_calc
            

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_magls_5 :

    if cur_level == 1 :
        ">текст преивента маглов 5-1"
    elif cur_level == 2 :
        ">текст преивента маглов 5-2"
    elif cur_level == 3 :
        ">текст преивента маглов 5-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 5-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 5-5"   
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_5_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маглах "
    $ nsp_genie_sphere_req = nsp_germiona_magls_5_photo
    
    if nsp_germiona_magls_5_statimg == "New" :
        $ cur_level = nsp_event_magls_5 + 1
    else :
        $ cur_level = nsp_event_magls_5

    if cur_level == 1 :
        ">текст ивента маглов 5-1"  
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc

    elif cur_level == 2 :
        ">текст ивента маглов 5-2"  
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc

    elif cur_level == 3 :
        ">текст ивента маглов 5-3"   
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc
           
    elif cur_level == 4 :
        ">текст ивента маглов 5-4"   
        
        if nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc
           
    elif cur_level == 5 :
        ">текст ивента маглов 5-5"   
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 210

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

