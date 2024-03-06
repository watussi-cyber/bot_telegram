import asyncio
import telegram

async def main():
    token = 'XXXX' # Pour obtenir un nouveau token, il faut taper la commande /newbot auprès du bot BotFather
    chat_id = 'XXXX' # Pour obtenir son chat_id, on peut demander à @get_id_bot 
    bot = telegram.Bot(token)
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=chat_id)


if __name__ == '__main__':
    asyncio.run(main())

