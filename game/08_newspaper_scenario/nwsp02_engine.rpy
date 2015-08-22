################
### Основные обработчики ###                
################

label newsp_letter:

    $ letter_text = "{size=-7}От: Министерства Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой профессор Дамблдор.\n\nМы хотим сообщить Вам, что Комитет по Прессе изучил реакцию ваших читателей в школе и постановил следующее:\n\nВ соответствии с популярностью последнего выпуска газеты выплатить редакции [nsp_newspaper_cur_money] галлеонов.\n\n Спасибо за сотрудничество !\n\n{size=-3}С уважением,\nМинистерство Магии.{/size}"        
    
    hide screen points
    $ gold += nsp_newspaper_cur_money
    show screen points
    
    $ letters -= 1
    if letters <= 0 :
        $screens.Hide("owl").Show("owl_02")
    
    show screen bld1
    show screen letter
    show screen ctc
    pause
    hide screen letter
    hide screen bld1
    hide screen ctc
    
    $ nsp_newspaper_published = False
    $ nsp_newspaper_published_mail = False
    $ nsp_newspaper_last_money = nsp_newspaper_cur_money
    
    if (hermi._incomePercent>0):
        $nsp_newspaper_cur_money=nsp_newspaper_cur_money*hermi._incomePercent//100
        hide screen points
        $gold-=nsp_newspaper_cur_money
        show screen points
        "> Согласно вашему соглашению с Гермионой [dgold] галеонов ([hermi._incomePercent]%%) перечисляются на ее счет"
    
    if nsp_newspaper_menu == 2:
        $hero(m,"{size=+1}АРГХ ! Тысяча песчаных змей и один питон!..{/size}")
        $hero("{size=+1}Проклятые разработчики модов ! Да вы издеваетесь !{/size}")
        dev "Одну минутку..."
        $hero("{size=+1}Столько стараний ради [nsp_newspaper_cur_money] галлеонов ? Сейчас здесь будет убийство !{/size}")
        dev "Да погоди, не кипятись. Дело в том, что..."
        $hero("{size=-1}Да пошел ты ! Больше никаких модов, только классика !{/size}")
        dev "О не-е-е-е-е-е-ет... Джинни, я обещаю, что ты не зря учился газетному делу ! Спроси Снейпа, и он подскажет, как заработать больше !"
        $hero("{size=-4}Хммм. Ладно, только ради тебя, дам моду еще один шанс.{/size}")
        $ nsp_newspaper_menu = 3
   
    call screen main_menu_01

label nsp_newsp_themes:
 
    $ nsp_germiona_statimg_rights = "Block" # Гермиона: Доступность раздела "Права и дискриминация"
    $ nsp_germiona_statimg_magls = "Block" # Гермиона: Доступность раздела "О жизни маглов публично"
    $ nsp_germiona_statimg_kviddich = "Block"  # Гермиона: Доступность раздела "О квиддиче"
    $ nsp_germiona_statimg_sex = "Block"  # Гермиона: Доступность раздела "О Сексе"
    $ nsp_germiona_statimg_maniac = "Block"  # Гермиона: Доступность раздела "Маньяк"
    $ nsp_germiona_statimg_nude = "Block"  # Гермиона: Доступность раздела "Голый репортер в маске"
    $ nsp_germiona_statimg_forest = "Block"  # Гермиона: Доступность раздела "Запретный лес"
    $ nsp_germiona_statimg_studio = "Block"  # Гермиона: Доступность раздела "Студия у Джина"
    
    $ nsp_germiona_rights_1_statimg = "Block"
    $ nsp_germiona_rights_2_statimg = "Block"
    $ nsp_germiona_rights_3_statimg = "Block"
    $ nsp_germiona_rights_4_statimg = "Block"
    $ nsp_germiona_rights_5_statimg = "Block"
    
    $ nsp_germiona_magls_1_statimg = "Block"
    $ nsp_germiona_magls_2_statimg = "Block"
    $ nsp_germiona_magls_3_statimg = "Block"
    $ nsp_germiona_magls_4_statimg = "Block"
    $ nsp_germiona_magls_5_statimg = "Block"
    
    $ nsp_germiona_kviddich_1_statimg = "Block"
    $ nsp_germiona_kviddich_2_statimg = "Block"
    $ nsp_germiona_kviddich_3_statimg = "Block"
    $ nsp_germiona_kviddich_4_statimg = "Block"
    $ nsp_germiona_kviddich_5_statimg = "Block"
    $ nsp_germiona_kviddich_6_statimg = "Block"
    
    $ nsp_germiona_sex_1_statimg = "Block"
    $ nsp_germiona_sex_2_statimg = "Block"
    $ nsp_germiona_sex_3_statimg = "Block"
    $ nsp_germiona_sex_4_statimg = "Block"
    $ nsp_germiona_sex_5_statimg = "Block"
    
    $ nsp_germiona_maniac_1_statimg = "Block"
    $ nsp_germiona_maniac_2_statimg = "Block"
    $ nsp_germiona_maniac_3_statimg = "Block"
    
    $ nsp_germiona_nude_1_statimg = "Block"
    $ nsp_germiona_nude_2_statimg = "Block"
    $ nsp_germiona_nude_3_statimg = "Block"
    $ nsp_germiona_nude_4_statimg = "Block"
    $ nsp_germiona_nude_5_statimg = "Block"
    
    $ nsp_germiona_forest_1_statimg = "Block"
    $ nsp_germiona_forest_2_statimg = "Block"
    
    $ nsp_germiona_studio_1_statimg = "Block"
    $ nsp_germiona_studio_2_statimg = "Block"
    $ nsp_germiona_studio_3_statimg = "Block"
    $ nsp_germiona_studio_4_statimg = "Block"
    $ nsp_germiona_studio_5_statimg = "Block"
    $ nsp_germiona_studio_6_statimg = "Block"
    
    $ nsp_germiona_rights_1_photo = "dis"
    $ nsp_germiona_rights_2_photo = "dis"
    $ nsp_germiona_rights_3_photo = "dis"
    $ nsp_germiona_rights_4_photo = "dis"
    $ nsp_germiona_rights_5_photo = "dis"
    
    $ nsp_germiona_magls_1_photo = "dis"
    $ nsp_germiona_magls_2_photo = "dis"
    $ nsp_germiona_magls_3_photo = "dis"
    $ nsp_germiona_magls_4_photo = "dis"
    $ nsp_germiona_magls_5_photo = "dis"
    
    $ nsp_germiona_kviddich_1_photo = "dis"
    $ nsp_germiona_kviddich_2_photo = "dis"
    $ nsp_germiona_kviddich_3_photo = "dis"
    $ nsp_germiona_kviddich_4_photo = "dis"
    $ nsp_germiona_kviddich_5_photo = "dis"
    $ nsp_germiona_kviddich_6_photo = "dis"
    
    $ nsp_germiona_sex_1_photo = "dis"
    $ nsp_germiona_sex_2_photo = "dis"
    $ nsp_germiona_sex_3_photo = "dis"
    $ nsp_germiona_sex_4_photo = "dis"
    $ nsp_germiona_sex_5_photo = "dis"
    
    $ nsp_germiona_maniac_1_photo = "dis"
    $ nsp_germiona_maniac_2_photo = "dis"
    $ nsp_germiona_maniac_3_photo = "dis"
    
    $ nsp_germiona_nude_1_photo = "dis"
    $ nsp_germiona_nude_2_photo = "dis"
    $ nsp_germiona_nude_3_photo = "dis"
    $ nsp_germiona_nude_4_photo = "dis"
    $ nsp_germiona_nude_5_photo = "dis"
    
    $ nsp_germiona_forest_1_photo = "dis"
    $ nsp_germiona_forest_2_photo = "dis"
    
    $ nsp_germiona_studio_1_photo = "en"
    $ nsp_germiona_studio_2_photo = "en"
    $ nsp_germiona_studio_3_photo = "en"
    $ nsp_germiona_studio_4_photo = "en"
    $ nsp_germiona_studio_5_photo = "en"
    $ nsp_germiona_studio_6_photo = "en"
    
    $ cur_level = 0
    
    if nsp_germiona_menu_rights > 0:
        call nsp_init_flags_rights
    if nsp_germiona_menu_magls > 0:
        call nsp_init_flags_magls
    if nsp_germiona_menu_kviddich > 0:
        call nsp_init_flags_kviddich
    if nsp_germiona_menu_sex > 0:
        call nsp_init_flags_sex
    if nsp_germiona_menu_maniac > 0:
        call nsp_init_flags_maniac
    if nsp_germiona_menu_nude > 0:
        call nsp_init_flags_nude
    if nsp_germiona_menu_forest > 0:
        call nsp_init_flags_forest
    if nsp_germiona_menu_studio > 0:
        call nsp_init_flags_studio
    
    if nsp_germiona_menu_rights == 1:
        $ nsp_germiona_statimg_rights = "New"
    if nsp_germiona_menu_magls == 1:
        $ nsp_germiona_statimg_magls = "New"
    if nsp_germiona_menu_kviddich == 1:
        $ nsp_germiona_statimg_kviddich = "New"
    if nsp_germiona_menu_sex == 1:
        $ nsp_germiona_statimg_sex = "New"
    if nsp_germiona_menu_maniac == 1:
        $ nsp_germiona_statimg_maniac = "New"
    if nsp_germiona_menu_nude == 1:
        $ nsp_germiona_statimg_nude = "New"
    if nsp_germiona_menu_forest == 1:
        $ nsp_germiona_statimg_forest = "New"
    if nsp_germiona_menu_studio == 1:
        $ nsp_germiona_statimg_studio = "New"  
        
    call nsp_init_flag_photo
    
    menu:
    
        "- О правах и дискриминации {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_rights].png} -" if nsp_newspaper_menu >= 6:
    
            if nsp_germiona_menu_rights == 1 :
                call nsp_theme_rights
                $ nsp_germiona_menu_rights = 2
        
            if nsp_germiona_menu_rights == 2 :
                menu:
                    "- Сексуальные домогательства учеников -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_rights_1_photo].png}" :
                        if nsp_germiona_rights_1_statimg == "New" :
                            $ cur_level = nsp_event_rights_1 + 1
                            if cur_level == 2 :
                                jump nsp_her_demo
                            jump nsp_event_rights_1
                        elif nsp_germiona_rights_1_statimg == "Explored" or nsp_germiona_rights_1_statimg == "Full":
                            $ cur_level = nsp_event_rights_1
                            jump nsp_event_rights_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
