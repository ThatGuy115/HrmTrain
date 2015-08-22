label nsp_theme_kviddich :

    $herView.hideshowQQ( "body_01.png", pos )
    m "Скажи мне, как девочки твоего возраста обычно относятся к квиддичу ?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "Сэр ?"
    m "У меня есть идеи на счет новых репортажей, но сначала ответь."
    her "Хм. Вообще-то по-разному. Некоторым он нравится меньше, но большинство без ума от игроков... То есть от игры."
    m "Отлично, а как к нему относишься ты сама ?"
    $herView.hideshowQQ( "body_09.png", pos )
    her "Ну, меня такие глупости совсем не интересуют. Эти игры совсем не то, чем должны интересоваться {size=+3}умные{/size} ученики"
    $herView.hideshowQQ( "body_24.png", pos )
    her "Подумаешь, грубые накачанные мужики показывают на поле свою силу и выносливость."
    ">Гермиона вдрогнула и вздохнула."
    m "Мужики ? Ты про своих однокурсников ?"
    $herView.hideshowQQ( "body_16.png", pos )
    her "Ну что вы, сэр. Если уж говорить о квиддиче, то о национальных командах и игроках."
    $herView.hideshowQQ( "body_54.png", pos )
    her "Пушки Педдл, тот же Крам... Крам, да. Ах."
    "Гермиона чаще задышала."
    m "(Не представляю о чем речь.)"
    m "Хорошо, а ты сама хотела бы как-то в этом участвовать ? "
    $herView.hideshowQQ( "body_02.png", pos )
    her "Я, сэр ? Не думаю. Вообще-то полеты на метле - единственный предмет, где меня с самого начала преследуют неудачи."
    her "Надеюсь, вы не предложите мне теперь стать болельщицей ?"
    m "(С каждой встречей она все лучше понимает ход моих мыслей, с этим надо что-то делать.)"
    g9 "На самом деле у меня совсем другие планы."
    $herView.hideshowQQ( "body_01.png", pos )
    
    return

