# %%
# pip install python-telegram-bot==13.7

# %%
# import sys

# locate_python = sys.exec_prefix

# print(locate_python)

# %%
import cons
from telegram.ext import *
import resp as R
import pandas as pd
import numpy as np
import requests
pd.set_option('display.max_rows', 100)
import seaborn as sns
sns.set_style('darkgrid')
import random


def start_command(update, context):
    update.message.reply_text('Let\'s start stocking!')

def help_command(update, context):
    update.message.reply_text(cons.HELP)

def buy(updt, context):
    updt.message.reply_animation(random.choice(cons.WAIT))
    nothing_to_buy = True
    stocks = cons.STOCKS
    for stock, link in stocks.items():
        url = requests.get(link)
        try:
            table_ = pd.read_html(url.text)[1]
            table_.columns = ['Date','Price','Open','Max','Min','Vol','Change']

            table = table_.iloc[:5,:].copy()
            prices = pd.concat([table.Price,table.Open,table.Max,table.Min])

            fq = np.quantile(prices,0.25)
            sq = np.quantile(prices,0.5)
            tq = np.quantile(prices,0.75)
            
            go = (table.Price+table.Open+table.Max+table.Min)/4
            go = go.iloc[::-1].reset_index()[0]
            for i in range(len(go)-1):
                go[i] = go[i+1] - go[i]
            go = (go[:-1].mean()*100)/((table.Price+table.Open+table.Max+table.Min)/4).mean()

            table_ = table_.iloc[:-2,:]
            prices_ = pd.concat([table_.Price,table_.Open,table_.Max,table_.Min])
            fq_ = np.quantile(prices_,0.25)
            sq_ = np.quantile(prices_,0.5)
            tq_ = np.quantile(prices_,0.75)

            go_ = (table_.Price+table_.Open+table_.Max+table_.Min)/4
            go_ = go_.iloc[::-1].reset_index()[0]
            for i in range(len(go_)-1):
                go_[i] = go_[i+1] - go_[i]
            go_ = (go_[:-1].mean()*100)/((table_.Price+table_.Open+table_.Max+table_.Min)/4).mean()



            if ((table.Price[0] <= fq and round(tq/fq-1,2) >= 0.04)) and not ((go < -0.5)):
                updt.message.reply_text(f"Buy {stock.upper()} under {fq}\nAs it's {stock.upper()}\'s first weekly quarter\nAnd you'll have a chance to get profit of {round((tq/fq-1)*100,2)}%")
                nothing_to_buy = False
            elif (table.Price[0] <= sq and round(tq/fq-1,2) >= 0.8) and not ((go < -0.5)):
                updt.message.reply_text(f"Buy {stock.upper()} under {sq}\nAs it's {stock.upper()}\'s second weekly quarter\nAnd you'll have a chance to get profit of {round((tq/fq-1)*100/2,2)}%")
                nothing_to_buy = False
            elif (table.Price[0] <= fq_ and round(tq_/fq_-1,2) >= 0.06) and not ((go_ < -0.25)):
                updt.message.reply_text(f"Buy {stock.upper()} under {fq_}\nAs it's {stock.upper()}\'s first monthly quarter\nAnd you'll have a chance to get profit of {round((tq_/fq_-1)*100,2)}%")
                nothing_to_buy = False
            elif ( (table.Price[0] <= sq_ and round(tq_/fq_-1,2) >= 0.12)) and not ((go_ < -0.25)):
                updt.message.reply_text(f"Buy {stock.upper()} under {sq_}\nAs it's {stock.upper()}\'s second weekly quarter\nAnd you'll have a chance to get profit of {round(((tq_/fq_-1)*100)/2,2)}%")
                nothing_to_buy = False

        except:
            updt.message.reply_text(f"Couldn't stock {stock}")
    if nothing_to_buy:
        updt.message.reply_text("Sorry, but there's nothing to buy RN!")
    else:
        updt.message.reply_animation(random.choice(cons.DONE))

def sell(updt, context):
    updt.message.reply_animation(random.choice(cons.WAIT))
    nothing_to_sell = True
    stocks = cons.STOCKS
    for stock, link in stocks.items():
        url = requests.get(link)
        try:
            table_ = pd.read_html(url.text)[1]
            table_.columns = ['Date','Price','Open','Max','Min','Vol','Change']

            table = table_.iloc[:5,:].copy()
            prices = pd.concat([table.Price,table.Open,table.Max,table.Min])

            tq = np.quantile(prices,0.75)
            
            go = (table.Price+table.Open+table.Max+table.Min)/4
            go = go.iloc[::-1].reset_index()[0]
            for i in range(len(go)-1):
                go[i] = go[i+1] - go[i]
            go = (go[:-1].mean()*100)/((table.Price+table.Open+table.Max+table.Min)/4).mean()

            table_ = table_.iloc[:-2,:]
            prices_ = pd.concat([table_.Price,table_.Open,table_.Max,table_.Min])
            tq_ = np.quantile(prices_,0.75)

            go_ = (table_.Price+table_.Open+table_.Max+table_.Min)/4
            go_ = go_.iloc[::-1].reset_index()[0]
            for i in range(len(go_)-1):
                go_[i] = go_[i+1] - go_[i]
            go_ = (go_[:-1].mean()*100)/((table_.Price+table_.Open+table_.Max+table_.Min)/4).mean()

            if (table.Price[0] >= tq_) and (not ((go > 0.5)) ):
                updt.message.reply_text(f"sell {stock.upper()} above {round(tq_,3)}\nAs it's {stock.upper()}'s third monthly quarter.")
                nothing_to_sell = False
            elif (table.Price[0] >= tq) and (not ((go > 0.5))):
                updt.message.reply_text(f"sell {stock.upper()} above {round(tq,3)}\nAs it's {stock.upper()}'s third weekly quarter.")
                nothing_to_sell = False
        except:
            updt.message.reply_text(f"Couldn't stock {stock}")
    if nothing_to_sell:
        updt.message.reply_text("Sorry, but there's nothing to sell RN!")
    else:
        updt.message.reply_animation(random.choice(cons.DONE))

def update_me(updt,context):
    updt.message.reply_animation(random.choice(cons.OK))
    if cons.STOP:
        cons.STOP = False
        while not cons.STOP:
            R.update(updt)
            print('round completed!')
    else:
        while not cons.STOP:
            R.update(updt)
            print('round completed!')

def handle(updt, context):
    text = str(updt.message.text).lower()
    R.resps(updt,text,updater)

def error(updt,context):
    updt.message.reply_text('Something went wrong!')
    print(context.error)

def hey(updt,context):
    updt.message.reply_animation(random.choice(cons.HEY))

def stop(updt,context):
    updt.message.reply_animation("https://media.giphy.com/media/8TweEdaxxfuElKkRxz/giphy.gif")
    cons.STOP = True
    cons.UPDATED = {}

def main():

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',help_command))
    dp.add_handler(CommandHandler('buy_what',buy,run_async=True))
    dp.add_handler(CommandHandler('sell_what',sell,run_async=True))
    dp.add_handler(CommandHandler('keep_me_updated',update_me,run_async=True))
    dp.add_handler(CommandHandler('hey',hey))
    dp.add_handler(CommandHandler('stop',stop))
    dp.add_error_handler(error)
    dp.add_handler(MessageHandler(Filters.text,handle))

    updater.start_polling()
    updater.idle()

updater = Updater(cons.API_KEY, use_context=True)
main()



# %%


# %%