# DR'S PUB DISABLE        
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 1 and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Сексуальные домогательства учителей -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_rights_2_photo].png}" if nsp_genie_writer >= 1 and False :
                        if nsp_germiona_rights_2_statimg == "New" :
                            $ cur_level = nsp_event_rights_2 + 1
                            jump nsp_event_rights_2
                        elif nsp_germiona_rights_2_statimg == "Explored" or nsp_germiona_rights_2_statimg == "Full":
                            $ cur_level = nsp_event_rights_2
                            jump nsp_event_rights_2                       
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if (nsp_genie_writer < 4 or (nsp_letter_7 < 3 and nsp_event_rights_3 == 0)) and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Интервью с защитницей прав женщин -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_rights_3_photo].png}" if nsp_genie_writer >= 4 and (nsp_letter_7 ==3 or nsp_event_rights_3 > 0)  and False:
                        if nsp_germiona_rights_3_statimg == "New" :
                            $ cur_level = nsp_event_rights_3 + 1
                            jump nsp_event_rights_3
                        elif nsp_germiona_rights_3_statimg == "Explored" or nsp_germiona_rights_3_statimg == "Full":
                            $ cur_level = nsp_event_rights_3
                            jump nsp_event_rights_3
                        elif nsp_germiona_rights_3_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_rights_3_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 8 and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Заседание ООП с демонстрацией для девочек -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_4_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_rights_4_photo].png}" if nsp_genie_writer >= 8  and False:
                        if nsp_germiona_rights_4_statimg == "New" :
                            $ cur_level = nsp_event_rights_4 + 1
                            jump nsp_event_rights_4
                        elif nsp_germiona_rights_4_statimg == "Explored" or nsp_germiona_rights_4_statimg == "Full":
                            $ cur_level = nsp_event_rights_4
                            jump nsp_event_rights_4                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if (nsp_genie_writer < 10 or (nsp_event_rights_4 < 3)) and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Заседание ООП с демонстрацией для смешанной группы -\n{image=08_newspaper_scenario/hearts/heart_7[nsp_event_rights_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_5_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_rights_5_photo].png}" if nsp_genie_writer >= 10 and (nsp_event_rights_4 >= 3)  and False:
                        if nsp_germiona_rights_5_statimg == "New" :
                            $ cur_level = nsp_event_rights_5 + 1
                            jump nsp_event_rights_5
                        elif nsp_germiona_rights_5_statimg == "Explored" or nsp_germiona_rights_5_statimg == "Full":
                            $ cur_level = nsp_event_rights_5
                            jump nsp_event_rights_5                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes

        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and nsp_genie_writer < 2:
            jump nsp_newsp_themes
                        
        "- О жизни маглов {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_magls].png} -" if nsp_newspaper_menu >= 6 and nsp_genie_writer >= 2 :
    
            if nsp_germiona_menu_magls == 1 :
                call nsp_theme_magls
                $ nsp_germiona_menu_magls = 2
                
            if nsp_germiona_menu_magls == 2 :
                menu:
                    "- Откровенная одежда маглов -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_magls_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_magls_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_magls_1_photo].png}" :
                        if nsp_germiona_magls_1_statimg == "New" :
                            $ cur_level = nsp_event_magls_1 + 1
                            if cur_level == 1 and wrd_rent_business == 0 and ( not hermi.Items.Any("tights") or not hermi.Items.Any("skirt_business") or not hermi.Items.Any("shirt_business") ) :
                                ">Для данного задания понадобятся юбка и рубашка бизнес-леди, колготки. Как вариант, можно воспользоваться прокатом."
                                jump nsp_newsp_themes
                            if cur_level == 2 :
                                jump nsp_her_demo
                            jump nsp_event_magls_1
                        elif nsp_germiona_magls_1_statimg == "Explored" or nsp_germiona_magls_1_statimg == "Full":
                            $ cur_level = nsp_event_magls_1
                            if cur_level == 1 and wrd_rent_business == 0 and ( not hermi.Items.Any("tights") or not hermi.Items.Any("skirt_business") or not hermi.Items.Any("shirt_business") ) :
                                ">Для данного задания понадобятся юбка и рубашка бизнес-леди, колготки. Как вариант, можно воспользоваться прокатом."
                                jump nsp_newsp_themes
                            jump nsp_event_magls_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 4 and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Сауна маглов -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_magls_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_magls_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_magls_2_photo].png}" if nsp_genie_writer >= 4  and False:
                        if nsp_germiona_magls_2_statimg == "New" :
                            $ cur_level = nsp_event_magls_2 + 1
                            jump nsp_event_magls_2
                        elif nsp_germiona_magls_2_statimg == "Explored" or nsp_germiona_magls_2_statimg == "Full":
                            $ cur_level = nsp_event_magls_2
                            jump nsp_event_magls_2                       
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 6  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Пляж маглов -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_magls_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_magls_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_magls_3_photo].png}" if nsp_genie_writer >= 6  and False:
                        if nsp_germiona_magls_3_statimg == "New" :
                            $ cur_level = nsp_event_magls_3 + 1
                            jump nsp_event_magls_3
                        elif nsp_germiona_magls_3_statimg == "Explored" or nsp_germiona_magls_3_statimg == "Full":
                            $ cur_level = nsp_event_magls_3
                            jump nsp_event_magls_3
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 8 and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Фотостудия маглов -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_magls_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_magls_4_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_magls_4_photo].png}" if nsp_genie_writer >= 8  and False:
                        if nsp_germiona_magls_4_statimg == "New" :
                            $ cur_level = nsp_event_magls_4 + 1
                            jump nsp_event_magls_4
                        elif nsp_germiona_magls_4_statimg == "Explored" or nsp_germiona_magls_4_statimg == "Full":
                            $ cur_level = nsp_event_magls_4
                            jump nsp_event_magls_4                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 10  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Медобследование по-магловски -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_magls_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_magls_5_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_magls_5_photo].png}" if nsp_genie_writer >= 10  and False:
                        if nsp_germiona_magls_5_statimg == "New" :
                            $ cur_level = nsp_event_magls_5 + 1
                            jump nsp_event_magls_5
                        elif nsp_germiona_magls_5_statimg == "Explored" or nsp_germiona_magls_5_statimg == "Full":
                            $ cur_level = nsp_event_magls_5
                            jump nsp_event_magls_5
                        elif nsp_germiona_magls_5_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_magls_5_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes
        
        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and nsp_genie_writer < 4 :
            jump nsp_newsp_themes
            
        "- О квиддиче {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_kviddich].png} -" if nsp_newspaper_menu >= 6 and nsp_genie_writer >= 4 :
    
            if nsp_germiona_menu_kviddich == 1 :
                call nsp_theme_kviddich
                $ nsp_germiona_menu_kviddich = 2
                
            if nsp_germiona_menu_kviddich == 2 :
                menu:
                    "- Тренировка болельщицы -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_kviddich_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_kviddich_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_kviddich_1_photo].png}" :
                        if nsp_germiona_kviddich_1_statimg == "New" :
                            $ cur_level = nsp_event_kviddich_1 + 1
                            $ cur_level = nsp_event_magls_1 + 1
                            if cur_level == 1 and wrd_rent_cheerleader == 0 and ( not hermi.Items.Any("skirt_cheerleader") or not hermi.Items.Any("shirt_cheerleader") ) :
                                ">Для данного задания понадобятся юбка и кофта болельщицы Гриффиндора. Как вариант, можно воспользоваться прокатом."
                                jump nsp_newsp_themes
                            if cur_level == 2 :
                                jump nsp_her_demo
                            jump nsp_event_kviddich_1
                        elif nsp_germiona_kviddich_1_statimg == "Explored" or nsp_germiona_kviddich_1_statimg == "Full":
                            $ cur_level = nsp_event_kviddich_1
                            if cur_level == 1 and wrd_rent_cheerleader == 0 and ( not hermi.Items.Any("wrd_skirt_cheerleader") or not hermi.Items.Any("wrd_shirt_cheerleader") ) :
                                ">Для данного задания понадобятся юбка и кофта болельщицы Гриффиндора. Как вариант, можно воспользоваться прокатом."
                                jump nsp_newsp_themes
                            jump nsp_event_kviddich_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 4 and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Помощь команде Гриффиндора -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_kviddich_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_kviddich_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_kviddich_2_photo].png}" if nsp_genie_writer >= 4  and False:
                        if nsp_germiona_kviddich_2_statimg == "New" :
                            $ cur_level = nsp_event_kviddich_2 + 1
                            jump nsp_event_kviddich_2
                        elif nsp_germiona_kviddich_2_statimg == "Explored" or nsp_germiona_kviddich_2_statimg == "Full":
                            $ cur_level = nsp_event_kviddich_2
                            jump nsp_event_kviddich_2
                        elif nsp_germiona_kviddich_2_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_kviddich_2_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                       
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 6  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Диверсия для команды Слизерина -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_kviddich_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_kviddich_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_kviddich_3_photo].png}" if nsp_genie_writer >= 6  and False:
                        if nsp_germiona_kviddich_3_statimg == "New" :
                            $ cur_level = nsp_event_kviddich_3 + 1
                            jump nsp_event_kviddich_3
                        elif nsp_germiona_kviddich_3_statimg == "Explored" or nsp_germiona_kviddich_3_statimg == "Full":
                            $ cur_level = nsp_event_kviddich_3
                            jump nsp_event_kviddich_3
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 8 and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Бег на стадионе без одежды -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_kviddich_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_kviddich_4_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_kviddich_4_photo].png}" if nsp_genie_writer >= 8  and False:
                        if nsp_germiona_kviddich_4_statimg == "New" :
                            $ cur_level = nsp_event_kviddich_4 + 1
                            jump nsp_event_kviddich_4
                        elif nsp_germiona_kviddich_4_statimg == "Explored" or nsp_germiona_kviddich_4_statimg == "Full":
                            $ cur_level = nsp_event_kviddich_4
                            jump nsp_event_kviddich_4
                        elif nsp_germiona_kviddich_4_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_kviddich_4_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 10  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Полет без одежды -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_kviddich_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_kviddich_5_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_kviddich_5_photo].png}" if nsp_genie_writer >= 10  and False:
                        if nsp_germiona_kviddich_5_statimg == "New" :
                            $ cur_level = nsp_event_kviddich_5 + 1
                            jump nsp_event_kviddich_5
                        elif nsp_germiona_kviddich_5_statimg == "Explored" or nsp_germiona_kviddich_5_statimg == "Full":
                            $ cur_level = nsp_event_kviddich_5
                            jump nsp_event_kviddich_5
                        elif nsp_germiona_kviddich_5_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_kviddich_5_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                            
                    "{color=#858585}-Не открытое действие-{/color}" if (nsp_genie_writer < 10 or nsp_event_kviddich_2 < 5 or nsp_event_kviddich_5 < 5)  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Игра в команде Гриффиндора -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_kviddich_6].png} {image=08_newspaper_scenario/flags/[nsp_germiona_kviddich_6_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_kviddich_6_photo].png}" if nsp_genie_writer >= 10 and nsp_event_kviddich_2 >= 5 and nsp_event_kviddich_5 >= 5  and False:
                        if nsp_germiona_kviddich_6_statimg == "New" :
                            $ cur_level = nsp_event_kviddich_6 + 1
                            jump nsp_event_kviddich_6
                        elif nsp_germiona_kviddich_6_statimg == "Explored" or nsp_germiona_kviddich_6_statimg == "Full":
                            $ cur_level = nsp_event_kviddich_6
                            jump nsp_event_kviddich_6
                        elif nsp_germiona_kviddich_6_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_kviddich_6_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes

        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and nsp_genie_writer < 1  and False:
            jump nsp_newsp_themes
            
        "- О сексе {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_sex].png} -" if nsp_newspaper_menu >= 6 and nsp_genie_writer >= 1  and False:
    
            if nsp_germiona_menu_sex == 1 :
                call nsp_theme_sex
                $ nsp_germiona_menu_sex = 2
        
            if nsp_germiona_menu_sex == 2 :
                menu:
                    "- Без трусов -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_sex_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_sex_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_sex_1_photo].png}" :
                        if nsp_germiona_sex_1_statimg == "New" :
                            $ cur_level = nsp_event_sex_1 + 1
                            jump nsp_event_sex_1
                        elif nsp_germiona_sex_1_statimg == "Explored" or nsp_germiona_sex_1_statimg == "Full":
                            $ cur_level = nsp_event_sex_1
                            jump nsp_event_sex_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 4:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Дилдо в вагине -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_sex_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_sex_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_sex_2_photo].png}" if nsp_genie_writer >= 4 :
                        if nsp_germiona_sex_2_statimg == "New" :
                            $ cur_level = nsp_event_sex_2 + 1
                            jump nsp_event_sex_2
                        elif nsp_germiona_sex_2_statimg == "Explored" or nsp_germiona_sex_2_statimg == "Full":
                            $ cur_level = nsp_event_sex_2
                            jump nsp_event_sex_2                       
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 5 :
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Дилдо в попе -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_sex_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_sex_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_sex_3_photo].png}" if nsp_genie_writer >= 5 :
                        if nsp_germiona_sex_3_statimg == "New" :
                            $ cur_level = nsp_event_sex_3 + 1
                            jump nsp_event_sex_3
                        elif nsp_germiona_sex_3_statimg == "Explored" or nsp_germiona_sex_3_statimg == "Full":
                            $ cur_level = nsp_event_sex_3
                            jump nsp_event_sex_3
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes    

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 6:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- День вибратора -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_sex_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_sex_4_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_sex_4_photo].png}" if nsp_genie_writer >= 6 :
                        if nsp_germiona_sex_4_statimg == "New" :
                            $ cur_level = nsp_event_sex_4 + 1
                            jump nsp_event_sex_4
                        elif nsp_germiona_sex_4_statimg == "Explored" or nsp_germiona_sex_4_statimg == "Full":
                            $ cur_level = nsp_event_sex_4
                            jump nsp_event_sex_4                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 9 :
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Афродизиак -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_sex_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_sex_5_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_sex_5_photo].png}" if nsp_genie_writer >= 9 :
                        if nsp_germiona_sex_5_statimg == "New" :
                            $ cur_level = nsp_event_sex_5 + 1
                            jump nsp_event_sex_5
                        elif nsp_germiona_sex_5_statimg == "Explored" or nsp_germiona_sex_5_statimg == "Full":
                            $ cur_level = nsp_event_sex_5
                            jump nsp_event_sex_5                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes
                
        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and (nsp_letter_2 < 2 or nsp_genie_writer < 6)  and False:
            jump nsp_newsp_themes
            
        "- Маньяк {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_maniac].png} -" if nsp_newspaper_menu >= 6 and nsp_letter_2 >= 2 and nsp_genie_writer >= 6  and False:
    
            if nsp_germiona_menu_maniac == 1 :
                call nsp_theme_maniac
                $ nsp_germiona_menu_maniac = 2
                
            if nsp_germiona_menu_maniac == 2 :
                menu:
                    "- Выслеживание маньяка -\n{image=08_newspaper_scenario/hearts/heart_4[nsp_event_maniac_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_maniac_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_maniac_1_photo].png}" :
                        if nsp_germiona_maniac_1_statimg == "New" :
                            $ cur_level = nsp_event_maniac_1 + 1
                            jump nsp_event_maniac_1
                        elif nsp_germiona_maniac_1_statimg == "Explored" or nsp_germiona_maniac_1_statimg == "Full":
                            $ cur_level = nsp_event_maniac_1
                            jump nsp_event_maniac_1
                        elif nsp_germiona_maniac_1_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_maniac_1_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes 
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 6 or nsp_event_maniac_1 < 4:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Интервью с маньяком -\n{image=08_newspaper_scenario/hearts/heart_4[nsp_event_maniac_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_maniac_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_maniac_2_photo].png}" if nsp_genie_writer >= 6 and nsp_event_maniac_1 >= 4 :
                        if nsp_germiona_maniac_2_statimg == "New" :
                            $ cur_level = nsp_event_maniac_2 + 1
                            jump nsp_event_maniac_2
                        elif nsp_germiona_maniac_2_statimg == "Explored" or nsp_germiona_maniac_2_statimg == "Full":
                            $ cur_level = nsp_event_maniac_2
                            jump nsp_event_maniac_2  
                        elif nsp_germiona_maniac_2_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_maniac_2_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                             
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 6 or nsp_event_maniac_2 < 4 :
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Ловля маньяка на живца -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_maniac_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_maniac_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_maniac_3_photo].png}" if nsp_genie_writer >= 6 and nsp_event_maniac_2 >= 4:
                        if nsp_germiona_maniac_3_statimg == "New" :
                            $ cur_level = nsp_event_maniac_3 + 1
                            jump nsp_event_maniac_3
                        elif nsp_germiona_maniac_3_statimg == "Explored" or nsp_germiona_maniac_3_statimg == "Full":
                            $ cur_level = nsp_event_maniac_3
                            jump nsp_event_maniac_3
                        elif nsp_germiona_maniac_3_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_maniac_3_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                             
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes 
                
                    "- Ничего -" :
                        jump nsp_newsp_themes
        
        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and nsp_genie_writer < 4  and False:
            jump nsp_newsp_themes
            
        "- Голый репортер в маске {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_nude].png} -" if nsp_newspaper_menu >= 6 and nsp_genie_writer >= 4  and False:
    
            if nsp_germiona_menu_nude == 1 :
                call nsp_theme_nude
                $ nsp_germiona_menu_nude = 2
        
            if nsp_germiona_menu_nude == 2 :
                menu:
                    "- Перед спальней Слизерина -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_nude_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_nude_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_nude_1_photo].png}" :
                        if nsp_germiona_nude_1_statimg == "New" :
                            $ cur_level = nsp_event_nude_1 + 1
                            jump nsp_event_nude_1
                        elif nsp_germiona_nude_1_statimg == "Explored" or nsp_germiona_nude_1_statimg == "Full":
                            $ cur_level = nsp_event_nude_1
                            jump nsp_event_nude_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 5:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Женская спальня Слизерина -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_nude_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_nude_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_nude_2_photo].png}" if nsp_genie_writer >= 5 :
                        if nsp_germiona_nude_2_statimg == "New" :
                            $ cur_level = nsp_event_nude_2 + 1
                            jump nsp_event_nude_2
                        elif nsp_germiona_nude_2_statimg == "Explored" or nsp_germiona_nude_2_statimg == "Full":
                            $ cur_level = nsp_event_nude_2
                            jump nsp_event_nude_2                       
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 6 :
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Мужская спальня Слизерина -\n{image=08_newspaper_scenario/hearts/heart_6[nsp_event_nude_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_nude_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_nude_3_photo].png}" if nsp_genie_writer >= 6 :
                        if nsp_germiona_nude_3_statimg == "New" :
                            $ cur_level = nsp_event_nude_3 + 1
                            jump nsp_event_nude_3
                        elif nsp_germiona_nude_3_statimg == "Explored" or nsp_germiona_nude_3_statimg == "Full":
                            $ cur_level = nsp_event_nude_3
                            jump nsp_event_nude_3
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes    

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 8:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Стойкость без одежды -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_nude_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_nude_4_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_nude_4_photo].png}" if nsp_genie_writer >= 8 :
                        if nsp_germiona_nude_4_statimg == "New" :
                            $ cur_level = nsp_event_nude_4 + 1
                            jump nsp_event_nude_4
                        elif nsp_germiona_nude_4_statimg == "Explored" or nsp_germiona_nude_4_statimg == "Full":
                            $ cur_level = nsp_event_nude_4
                            jump nsp_event_nude_4 
                        elif nsp_germiona_nude_4_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_nude_4_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes                            
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 10 :
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Маскировка без одежды -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_nude_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_nude_5_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_nude_5_photo].png}" if nsp_genie_writer >= 10 :
                        if nsp_germiona_nude_5_statimg == "New" :
                            $ cur_level = nsp_event_nude_5 + 1
                            jump nsp_event_nude_5
                        elif nsp_germiona_nude_5_statimg == "Explored" or nsp_germiona_nude_5_statimg == "Full":
                            $ cur_level = nsp_event_nude_5
                            jump nsp_event_nude_5                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes

        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and nsp_letter_1 < 2 and nsp_letter_9 < 2 :
            jump nsp_newsp_themes
            
        "- Запретный лес {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_forest].png} -" if nsp_newspaper_menu >= 6 and ( nsp_letter_1 >= 2 or nsp_letter_9 >= 2 ) :
    
            if nsp_germiona_menu_forest == 1 :
                call nsp_theme_forest
                $ nsp_germiona_menu_forest = 2
                
            if nsp_germiona_menu_forest == 2 :
                menu:
                
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 4 or nsp_letter_1 < 2 :
                        call nsp_vague_idea
                        jump nsp_newsp_themes  
                
                    "- Поход в Запретный лес -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_forest_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_forest_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_forest_1_photo].png}" if nsp_genie_writer >= 4 and nsp_letter_1 >= 2 :
                        if nsp_germiona_forest_1_statimg == "New" :
                            $ cur_level = nsp_event_forest_1 + 1
                            if cur_level == 2 :
                                jump nsp_her_demo
                            jump nsp_event_forest_1
                        elif nsp_germiona_forest_1_statimg == "Explored" or nsp_germiona_forest_1_statimg == "Full":
                            $ cur_level = nsp_event_forest_1
                            jump nsp_event_forest_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 7 or nsp_letter_9 < 2  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Контакт с кентавром -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_forest_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_forest_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_forest_2_photo].png}" if nsp_genie_writer >= 7 and nsp_letter_9 >= 2  and False:
                        if nsp_germiona_forest_2_statimg == "New" :
                            $ cur_level = nsp_event_forest_2 + 1
                            jump nsp_event_forest_2
                        elif nsp_germiona_forest_2_statimg == "Explored" or nsp_germiona_forest_2_statimg == "Full":
                            $ cur_level = nsp_event_forest_2
                            jump nsp_event_forest_2
                        elif nsp_germiona_forest_2_statimg == "Denied" :
                            ">Сейчас выполнение данного задания невозможно."
                            jump nsp_newsp_themes
                        elif nsp_germiona_forest_2_statimg == "Full_block" :
                            ">Данное задание является уникальным и полностью выполнено."
                            jump nsp_newsp_themes 
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes
        
        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu >= 6 and nsp_genie_photocamera == 0 :
            jump nsp_newsp_themes
            
        "- Студия у Джина {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_studio].png} -" if nsp_newspaper_menu >= 6 and nsp_genie_photocamera > 0 :
    
            if nsp_germiona_menu_studio == 1 :
                call nsp_theme_studio
                $ nsp_germiona_menu_studio = 2

            if nsp_germiona_menu_studio == 2 :
                menu:
                    "- Интервью с фотосессией -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_studio_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_studio_1_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_studio_1_photo].png}" :
                        if nsp_germiona_studio_1_statimg == "New" :
                            $ cur_level = nsp_event_studio_1 + 1
                            if cur_level == 2 :
                                jump nsp_her_demo
                            jump nsp_event_studio_1
                        elif nsp_germiona_studio_1_statimg == "Explored" or nsp_germiona_studio_1_statimg == "Full":
                            $ cur_level = nsp_event_studio_1
                            jump nsp_event_studio_1                        
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                    
                    "{color=#858585}-Не открытое действие-{/color}" if (nsp_genie_writer < 0 or not nsp_genie_sphere_video)  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Интервью с видеосессией -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_studio_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_studio_2_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_studio_2_photo].png}" if nsp_genie_writer >= 0 and nsp_genie_sphere_video  and False:
                        if nsp_germiona_studio_2_statimg == "New" :
                            $ cur_level = nsp_event_studio_2 + 1
                            jump nsp_event_studio_2
                        elif nsp_germiona_studio_2_statimg == "Explored" or nsp_germiona_studio_2_statimg == "Full":
                            $ cur_level = nsp_event_studio_2
                            jump nsp_event_studio_2                   
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 0  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Постановочные фото папарацци -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_studio_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_studio_3_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_studio_3_photo].png}" if nsp_genie_writer >= 0  and False:
                        if nsp_germiona_studio_3_statimg == "New" :
                            $ cur_level = nsp_event_studio_3 + 1
                            jump nsp_event_studio_3
                        elif nsp_germiona_studio_3_statimg == "Explored" or nsp_germiona_studio_3_statimg == "Full":
                            $ cur_level = nsp_event_studio_3
                            jump nsp_event_studio_3
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if (nsp_genie_writer < 0 or not nsp_genie_sphere_video) and False :
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Постановочные видео папарацци -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_studio_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_studio_4_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_studio_4_photo].png}" if nsp_genie_writer >= 0 and nsp_genie_sphere_video  and False:
                        if nsp_germiona_studio_4_statimg == "New" :
                            $ cur_level = nsp_event_studio_4 + 1
                            jump nsp_event_studio_4
                        elif nsp_germiona_studio_4_statimg == "Explored" or nsp_germiona_studio_4_statimg == "Full":
                            $ cur_level = nsp_event_studio_4
                            jump nsp_event_studio_4                       
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes

                    "{color=#858585}-Не открытое действие-{/color}" if nsp_genie_writer < 0  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Порнофото инкогнито -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_studio_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_studio_5_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_studio_5_photo].png}" if nsp_genie_writer >= 0  and False:
                        if nsp_germiona_studio_5_statimg == "New" :
                            $ cur_level = nsp_event_studio_5 + 1
                            jump nsp_event_studio_5
                        elif nsp_germiona_studio_5_statimg == "Explored" or nsp_germiona_studio_5_statimg == "Full":
                            $ cur_level = nsp_event_studio_5
                            jump nsp_event_studio_5                      
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                            
                    "{color=#858585}-Не открытое действие-{/color}" if (nsp_genie_writer < 0 or not nsp_genie_sphere_video)  and False:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Порновидео инкогнито -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_studio_6].png} {image=08_newspaper_scenario/flags/[nsp_germiona_studio_6_statimg].png} {image=08_newspaper_scenario/flags/Photo_[nsp_germiona_studio_6_photo].png}" if nsp_genie_writer >= 0 and nsp_genie_sphere_video  and False:
                        if nsp_germiona_studio_6_statimg == "New" :
                            $ cur_level = nsp_event_studio_6 + 1
                            jump nsp_event_studio_6
                        elif nsp_germiona_studio_6_statimg == "Explored" or nsp_germiona_studio_6_statimg == "Full":
                            $ cur_level = nsp_event_studio_6
                            jump nsp_event_studio_6                      
                        else :
                            ">Предлагать это задание Гермионе сейчас не имеет смысла. Нужно сначала ее морально подготовить."
                            jump nsp_newsp_themes
                
                    "- Ничего -" :
                        jump nsp_newsp_themes
                
                
        "- Ничего -" :
            jump hermione_main_menu