label nsp_event_kviddich_1 :

    if cur_level == 1 :

        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_event_kviddich_1 == 0 :
    
            g9 "(Хорошо, что у меня под рукой уже есть комплект формы.)"
            m "Итак, девочка, ты не хочешь быть болельщицей ?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Нет, сэр. Я уже вам говорила. А почему вы спрашиваете ?"
            m "Простое любопытство. Ведь ты стремишься быть лучше всех во всем, а быть болельщицей, насколько я понимаю, престижно."
            $herView.hideshowQQ( "body_28.png", pos )
            her "Престижно ? При чем тут престижность ? Быть болельщицей, значит заявить, что ты тупая шл… , в смысле спортсменка."
            $herView.hideshowQQ( "body_16.png", pos )
            her "И ничего более. Простите, сэр."
            m "Все в порядке, продолжай."
            $herView.hideshowQQ( "body_04.png", pos )
            her "Сэр, эти болельщицы постоянно флиртуют и вертят парнями. А может быть и учителями."
            her "Именно они чаще всего добывают баллы нечестным путем."
            her "А еще, у них что-то вроде закрытого клуба, куда не берут посторонних."
            m "Вот как. Ну что же, я рад, что наши наблюдения совпадают."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Сэр, не стоит их защи… Совпадают ?"
            m "Да, и более того, мне кажется, что давно пора расследовать их деятельность."
            m "Правда как директор я не должен вмешиваться напрямую."
            m "А вот в качестве редактора газеты..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "Вы сделаете это, сэр ?"
            her "Вы покажете всем, что накачанные попы и оголенные животы - это ничто по сравнению со знаниями и высокими оценками ?"
            m "Кто, я ? То есть да, именно так."
            m "Но тебе придется внедриться к ним, а сначала - потренироваться."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Но сэр, какой в этом смысл ? Ведь они не возьмут постороннюю девчонку, тем более у них пока есть полный состав."
            her "К тому же, меня. Они уже знают о моем отношении."
            m "Да, но подумай на один шаг вперед."
            m "Предположим, в клубе болельщиц появится вакансия. Кого они возьмут ?"
            m "Ученицу, которая уже много тренировалась или полного новичка ?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Я поняла, сэр."
            her "Да, вы правы, как всегда."
            g9 "Приходи вечером, я помогу тебе изучить основы."
            $herView.hideshowQQ( "body_17.png", pos )
            her "У меня нет формы болельщицы, профессор."
            her "(Похоже это не станет проблемой.)"
            m "Это не станет проблемой."
            $herView.hideshowQQ( "body_16.png", pos )
            her "(Ну что я говорила.)"

        else :
        
            m "Предлагаю продолжить твою тренировку болельщицы вечером."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Сэр, я по-прежнему не уверена, что это хорошая идея."
            g9 "Я гарантирую, в конце ты признаешь, что все это было не зря."
            $herView.hideshowQQ( "body_15.png", pos )
            her "Как скажете, сэр."
            
        $herView.hideshowQQ( "body_01.png", pos )
        
    elif cur_level == 2 :
        ">текст преивента квиддича 1-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 1-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 1-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 1-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_req = nsp_germiona_kviddich_1_photo
    
    if nsp_germiona_kviddich_1_statimg == "New" :
        $ cur_level = nsp_event_kviddich_1 + 1
    else :
        $ cur_level = nsp_event_kviddich_1

    if cur_level == 1 :
    
        show screen hermione_02
        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_event_kviddich_1 == 0 :
            her "Здравствуйте, сэр. Я буду тренироваться здесь ?"
            m "Да. Вот твой костюм."
        else :
            her "Добрый вечер, сэр."
            m "Привет. Вот твой костюм."
        
        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        #call wrd_dress_undress
        #$ herView.data().addItem ("item_tits_no")
        #$ herView.data().addItemSet( 'hermione_cheerleader_gryffindor' )
        
        $hermi.WrdDress ("skirt_cheerleader")
        $hermi.WrdDress ("shirt_cheerleader")
        $hermi.WrdNoStockings()
        $hermi.WrdNoOther()
               
        hide screen hermione_02
        show screen nsp_hermione_cheerleader_gryffindor
        $hermi.WrdMain()
        $herView.hideshowQQ( "body_03.png", pos )
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")
            
        her "Я готова, сэр."
        $herView.hideshowQQ( "body_13.png", pos )
        her "Никак не могу сообразить, откуда у вас взялся костюм для меня."
        g9 "(Лучше спроси об этом Дамблдора. Хотелось бы увидеть его лицо…)"
        her "Что ?"
        m "Я говорю, лучше спросить об этом попозже. Скажем, через пару месяцев."
        m "А сейчас, приступим. Тебе нужно исполнить танец болельщицы."
        m "Попробуй танцевать так, как ты сама это представляешь."
        $herView.hideshowQQ( "body_15.png", pos )
        her "Я попробую, профессор."
        
        show screen ctc
        pause
        ">Гермиона танцует очень скованно, словно делает это впервые."
        hide screen nsp_hermione_cheerleader_gryffindor
        show screen nsp_hermione_cheerleader_gryffindor_dance1
        with d3
        pause
        
        m "Мда, хотел бы я сказать, что у тебя неплохо получается, но это не соответствует роли жесткого тренера."
        $herView.hideshowQQ( "body_13.png", pos )
        her "Жесткого тренера ?"
        g4 "Да, девочка. {size=+4}Выше колени !{/size}"
        
        ">Гермиона начинает прыгать активнее, ее юбку подбрасывает при каждом движении. Лицо краснеет."
        $herView.hideshowQQ( "body_94.png", pos )
        hide screen nsp_hermione_cheerleader_gryffindor_dance1
        show screen nsp_hermione_cheerleader_gryffindor_dance2
        with d3
        pause
        
        her "Уфф… Уфф..."
        g9 "Отлично, так гораздо лучше."
        $herView.hideshowQQ( "body_94.png", pos )
        her "Уфф…. Правда… Уфф…. Сэр ?"
        g4 "Да. То есть {size=+4}отставить разговоры ! Выпячивай грудь между прыжками ! {/size}"
        g4 "{size=+4}Еще сильнее ! Да, вот так. И верти задом так, как будто хочешь им стереть с доски свою ошибку в домашнем задании ! {/size}"
        $herView.hideshowQQ( "body_97.png", pos )
        her "Ох, сэр. Уфф… Я больше не могу."
        g4 "Еще 20 секунд."
        $herView.hideshowQQ( "body_98.png", pos )
        her "Уфф… Уфф… Ах..."
        m "Хорошо. Можешь расслабиться. Ты теперь на один шаг ближе к цели."
        $herView.hideshowQQ( "body_90.png", pos )
        her "Ох… Да, сэр."

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $hermi.WrdSetMain()
        hide screen nsp_hermione_cheerleader_gryffindor_dance2
        show screen hermione_02
        $herView.hideshowQQ( "body_33.png", pos )
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")
        
        her "Пойду под душ, профессор."
        g9 "Я бы не отказался тебя проводить, но дела... "
        $herView.hideshowQQ( "body_45.png", pos )
        her "Пожалуйста, держите себя в руках, сэр !"

        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc
            
    elif cur_level == 2 :
        ">текст ивента квиддича 1-2"
        
        if nsp_germiona_mediawhoring < 25 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 35 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 35

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента квиддича 1-3" 
        
        if nsp_germiona_mediawhoring < 35 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 45

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента квиддича 1-4"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
        
    elif cur_level == 5 :
        ">текст ивента квиддича 1-5"
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_kviddich_2 :

    if cur_level == 1 :
        ">текст преивента квиддича 2-1" 
        
        m "Гермиона, соревнование между школами и их газетами привело к определенным последствиям."
        her "Плохим последствиям, сэр ?"
        m "Хороший вопрос. Дело в том, что теперь все школьные команды по квиддичу будут в центре внимания."
        m "Возможно в будущем состоятся межшкольные игры. А пока что от нас требуется освещение состояния команд в прессе."
        m "Ты в курсе, как обстоят дела "

        
        
    elif cur_level == 2 :
        ">текст преивента квиддича 2-2"
        
    elif cur_level == 3 :
        ">текст преивента квиддича 2-3"
        
    elif cur_level == 4 :
        ">текст преивента квиддича 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента квиддича 2-5" 
        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_req = nsp_germiona_kviddich_2_photo
    
    if nsp_germiona_kviddich_2_statimg == "New" :
        $ cur_level = nsp_event_kviddich_2 + 1
    else :
        $ cur_level = nsp_event_kviddich_2

    if cur_level == 1 :
        ">текст ивента квиддича 2-1"  
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc       

    elif cur_level == 2 :
        ">текст ивента квиддича 2-2"
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента квиддича 2-3"   
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента квиддича 2-4"            
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента квиддича 2-5" 
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_kviddich_3 :

    if cur_level == 1 :
        ">текст преивента квиддича 3-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 3-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 3-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 3-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 3-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_req = nsp_germiona_kviddich_3_photo
    
    if nsp_germiona_kviddich_3_statimg == "New" :
        $ cur_level = nsp_event_kviddich_3 + 1
    else :
        $ cur_level = nsp_event_kviddich_3

    if cur_level == 1 :
        ">текст ивента квиддича 3-1"
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента квиддича 3-2"
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
        
    elif cur_level == 3 :
        ">текст ивента квиддича 3-3" 
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_kviddich_3 = cur_level 
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc
        
        $ hermi.liking -= 2
        
    elif cur_level == 4 :
        ">текст ивента квиддича 3-4" 
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc
        
        $ hermi.liking -= 3
            
    elif cur_level == 5 :
        ">текст ивента квиддича 3-5"  
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 210

        call nsp_bonus_calc
            

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_kviddich_4 :

    if cur_level == 1 :
        ">текст преивента квиддича 4-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 4-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 4-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 4-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 4-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_req = nsp_germiona_kviddich_4_photo
    
    if nsp_germiona_kviddich_4_statimg == "New" :
        $ cur_level = nsp_event_kviddich_4 + 1
    else :
        $ cur_level = nsp_event_kviddich_4
        
    if cur_level == 1 :
        ">текст ивента квиддича 4-1"
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента квиддича 4-2"
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента квиддича 4-3" 
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента квиддича 4-4"  
        
        if nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 190

        call nsp_bonus_calc
        
        $ hermi.liking -= 4
            
    elif cur_level == 5 :
        ">текст ивента квиддича 4-5"  
        
        if nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 180 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
        
        $ hermi.liking -= 6
            

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_kviddich_5 :

    if cur_level == 1 :
        ">текст преивента квиддича 5-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 5-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 5-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 5-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 5-5"   
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_5_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_req = nsp_germiona_kviddich_5_photo
    
    if nsp_germiona_kviddich_5_statimg == "New" :
        $ cur_level = nsp_event_kviddich_5 + 1
    else :
        $ cur_level = nsp_event_kviddich_5

    if cur_level == 1 :
        ">текст ивента квиддича 5-1"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    elif cur_level == 2 :
        ">текст ивента квиддича 5-2"  
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 3 :
        ">текст ивента квиддича 5-3"   
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
        
        $ hermi.liking -= 2
           
    elif cur_level == 4 :
        ">текст ивента квиддича 5-4"   
        
        if nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 180

        call nsp_bonus_calc
        
        $ hermi.liking -= 4
           
    elif cur_level == 5 :
        ">текст ивента квиддича 5-5"   
        
        if nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 180 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
        
        $ hermi.liking -= 6
        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_kviddich_6 :

    if cur_level == 1 :
        ">текст преивента квиддича 6-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 6-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 6-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 6-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 6-5"   
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_6_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_req = nsp_germiona_kviddich_6_photo
    
    if nsp_germiona_kviddich_6_statimg == "New" :
        $ cur_level = nsp_event_kviddich_6 + 1
    else :
        $ cur_level = nsp_event_kviddich_6

    if cur_level == 1 :
        ">текст ивента квиддича 6-1"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 2 :
        ">текст ивента квиддича 6-2"  
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    elif cur_level == 3 :
        ">текст ивента квиддича 6-3"   
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 180

        call nsp_bonus_calc
           
    elif cur_level == 4 :
        ">текст ивента квиддича 6-4"   
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 70 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
           
    elif cur_level == 5 :
        ">текст ивента квиддича 6-5"   
        
        if nsp_germiona_mediawhoring < 190 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 200 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 80 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 260

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return
