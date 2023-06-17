from bot import telegram_chatbot

bot = telegram_chatbot()


def make_reply(item):
    reply = "Hello {}, What do you need".format(item['message']['from']['first_name'])
    # if msg is not None:
    #     reply = gizoogle.text(msg)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            print(item)
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(item)
            bot.send_message(reply, from_)