label nsp_init_flags_rights :

#### Event Rights_1
    if nsp_event_rights_1 == 0 and nsp_genie_writer >= 0 :
        if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
    elif nsp_event_rights_1 == 1 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 2 :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 3 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 4 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 5 :
        $ nsp_germiona_rights_1_statimg = "Full"

### Event Rights_2
    if nsp_event_rights_2 == 0 and nsp_genie_writer >= 1 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_2_statimg = "New"
    elif nsp_event_rights_2 == 1 :            
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 2 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 3 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 4 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 5 :
        $ nsp_germiona_rights_2_statimg = "Full"
        
### Event Rights_3
    if nsp_letter_7 < 3:
        if nsp_event_rights_3 == 5 :
            $ nsp_germiona_rights_3_statimg = "Full_block"
        else :
            $ nsp_germiona_rights_3_statimg = "Denied"
    else :
        if nsp_event_rights_3 == 0 and nsp_genie_writer >= 4 :
            if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
                $ nsp_germiona_rights_3_statimg = "New"
        elif nsp_event_rights_3 == 1 :            
            if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored_block"
        elif nsp_event_rights_3 == 2 :
            if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored_block"
        elif nsp_event_rights_3 == 3 :
            if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored_block"
        elif nsp_event_rights_3 == 4 :
            if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 30 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored_block"
        elif nsp_event_rights_3 == 5 :
            $ nsp_germiona_rights_3_statimg = "Full_block"
        
