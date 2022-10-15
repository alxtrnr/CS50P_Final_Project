import pushup_tables as put
import project


def main_text():
    print("""The Hundred Push Up Program
    
If you're serious about increasing your strength, follow this six week training program and you'll soon be on your way 
to completing 100 consecutive pushups!

Think there's no way you could do this? I think you can. All you need is a good plan, plenty of discipline and about 30 
minutes a week to achieve this goal!

No doubt some of you can already do 50 consecutive pushups, but let's face it, you're in a big minority. Most of you 
reading this won't even be able to manage 20 pushups. Actually, I'm sure many of you can't even do 10.

However, it really doesn't matter which group you fall into. If you follow the progressive pushups training program, 
I'm positive you'll soon be able to do 100 pushups!""")


def intro():
    print("""
Before you dive in and start the 100 Pushups Program, you should:
    
* Obtain medical advice and clearance from your doctor
* Take an initial pushups test
    
The test will highlight your current fitness level and determine where to start and how to plan your pushups training 
program.
""")


def perform_test():
    print("""To perform the test, simply execute as many good-form pushups as you can. Don't cut corners and please 
don't cheat - the last thing you want to do is end up in the wrong level of the training program! The results may be 
humbling, but trust me, honesty is the best policy if you want to maximize your strength gains!""")


def post_first_test():
    return """
(!)If you're concerned about your Rank in the extreme left column; there's really no need. The scale of 1 to 7 is purely
an indicator of current fitness, and can be used as a comparison tool between yourself, friends, family & co-workers.

Most people tend to fall into Rank 2 or 3 which is a great starting point for the plan. If you're ranked 1, you may need
to consider one of the alternative pushups on the What is a Pushup? page. If you're ranked 6 or 7, maybe you need a 
tougher plan?!

Before starting Week 1, I recommend taking a couple of days to familiarize yourself with the program and recover from 
the exertion of the initial test. You'll be required to work out three times per week - Monday, Wednesday, Friday worked
well for me."""


def w1d1_start_text():
    return """
So, you've completed your initial test and keen to start the program? Excellent news!

* If you managed 5 or less pushups in the test, follow column 1.
* If you completed between 6 and 10 pushups, column 2 is for you.
* Between 11 and 20 consecutive pushups? Impressive! Column 3 is what you're looking for.
        
More than 20 pushups? I would suggest starting the program on Week 3.

For example: let's say you managed 8 pushups. Looking at the second column, Day 1 begins with Set 1 (6 pushups), a rest 
period of 60 seconds, before moving on to Set 2 (6 pushups). Rest for 60 seconds and continue with Set 3 (4 pushups) and
Set 4 (4 pushups), before finishing with Set 5 and as many consecutive pushups as you can comfortably manage (at least 
5, but not so many that you damage muscle tissue). The 60 seconds rest between each level should allow you to complete 
the workout, but I promise it will get tough towards the end.
"""


def w1d1_end_text():
    return """
Treat yourself to a rest day before moving on to Day 2, and then again before you complete Day 3. I find that Monday, 
Wednesday, Friday works well and allows you to use the weekend for rest and recovery before moving on to the next stage 
of the program. Feel free to juggle the plan around to meet your busy schedule, but make sure you rest in between 
workout days."""


def w2d3_start_text():
    return """
After today it will be time to check your strength and perform an exhaustion test. 

In simple terms, perform as many good-form pushups as you can comfortably manage before you physically can't do another 
rep. Stress your system by all means, but please don't go beyond the safety limit. The number of pushups you complete 
will determine which level of the program you'll start in Week 3. Perform this test within a couple of days of 
completing Week 2. Good luck!
"""


def wk2d3_end_text():
    return """
Don't forget, now you've completed Week 2, it's time to take an exhaustion test. Have a day or two rest then perform as 
many good-form pushups as you can manage before you physically can't do another one. Make a note of how many pushups you
complete, and move on to Week 3. Hope you're ready for the next level!"""


def w1d3_end_text():
    return """
Hopefully you made it safely through the first week and now you're keen to move on to Week 2. However, if for some 
reason you struggled with the program, I would suggest either retaking the initial test or repeating Week 1. You'll 
probably be surprised at how much stronger you already are and will sail through the first week and be fired up and 
raring to go.

If you're ready to move on, take a look at Week 2 of the Hundred Pushups Program."""

