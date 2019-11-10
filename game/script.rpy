# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define py =     Character("Python")
define java =       Character("Java")
define c =          Character("C")
define user =       Character("User")
init:
    $ pyAff=        0
    $ javaAff =     0
    $ cAff =        0
    $ pyEvent =     0
    $ javaEvent =   0
    $ cEvent =      0
    $ days =        0
    $ mclass = "audio/classroom_music.mp3"
    $ mbed = "audio/bedroom_music.mp3"
    $ mcafe = "audio/cafe_music.mp3"
    $ mclub = "audio/clubroom_music.mp3"
    $ mfield = "audio/field_music.mp3"
    $ mhall = "audio/hallway_music.mp3"
    $ mlib = "audio/library_music.mp3"
    $ mrace = "audio/Python_Race_Event_Music.mp3"
    $ mroof = "audio/rooftop_music.mp3"
    $ mschool = "audio/schoolgate_music.mp3"
$ fade =            Fade(2, 3, 2)

# The game starts here.

label start:
    with fade
    label day1:

        scene       bedroom
        $ renpy.music_start(mbed)
        "I’ve finally moved out to live on my own! I’m so excited, I wonder what it’s going to be like, and who I’m going to meet."
        "Tomorrow will be the first day of school, I hope it goes smoothly. I want to meet a bunch of new people and maybe even join a club!"
        "But what kind of club do I want to join? Do I choose based on whose in the club? Or should I focus on my interests? Maybe I’ll just join whatever club the friends I make are in, God I hope I can make some new friends."
        "Well whatever, overthinking everything isn’t going to help. I just have to finish packing and I’ll go to sleep. Gotta make sure I’m at my best tomorrow to make a good impression!"

        $ renpy.music_stop()

    label day2:

        scene       bedroom
        $ renpy.music_start(mbed)
        with        fade
        "Okay. First day. Lots do to."
        "I'm up thirty minutes earlier than planned, but I might as well head to school now. This'll give me time in case I get lost or something."

        $ renpy.music_stop()

        scene       field
        $ renpy.music_start(mfield)
        with        fade
        "Woah, their athletics complex is big. Look at all the clubs practicing already!"
        "It looks like the track and field club... Maybe I should join them, I could always use the exercise."
        show        pyimage
        with        fade
        "Wow, she's so much faster than the others... she's got to be the captain or something."
        "There's something elegant about how she runs... simple, yet efficient, with no wasted movement."
        "Oh, she's looking this way."
        "Track Girl" "Heeeeeeeey!"
        user "Oh, uh, hey!"
        "I wave back but she's already run by. She leaps over hurdles with ease, and I can’t help but to look on in awe for a moment."
        "Maybe if I join the track team, I can be like that person as well?"

        $ renpy.music_stop()

        scene       schoolgate
        $ renpy.music_start(mschool)
        with        fade
        "I was told that the student council president would show me around the school today, but I don't see them anywhere..."
        "I wonder if I'll see her tomorrow or something. I hope so, because it'll be a pain to figure out where everything is on my own."

        $ renpy.music_stop()

        scene       classroom
        $ renpy.music_start(mclass)
        with        fade
        "There aren't many people here yet. I guess I did come here early... the track team was pretty early, too."
        "This classroom is pretty big! I wonder if it'll get full."

        $ renpy.music_stop()

        scene       schoolgate
        $ renpy.music_start(mschool)
        with        fade
        "Nothing really happened today, but the track club seems like it'll be fun."
        "I never got to see the student council president, either."
        "Oh well, I got around well enough today. I guess I'll just go home."

        $ renpy.music_stop()

        scene       bedroom
        $ renpy.music_start(mbed)
        with        fade
        "It was a pretty good day today, I hope I get to start making friends tomorrow though."

        $ renpy.music_stop()

    label day3:

        scene       schoolgate
        $ renpy.music_start(mschool)
        with        fade
        "Second day of school! I wonder if I'll see that runner again today."

        $ renpy.music_stop()

        scene       classroom
        $ renpy.music_start(mclass)
        with        fade
        "???" "is User here?"
        user "Yes, that's me."
        show        java
        with        fade
        java "Hi, I'm the student council president, Java Oracle."
        java "Sorry I couldn't show you around yesterday... I misplaced some objects in the wrong array, and that threw errors around everywhere."
        java "It took more time than I thought to re-organize everything... I apologize once again."
        user "Oh, that's okay. I didn't really run into any trouble."
        java "Glad to hear it! Come on, I'll show you around..."
        user "Thank you, president!"
        java "Please, call me Java."

        $ renpy.music_stop()

        scene       schoolgate
        $ renpy.music_start(mschool)
        show        java
        with        fade
        "Java spent the morning introducing me to various departments and clubs around the school."
        user "The school is bigger than I thought, I'm glad to have someone showing me around."
        java "My pleasure! And for our sports, we have tennis, track and field..."
        user "Track and field?"
        java "Are you interested?"
        user "Yeah... kinda. I'm just looking for a club I might like to join."
        java "That's great!"
        java "... It's not exactly a club, but the student council might be interested in someone as enthusiastic as you."
        user "Really? Wouldn't I be too inexperienced?"
        java "Not at all! We would love to have some fresh bloo..."
        java "*Ahem* I mean some new students as members!"
        java "We also have a club fair you can check out."
        user "When will it be?"
        java "In about a week."
        user "That's awesome! I'll definitely be there."
        java "That's great to hear! In the meantime, do you need anything else?"
        user "Can you show me where the library is again? I need to pick up some books for class."
        java "Sure thing, User!"
        "Afterwards, Java showed me where the library is."
        "We talked for a little bit, althought It was mostly Java trying to recruit me."
        "It got a bit late, so I went home afterwards."

        $ renpy.music_stop()

        scene       bedroom
        $ renpy.music_start(mbed)
        with        fade
        "Java was a lot of fun to hang out with today, although it would be nice to get to talk to that runner girl again."
        "Guess I'll just have to wait and see what tomorrow holds."

        $ renpy.music_stop()

    label day4:
        scene       schoolgate
        $ renpy.music_start(mschool)
        with        fade
        "School is finally over! I think I'm getting used to the lessons, but extra studying won't hurt."
        "If I remember right, the library was this way..."

        $ renpy.music_stop()

        scene       library
        $ renpy.music_start(mlib)
        with        fade
        "Mmm... It's a nice library."
        "There's the help desk! I should ask ask where the book I need is."
        user "Hello, where can I find the book [String Theory]?"
        "Library Worker" "It should be in that section of the library."
        user "Thank you!"
        user "String... String... No, not char! Ugh...."
        user "Ah! Here it is! Glad I found it."
        show        c
        with        fade
        "girl" "String theory.. I wanted that..."
        user "Oh, were you looking for the same book? It doesn't look like they have a second copy..."
        user "You can borrow it before me."
        "girl" "Really? Thanks. I'll try to return the String in one piece, not a character array."
        hide        c
        with        fade
        "I guess I can try to come back sometime to see if the book is still there."
        "For now, I might as well go home."

        $ renpy.music_stop()

        scene       bedroom
        $ renpy.music_start(mbed)
        with        fade
        "Finally time for bed again."

        $ renpy.music_stop()

    label choose:
        if days == 3:
            if pyAff > javaAff and pyAff > cAff:
                jump day8py
            if cAff > javaAff and cAff > pyAff:
                jump day8c
            if javaAff > pyAff and javaAff > cAff:
                jump day8j
            if javaAff < 1 and pyAff < 1 and cAff < 1:
                jump gameOver
            jump day8py
        scene       bedroom
        $ renpy.music_start(mbed)
        with        fade
        $ days += 1
        menu        whatToDo:
            "Where should I go today?"
            "Track Field":
                if pyEvent == 1:
                    $ pyEvent += 1
                    jump w1py2
                if pyEvent == 2:
                    $ pyEvent += 1
                    jump w1py3
                $ pyEvent += 1
                jump w1py1
            "Student Council Club Room":
                if javaEvent == 1:
                    $ javaEvent += 1
                    jump w1j2
                if javaEvent == 2:
                    $ javaEvent += 1
                    jump w1j3
                $ javaEvent += 1
                jump w1j1
            "Library":
                if cEvent == 1:
                    $ cEvent += 1
                    jump w1c2
                if cEvent == 2:
                    $ cEvent += 1
                    jump w1c3
                $ cEvent += 1
                jump w1c1

    label w1j1:
        $ renpy.music_stop()

        scene clubroom
        $ renpy.music_start(mclub)
        show java
        with fade
        $ javaAff += 1

        user "Hello? is this the student council?"
        java "Hey User, I’m so glad you came!"
        user "Huh, so this is the famous student council."
        java "Yep! In the flesh!"
        user "Everything is so organized and neat here."
        java "Yeah, I really like to structure things, it makes it much easier to access whatever I need. Although some people say I am a bit obsessive."
        user "I think it’s nice though, at least you know where everything is, you’ll never lose anything."
        java "I know right! Actually, since you’re here, I need some help."
        java "I have this book about cats here, where should I put it?"

        menu:
            "Hmm, you should put it in the pet drawer, since cat is a pet.":
                jump c1j1
            "I think the animal drawer is fine.":
                jump c1j2
            "A cat belongs anywhere, so anywhere is fine!.":
                jump c1j3

        label c1j1:
            java "That’s a really good idea! Since cat is a subclass of pet afterall."
            $ javaAff += 1
            jump j1c1cont

        label c1j2:
            java "I think that’s okay."
            jump j1c1cont

        label c1j3:
            java "Eh….Eh??? Wouldn’t putting cat with other pets make more sense? But I guess any object works."
            $ javaAff -= 1
            jump j1c1cont

        label j1c1cont:
            java "Thank you for your input."
            user "No problem! I gotta run to class now, I will see you around!"
            java "See you!"

            $ renpy.music_stop()

            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "I didn't realize how much Java loved organization. I guess we all have our interests."
            "Anyways, I better get to bed."

            $ renpy.music_stop()

            jump choose

    label w1j2:
        $ renpy.music_stop()

        scene schoolgate
        $ renpy.music_start(mschool)
        with fade

        "The student council was interesting the last time I went there, I guess I will check it out again"
        $ javaAff += 1

        $ renpy.music_stop()

        scene classroom
        $ renpy.music_start(mclass)
        show java
        with fade
        user "Hey Java, anything interesting happening today?"
        java "Oh hey User, fancy seeing you again."
        java "We’re approving club request forms right now."
        user "What are club request forms?"
        java "It’s when a club wants to request for something, like to reserve a space or for extra funding."
        user "Sounds important, does everything gets approved?"
        java "If the forms are filled correctly then yes, but people don’t actually take time to do it, so they get turn down according to the school policy."
        user "What are some of the things people get wrong."
        java "Oh like, when they declare the wrong type of request, or if they request something that is only accessible by private students."

        menu:
            "I guess it makes sense, the requests have to be formatted correctly or nothing will make sense after all.":
                jump c2j1
            "That’s oddly specific, but I guess that’s just how it works.":
                jump c2j2
            "It’s a bit unnecessary I think.":
                jump c2j3

        label c2j1:
            java "I agree with you, rules exist for a reason!"
            $ javaAff += 1
            jump j2c1cont

        label c2j2:
            java "Yeah."
            jump j2c1cont

        label c2j3:
            java "I think rules exist for a reason, but to each their own."
            $ javaAff -= 1
            jump j2c1cont

        label j2c1cont:
            user "Anything else you do besides approving forms?"
            java "We are also working on the club fair later, you’re more than welcome to join us to organize."
            user "I’ll think about it. I’m going to class now. Good luck with the forms."
            java "Thanks, see you later!"

            $ renpy.music_stop()

            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "I don't think I can keep up with Java's organization, I need to sleep more than ever after today."

            $ renpy.music_stop()

            jump choose

    label w1j3:
        $ renpy.music_stop()

        scene schoolgate
        $ renpy.music_start(mschool)
        with fade

        user "I don’t really know what to do now, maybe I’ll help Java with the club fair."
        $ javaAff += 1

        $ renpy.music_stop()

        scene clubroom
        $ renpy.music_start(mclub)
        show java
        with fade
        user "Java? Hello? Java? Is that you in the paper pile?"
        java "User? Hi! Umm….. I have a bit too much of club fair entries, but my drawers don’t have space for them."
        java "I tried stuffing them but that didn’t work."
        user "That sounds rough, here let me help pick everything up."
        with fade
        user "So now what do we do with all of these?"
        java "I'm not sure, we don't have space in the drawers anymore."

        menu:
            "We can report to the school that the entries are too much for the club room.":
                jump c3j1
            "We can try to get more drawers?":
                jump c3j2
            "We can try to stuff them in the drawers again.":
                jump c3j3

        label c3j1:
            java "Yeah, maybe the school would know what to do with them!"
            $ javaAff += 1
            jump j3c1cont

        label c3j2:
            java "I don’t think the clubroom has any more space for drawers, let’s report this to the school."
            jump j3c1cont

        label c3j3:
            java "The only way that can happen is if we remove some entries from the drawer. I think we should report this to the school."
            $ javaAff -= 1
            jump j3c1cont

        label j3c1cont:
            user "Okay, let’s go to the school then. After reporting the problem to the school, we went back to the club room."
            user "Thank goodness the school can lend us their room to store the entries"
            java "Yeah, it was nice of them to do that."
            java "Thanks User, that was nice of you."
            user "I gotta run now, see you later?"
            java "Of course!"

            $ renpy.music_stop()

            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "I don't think I can keep up with Java's organization, I need to sleep more than ever after today."

            $ renpy.music_stop()

            jump choose

    label day8j:
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade

        "Hmm... I got a text..."
        "Oh, it's from Java, she wants to eat lunch with me today."
        "I guess I have nothing else to do... might as well."

        $ renpy.music_stop()

        scene cafe
        $ renpy.music_start(mcafe)
        with fade

        java "Hey User! Over here!"

        show java
        with fade

        user "Hey Java!"
        java "Thanks for coming today!"
        java "This is my favorite restaurant in town, you see."
        java "The food is really nice, and the place is very organized as well!"
        user "I bet it is. I can't wait to eat."
        user "Anyways, what's the occasion for calling me out here?"
        java "Oh, I was just wondering if maybe you were interested in the student council?"
        java "You looked interested in the past couple days, coming to help us and all."

        menu:
            "It looked nice, I really like the work that you do and the impact you’re making. Also I love how organized everything is with you":
                jump w2c1j1
            "I don’t know. It sounds like a grand time, but I’m worried that it may take up too much time":
                jump w2c1j2
            "Maybe.... but it doesn't seem to suit me too well.":
                jump w2c1j3

        label w2c1j1:
            java "Thank you User, that means a lot to me."
            $ javaAff += 1
            jump j1cont

        label w2c1j2:
            java "Yeah, it can look intimidating at first, but I think you’ll find it’s pretty easy to get the hang of."
            jump j1cont

        label w2c1j3:
            java "That’s too bad, you would’ve been perfect for the student council."
            $ javaAff -= 1
            jump j1cont

        label j1cont:
            "We spoke for a while longer. Java seemed pretty keen on getting me to join the student council."
            "I'll have to give it some more thought."
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Im glad Java and I are getting along, it's been a lot of fun!"
            "Well, time to get some rest."
            $ renpy.music_stop()
            jump day9j

    label day9j:
        scene classroom
        $ renpy.music_start(mclass)
        with fade
        "Yesterday was a lot of fun with Java, I’m glad she invited me to join her club, but I don’t really know if I have what it takes."
        "Speak of the devil, here she is now."

        show java
        with fade

        java "Hey User! Thank you for meeting me yesterday, it was a lot of fun."
        user "I should be thanking you!"
        java "So, what’s your thoughts on joining?"
        user "I'm interested! The club seems like a lot of fun, but I’m still not totally sure."
        java "How about we get lunch together tomorrow? At the roof of the school? The view’s pretty nice there."
        user "Sure thing! I’ll see you there tomorrow."
        java "Okay! I’ll see you later."
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "Im excited to eat on the roof tomorrow, I havn't had a chance to check out the view!"
        "Better get to bed though, the sooner I sleep, the sooner I get to meet up with Java."
        $ renpy.music_stop()
        jump day10j

    label day10j:
        scene rooftop
        $ renpy.music_start(mroof)
        show java
        with fade
        java "Hey User, thanks for coming up here to meet me!"
        user "Thanks for inviting me. I didn’t realize we had such an awesome view!"
        user "Yeah, but that’s not why I wanted to bring you here, I actually had a question!"
        java "Yeah. It is. I asked you to come to ask you about something, though."
        user "Sure thing, what is it?"
        java "Well first, I wanted to know if you’d made up your mind yet?"
        user "Yeah, I think I really do want to join the book club!"
        java "Great! Well then about my question. If I’m going to recommend to let you in, I feel like we should know each other better."
        java "So I planned a fun little test!"
        user "Uh, ok. What did you have in mind?"
        java "I just need you to answer one question about me."
        java "If footBall and tennisBall are subclasses of genericBall, how would they be able to call the private variable diameter?"

        menu:
            "You can call the variable directly by using this.diameter, because the subclass has access to the variables of the superclass":
                jump w2c2j1
            "You have to create a public getDiameter() method, then pass the private variable as a return":
                jump w2c2j2

        label w2c2j1:
            java "Mmm… That’s not quite right."
            java "Since the variable is private, a subclass would not be able to access it."
            $ javaAff -= 2
            jump j2cont

        label w2c2j2:
            java "Yes! I see that you are well-organized in your thought process. That's good!"
            $ javaAff += 1
            jump j2cont

        label j2cont:
            "Bells ring"
            java "We should head back to class."
            user "You're right. I'll see you around!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Man, I wasn't expecting that question from Java."
            "Racking my brain about why she's asking these questions won't do any good, time for bed."
            $ renpy.music_stop()
            jump day11j

    label day11j:
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "The quiz is ofinally over! Thank God I studied for that one."
        "I should head over to the student council room and see how Java did."
        $ renpy.music_stop()
        scene clubroom
        $ renpy.music_start(mclub)
        show java
        with fade
        user "Hey Java!"
        java "Hey User! What's up?"
        user "I was going to ask you about the quiz! Was wondering how you did."
        java "I actually did fairly well, I'm pretty happy about it."
        user "As expected of our student council president!"
        java "Oh! Right, I wanted to ask, can you come and help us out tomorrow? We have a lot to prepare!"
        user "Sure! My pleasure."
        java "Great, thank you!"
        user "I’ll see you tomorrow then."
        java "See you then!"
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "Time for bed, I wonder what Java will have me doing tomorrow."
        $ renpy.music_stop()
        jump day12j

    label day12j:
        scene clubroom
        $ renpy.music_start(mclub)
        show java
        with fade
        "I show up to the student council room, as always, I help Java organize and arrange everything."
        "Everything runs smoothly, but it seems like planning for the club fair is a lot more than what the student council is used to."
        "Java, of course, has no problem with it."
        java "Good work everyone! Just one more task to do!"
        java "What kind of music should we play during the club fair?"

        menu:
            "I think something jazzy, because it is a party after all, but we don’t want anything that’s too inappropriate.":
                jump w2c3j1
            "Something exciting, like pop music would be nice.":
                jump w2c3j2
            "We should go all out, and play rock music! It should be an energetic day after all!":
                jump w2c3j3

        label w2c3j1:
            java "That’s a really good idea User!"
            $ javaAff += 1
            jump j3cont

        label w2c3j2:
            java "Hmm... I think that would be nice, but let’s hear other ideas."
            jump j3cont

        label w2c3j3:
            java "I’m not too sure about that..."
            $ javaAff -= 1
            jump j3cont

        label j3cont:
            "After discussing it with everyone else, we decided that jazz would be a good genre to play during the fair."
            user "That was a lot to do."
            java "Oh my, are you tired? I’m so sorry for dragging you into this."
            user "Oh don’t worry about it! I had a lot of fun as well!"
            java "I’m glad you did, since we’re talking about the fair, any chance you would want to join the student council now?"
            user "After spending time with all of you, I think I will put in the application!"
            java "Great! I hope you can get in!"
            user "Me too!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "I' better get to bed, I don't want to be late for the fair tomorrow."
            $ renpy.music_stop()
            jump day13j

    label day13j:
        scene hallway
        $ renpy.music_start(mhall)
        with fade
        "Today's the big day! The club fair is finally here!"
        "I finally have a club I want to register for... I really hope they let me in."
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "After submitting my application, I walk around the fair for a short while, admiring all the different booths and their activities before returning home."
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "I can barely sleep tonight! I hope my application will be accepted tomorrow."
        $ renpy.music_stop()
        jump jend

    label jend:

        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "I can hardly wait to find out if I got into the club!"
        "I should hurry to school."

        if javaAff >= 5:
            jump jaccept
        if javaAff <= 5:
            jump jreject

        label jaccept:
            $ renpy.music_stop()
            scene classroom
            $ renpy.music_start(mclass)
            show java
            with fade

            java "User? User! Great news! You got in!"
            user "Really? I got in!"
            user "I thought with me being a new student and all, I wouldn't a chance against my seniors!"
            java "Not at all! You did help us a lot you know, it only makes sense that you join."
            user "And I’m glad I did! You wanna go have lunch to celebrate this good news?"
            java "Don’t get ahead of yourself."
            java " You do realize that this is only the beginning, and that the real work starts now, right?"
            user "Is that a no on the invite?"
            java "You’re right, we do have to celebrate your joining."
            java "Lunch sounds great!"
            "After we went for lunch and discussed our plans for the student council and future activites."
            "After joining the student council, Java and I became closer and closer. Before I knew it, we became the best of friends."
            "When she graduates, I'm in line to be the next president, I hope that I’ll be as good as she once was."
            $ renpy.music_stop()
            jump EndScreen

        label jreject:

            scene classroom
            $ renpy.music_start(mclass)
            show java
            with fade

            user "Oh hey, Java! How are you doing?"
            java "Fine, I guess."
            user "Any news on my application?"
            java "I actually haven't checked it yet."
            java "Do you want to see it together?"
            user "Sure!"
            "Enthusiastically, I sat down with Java and checked the result."
            "I did not get in."
            "I'm disappointed. But more importantly, I'm embarrassed before the student council president."
            java "I'm so sorry."
            user "It's fine. I'm a new student here after all..."
            user "It'd be out of the norm for me to join the student council so quickly."
            java "Don't put yourself down like that!"
            java "I think you got rejected because the other members don't know you that well yet."
            "I know that Java is trying to comfort me, but I'm still sad I didn't get in."
            user "Well, I can always try again next year, right?"
            java "Exactly! Tell you waht, if you keep helping us, I'm sure the other members will get to know you."
            java "That way, you're basically guaranteeed to get in next time!"
            "I smile, feeling a little more hopeful now."
            user "Sounds great. I'll be seeing you here and there, then, president!"
            java "Of course!"
            $ renpy.music_stop()

            jump EndScreen

    label w1c1:

        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade

        "I'll check the library. That person might have returned by now."
        $ cAff += 1
        $ renpy.music_stop()
        scene library
        $ renpy.music_start(mlib)
        with fade

        "girl" "Oh, it's you."

        show c

        user "Hey! Did you finish the book yet?"
        c "I tried, but I don't think I can understand strings, after all. I'm C, by the way."
        user "We never introduced ourselves, have we? Well, I'm User. Nice to meet you."
        user "So, why were you looking for the String theory book?"
        c "I just didn't understand it in class..."
        c "I can get to the character part, but I just can't seem to put it all together."
        user "Hey, everyone has different talents!"
        user "Don't worry about it. I'm sure you'll find a way."
        c "Hmm... What do you suggest?"
        c "I've had some ideas, but I want to know what you're thinking."

        menu:
            "Maybe show it as a collection of characters? You know, like an array!":
                jump w1c1c1
            "Hmm... I don't know. I'll read the book and get back to you on that.":
                jump w1c1c2
            "I would go to the teacher and ask for help with strings. I'm not too familiar with it myself.":
                jump w1c1c3

        label w1c1c1:
            c "That's a brilliant idea! I'll go try that."
            $ cAff += 1
            jump w1c1cont

        label w1c1c2:
            c "Okay."
            jump w1c1cont

        label w1c1c3:
            c "I really don't think it'll help.. I'll try anyway."
            $ cAff -= 1
            jump w1c1cont

        label w1c1cont:
            c "Well, here's the book. I'm a part of the book club, so if you have any more ideas, you can come find me here."
            user "Thanks! I'll give it a read."
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "It's weird that C has so much trouble with strings, she seems so smart."
            "Well I'm sure she'll figure it out soon, I gotta stop thinking about it and sleep."
            $ renpy.music_stop()
            jump choose

    label w1c2:
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade

        "Hm... the book club sounded interesting. I want to go and learn more about them."
        $ cAff += 1
        $ renpy.music_stop()
        scene library
        $ renpy.music_start(mlib)
        with fade

        user "Hey, C!"

        show c
        with fade

        c "Oh hey, User. How was the book?"
        user "It was pretty interesting. I think I understand it a bit now."
        c "That's good. I gave up on understanding strings... I think I'll manage somehow."
        user "Hmm, ok. You have that quiz in a week or so too, right?"
        c "Yeah... What about it?"
        user "I was wondering if you could quiz me on something we need to know. I want to be prepared."
        c "Hmm.. Well, here's one. What can you replace curly brackets with?"

        menu:
            "<percent, percent>! I was studying last night!":
                jump w1c2c1
            "Was it <:, :>?":
                jump w1c2c2
            "That's such an easy question! You can't! What kind of dumb person would replace that with anything?":
                jump w1c2c3

        label w1c2c1:
            c "Oh, you actually got it! That's correct."
            $ cAff += 1
            jump w1c2cont

        label w1c2c2:
            c "Close, but not quite. That's for replacing square braces. You need <% %> for curly braces."
            jump w1c2cont

        label w1c2c3:
            c ".. There's more than one way to do anything, you know? You should go study a bit more."
            $ cAff -= 1
            jump w1c2cont

        label w1c2cont:
            c "Well, it's getting pretty late. I'm going to head home."
            user "Ok! I'll see you later, then."
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "C is keeping me on my toes for sure. But studying with her is a lot of fun!"
            "I better sleep soon, I have to stay rested to be ready for the quiz."
            $ renpy.music_stop()
            jump choose

    label w1c3:
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade

        "Let's go to the library again!"
        $ cAff += 1
        $ renpy.music_stop()
        scene library
        $ renpy.music_start(mlib)
        with fade

        user "Hey, C! I'm here again."

        show c
        with fade

        c "You've been coming here quire often. You must be interested in books."
        user "Yeah! I've been having fun here."
        c "That's good."
        user "I actually came here to do some work today."
        user "I couldn't really concentrate at home, you see."
        c "The library is great for studying. I've got to finish my work, too."
        c "There's an assignmet due tomorrow, but there's a project that was assigned before that."
        c "I'm in a rush to finish the project first..."

        menu:
            "Going through your work in order, I see. I try to do that too! It makes it easy to keep track of what I need to do next.":
                jump w1c3c1
            "I see. That certainly is a good way to go through your work! I haven't done that before, but maybe I should give it a try.":
                jump w1c3c2
            "Shouldn't you work on the assignment that's due tomorrow first? I feel like that's more important.":
                jump w1c3c3

        label w1c3c1:
            c "I'm glad someone understands! It does hold me up here and there, but it's just easier overall for me."
            $ cAff += 1
            jump w1c3cont

        label w1c3c2:
            c "Yeah, you should give it a shot. It's nice once you get used to it."
            jump w1c3cont

        label w1c3c3:
            c "Hey, it's worked for me in the past."
            c "I'm sure I'll pull through... Everyone has their own way of doing things, you know."
            $ cAff -= 1
            jump w1c3cont

        label w1c3cont:
            user "Well, I better get working. Good luck on your project!"
            c "Thanks!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "C is so fussy about organization sometimes it's hard to keep up."
            "I'm tired out, time to finally rest."
            $ renpy.music_stop()
            jump choose

    label day8c:
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade

        "Hmm... I got a text..."
        "Oh, it's from C, she wants to eat lunch with me today."
        "I guess I have nothing else to do... might as well."
        $ renpy.music_stop()
        scene cafe
        $ renpy.music_start(mcafe)
        with fade

        c "Hey User! Over here!"

        show c
        with fade

        user "Hey C!"
        c "Thanks for coming today!"
        c "This is my favorite restaurant in town, you see."
        c "The food is really nice, and the place is very organized as well!"
        user "I bet it is. I can't wait to eat."
        user "Anyways, what's the occasion for calling me out here?"
        c "You look like someone who really loves books and learning new things, I was thinking that you would be perfect for the book club!"
        c " Care to learn more? And perhaps join it!"

        menu:
            "Oh yeah, you did mention that you are in the book club. I would love to try it out, tell me more bout it!":
                jump c1c1
            "I don’t know. It sounds like a grand time, but I’m worried that it may take up too much time":
                jump c1c2
            "Maybe.... but it doesn't seem to suit me too well.":
                jump c1c3

        label c1c1:
            c "I’m so glad to hear that! Ok, so basically the book club is..."
            $ cAff += 1
            jump c1cont

        label c1c2:
            c "I understand, you have to focus on school after all."
            c "Though if you join the book club, I wouldn’t mind helping you with school work!"
            jump c1cont

        label c1c3:
            c "That’s ok, you can always come by if you decide to change your mind."
            $ cAff -= 1
            jump c1cont

        label c1cont:
            "We spoke for a while longer. C seemed pretty keen on getting me to join the book club."
            "I'll have to give it some more thought."
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Im glad C and I are getting along, it's been a lot of fun!"
            "Well, time to get some rest."
            $ renpy.music_stop()
            jump day9c

    label day9c:
        scene classroom
        $ renpy.music_start(mclass)
        with fade
        "Yesterday was a lot of fun with C, I’m glad she invited me to join her club, but I don’t really know if I have what it takes."
        "Speak of the devil, here she is now."

        show c
        with fade

        c "Hey User! Thank you for meeting me yesterday, it was a lot of fun."
        user "I should be thanking you!"
        c "So, what’s your thoughts on joining?"
        user "I'm interested! The club seems like a lot of fun, but I’m still not totally sure."
        c "How about we get lunch together tomorrow? At the roof of the school? The view’s pretty nice there."
        user "Sure thing! I’ll see you there tomorrow."
        c "Okay! I’ll see you later."
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "Im excited to eat on the roof tomorrow, I havn't had a chance to check out the view!"
        "Better get to bed though, the sooner I sleep, the sooner I get to meet up with C."
        $ renpy.music_stop()
        jump day10c

    label day10c:
        scene rooftop
        $ renpy.music_start(mroof)
        show c
        with fade

        c "Hey User, thanks for coming up here to meet me!"
        user "Thanks for inviting me. I didn’t realize we had such an awesome view!"
        user "Yeah, but that’s not why I wanted to bring you here, I actually had a question!"
        c "Yeah. It is. I asked you to come to ask you about something, though."
        user "Sure thing, what is it?"
        c "Well first, I wanted to know if you’d made up your mind yet?"
        user "Yeah, I think I really do want to join the book club!"
        c "Great! Well then about my question. If I’m going to recommend to let you in, I feel like we should know each other better."
        c "So I planned a fun little test!"
        user "Uh, ok. What did you have in mind?"
        c "I just need you to answer one question about me."
        c "I was given an int a, and I want to print out a+1, what should I do?"

        menu:
            "printf(a++);":
                jump c2c1
            "printf(++a);":
                jump c2c2

        label c2c1:
            c "Mmm... That's not quite right."
            c "Since a++ returns the old value of a, then increment it, so printf(a++) would just print a."
            $ cAff -= 2
            jump c2cont

        label c2c2:
            c "Yes! That’s the correct answer, it’s such a small mistake that people usually get wrong."
            c "I’m impressed with how well you remember things!"
            $ cAff += 1
            jump c2cont

        label c2cont:
            "Bells ring"
            c "We should head back to class."
            user "You're right. I'll see you around!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Man, I wasn't expecting that question from C."
            "Racking my brain about why she's asking these questions won't do any good, time for bed."
            $ renpy.music_stop()
            jump day11c

    label day11c:

        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "The quiz is over!!! Studying sure helped me out with that one."
        "I wonder how C did... I should head over to the library and see if she's there."
        $ renpy.music_stop()
        scene library
        $ renpy.music_start(mlib)
        show c
        with fade
        user "Hey C!"
        c "Hey User! What's up?"
        user "I was going to ask you about the quiz! Was wondering how you did."
        c "Umm...I’m not sure…I hope I did okay."
        user "Knowing you, you probably scored the highest out of all of us"
        c "Haha, thanks for the encouragement."
        c "Hey, wanna stop by at the library tomorrow? I can use some input picking out a new book."
        user "Sure! My pleasure."
        c "Hehe, thanks~!"
        user "I’ll see you tomorrow then."
        c "See you then!"
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "Time for bed, I wonder what book C'll choose tomorrow."
        $ renpy.music_stop()
        jump day12c

    label day12c:
        scene library
        $ renpy.music_start(mlib)
        show c
        with fade

        "Walking in the library, C sits surrounded by a small mountain of books, brow furrowed as she scrutanizes them one by one."
        user "Find anything good?"
        "C jumps slightly, having been too engrossed in her reading to hear me appraoch."
        c "Ah, no, not yet. But that's why you're here right?"
        user "Of course! You should read..."

        menu:
            "I found this one book about AI and their impact on society you might like.":
                jump c3c1
            "This new graphic novel I heard about! It's supposed to be really good.":
                jump c3c2
            "A magazine or something right? All these long books get boring.":
                jump c3c3

        label c3c1:
            c "Oh that sounds interesting! Thanks for the suggestion."
            $ cAff += 1
            jump c3cont

        label c3c2:
            c "Is that so? Maybe I'll give it a look if I have time."
            jump c3cont

        label c3c3:
            c "I happen to enjoy the longer books quite a lot..."
            $ cAff -= 1
            jump c3cont

        label c3cont:
            c "Anyways, tomorrow's the club fair."
            c "Do you think you'll register for the book club?"
            user "Of course!"
            c "Wonderful, I'm sure they'll let you in."
            c "Well, good luck! I should get going."
            user "Okay. I'll see you later!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "I better get to sleep, don't wanna be late to the fair!"
            $ renpy.music_stop()
            jump day13c

    label day13c:
        scene hallway
        $ renpy.music_start(mhall)
        with fade
        "Today's the big day! The club fair is finally here!"
        "I finally have a club I want to register for... I really hope they let me in."
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "After submitting my application, I walk around the fair for a short while, admiring all the different booths and their activities before returning home."
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "I can barely sleep tonight! I hope my application will be accepted tomorrow."
        $ renpy.music_stop()
        jump cend

    label cend:
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "I can hardly wait to find out if I got into the club!"
        "I should hurry to school."

        if cAff >= 5:
            jump caccept
        if cAff <= 5:
            jump creject

        label caccept:
            $ renpy.music_stop()
            scene classroom
            $ renpy.music_start(mclass)
            show c
            with fade

            c "Hello User!"
            user "Hey C! Any news on my club application?"
            c "Actually, yes."
            c "I'm so happy to say that you were accepted!"
            user "That's awesome news! I'm excited to join you there."
            c "It's going to be a lot of fun, you're going to help me pick out and carry so many books!"
            user "Oh, yeah I guess I will be."
            c "I'm just teasing, it'll be great!"
            c "After all, you're with the best designed character for the devs least favorite programming language!"
            user "Wait, what?"
            c "Books are great!"
            "From then on, I spent lots of my free time with the book club."
            "My grades began to steadily improve from all the time spent reading"
            "C and I never quite figured out strings, but it was always a good time."
            jump EndScreen


        label creject:
            $ renpy.music_stop()
            scene classroom
            $ renpy.music_start(mclass)
            show c
            with fade

            user "Hey, C!"
            c "Oh.. Hey, User."
            user "Any news about my club application yet?"
            c "Yes, I'm afraid you weren't accepted this year."
            user "Oh.. that's a bummer. I was really excited too..."
            c "Yeah. Maybe you could try again next year?"
            c "We can still see each other around school every now and then."
            user "Yeah. I guess you're right."
            user "I'll see you around, then."

            "I never got much closer to C after that."
            "We exchanged friendly smiles when we passed, and waved to each other every now and then. But that's pretty much the extent of it."
            "I guess it was how it was meant to be. I can't be friends with everyone, after all."
            "At least there's always next year!"
            jump EndScreen

    label w1py1:

        "I'll check out the track and field club today!"
        $ pyAff += 1
        $ renpy.music_stop()
        scene       field
        $ renpy.music_start(mfield)
        with        fade

        "There's a lot of people here! I wonder what time the club starts at."
        "???" "Heeey! Haven't I seen you before?"

        show        pyimage
        with        fade

        py "I'm Python! Are you new around here?"
        user "Yeah. I was looking for a club to join."
        user "Track looked like it's not too hard to pick up, and it looked really fun, so I'm here to check it out."
        py "That's true, beginners can pick up the basics pretty quickly"
        py "We like to teach things simple! Unlike that student council president, Java..."
        py "She's so obsessed with organizing things and having weird punctuations. Isn't that just, extra work?"

        menu:
            "Yeah, keeping things simple and straightforward is the best! Complicating things isn't fun.":
                jump w1py1c1
            "It does make sense to keep things simple, I guess. Organization has its uses from time to time, though.":
                jump w1py1c2
            "Organization makes everything so much easier, though! Simple is nice, but I feel like that's not important.":
                jump w1py1c3

        label w1py1c1:
            py "I'm glad you see it that way!"
            py "I believe there's only one beautiful way to do one thing."
            py "There can be other methods, but what's the point if they're ugly and inefficient?"
            $ pyAff+=    1
            jump        w1py1cont

        label w1py1c2:
            py "I still prefer the simplest way, but I guess having both could have its uses."
            jump        w1py1cont

        label w1py1c3:
            py "Hey, simplicity makes it easy to learn, you know."
            py "Overly complicating stuff will just confuse you in the end. Hmph."
            $ pyAff -=    1
            jump        w1py1cont

        label w1py1cont:
            user "Well, I'll stick around for a bit longer, but I think someone's calling you, Python."
            py "Oh, yeah. I better get going. See you around!"
            $ renpy.music_stop()
            scene       bedroom
            $ renpy.music_start(mbed)
            with        fade
            "Today was fun, time for bed now though."
            $ renpy.music_stop()
            jump        choose

    label w1py2:
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "The track club was fun. Let's go there again!"
        $ pyAff += 1
        $ renpy.music_stop()
        scene field
        $ renpy.music_start(mfield)
        with fade
        py "Heeeey, User!"

        show pyimage
        with fade

        user "Oh, hey there, Python!"
        user "It looks like a group is practicing there... is it okay to not be with them? It looks like they're up to something."
        py "Yeah! I'm just taking a little break."
        py "I saw you and was wondering if you wanted someone to show you around, you see!"
        py "I totally didn't want to slack off or anything... I promise!"
        user "Heh, sure, sure. I believe you. No matter, I wanted to look around anyway."
        user "Having a club member show me around would be amazing."
        py "All right! Follow me..."

        with fade

        py "... and here is the equipment room! We have tons of stuff we don't use, too."
        py "It's more like our general storage."
        user "I see. What's this? *;*"
        py "Oh, the semicolon. I don't know, we never used it."
        py "I asked about it before, and from what I've been told, it's pretty much useless."
        py "We use things like *:*, or nothing, really."

        menu:
            "I guess if there's a way to work without it, that would be simpler.":
                jump w1py2c1
            "If nobody else is using it, might as well not use it. It could throw off new members that are used to it though... But they'll get used to it, I guess.":
                jump w1py2c2
            "I'm sure it has some uses! Just discarding them doesn't sit right with me.":
                jump w1py2c3

        label w1py2c1:
            py "Yeah! It's one less thing to learn how to use."
            $ pyAff += 1
            jump w1py2cont

        label w1py2c2:
            py "Yeah, we've had some new members confused about that."
            py "They learned to deal with its absence pretty soon, though."
            jump w1py2cont

        label w1py2c3:
            py "I guess everyone has their own preference."
            $ pyAff -= 1
            jump w1py2cont

        label w1py2cont:
            py "Well, I better get going. I'll see you around!"
            user "Bye!"
            $ renpy.music_stop()
            scene       bedroom
            $ renpy.music_start(mbed)
            with        fade
            "Today was fun, time for bed now though."
            $ renpy.music_stop()
            jump        choose

    label w1py3:
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade

        "I wonder if Python is at the field again."
        $ pyAff += 1
        $ renpy.music_stop()
        scene field
        $ renpy.music_start(mfield)
        with fade

        "It looks like some kind of race is going on..."
        "Oh, look! Python is running next!"

        user "Python! You won!"

        show pyimage
        with fade

        py "You were watching? Hehe, thanks!"
        py "Everyone was fixated on making really complicated training routines, and I think that threw them off a bit."
        py "I just followed the basics. Simpler, the better!"

        menu:
            "It's easier to concentrate if it's simple, after all. Nice work!":
                jump w1py3c1
            "Complicating it when you don't know how it works can be negative, after all. Nice work!":
                jump w1py3c2
            "I think optimizing everything is the ideal way to go, but hey, it worked for you I guess. Nice work!":
                jump w1py3c3

        label w1py3c1:
            py "Hehe, thanks~! I really worked hard for this."
            $ pyAff += 1
            jump w1py3cont

        label w1py3c2:
            py "Hehe, thanks~! I really worked hard for this."
            jump w1py3cont

        label w1py3c3:
            py "I guess... I don't think complicated things work for me though. Thanks anyway."
            $ pyAff -= 1
            jump w1py3cont

        label w1py3cont:
            py "I'll be going to meet with my teammates. I'll catch you around!"
            user "All right. Have fun!"
            $ renpy.music_stop()
            scene       bedroom
            $ renpy.music_start(mbed)
            with        fade
            "Today was fun, time for bed now though."
            $ renpy.music_stop()
            jump        day8py

    label day8py:
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade

        "Hmm... I got a text.."
        "Oh, it's from Python, she wants to eat lunch with me today."
        "I guess I should go... I've got nothing else to do, after all."
        $ renpy.music_stop()
        scene cafe
        $ renpy.music_start(mcafe)
        with fade

        py "Hey User! Over here!"

        show pyimage
        with fade

        user "Hey Python!"
        py "Thanks for coming today!"
        py "This is my favorite restaurant in town, you see."
        py "The food is soooooo gooooooood...."
        user "I bet it is. I can't wait to eat."
        user "Anyways, what's the occasion for calling me out here?"
        py "Oh, I was just wondering if you were interested in the track and field club."
        py "You visited us for the past couple days, so.. yeah."

        menu:
            "Yeah, it looked fun! The simple elegance of running seems like something I want to get into.":
                jump py1c1
            "I don't know. It looks fun, but it's a bit different from what I've done before. I'm up for trying it out, though.":
                jump py1c2
            "Maybe.... but it doesn't seem to suit me too well.":
                jump py1c3

        label py1c1:
            py "I totally agree! Over-complicating things have never been my style."
            py "Things should be easy to understand, like running!"
            $ pyAff += 1
            jump py1cont

        label py1c2:
            py "Yeah, trying out new things can be intimidating."
            py "I think you'll find that it's pretty easy to get the hang of running, though."
            jump py1cont

        label py1c3:
            py "You sure? It's pretty fun you know..."
            py "I'm sure you'll have fun if you try it out."
            $ pyAff -= 1
            jump py1cont

        label py1cont:
            "We spoke for a while longer. Python seemed pretty keen on getting me to join the track and field club."
            "I'll have to give it some more thought."
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Im glad Python and I are getting along, it's been a lot of fun!"
            "Well, time to get some rest."
            jump day9py

    label day9py:
        scene classroom
        $ renpy.music_start(mclass)
        with fade
        "I had a lot of fun with Python yesterday!"
        "I'm glad she invited me to the club, but I'm really not sure if I have what it takes..."
        "Oh, speak of the devil. Here she comes."
        show pyimage
        with fade
        py "Hey User! Thank you for meeting me yesterday. It was a lot of fun~"
        user "I should be thanking you!"
        py "So, have you thought about what I said yesterday?"
        user "Yeah! The club seems like a lot of fun."
        user "I'm still not too sure about joining, though."
        py "How about we get lunch together tomorrow? At the roof of the school?"
        py "The views pretty nice there, you know."
        user "Sure thing! I'll see you there tomorrow."
        py "Okay! I'll see you later."
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "Im excited to eat on the roof tomorrow, I havn't had a chance to check out the view!"
        "Better get to bed though, the sooner I sleep, the sooner I get to meet up with Python."
        $ renpy.music_stop()
        jump day10py

    label day10py:

        scene rooftop
        $ renpy.music_start(mroof)
        show pyimage
        with fade

        py "Hey User, thanks for coming up here to meet me!"
        user "Of course! Thanks for inviting me."
        user "The view up here really is great."
        py "Yeah. It is. I asked you to come to ask you about something, though."
        user "Okay. What did you want to ask?"
        py "Well, first, I was wondering if you made a decision on wanting to join the club yet."
        user "Yeah, I've been giving it some thought, and I think I want to join the club after all."
        py "Great! Well in that case, I'm going to have to give you a little test."
        py "If I'm going to recommend you to the club captain, I feel like we should know a bit more about each other."
        user "Uh, ok. What did you have in mind?"
        py "I just need you to answer one question about me."
        py "Which of the following generally executes faster?"

        menu:
            "For loops":
                jump py2c1
            "Loop comprehensions":
                jump py2c2

        label py2c1:
            py "Mmm... That's not quite right. That's the slow way!"
            py "You've got to be faster if you want to be in the track and field club, you know!"
            $ pyAff -= 2
            jump py2cont

        label py2c2:
            py "Yes! I see that speed comes naturally to you!"
            py "I'm glad! Hehehe~"
            $ pyAff += 1
            jump py2cont

        label py2cont:
            "Bells ring"
            py "We should head back to class."
            user "You're right. I'll see you around!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Man, I wasn't expecting that question from Python."
            "Racking my brain about why she's asking these questions won't do any good, time for bed."
            $ renpy.music_stop()
            jump day11py

    label day11py:
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "The quiz is over!!! Studying sure helped me out with that one."
        "I wonder how Python did... I should head over to the field and see if she's there."
        $ renpy.music_stop()
        scene field
        $ renpy.music_start(mfield)
        show pyimage
        with fade
        user "Hey Python!"
        py "Hey User! What's up?"
        user "I was going to ask you about the quiz! Was wondering how you did."
        py "Ehh, not that well. I didn't have time to study, you see. I've been training for the race tomorrow."
        py "... about that race, I wanted to ask... Will you come watch me race tomorrow?"
        user "Sure! It'll be my pleasure."
        py "Hehe, thanks~!"
        user "I'll see you tomorrow then! Good luck!!!"
        py "Thanks!"
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "Time for bed, I can't wait for Python's race!"
        $ renpy.music_stop()
        jump day12py

    label day12py:

        scene field
        $ renpy.music_start(mrace)
        with fade

        user "GO PYTHON!!!!!"

        show pyimage
        with fade

        py "You came!"
        user "Of course I did! You're competing, after all!"
        py "Thank you! I'm so happy I won the race! It's nice to see hard work pay off."

        menu:
            "It is. It was amazing to see you run passed all of the others! I was really worried at the start when you were behind, but I knew you could do it! Omega good job!":
                jump py3c1
            "I had fun wathing! it was an exciting race.":
                jump py3c2
            "It's nice. I thought the race was over at the start when you fell behind, but I guess fortunate events happen! Good job.":
                jump py3c3

        label py3c1:
            py "It was really nerve-wrecking when I passed them! I'm glad it's over."
            $ pyAff += 1
            jump py3cont

        label py3c2:
            py "It was a close race indeed. I'm glad you had fun."
            jump py3cont

        label py3c3:
            py "I guess... It could have turned out differently on another day, I suppose."
            $ pyAff -= 1
            jump py3cont

        label py3cont:
            py "Anyways, tomorrow's the club fair!"
            py "You're coming to register for the club, right?"
            user "Of course!"
            py "I hope you get in!!! It's always fun to have a new person around."
            py "Well, good luck tomorrow! I should get going."
            user "Okay. I'll see you later!"
            $ renpy.music_stop()
            scene bedroom
            $ renpy.music_start(mbed)
            with fade
            "Well, I better get to sleep, don't wanna be late to the fair!"
            $ renpy.music_stop()
            jump day13py

    label day13py:
        scene hallway
        $ renpy.music_start(mhall)
        with fade
        "Today's the big day! The club fair is finally here!"
        "I finally have a club I want to register for... I really hope they let me in."
        $ renpy.music_stop()
        scene schoolgate
        $ renpy.music_start(mschool)
        with fade
        "After submitting my application, I walk around the fair for a short while, admiring all the different booths and their activities before returning home."
        $ renpy.music_stop()
        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "I can barely sleep tonight! I hope my application will be accepted tomorrow."
        $ renpy.music_stop()
        jump pyend

    label pyend:

        scene bedroom
        $ renpy.music_start(mbed)
        with fade
        "I can hardly wait to find out if I got into the club!"
        "I should hurry to school."

        if pyAff >= 5:
            jump pyaccept
        if pyAff <= 5:
            jump pyreject

        label pyaccept:
            $ renpy.music_stop()
            scene classroom
            $ renpy.music_start(mclass)
            show pyimage
            with fade

            py "Hey, User! Over here!"
            user "Hey Python! Any news on my club application?"
            py "Actually, yes!"
            py "I wanted to be the one to tell you that..."
            py "You're totally in! Hehe~"
            user "Hooray! That's great news! I'm excited to try it out."
            py "You'll have to take it seriously, you know? Track and field is rewarding, but it's not all fun and games."
            py "It takes practice to get good at, like anything else."
            user "Of course! I'll be doing my best."
            py "Great! I'm glad you will get to spend more time with..."
            py "Me, Python, the FAR SUPERIOR coding language that the game devs are only *slightly* biased towards!"
            user "Oh... uh, yeah, sure."
            py "Yay!"
            "From then on, I was the member of the track and field club."
            "Slowly but surely, my skills improved over time."
            "Python helped me out with simple tips and tricks, and we're having fun going to the same club."
            jump EndScreen


        label pyreject:
            $ renpy.music_stop()
            scene classroom
            $ renpy.music_start(mclass)
            show pyimage
            with fade

            user "Hey, Python!"
            py "Oh.. Hey, User."
            user "Any news about my club application yet?"
            py "Yeah.. About that. I'm sorry, but it doesn't look like we have any room in the club for you this year."
            user "Oh.. that's a bummer. I was really excited too..."
            py "Yeah. Maybe you could try again next year?"
            py "We can still see each other around school every now and then, right?"
            user "Yeah. I guess you're right."
            user "I'll see you around, then."

            "I never got much closer to Python after that."
            "We exchanged friendly smiles when we passed, and wave to each other every now and then. But that's pretty much the extent of it."
            "I guess it was how it was meant to be. I can't be friends with everyone, after all."
            "Well, there's always next year!"
            jump EndScreen

    label gameOver:
        scene bedroom
        #$ renpy.music_start()

        "Unfortunately, it seems like I didn't make much of an impact on anybody I met."
        "I guess making friends is harder than I thought"
        "G A M E   O V E R"

    label EndScreen:
        scene bedroom
        #$ renpy.music_start()
        with fade
        "Hello and thank you for playing our game: Hello World The Visual Novel!"
        "We hope you had a good time and enjoyed the fruits of our sleep deprived labor."
        "Maybe try playing again for a different ending?"
        "Thanks again!      - The Hello World VN Team"
        return