### Event Rights_4

    if nsp_event_rights_4 == 0 and nsp_genie_writer >= 8 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_4_statimg = "New"
    elif nsp_event_rights_4 == 1 :            
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 5 :
        $ nsp_germiona_rights_4_statimg = "Full"
        
### Event Rights_5
    if nsp_event_rights_5 == 0 and nsp_genie_writer >= 10 and nsp_event_rights_4 >= 3 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_5_statimg = "New"
    elif nsp_event_rights_5 == 1 :            
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 5 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 6 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 140 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 7 :
        $ nsp_germiona_rights_5_statimg = "Full"
        
### Theme Rights
    $ nsp_germiona_statimg_rights = "Full"
    
    if nsp_germiona_rights_1_statimg != "Full" and nsp_germiona_rights_1_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_2_statimg != "Full" and nsp_germiona_rights_2_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_3_statimg != "Full" and nsp_germiona_rights_3_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_4_statimg != "Full" and nsp_germiona_rights_4_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_5_statimg != "Full" and nsp_germiona_rights_5_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
        
    if nsp_germiona_rights_1_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_2_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_3_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_4_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_5_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"

    return

    
    
label nsp_init_flags_magls :

#### Event Magls_1
    if nsp_event_magls_1 == 0 and nsp_genie_writer >= 2 :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_1_statimg = "New"
    elif nsp_event_magls_1 == 1 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_1_statimg = "New"
        else :
            $ nsp_germiona_magls_1_statimg = "Explored"
    elif nsp_event_magls_1 == 2 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_1_statimg = "New"
        else :
            $ nsp_germiona_magls_1_statimg = "Explored"
    elif nsp_event_magls_1 == 3 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_magls_1_statimg = "New"
        else :
            $ nsp_germiona_magls_1_statimg = "Explored"
    elif nsp_event_magls_1 == 4 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_magls_1_statimg = "New"
        else :
            $ nsp_germiona_magls_1_statimg = "Explored"
    elif nsp_event_magls_1 == 5 :
        $ nsp_germiona_magls_1_statimg = "Full"

### Event Magls_2
    if nsp_event_magls_2 == 0 and nsp_genie_writer >= 4 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_2_statimg = "New"
    elif nsp_event_magls_2 == 1 :            
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_2_statimg = "New"
        else :
            $ nsp_germiona_magls_2_statimg = "Explored"
    elif nsp_event_magls_2 == 2 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_magls_2_statimg = "New"
        else :
            $ nsp_germiona_magls_2_statimg = "Explored"
    elif nsp_event_magls_2 == 3 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_magls_2_statimg = "New"
        else :
            $ nsp_germiona_magls_2_statimg = "Explored"
    elif nsp_event_magls_2 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_magls_2_statimg = "New"
        else :
            $ nsp_germiona_magls_2_statimg = "Explored"
    elif nsp_event_magls_2 == 5 :
        $ nsp_germiona_magls_2_statimg = "Full"
        
### Event Magls_3

    if nsp_event_magls_3 == 0 and nsp_genie_writer >= 6 :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_3_statimg = "New"
    elif nsp_event_magls_3 == 1 :            
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_3_statimg = "New"
        else :
            $ nsp_germiona_magls_3_statimg = "Explored"
    elif nsp_event_magls_3 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_magls_3_statimg = "New"
        else :
            $ nsp_germiona_magls_3_statimg = "Explored"
    elif nsp_event_magls_3 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_magls_3_statimg = "New"
        else :
            $ nsp_germiona_magls_3_statimg = "Explored"
    elif nsp_event_magls_3 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_magls_3_statimg = "New"
        else :
            $ nsp_germiona_magls_3_statimg = "Explored"
    elif nsp_event_magls_3 == 5 :
        $ nsp_germiona_magls_3_statimg = "Full"
        
### Event Magls_4

    if nsp_event_magls_4 == 0 and nsp_genie_writer >= 8 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_magls_4_statimg = "New"
    elif nsp_event_magls_4 == 1 :            
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 35 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_magls_4_statimg = "New"
        else :
            $ nsp_germiona_magls_4_statimg = "Explored"
    elif nsp_event_magls_4 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_magls_4_statimg = "New"
        else :
            $ nsp_germiona_magls_4_statimg = "Explored"
    elif nsp_event_magls_4 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_magls_4_statimg = "New"
        else :
            $ nsp_germiona_magls_4_statimg = "Explored"
    elif nsp_event_magls_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_magls_4_statimg = "New"
        else :
            $ nsp_germiona_magls_4_statimg = "Explored"
    elif nsp_event_magls_4 == 5 :
        $ nsp_germiona_magls_4_statimg = "Full"
        
### Event Magls_5

    if nsp_event_magls_5 == 0 and nsp_genie_writer >= 10 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_magls_5_statimg = "New"
    elif nsp_event_magls_5 == 1 :            
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_magls_5_statimg = "New"
        else :
            $ nsp_germiona_magls_5_statimg = "Explored_block"
    elif nsp_event_magls_5 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_magls_5_statimg = "New"
        else :
            $ nsp_germiona_magls_5_statimg = "Explored_block"
    elif nsp_event_magls_5 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_magls_5_statimg = "New"
        else :
            $ nsp_germiona_magls_5_statimg = "Explored_block"
    elif nsp_event_magls_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 150 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_magls_5_statimg = "New"
        else :
            $ nsp_germiona_magls_5_statimg = "Explored_block"
    elif nsp_event_magls_5 == 5 :
        $ nsp_germiona_magls_5_statimg = "Full_block"
        
### Theme Magls
    $ nsp_germiona_statimg_magls = "Full"
    
    if nsp_germiona_magls_1_statimg != "Full" and nsp_germiona_magls_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_magls = "Explored"
    elif  nsp_germiona_magls_2_statimg != "Full" and nsp_germiona_magls_2_statimg != "Full_block":
        $ nsp_germiona_statimg_magls = "Explored"
    elif  nsp_germiona_magls_3_statimg != "Full" and nsp_germiona_magls_3_statimg != "Full_block":
        $ nsp_germiona_statimg_magls = "Explored"
    elif  nsp_germiona_magls_4_statimg != "Full" and nsp_germiona_magls_4_statimg != "Full_block":
        $ nsp_germiona_statimg_magls = "Explored"
    elif  nsp_germiona_magls_5_statimg != "Full" and nsp_germiona_magls_5_statimg != "Full_block":
        $ nsp_germiona_statimg_magls = "Explored"
        
    if nsp_germiona_magls_1_statimg == "New":
        $ nsp_germiona_statimg_magls = "New"
    elif  nsp_germiona_magls_2_statimg == "New":
        $ nsp_germiona_statimg_magls = "New"
    elif  nsp_germiona_magls_3_statimg == "New":
        $ nsp_germiona_statimg_magls = "New"
    elif  nsp_germiona_magls_4_statimg == "New":
        $ nsp_germiona_statimg_magls = "New"
    elif  nsp_germiona_magls_5_statimg == "New":
        $ nsp_germiona_statimg_magls = "New"

    return

    
    
    
label nsp_init_flags_kviddich :

#### Event Kviddich_1
    if nsp_event_kviddich_1 == 0 and nsp_genie_writer >= 4 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_kviddich_1_statimg = "New"
    elif nsp_event_kviddich_1 == 1 :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 15 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_kviddich_1_statimg = "New"
        else :
            $ nsp_germiona_kviddich_1_statimg = "Explored"
    elif nsp_event_kviddich_1 == 2 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 25 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_kviddich_1_statimg = "New"
        else :
            $ nsp_germiona_kviddich_1_statimg = "Explored"
    elif nsp_event_kviddich_1 == 3 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_kviddich_1_statimg = "New"
        else :
            $ nsp_germiona_kviddich_1_statimg = "Explored"
    elif nsp_event_kviddich_1 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_1_statimg = "New"
        else :
            $ nsp_germiona_kviddich_1_statimg = "Explored"
    elif nsp_event_kviddich_1 == 5 :
        $ nsp_germiona_kviddich_1_statimg = "Full"

### Event Kviddich_2
    if nsp_event_kviddich_2 == 0 and nsp_genie_writer >= 6 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_kviddich_2_statimg = "New"
    elif nsp_event_kviddich_2 == 1 :            
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_kviddich_2_statimg = "New"
        else :
            $ nsp_germiona_kviddich_2_statimg = "Explored"
    elif nsp_event_kviddich_2 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_kviddich_2_statimg = "New"
        else :
            $ nsp_germiona_kviddich_2_statimg = "Explored"
    elif nsp_event_kviddich_2 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_2_statimg = "New"
        else :
            $ nsp_germiona_kviddich_2_statimg = "Explored_block"
    elif nsp_event_kviddich_2 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_kviddich_2_statimg = "New"
        else :
            $ nsp_germiona_kviddich_2_statimg = "Explored"
    elif nsp_event_kviddich_2 == 5 :
        $ nsp_germiona_kviddich_2_statimg = "Full"
        