def wk3d1_start_text():
    print("""
You should be a little stronger than you were a couple of weeks ago and able to complete considerably more pushups than 
your initial test.

* If you managed 16-20 pushups in the latest test, follow column 1.
* If you completed between 21 & 25, column 2 is for you.
* More than 25 consecutive pushups? Excellent! You'll be following column 3.

If you're struggling with the program, don't lose heart. Some people will still be doing less than 16 consecutive 
pushups, but this is ok. Just repeat the week you struggled with until you're strong enough to move on to the next level
 - I promise it will be worth your while! 
""")


def wk3d3_end_text():
    return """
Hopefully you made it safely through the third week and you're ready to move on to Week 4. Keep up the great work - 
you're halfway through the program and well on your way to performing one hundred consecutive pushups.

Let's continue with the program and take a look at Week 4."""


def wk4d1_start_text():
    return """
Week 3 is now comfortably behind you and it's time to start Week 4. Continue by following the same column of exercises 
as you did last week.

At the end of Week 4 it will be time to perform another exhaustion test. You should know what to do by now - simply 
perform as many good-form pushups as you can comfortably manage before you're unable to perform another one. As per the 
end of Week 2, stress your system by all means, but please don't go beyond the safety limit.

The number of pushups you complete will determine which level of the program you'll start in Week 5. Make sure you 
perform this test within a couple of days of completing Week 4.
"""


def wk4d3_end_text():
    return """
Ok, time for another exhaustion test. You should be feeling much stronger now than your initial test 4 weeks ago. Make a
note of how many pushups you complete, and move on to Week 5."""


def wk5d1_start_text():
    return """
Depending on the results of your latest test, continue with an appropriate week and column, even if it means you have to
complete Week 3 or Week 4 again.

* If you managed 31 - 35 pushups, follow column 1.
* If you completed between 36 & 40, column 2 is for you.
* More than 40 consecutive pushups? Great work! You'll be following column 3.\n"""


def wk5d3_end_text():
    return """
Surprise, surprise, it's time for another exhaustion test. Week 5 was a tough one, and if you've made it this far, 
you're getting close to reaching your goal. If you're able to perform more than 45 consecutive pushups, feel free to 
move on to Week 6. Couldn't quite manage 45? No problem, just repeat the week and you should be ready to go after 
another three workout days. Good luck!"""


def wk6d1_start_text():
    return """
Depending on the results of your latest test, continue with an appropriate week and column, even if it means you have to
complete Week 5 again.

* If you managed 46 - 50 pushups, follow column 1.
* If you completed between 51 & 60, column 2 is for you.
* More than 60 consecutive pushups? Tremendous! You'll be following column 3.
"""


def wk6d3_end_text():
    return """
Well? Did you make it through Week 6? If you did; congratulations - you should be very proud of your achievements and 
ready for one final test.

If you struggled with Week 6 (many people do), no problem, just repeat the appropriate week and try again. Maybe an 
extra couple of days rest will benefit you?"""


def final_test_start_text():
    return """
If you're reading this page you should be very proud of your achievements and ready for one final test. As you're well 
aware, the program you've been following is called One Hundred Pushups and that's what this final test is all about.

To perform the test, simply execute as many good-form pushups as you can. If you've completed the six week program with 
no cheating and no short cuts, experience has shown that you should be strong enough to perform one hundred consecutive 
pushups!

After completing Week 6 of the program, treat yourself to a day or two of rest. Eat well and maintain good hydration. 
Try not to perform any exercises or tasks around the home that will drain you of energy - you'll need every ounce of 
strength to meet your goal. Ready?

Take your time, don't rush and focus on performing ten pushups at a time. Breaking the magic hundred into smaller chunks
will make the goal more achievable and give you more chance of success. Maintain good form and don't hold your breath. 
It sounds simple, but just take it one push up at a time until you reach one hundred! If you start to feel shaky, take 
a few deep breaths and regain your composure before starting again. Good luck - I know you can do it!!"""


def final_test_end_text():
    return """
Just in case you didn't manage the hundred, I would suggest going back a couple of weeks in the program and building up 
your strength again. Maybe Week 5 or Week 6 would be good for you and help regain your confidence? Don't give up though,
you're closer than you think!"""
