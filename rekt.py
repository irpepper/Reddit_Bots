#Rekt List Bot
import time
import praw

r = praw.Reddit("Rekt List by u/irpepper v 1.0")
r.login(username="you_need_a_rekt_list", password="SFRaai17")
already_rekt = []

rekt_text = "i need a rekt list!"
rekt_list = ["Not REKT","is REKT", "REKTangle", "t-REKT"]
while True:
    subreddit = r.get_subreddit("ineedarektlist")
    for submission in subreddit.get_hot(limit=10):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            op_text = comment.body.lower()
            if(rekt_text in op_text):
                needs_list = True
            else:
                needs_list = False

            if comment.id not in already_rekt and needs_list:
                msg = ""
                rekts = [False for x in range(4)]
                if op_text.count("rekt") == 1:
                    msg+="[  ]  " + rekt_list[0] + "\n\n"
                    for x in range(1,4):
                        msg+="[X]  "
                        msg+=rekt_list[x]+"\n\n"
                else:
                    for x in range(4):
                        if(rekt_list[x].lower() in op_text):
                            msg+="[X]  "
                        else:
                            msg+="[  ]  "
                        msg+=rekt_list[x]+"\n\n"

                print comment.id
                print "Got Rekt"
                already_rekt.append(comment.id)
                comment.reply(msg)
                time.sleep(2)
    time.sleep(30)