### Event Kviddich_3

    if nsp_event_kviddich_3 == 0 and nsp_genie_writer >= 7 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_kviddich_3_statimg = "New"
    elif nsp_event_kviddich_3 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_3_statimg = "New"
        else :
            $ nsp_germiona_kviddich_3_statimg = "Explored"
    elif nsp_event_kviddich_3 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_3_statimg = "New"
        else :
            $ nsp_germiona_kviddich_3_statimg = "Explored"
    elif nsp_event_kviddich_3 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_kviddich_3_statimg = "New"
        else :
            $ nsp_germiona_kviddich_3_statimg = "Explored"
    elif nsp_event_kviddich_3 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 150 and nsp_germiona_impudence >= 50 and nsp_genie_sphere_diamond_level >= 3 :
            $ nsp_germiona_kviddich_3_statimg = "New"
        else :
            $ nsp_germiona_kviddich_3_statimg = "Explored"
    elif nsp_event_kviddich_3 == 5 :
        $ nsp_germiona_kviddich_3_statimg = "Full"
        
### Event Kviddich_4

    if nsp_event_kviddich_4 == 0 and nsp_genie_writer >= 8 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_kviddich_4_statimg = "New"
    elif nsp_event_kviddich_4 == 1 :            
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_kviddich_4_statimg = "New"
        else :
            $ nsp_germiona_kviddich_4_statimg = "Explored_block"
    elif nsp_event_kviddich_4 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_4_statimg = "New"
        else :
            $ nsp_germiona_kviddich_4_statimg = "Explored_block"
    elif nsp_event_kviddich_4 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 140 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_kviddich_4_statimg = "New"
        else :
            $ nsp_germiona_kviddich_4_statimg = "Explored_block"
    elif nsp_event_kviddich_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 160 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_kviddich_4_statimg = "New"
        else :
            $ nsp_germiona_kviddich_4_statimg = "Explored_block"
    elif nsp_event_kviddich_4 == 5 :
        $ nsp_germiona_kviddich_4_statimg = "Full_block"
        
### Event Kviddich_5

    if nsp_event_kviddich_5 == 0 and nsp_genie_writer >= 10 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_kviddich_5_statimg = "New"
    elif nsp_event_kviddich_5 == 1 :            
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_kviddich_5_statimg = "New"
        else :
            $ nsp_germiona_kviddich_5_statimg = "Explored_block"
    elif nsp_event_kviddich_5 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_5_statimg = "New"
        else :
            $ nsp_germiona_kviddich_5_statimg = "Explored_block"
    elif nsp_event_kviddich_5 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 130 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_kviddich_5_statimg = "New"
        else :
            $ nsp_germiona_kviddich_5_statimg = "Explored_block"
    elif nsp_event_kviddich_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 160 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_kviddich_5_statimg = "New"
        else :
            $ nsp_germiona_kviddich_5_statimg = "Explored_block"
    elif nsp_event_kviddich_5 == 5 :
        $ nsp_germiona_kviddich_5_statimg = "Full_block"
        
### Event Kviddich_6

    if nsp_event_kviddich_6 == 0 and nsp_genie_writer >= 10 and nsp_event_kviddich_2 == 5 and nsp_event_kviddich_5 == 5 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_kviddich_6_statimg = "New"
    elif nsp_event_kviddich_6 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_kviddich_6_statimg = "New"
        else :
            $ nsp_germiona_kviddich_6_statimg = "Explored_block"
    elif nsp_event_kviddich_6 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_kviddich_6_statimg = "New"
        else :
            $ nsp_germiona_kviddich_6_statimg = "Explored_block"
    elif nsp_event_kviddich_6 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 150 and nsp_germiona_impudence >= 60 :
            $ nsp_germiona_kviddich_6_statimg = "New"
        else :
            $ nsp_germiona_kviddich_6_statimg = "Explored_block"
    elif nsp_event_kviddich_6 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 180 and nsp_germiona_impudence >= 70 :
            $ nsp_germiona_kviddich_6_statimg = "New"
        else :
            $ nsp_germiona_kviddich_6_statimg = "Explored_block"
    elif nsp_event_kviddich_6 == 5 :
        $ nsp_germiona_kviddich_6_statimg = "Full_block"
        
### Theme Kviddich
    $ nsp_germiona_statimg_kviddich = "Full"
    
    if nsp_germiona_kviddich_1_statimg != "Full" and nsp_germiona_kviddich_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_kviddich = "Explored"
    elif  nsp_germiona_kviddich_2_statimg != "Full" and nsp_germiona_kviddich_2_statimg != "Full_block":
        $ nsp_germiona_statimg_kviddich = "Explored"
    elif  nsp_germiona_kviddich_3_statimg != "Full" and nsp_germiona_kviddich_3_statimg != "Full_block":
        $ nsp_germiona_statimg_kviddich = "Explored"
    elif  nsp_germiona_kviddich_4_statimg != "Full" and nsp_germiona_kviddich_4_statimg != "Full_block":
        $ nsp_germiona_statimg_kviddich = "Explored"
    elif  nsp_germiona_kviddich_5_statimg != "Full" and nsp_germiona_kviddich_5_statimg != "Full_block":
        $ nsp_germiona_statimg_kviddich = "Explored"
    elif  nsp_germiona_kviddich_6_statimg != "Full" and nsp_germiona_kviddich_6_statimg != "Full_block":
        $ nsp_germiona_statimg_kviddich = "Explored"
        
    if nsp_germiona_kviddich_1_statimg == "New":
        $ nsp_germiona_statimg_kviddich = "New"
    elif  nsp_germiona_kviddich_2_statimg == "New":
        $ nsp_germiona_statimg_kviddich = "New"
    elif  nsp_germiona_kviddich_3_statimg == "New":
        $ nsp_germiona_statimg_kviddich = "New"
    elif  nsp_germiona_kviddich_4_statimg == "New":
        $ nsp_germiona_statimg_kviddich = "New"
    elif  nsp_germiona_kviddich_5_statimg == "New":
        $ nsp_germiona_statimg_kviddich = "New"
    elif  nsp_germiona_kviddich_6_statimg == "New":
        $ nsp_germiona_statimg_kviddich = "New"

    return

    
    

label nsp_init_flags_sex :

#### Event Sex_1
    if nsp_event_sex_1 == 0 and nsp_genie_writer >= 1 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_sex_1_statimg = "New"
    elif nsp_event_sex_1 == 1 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 25 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_sex_1_statimg = "New"
        else :
            $ nsp_germiona_sex_1_statimg = "Explored"
    elif nsp_event_sex_1 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_sex_1_statimg = "New"
        else :
            $ nsp_germiona_sex_1_statimg = "Explored"
    elif nsp_event_sex_1 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_sex_1_statimg = "New"
        else :
            $ nsp_germiona_sex_1_statimg = "Explored"
    elif nsp_event_sex_1 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_sex_1_statimg = "New"
        else :
            $ nsp_germiona_sex_1_statimg = "Explored"
    elif nsp_event_sex_1 == 5 :
        $ nsp_germiona_sex_1_statimg = "Full"

### Event Sex_2
    if nsp_event_sex_2 == 0 and nsp_genie_writer >= 4 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_sex_2_statimg = "New"
    elif nsp_event_sex_2 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_sex_2_statimg = "New"
        else :
            $ nsp_germiona_sex_2_statimg = "Explored"
    elif nsp_event_sex_2 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_sex_2_statimg = "New"
        else :
            $ nsp_germiona_sex_2_statimg = "Explored"
    elif nsp_event_sex_2 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_sex_2_statimg = "New"
        else :
            $ nsp_germiona_sex_2_statimg = "Explored"
    elif nsp_event_sex_2 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_sex_2_statimg = "New"
        else :
            $ nsp_germiona_sex_2_statimg = "Explored"
    elif nsp_event_sex_2 == 5 :
        $ nsp_germiona_sex_2_statimg = "Full"
        
### Event Sex_3

    if nsp_event_sex_3 == 0 and nsp_genie_writer >= 5 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_sex_3_statimg = "New"
    elif nsp_event_sex_3 == 1 :            
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_sex_3_statimg = "New"
        else :
            $ nsp_germiona_sex_3_statimg = "Explored"
    elif nsp_event_sex_3 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 65 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_sex_3_statimg = "New"
        else :
            $ nsp_germiona_sex_3_statimg = "Explored"
    elif nsp_event_sex_3 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 85 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_sex_3_statimg = "New"
        else :
            $ nsp_germiona_sex_3_statimg = "Explored"
    elif nsp_event_sex_3 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 105 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_sex_3_statimg = "New"
        else :
            $ nsp_germiona_sex_3_statimg = "Explored"
    elif nsp_event_sex_3 == 5 :
        $ nsp_germiona_sex_3_statimg = "Full"
        
### Event Sex_4

    if nsp_event_sex_4 == 0 and nsp_genie_writer >= 6 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 35 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_sex_4_statimg = "New"
    elif nsp_event_sex_4 == 1 :            
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_sex_4_statimg = "New"
        else :
            $ nsp_germiona_sex_4_statimg = "Explored"
    elif nsp_event_sex_4 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 75 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_sex_4_statimg = "New"
        else :
            $ nsp_germiona_sex_4_statimg = "Explored"
    elif nsp_event_sex_4 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_sex_4_statimg = "New"
        else :
            $ nsp_germiona_sex_4_statimg = "Explored"
    elif nsp_event_sex_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 130 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_sex_4_statimg = "New"
        else :
            $ nsp_germiona_sex_4_statimg = "Explored"
    elif nsp_event_sex_4 == 5 :
        $ nsp_germiona_sex_4_statimg = "Full"
        
### Event Sex_5

    if nsp_event_sex_5 == 0 and nsp_genie_writer >= 9 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_sex_5_statimg = "New"
    elif nsp_event_sex_5 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 55 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_sex_5_statimg = "New"
        else :
            $ nsp_germiona_sex_5_statimg = "Explored"
    elif nsp_event_sex_5 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_sex_5_statimg = "New"
        else :
            $ nsp_germiona_sex_5_statimg = "Explored"
    elif nsp_event_sex_5 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 105 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_sex_5_statimg = "New"
        else :
            $ nsp_germiona_sex_5_statimg = "Explored"
    elif nsp_event_sex_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 150 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_sex_5_statimg = "New"
        else :
            $ nsp_germiona_sex_5_statimg = "Explored"
    elif nsp_event_sex_5 == 5 :
        $ nsp_germiona_sex_5_statimg = "Full"
        
### Theme Sex
    $ nsp_germiona_statimg_sex = "Full"
    
    if nsp_germiona_sex_1_statimg != "Full" and nsp_germiona_sex_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_sex = "Explored"
    elif  nsp_germiona_sex_2_statimg != "Full" and nsp_germiona_sex_2_statimg != "Full_block":
        $ nsp_germiona_statimg_sex = "Explored"
    elif  nsp_germiona_sex_3_statimg != "Full" and nsp_germiona_sex_3_statimg != "Full_block":
        $ nsp_germiona_statimg_sex = "Explored"
    elif  nsp_germiona_sex_4_statimg != "Full" and nsp_germiona_sex_4_statimg != "Full_block":
        $ nsp_germiona_statimg_sex = "Explored"
    elif  nsp_germiona_sex_5_statimg != "Full" and nsp_germiona_sex_5_statimg != "Full_block":
        $ nsp_germiona_statimg_sex = "Explored"
        
    if nsp_germiona_sex_1_statimg == "New":
        $ nsp_germiona_statimg_sex = "New"
    elif  nsp_germiona_sex_2_statimg == "New":
        $ nsp_germiona_statimg_sex = "New"
    elif  nsp_germiona_sex_3_statimg == "New":
        $ nsp_germiona_statimg_sex = "New"
    elif  nsp_germiona_sex_4_statimg == "New":
        $ nsp_germiona_statimg_sex = "New"
    elif  nsp_germiona_sex_5_statimg == "New":
        $ nsp_germiona_statimg_sex = "New"

    return    
 
    
    
    
