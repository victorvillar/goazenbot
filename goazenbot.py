import telebot

userStep = {}  # so they won't reset every time the bot restarts
knownUsers = []
with open(".\goazen.token", "r") as T:
    bot = telebot.TeleBot(T.read().strip())


# Detects new users
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


def listener(messages):

    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

# Create bot
bot = telebot.TeleBot(T)
bot.set_update_listener(listener)







# Ignore previous messages
bot.skip_pending = True

# Execute
print("Running...")
bot.polling()