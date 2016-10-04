import telebot

userStep = {}  # so they won't reset every time the bot restarts
knownUsers = []
with open("C:/Users/Victor/PycharmProjects/goazenbot/goazen.token", "r") as T:
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


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Funcionamiento: GOAZEN GOAZEN")


@bot.message_handler(regexp='.?([gG][oO][aA][zZ][eE][nN]).?')
def goazen(message):
    cid = message.chat.id
    with open("C:/Users/Victor/PycharmProjects/goazenbot/Goazen.ogg", "rb") as f:
        bot.send_voice(cid, f)
    bot.reply_to(message, 'GOAZEN GOAZEN')

# Ignore previous messages
bot.skip_pending = True

# Execute
print("Running...")
bot.polling()