label nsp_init_flags_maniac :

#### Event Maniac_1
    if nsp_event_maniac_1 == 0 and nsp_genie_writer >= 1 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_maniac_1_statimg = "New"
    elif nsp_event_maniac_1 == 1 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 25 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_maniac_1_statimg = "New"
        else :
            $ nsp_germiona_maniac_1_statimg = "Explored_block"
    elif nsp_event_maniac_1 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_maniac_1_statimg = "New"
        else :
            $ nsp_germiona_maniac_1_statimg = "Explored_block"
    elif nsp_event_maniac_1 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_maniac_1_statimg = "New"
        else :
            $ nsp_germiona_maniac_1_statimg = "Explored_block"
    elif nsp_event_maniac_1 == 4 :
        $ nsp_germiona_maniac_1_statimg = "Full_block"

### Event Maniac_2
    if nsp_event_maniac_2 == 0 and nsp_genie_writer >= 4 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_maniac_2_statimg = "New"
    elif nsp_event_maniac_2 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_maniac_2_statimg = "New"
        else :
            $ nsp_germiona_maniac_2_statimg = "Explored_block"
    elif nsp_event_maniac_2 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_maniac_2_statimg = "New"
        else :
            $ nsp_germiona_maniac_2_statimg = "Explored_block"
    elif nsp_event_maniac_2 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_maniac_2_statimg = "New"
        else :
            $ nsp_germiona_maniac_2_statimg = "Explored_block"
    elif nsp_event_maniac_2 == 4 :
        $ nsp_germiona_maniac_2_statimg = "Full_block"
        
### Event Maniac_3

    if nsp_event_maniac_3 == 0 and nsp_genie_writer >= 5 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_maniac_3_statimg = "New"
    elif nsp_event_maniac_3 == 1 :            
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_maniac_3_statimg = "New"
        else :
            $ nsp_germiona_maniac_3_statimg = "Explored_block"
    elif nsp_event_maniac_3 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 65 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_maniac_3_statimg = "New"
        else :
            $ nsp_germiona_maniac_3_statimg = "Explored_block"
    elif nsp_event_maniac_3 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 85 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_maniac_3_statimg = "New"
        else :
            $ nsp_germiona_maniac_3_statimg = "Explored_block"
    elif nsp_event_maniac_3 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 105 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_maniac_3_statimg = "New"
        else :
            $ nsp_germiona_maniac_3_statimg = "Explored_block"
    elif nsp_event_maniac_3 == 5 :
        $ nsp_germiona_maniac_3_statimg = "Full_block"
        
### Theme Maniac
    $ nsp_germiona_statimg_maniac = "Full_block"
    
    if nsp_germiona_maniac_1_statimg != "Full" and nsp_germiona_maniac_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_maniac = "Explored_block"
    elif  nsp_germiona_maniac_2_statimg != "Full" and nsp_germiona_maniac_2_statimg != "Full_block":
        $ nsp_germiona_statimg_maniac = "Explored_block"
    elif  nsp_germiona_maniac_3_statimg != "Full" and nsp_germiona_maniac_3_statimg != "Full_block":
        $ nsp_germiona_statimg_maniac = "Explored_block"
        
    if nsp_germiona_maniac_1_statimg == "New":
        $ nsp_germiona_statimg_maniac = "New"
    elif  nsp_germiona_maniac_2_statimg == "New":
        $ nsp_germiona_statimg_maniac = "New"
    elif  nsp_germiona_maniac_3_statimg == "New":
        $ nsp_germiona_statimg_maniac = "New"

    return       
    
  
    
    
label nsp_init_flags_nude :

#### Event Nude_1
    if nsp_event_nude_1 == 0 and nsp_genie_writer >= 4 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_nude_1_statimg = "New"
    elif nsp_event_nude_1 == 1 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 45 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_nude_1_statimg = "New"
        else :
            $ nsp_germiona_nude_1_statimg = "Explored"
    elif nsp_event_nude_1 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_nude_1_statimg = "New"
        else :
            $ nsp_germiona_nude_1_statimg = "Explored"
    elif nsp_event_nude_1 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_nude_1_statimg = "New"
        else :
            $ nsp_germiona_nude_1_statimg = "Explored"
    elif nsp_event_nude_1 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 125 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_nude_1_statimg = "New"
        else :
            $ nsp_germiona_nude_1_statimg = "Explored"
    elif nsp_event_nude_1 == 5 :
        $ nsp_germiona_nude_1_statimg = "Full"

### Event Nude_2
    if nsp_event_nude_2 == 0 and nsp_genie_writer >= 5 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_nude_2_statimg = "New"
    elif nsp_event_nude_2 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_nude_2_statimg = "New"
        else :
            $ nsp_germiona_nude_2_statimg = "Explored"
    elif nsp_event_nude_2 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_nude_2_statimg = "New"
        else :
            $ nsp_germiona_nude_2_statimg = "Explored"
    elif nsp_event_nude_2 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_nude_2_statimg = "New"
        else :
            $ nsp_germiona_nude_2_statimg = "Explored"
    elif nsp_event_nude_2 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_nude_2_statimg = "New"
        else :
            $ nsp_germiona_nude_2_statimg = "Explored"
    elif nsp_event_nude_2 == 5 :
        $ nsp_germiona_nude_2_statimg = "Full"
        
### Event Nude_3

    if nsp_event_nude_3 == 0 and nsp_genie_writer >= 6 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_nude_3_statimg = "New"
    elif nsp_event_nude_3 == 1 :            
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_nude_3_statimg = "New"
        else :
            $ nsp_germiona_nude_3_statimg = "Explored"
    elif nsp_event_nude_3 == 2 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_nude_3_statimg = "New"
        else :
            $ nsp_germiona_nude_3_statimg = "Explored"
    elif nsp_event_nude_3 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 140 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_nude_3_statimg = "New"
        else :
            $ nsp_germiona_nude_3_statimg = "Explored"
    elif nsp_event_nude_3 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 160 and nsp_germiona_impudence >= 60 :
            $ nsp_germiona_nude_3_statimg = "New"
        else :
            $ nsp_germiona_nude_3_statimg = "Explored"
    elif nsp_event_nude_3 == 5 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 170 and nsp_germiona_impudence >= 60 :
            $ nsp_germiona_nude_3_statimg = "New"
        else :
            $ nsp_germiona_nude_3_statimg = "Explored"
    elif nsp_event_nude_3 == 6 :
        $ nsp_germiona_nude_3_statimg = "Full"
        
### Event Nude_4

    if nsp_event_nude_4 == 0 and nsp_genie_writer >= 8 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_nude_4_statimg = "New"
    elif nsp_event_nude_4 == 1 :            
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 140 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_nude_4_statimg = "New"
        else :
            $ nsp_germiona_nude_4_statimg = "Explored"
    elif nsp_event_nude_4 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 150 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_nude_4_statimg = "New"
        else :
            $ nsp_germiona_nude_4_statimg = "Explored_block"
    elif nsp_event_nude_4 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 160 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_nude_4_statimg = "New"
        else :
            $ nsp_germiona_nude_4_statimg = "Explored"
    elif nsp_event_nude_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 170 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_nude_4_statimg = "New"
        else :
            $ nsp_germiona_nude_4_statimg = "Explored"
    elif nsp_event_nude_4 == 5 :
        $ nsp_germiona_nude_4_statimg = "Full"
        
### Event Nude_5

    if nsp_event_nude_5 == 0 and nsp_genie_writer >= 10 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_nude_5_statimg = "New"
    elif nsp_event_nude_5 == 1 :            
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_nude_5_statimg = "New"
        else :
            $ nsp_germiona_nude_5_statimg = "Explored"
    elif nsp_event_nude_5 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_nude_5_statimg = "New"
        else :
            $ nsp_germiona_nude_5_statimg = "Explored"
    elif nsp_event_nude_5 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_nude_5_statimg = "New"
        else :
            $ nsp_germiona_nude_5_statimg = "Explored"
    elif nsp_event_nude_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 130 and nsp_germiona_impudence >= 60 :
            $ nsp_germiona_nude_5_statimg = "New"
        else :
            $ nsp_germiona_nude_5_statimg = "Explored"
    elif nsp_event_nude_5 == 5 :
        $ nsp_germiona_nude_5_statimg = "Full"
        
### Theme Sex
    $ nsp_germiona_statimg_nude = "Full"
    
    if nsp_germiona_nude_1_statimg != "Full" and nsp_germiona_nude_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_nude = "Explored"
    elif  nsp_germiona_nude_2_statimg != "Full" and nsp_germiona_nude_2_statimg != "Full_block":
        $ nsp_germiona_statimg_nude = "Explored"
    elif  nsp_germiona_nude_3_statimg != "Full" and nsp_germiona_nude_3_statimg != "Full_block":
        $ nsp_germiona_statimg_nude = "Explored"
    elif  nsp_germiona_nude_4_statimg != "Full" and nsp_germiona_nude_4_statimg != "Full_block":
        $ nsp_germiona_statimg_nude = "Explored"
    elif  nsp_germiona_nude_5_statimg != "Full" and nsp_germiona_nude_5_statimg != "Full_block":
        $ nsp_germiona_statimg_nude = "Explored"
        
    if nsp_germiona_nude_1_statimg == "New":
        $ nsp_germiona_statimg_nude = "New"
    elif  nsp_germiona_nude_2_statimg == "New":
        $ nsp_germiona_statimg_nude = "New"
    elif  nsp_germiona_nude_3_statimg == "New":
        $ nsp_germiona_statimg_nude = "New"
    elif  nsp_germiona_nude_4_statimg == "New":
        $ nsp_germiona_statimg_nude = "New"
    elif  nsp_germiona_nude_5_statimg == "New":
        $ nsp_germiona_statimg_nude = "New"

    return      
    
    
    
    
    
 
label nsp_init_flags_forest :

#### Event Forest_1
    if nsp_event_forest_1 == 0 and nsp_genie_writer >= 4 and nsp_letter_1 == 2 :
        if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_forest_1_statimg = "New"
    elif nsp_event_forest_1 == 1 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_forest_1_statimg = "New"
        else :
            $ nsp_germiona_forest_1_statimg = "Explored"
    elif nsp_event_forest_1 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_forest_1_statimg = "New"
        else :
            $ nsp_germiona_forest_1_statimg = "Explored"
    elif nsp_event_forest_1 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_forest_1_statimg = "New"
        else :
            $ nsp_germiona_forest_1_statimg = "Explored"
    elif nsp_event_forest_1 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 140 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_forest_1_statimg = "New"
        else :
            $ nsp_germiona_forest_1_statimg = "Explored"
    elif nsp_event_forest_1 == 5 :
        $ nsp_germiona_forest_1_statimg = "Full"

### Event Forest_2
    if nsp_event_forest_2 == 0 and nsp_genie_writer >= 7 and nsp_letter_9 == 2:
        if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_forest_2_statimg = "New"
    elif nsp_event_forest_2 == 1 :            
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_forest_2_statimg = "New"
        else :
            $ nsp_germiona_forest_2_statimg = "Explored_block"
    elif nsp_event_forest_2 == 2 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_forest_2_statimg = "New"
        else :
            $ nsp_germiona_forest_2_statimg = "Explored_block"
    elif nsp_event_forest_2 == 3 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_forest_2_statimg = "New"
        else :
            $ nsp_germiona_forest_2_statimg = "Explored_block"
    elif nsp_event_forest_2 == 4 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 70 and nsp_germiona_impudence >= 50 :
            $ nsp_germiona_forest_2_statimg = "New"
        else :
            $ nsp_germiona_forest_2_statimg = "Explored_block"
    elif nsp_event_forest_2 == 5 :
        $ nsp_germiona_forest_2_statimg = "Full_block"
      
        
