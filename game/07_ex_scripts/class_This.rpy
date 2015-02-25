init -992 python:
  
# Класс - тот же EventCollection , только со специфическим объявлениями
    class This(EventCollection): # Код специфический для игры, все в этом классе
        def __init__(self):
            super(This, self).__init__()
            self.Name=None

# this("event_01") пытается вернуть Event c именем event_01 (None, если не нашел в списке)
# Запоминает парметр - последнее обращение
        def __call__( self, sName=None):
            if (sName!=None): 
                this.Name=sName
# Если уже активирована глобальная переменная event, ей присваивается новое значение, если, конечно, это ивент 
            e=self.GetCall(self.Name)
            if hasattr(renpy.store,"event") and (e!=None): 
                renpy.store.event=e
            return e



# НЕ ПРИНАДЛЕЖИТ КЛАССУ
    def OnLabelExecute(s):
        try:
            if s[0]!="_":
                labelHistory.append(s)
                if len(labelHistory)>120:
                    del labelHistory[0:len(labelHistory)-121]

    # Каждый раз при переходе по метке происходит проверка - не имя ли ивента метка? Если да, переменной event присваивается значение, согласно текущей метке
                if this(s)!=None:
    # Если перешли на метку, которая есть ивент, автоматически запускается увеличение счетчика стартов-финишей. 
    # Случаи, когда ивент завершается на середине (и требуют уменьшения счетчика финишей) обрабатываются в коде самого ивента                
                    debug.SaveString("event.IncPassed()="+s+"   "+this().Name)
                    this().IncPassed()

        except Exception:
            pass


# Если текущий ивент - единственный после метки actualLabel, то пометить его, как не финишировавший.
# Пример: на метку too_much переход происходит только если Гермиона отказывается выполнять задания
# Часть из этих заданий оформлены как ивенты, часть - нет. Все задания начинаються после метки захода в меню выбора заданий
# Значит надо отследить запускался ли текущий ивент (хранящийся в event) после метки захода в меню выбора заданий, и если да, то откатить финиширование
# Альтернатива: 1. Все задания оформить как ивенты и ставить в too_much $event.NotFinished() без этого условия  2. В кажом ивенте перед каждой директивой jump too_much ставить $event.NotFinished()
    def IsEventOnlyAfter(actualLabel):
        for s in reversed(labelHistory[0:len(labelHistory)-2]): 
            if s==actualLabel:
                break
            if not this.GetCall(s) in [None, renpy.store.event.Name]: # Если результат - ивент, отличный от заданного
                return False
        return True

    def Execute(e, s, condition=True):
        if not condition: return False
        s=s.replace("_e.", "this.GetCall('"+e.Name+"').")
        exec s
        return True


    def Rand(iMax): #от 1 до iMax
        import random 
        return int(random.random()*iMax+1)

    def RandFromSet(availSet, onetimeSet={}):
        o=list(availSet)[Rand(len(availSet))-1]
        if o in onetimeSet:
            availSet-={o}                
        return o

    def GetStage(value, minValue, maxLevel=3, step=3): # Получить фазу в которой находится прохождение ивента. 0 - невозможно пройти, дальше - уровни
        value=value-minValue
        if value<0: return 0
        if int(value/step)+1>=maxLevel: return maxLevel
        return int(value/step)+1

    def OnValueChange(e, subKey, oldVal, newVal):
        if ("NIGHT" in e._points): # Если вторая половина публичной услуги - произвести случайный выбор варианта
            s="one_out_of_three=RandFromSet(_e._availChoices)" 
            if e.Name=="new_request_30_complete":
                s="one_out_of_three=RandFromSet(_e._availChoices,{1})"
            Execute(e,s, subKey=="startCount")  

#        debug.SaveString("Class="+e.Name+" subkey="+subKey)
#        debug.SaveClass(e.Name)
        if ("hearts" in e._points) and subKey=="whored": # Если требуется расчет количества сердечек - произвести его
            step=3
            if e._startWhoring==21: step=1 # На макс. ивенте сердечко за 1 балл
            if e._startWhoring==18: step=2 # На предпоследнем до макс. сердечко за 2 балла
            e.SetValue("heartCount",GetStage(newVal,e._startWhoring,3,step))
        return

#    def OnJumpExecute(loc, target, expression):
#        try:
#            if s[0]!="_":
#            jumpHistory.append({loc, target, expression})


#        except Exception:
#            pass