### Theme Sex
    $ nsp_germiona_statimg_forest = "Full"
    
    if nsp_germiona_forest_1_statimg != "Full" and nsp_germiona_forest_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_forest = "Explored"
    elif  nsp_germiona_forest_2_statimg != "Full" and nsp_germiona_forest_2_statimg != "Full_block":
        $ nsp_germiona_statimg_forest = "Explored"
        
    if nsp_germiona_forest_1_statimg == "New":
        $ nsp_germiona_statimg_forest = "New"
    elif  nsp_germiona_forest_2_statimg == "New":
        $ nsp_germiona_statimg_forest = "New"

    return
    
label nsp_init_flag_photo :
        
### Photo flags

    if nsp_genie_photocamera >= 1 and nsp_germiona_menu_studio >= 2:

        $ nsp_germiona_rights_1_photo = "en"
        $ nsp_germiona_rights_2_photo = "en" 

    if nsp_genie_sphere and nsp_genie_sphere_sapphire_level_eff >= 3 and nsp_genie_sphere_ruby_level_eff >= 1 :
            
        if nsp_genie_sphere_diamond_level_eff >= 2 :
        
            $ nsp_germiona_rights_4_photo = "en"
            $ nsp_germiona_rights_5_photo = "en"  
            
            $ nsp_germiona_magls_1_photo = "en"
            $ nsp_germiona_magls_4_photo = "en"
            $ nsp_germiona_magls_5_photo = "en"
            
            $ nsp_germiona_sex_1_photo = "en"
            $ nsp_germiona_sex_2_photo = "en"
            $ nsp_germiona_sex_3_photo = "en"
            $ nsp_germiona_sex_4_photo = "en"
            $ nsp_germiona_sex_5_photo = "en"
            
            $ nsp_germiona_sex_1_photo = "en"
            $ nsp_germiona_sex_2_photo = "en"
            $ nsp_germiona_sex_3_photo = "en"
            $ nsp_germiona_sex_4_photo = "en"
            $ nsp_germiona_sex_5_photo = "en"
            
            $ nsp_germiona_nude_1_photo = "en"
            $ nsp_germiona_nude_2_photo = "en"
            $ nsp_germiona_nude_3_photo = "en"
            $ nsp_germiona_nude_4_photo = "en"
            $ nsp_germiona_nude_5_photo = "en"
            
        if nsp_genie_sphere_diamond_level_eff >= 3 :
        
            $ nsp_germiona_magls_2_photo = "en"
            $ nsp_germiona_magls_3_photo = "en"
            
            $ nsp_germiona_kviddich_1_photo = "en"
            $ nsp_germiona_kviddich_2_photo = "en"
            $ nsp_germiona_kviddich_3_photo = "en"
            $ nsp_germiona_kviddich_4_photo = "en"
            $ nsp_germiona_kviddich_5_photo = "en"
            $ nsp_germiona_kviddich_6_photo = "en"
            
            $ nsp_germiona_maniac_1_photo = "en"
            $ nsp_germiona_maniac_2_photo = "en"
            $ nsp_germiona_maniac_3_photo = "en"
            
        if nsp_genie_sphere_diamond_level_eff >= 4 :
        
            $ nsp_germiona_rights_3_photo = "en"
            
            $ nsp_germiona_forest_1_photo = "en"
            $ nsp_germiona_forest_2_photo = "en"

    return      
    
    
    
    
label nsp_init_flags_studio :

#### Event Studio_1
    if nsp_event_studio_1 == 0 and nsp_genie_writer >= 0 and nsp_genie_photocamera >= 1 :
        if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_1_statimg = "New"
    elif nsp_event_studio_1 == 1 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_1_statimg = "New"
        else :
            $ nsp_germiona_studio_1_statimg = "Explored"
    elif nsp_event_studio_1 == 2 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_1_statimg = "New"
        else :
            $ nsp_germiona_studio_1_statimg = "Explored"
    elif nsp_event_studio_1 == 3 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_1_statimg = "New"
        else :
            $ nsp_germiona_studio_1_statimg = "Explored"
    elif nsp_event_studio_1 == 4 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_1_statimg = "New"
        else :
            $ nsp_germiona_studio_1_statimg = "Explored"
    elif nsp_event_studio_1 == 5 :
        $ nsp_germiona_studio_1_statimg = "Full"

### Event Studio_2
    if nsp_event_studio_2 == 0 and nsp_genie_writer >= 0 and nsp_genie_sphere_video :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_2_statimg = "New"
    elif nsp_event_studio_2 == 1 :            
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_2_statimg = "New"
        else :
            $ nsp_germiona_studio_2_statimg = "Explored"
    elif nsp_event_studio_2 == 2 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 55 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_2_statimg = "New"
        else :
            $ nsp_germiona_studio_2_statimg = "Explored"
    elif nsp_event_studio_2 == 3 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_2_statimg = "New"
        else :
            $ nsp_germiona_studio_2_statimg = "Explored"
    elif nsp_event_studio_2 == 4 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_2_statimg = "New"
        else :
            $ nsp_germiona_studio_2_statimg = "Explored"
    elif nsp_event_studio_2 == 5 :
        $ nsp_germiona_studio_2_statimg = "Full"
        
### Event Studio_3

    if nsp_event_studio_3 == 0 and nsp_genie_writer >= 0 and nsp_genie_photocamera >= 1 :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_3_statimg = "New"
    elif nsp_event_studio_3 == 1 :            
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_3_statimg = "New"
        else :
            $ nsp_germiona_studio_3_statimg = "Explored"
    elif nsp_event_studio_3 == 2 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_3_statimg = "New"
        else :
            $ nsp_germiona_studio_3_statimg = "Explored"
    elif nsp_event_studio_3 == 3 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_3_statimg = "New"
        else :
            $ nsp_germiona_studio_3_statimg = "Explored"
    elif nsp_event_studio_3 == 4 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_3_statimg = "New"
        else :
            $ nsp_germiona_studio_3_statimg = "Explored"
    elif nsp_event_studio_3 == 5 :
        $ nsp_germiona_studio_3_statimg = "Full"
        
### Event Studio_4

    if nsp_event_studio_4 == 0 and nsp_genie_writer >= 0 and nsp_genie_sphere_video :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 15 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_4_statimg = "New"
    elif nsp_event_studio_4 == 1 :            
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_4_statimg = "New"
        else :
            $ nsp_germiona_studio_4_statimg = "Explored"
    elif nsp_event_studio_4 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_4_statimg = "New"
        else :
            $ nsp_germiona_studio_4_statimg = "Explored"
    elif nsp_event_studio_4 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_4_statimg = "New"
        else :
            $ nsp_germiona_studio_4_statimg = "Explored"
    elif nsp_event_studio_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_4_statimg = "New"
        else :
            $ nsp_germiona_studio_4_statimg = "Explored"
    elif nsp_event_studio_4 == 5 :
        $ nsp_germiona_studio_4_statimg = "Full"
        
### Event Studio_5

    if nsp_event_studio_5 == 0 and nsp_genie_writer >= 0 and nsp_genie_photocamera >= 1 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_5_statimg = "New"
    elif nsp_event_studio_5 == 1 :            
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_5_statimg = "New"
        else :
            $ nsp_germiona_studio_5_statimg = "Explored"
    elif nsp_event_studio_5 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_5_statimg = "New"
        else :
            $ nsp_germiona_studio_5_statimg = "Explored"
    elif nsp_event_studio_5 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_5_statimg = "New"
        else :
            $ nsp_germiona_studio_5_statimg = "Explored"
    elif nsp_event_studio_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_5_statimg = "New"
        else :
            $ nsp_germiona_studio_5_statimg = "Explored"
    elif nsp_event_studio_5 == 5 :
        $ nsp_germiona_studio_5_statimg = "Full"
        
### Event Studio_6

    if nsp_event_studio_6 == 0 and nsp_genie_writer >= 0 and nsp_genie_sphere_video :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 35 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_6_statimg = "New"
    elif nsp_event_studio_6 == 1 :            
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_6_statimg = "New"
        else :
            $ nsp_germiona_studio_6_statimg = "Explored"
    elif nsp_event_studio_6 == 2 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 90 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_6_statimg = "New"
        else :
            $ nsp_germiona_studio_6_statimg = "Explored"
    elif nsp_event_studio_6 == 3 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 110 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_6_statimg = "New"
        else :
            $ nsp_germiona_studio_6_statimg = "Explored"
    elif nsp_event_studio_6 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 130 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_studio_6_statimg = "New"
        else :
            $ nsp_germiona_studio_6_statimg = "Explored"
    elif nsp_event_studio_6 == 5 :
        $ nsp_germiona_studio_6_statimg = "Full"
        
### Theme Sex
    $ nsp_germiona_statimg_studio = "Full"
    
    if nsp_germiona_studio_1_statimg != "Full" and nsp_germiona_studio_1_statimg != "Full_block" :
        $ nsp_germiona_statimg_studio = "Explored"
    elif  nsp_germiona_studio_2_statimg != "Full" and nsp_germiona_studio_2_statimg != "Full_block":
        $ nsp_germiona_statimg_studio = "Explored"
    elif  nsp_germiona_studio_3_statimg != "Full" and nsp_germiona_studio_3_statimg != "Full_block":
        $ nsp_germiona_statimg_studio = "Explored"
    elif  nsp_germiona_studio_4_statimg != "Full" and nsp_germiona_studio_4_statimg != "Full_block":
        $ nsp_germiona_statimg_studio = "Explored"
    elif  nsp_germiona_studio_5_statimg != "Full" and nsp_germiona_studio_5_statimg != "Full_block":
        $ nsp_germiona_statimg_studio = "Explored"
    elif  nsp_germiona_studio_6_statimg != "Full" and nsp_germiona_studio_6_statimg != "Full_block":
        $ nsp_germiona_statimg_studio = "Explored"
        
    if nsp_germiona_studio_1_statimg == "New":
        $ nsp_germiona_statimg_studio = "New"
    elif  nsp_germiona_studio_2_statimg == "New":
        $ nsp_germiona_statimg_studio = "New"
    elif  nsp_germiona_studio_3_statimg == "New":
        $ nsp_germiona_statimg_studio = "New"
    elif  nsp_germiona_studio_4_statimg == "New":
        $ nsp_germiona_statimg_studio = "New"
    elif  nsp_germiona_studio_5_statimg == "New":
        $ nsp_germiona_statimg_studio = "New"
    elif  nsp_germiona_studio_6_statimg == "New":
        $ nsp_germiona_statimg_studio = "New"

    return      
    
    
    
    
    
label nsp_vague_idea:
    show screen blktone8
    ">Вы не можете точно сформулировать новую идею. Возможно повышение писательского мастерства или какие-то особые условия могли бы помочь."
    hide screen blktone8
    return
    
label nsp_hermione_goout:

hide screen bld1
$herView.hideQ()
hide screen bld1
$herView.hideQ() 
hide screen blktone 
hide screen hermione_02
hide screen ctc
with d3

if daytime:
    $ hermione_takes_classes = True
else:
    $ hermione_sleeping = True
        
    return
    
label nsp_bonus_calc :
    
    $ nsp_photo_koef = 0
    $ nsp_ruby_koef = 0
    $ nsp_saphire_koef = 0
    
    if nsp_genie_photocamera == 0 or nsp_genie_sphere_req == "dis" :
        $ nsp_newspaper_bonus_point = nsp_newspaper_bonus_base
        $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base)
        
        if nsp_newspaper_menu == 7 :
            $ nsp_newspaper_menu = 6
        
        return
    
    if not nsp_genie_sphere_video :
        if nsp_genie_photocamera == 1 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с ч/б фото"
            $ nsp_photo_koef = 2
        elif nsp_genie_photocamera == 2 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с цв. фото"
            $ nsp_photo_koef = 4
        elif nsp_genie_photocamera == 3 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с 3д-фото"
            $ nsp_photo_koef = 6
        elif nsp_genie_photocamera == 4 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с живыми фото"
            $ nsp_photo_koef = 10
            
        if nsp_genie_sphere_ruby_level_eff == 0 :
            $ nsp_ruby_koef = 0
        elif nsp_genie_sphere_ruby_level_eff == 1 :
            $ nsp_ruby_koef = 1
        elif nsp_genie_sphere_ruby_level_eff == 2 :
            $ nsp_ruby_koef = 1.3
        elif nsp_genie_sphere_ruby_level_eff == 3 :
            $ nsp_ruby_koef = 1.5
        elif nsp_genie_sphere_ruby_level_eff == 4 :
            $ nsp_ruby_koef = 1.7
        elif nsp_genie_sphere_ruby_level_eff == 5 :
            $ nsp_ruby_koef = 2
            
        if nsp_genie_sphere_sapphire_level_eff == 0 :
            $ nsp_saphire_koef = 0
        elif nsp_genie_sphere_sapphire_level_eff == 1 :
            $ nsp_saphire_koef = 0
        elif nsp_genie_sphere_sapphire_level_eff == 2 :
            $ nsp_saphire_koef = 0.1
        elif nsp_genie_sphere_sapphire_level_eff == 3 :
            $ nsp_saphire_koef = 0.3
        elif nsp_genie_sphere_sapphire_level_eff == 4 :
            $ nsp_saphire_koef = 0.6
        elif nsp_genie_sphere_sapphire_level_eff == 5 :
            $ nsp_saphire_koef = 1
            
        $ nsp_newspaper_bonus_point = int ( nsp_newspaper_bonus_base * (1 + (nsp_photo_koef * nsp_ruby_koef * nsp_saphire_koef)) )
        
        if nsp_newspaper_menu == 7 :
            $ nsp_newspaper_menu = 6
            
        $ nsp_genie_photocamera_exp += 1
        
        if nsp_genie_sphere :
            $ nsp_genie_sphere_level_exp += 1
        
            call nsp_genie_sphere_level_check
        
        return
        
    else :          
        if nsp_genie_sphere_ruby_level_eff == 0 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base)
            $ nsp_ruby_koef = 0
        elif nsp_genie_sphere_ruby_level_eff == 1 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с 30 сек видео"
            $ nsp_ruby_koef = 15
        elif nsp_genie_sphere_ruby_level_eff == 2 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с 1 мин видео"
            $ nsp_ruby_koef = 25
        elif nsp_genie_sphere_ruby_level_eff == 3 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с 2 мин видео"
            $ nsp_ruby_koef = 35
        elif nsp_genie_sphere_ruby_level_eff == 4 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с 5 мин видео"
            $ nsp_ruby_koef = 55
        elif nsp_genie_sphere_ruby_level_eff == 5 :
            $ nsp_newspaper_bonus_text = "  Развратная статья\n  " + str (nsp_newspaper_bonus_text_base) + "\n   с 10 мин видео"
            $ nsp_ruby_koef = 80
            
        if nsp_genie_sphere_sapphire_level_eff == 0 :
            $ nsp_saphire_koef = 0
        elif nsp_genie_sphere_sapphire_level_eff == 1 :
            $ nsp_saphire_koef = 0
        elif nsp_genie_sphere_sapphire_level_eff == 2 :
            $ nsp_saphire_koef = 0.1
        elif nsp_genie_sphere_sapphire_level_eff == 3 :
            $ nsp_saphire_koef = 0.3
        elif nsp_genie_sphere_sapphire_level_eff == 4 :
            $ nsp_saphire_koef = 0.6
        elif nsp_genie_sphere_sapphire_level_eff == 5 :
            $ nsp_saphire_koef = 1
            
        $ nsp_newspaper_bonus_point = int ( nsp_newspaper_bonus_base * (1 + (nsp_ruby_koef * nsp_saphire_koef)) )
        
        $ nsp_genie_sphere_level_exp += 1
        
        call nsp_genie_sphere_level_check
        
        if nsp_newspaper_menu == 7 :
            $ nsp_newspaper_menu = 6
        
        return


    $ nsp_newspaper_bonus_point = nsp_newspaper_bonus_base
  
    if nsp_newspaper_menu == 7 :
        $ nsp_newspaper_menu = 6
    
    return
    
label nsp_bonus_calc_photo :
    
    $ nsp_photo_koef = 0
    
    if nsp_genie_photocamera == 0 :
        $ nsp_newspaper_bonus_point = nsp_newspaper_bonus_base
        
        if nsp_newspaper_menu == 7 :
            $ nsp_newspaper_menu = 6
        
        return
    
    if nsp_genie_photocamera == 1 :
        $ nsp_newspaper_bonus_text = "  Ч/б развратные фото\n   Гермионы"
        $ nsp_photo_koef = 2
    elif nsp_genie_photocamera == 2 :
        $ nsp_newspaper_bonus_text = "  Цв развратные фото\n   Гермионы"
        $ nsp_photo_koef = 4
    elif nsp_genie_photocamera == 3 :
        $ nsp_newspaper_bonus_text = "  Развратные 3д-фото\n   Гермионы"
        $ nsp_photo_koef = 6
    elif nsp_genie_photocamera == 4 :
        $ nsp_newspaper_bonus_text = "  Живые развратные фото\n   Гермионы"
        $ nsp_photo_koef = 10
    
    $ nsp_newspaper_bonus_point = int ( nsp_newspaper_bonus_base * (1 + nsp_photo_koef ) * (0.5 + ( nsp_germiona_artistry / 3)) )
    $ nsp_genie_photocamera_exp += 1
    
    if nsp_newspaper_menu == 6 and cur_level >= 2 :
        $ nsp_newspaper_menu = 7
    
    return
        
label nsp_bonus_calc_video :
    
    $ nsp_photo_koef = 0
    
    if nsp_genie_photocamera == 0 or not nsp_genie_sphere_video :
        $ nsp_newspaper_bonus_point = nsp_newspaper_bonus_base
        
        if nsp_newspaper_menu == 7 :
            $ nsp_newspaper_menu = 6
        
        return
              
    if nsp_genie_sphere_ruby_level_eff == 0 :
        $ nsp_newspaper_bonus_text = "  Развратная статья\n   о Гермионе"
        $ nsp_ruby_koef = 0
    elif nsp_genie_sphere_ruby_level_eff == 1 :
        $ nsp_newspaper_bonus_text = "  30 сек развратного видео\n   Гермионы"
        $ nsp_ruby_koef = 15
    elif nsp_genie_sphere_ruby_level_eff == 2 :
        $ nsp_newspaper_bonus_text = "  1 мин развратного видео\n   Гермионы"
        $ nsp_ruby_koef = 25
    elif nsp_genie_sphere_ruby_level_eff == 3 :
        $ nsp_newspaper_bonus_text = "  2 мин развратного видео\n   Гермионы"
        $ nsp_ruby_koef = 35
    elif nsp_genie_sphere_ruby_level_eff == 4 :
        $ nsp_newspaper_bonus_text = "  5 мин развратного видео\n   Гермионы"
        $ nsp_ruby_koef = 55
    elif nsp_genie_sphere_ruby_level_eff == 5 :
        $ nsp_newspaper_bonus_text = "  10 мин развратного видео\n   Гермионы"
        $ nsp_ruby_koef = 80
            
    $ nsp_newspaper_bonus_point = int ( nsp_newspaper_bonus_base * (1 + (nsp_ruby_koef/2)) )
    
    if nsp_newspaper_menu == 7 :
        $ nsp_newspaper_menu = 6
        
    $ nsp_genie_sphere_level_exp += 1
        
    call nsp_genie_sphere_level_check
        
    return
    
label nsp_genie_sphere_level_check :

    if nsp_genie_sphere_level == 0 and nsp_genie_sphere_level_exp >= 2 :
        $ nsp_genie_sphere_level_exp = 0
        $ nsp_genie_sphere_level += 1
        ">Ваше мастерство владения Хрустальным шаром повысилось до [nsp_genie_sphere_level] уровня."
    elif nsp_genie_sphere_level == 1 and nsp_genie_sphere_level_exp >= 5 :
        $ nsp_genie_sphere_level_exp = 0
        $ nsp_genie_sphere_level += 1
        ">Ваше мастерство владения Хрустальным шаром повысилось до [nsp_genie_sphere_level] уровня."
    elif nsp_genie_sphere_level == 2 and nsp_genie_sphere_level_exp >= 10 :
        $ nsp_genie_sphere_level_exp = 0
        $ nsp_genie_sphere_level += 1
        ">Ваше мастерство владения Хрустальным шаром повысилось до [nsp_genie_sphere_level] уровня."
    elif nsp_genie_sphere_level == 3 and nsp_genie_sphere_level_exp >= 20 :
        $ nsp_genie_sphere_level_exp = 0
        $ nsp_genie_sphere_level += 1
        ">Ваше мастерство владения Хрустальным шаром повысилось до [nsp_genie_sphere_level] уровня."
    elif nsp_genie_sphere_level == 4 and nsp_genie_sphere_level_exp >= 30 :
        $ nsp_genie_sphere_level_exp = 0
        $ nsp_genie_sphere_level += 1
        ">Ваше мастерство владения Хрустальным шаром повысилось до [nsp_genie_sphere_level] уровня."
        
    $ nsp_genie_sphere_ruby_level_eff = nsp_genie_sphere_ruby_level
    $ nsp_genie_sphere_diamond_level_eff = nsp_genie_sphere_diamond_level
    $ nsp_genie_sphere_sapphire_level_eff = nsp_genie_sphere_sapphire_level
        
    if nsp_genie_sphere_level == 0 :
        if nsp_genie_sphere_ruby_level_eff > 0 :
            $ nsp_genie_sphere_ruby_level_eff = 0
        if nsp_genie_sphere_diamond_level_eff > 0 :
            $ nsp_genie_sphere_diamond_level_eff = 0
        if nsp_genie_sphere_sapphire_level_eff > 1 :
            $ nsp_genie_sphere_sapphire_level_eff = 1
    elif nsp_genie_sphere_level == 1 :
        if nsp_genie_sphere_ruby_level_eff > 1 :
            $ nsp_genie_sphere_ruby_level_eff = 1
        if nsp_genie_sphere_diamond_level_eff > 2 :
            $ nsp_genie_sphere_diamond_level_eff = 2
        if nsp_genie_sphere_sapphire_level_eff > 3 :
            $ nsp_genie_sphere_sapphire_level_eff = 3
    elif nsp_genie_sphere_level == 2 :
        if nsp_genie_sphere_ruby_level_eff > 2 :
            $ nsp_genie_sphere_ruby_level_eff = 2
        if nsp_genie_sphere_diamond_level_eff > 3 :
            $ nsp_genie_sphere_diamond_level_eff =  3
        if nsp_genie_sphere_sapphire_level_eff > 4 :
            $ nsp_genie_sphere_sapphire_level_eff = 4
    elif nsp_genie_sphere_level == 3 :
        if nsp_genie_sphere_ruby_level_eff > 3 :
            $ nsp_genie_sphere_ruby_level_eff = 3
        if nsp_genie_sphere_diamond_level_eff > 3 :
            $ nsp_genie_sphere_diamond_level_eff = 3
        if nsp_genie_sphere_sapphire_level_eff > 4 :
            $ nsp_genie_sphere_sapphire_level_eff = 4
    elif nsp_genie_sphere_level == 4 :
        if nsp_genie_sphere_ruby_level_eff > 4 :
            $ nsp_genie_sphere_ruby_level_eff = 4
        if nsp_genie_sphere_diamond_level_eff > 4 :
            $ nsp_genie_sphere_diamond_level_eff = 4
        if nsp_genie_sphere_sapphire_level_eff > 5 :
            $ nsp_genie_sphere_sapphire_level_eff = 5

    return