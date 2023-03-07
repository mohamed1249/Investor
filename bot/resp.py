import cons
import pandas as pd
import numpy as np
import requests
import random
import os

def info(stock,link):
    output = ''
    url = requests.get(link)
    try:
        data = pd.read_html(url.text)[1]
        data.columns = ['Date','Price','Open','Max','Min','Vol','Change']

        table = data.iloc[:5,:].copy()

        prices = pd.concat([table.Price,table.Open,table.Max,table.Min])
        
        fq = np.quantile(prices,0.25)
        sq = np.quantile(prices,0.5)
        tq = np.quantile(prices,0.75)

        output += stock.upper() + ':\n'
        output += f'\tCurrent Price: {table.Price[0]}\n'
        output += f'\tWeekly First Quarter: {fq}\n'
        output += f'\tWeekly Second Quarter: {sq}\n'
        output += f'\tWeekly Third Quarter: {tq}\n'
        output += f'\tWeekly Minimum: {table.Min.min()}\n'
        output += f'\tWeekly Maximum: {table.Max.max()}\n'

        go = (table.Price+table.Open+table.Max+table.Min)/4
        go = go.iloc[::-1].reset_index()[0]
        for i in range(len(go)-1):
            go[i] = go[i+1] - go[i]
        go = (go[:-1].mean()*100)/(((table.Price+table.Open+table.Max+table.Min)/4).mean())

        output += f'\tWeekly Average: {round(((table.Price+table.Open+table.Max+table.Min)/4).mean(),2)}\n'
        output += f'\tWeekly Risk Percentage: {round(tq/fq-1,2)}\n'

        output += f'\tWeekly Growing Rate: {round(go,4)}\n'

        if go > 0.5:
            output += f'\tIt\'s Going Up This Week\n'
        elif go < -0.5:
            output += f'\tIt\'s Going Down This Week\n'
        else:
            output += f'\tIt\'s Static This Week\n'

        prices = prices.sort_values().to_frame()
        prices['DecileRank'] = [n*100/len(prices) for n in range(0,len(prices))]
        q = round(prices[prices[0] == table.Price[0]]['DecileRank'].mean())
        output += f'\tIt\'s At The {q}th Weekly Quarter\n'

        table_ = data.iloc[:-2,:]
        prices_ = pd.concat([table_.Price,table_.Open,table_.Max,table_.Min])
        fq_ = np.quantile(prices_,0.25)
        sq_ = np.quantile(prices_,0.5)
        tq_ = np.quantile(prices_,0.75)


        output += f'\tMonthly First Quarter: {fq_}\n'
        output += f'\tMonthly Second Quarter: {sq_}\n'
        output += f'\tMonthly Third Quarter: {tq_}\n'
        output += f'\tMonthly Minimum: {table_.Min.min()}\n'
        output += f'\tMonthly Maximum: {table_.Max.max()}\n'
        output += f'\tMonthly Average: {round(((table_.Price+table_.Open+table_.Max+table_.Min)/4).mean(),2)}\n'
        output += f'\tMonthly Risk Percentage: {round(tq_/fq_-1,2)}\n'

        go_ = (table_.Price+table_.Open+table_.Max+table_.Min)/4
        go_ = go_.iloc[::-1].reset_index()[0]
        for i in range(len(go_)-1):
            go_[i] = go_[i+1] - go_[i]
        go_ = (go_[:-1].mean()*100)/((table_.Price+table_.Open+table_.Max+table_.Min)/4).mean()

        output += f'\tMonthly Growing Rate: {round(go_,4)}\n'

        if go_ > 0.25:
            output += f'\tIt\'s Going Up This Month\n'
        elif go_ < -0.25:
            output += f'\tIt\'s Going Down This Month\n'
        else:
            output += f'\tIt\'s Static This Month\n'

        prices_ = prices_.sort_values().to_frame()
        prices_['DecileRank'] = [n*100/len(prices_) for n in range(0,len(prices_))]
        mq = round(prices_[prices_[0] == table.Price[0]]['DecileRank'].mean())
        output += f'\tIt\'s At The {mq}th Monthly Quarter\n'

        if ((table.Price[0] <= fq and round(tq/fq-1,2) >= 0.04)) and not ((go < -0.5)):
            output += f'\tAnd You Should Buy It Under {fq}.'

        elif (table.Price[0] <= sq and round(tq/fq-1,2) >= 0.8) and not ((go < -0.5)):
            output += f'\tAnd You Should Buy It Under {sq}.'

        elif (table.Price[0] <= fq_ and round(tq_/fq_-1,2) >= 0.06) and not ((go_ < -0.25)):
            output += f'\tAnd You Should Buy It Under {fq_}.'

        elif ( (table.Price[0] <= sq_ and round(tq_/fq_-1,2) >= 0.12)) and not ((go_ < -0.25)):
            output += f'\tAnd You Should Buy It Under {sq_}.'

        elif (table.Price[0] >= tq_) and (not ((go_ > 0.25) or (go > 0.5)) ):
            output += f'\tAnd You Should Sell It Above {tq_}.'

        elif (table.Price[0] >= tq) and (not ((go_ > 0.25) or (go > 0.5))):
            output += f'\tAnd You Should Sell It Above {tq}.'
        else:
            output += f'\tAnd You Should Hold On It.'

        return output
    except:
        return 'Couldn\'t Stock, Try again Later!'


def update(updt):
    
    for stock, link in cons.STOCKS.items():
        if cons.STOP:
            break
        url = requests.get(link)
        try:
            data = pd.read_html(url.text)[1]
            data.columns = ['Date','Price','Open','Max','Min','Vol','Change']

            table = data.iloc[:5,:].copy()
            prices = pd.concat([table.Price,table.Open,table.Max,table.Min])
            fq = np.quantile(prices,0.25)
            sq = np.quantile(prices,0.5)
            tq = np.quantile(prices,0.75)

            go = (table.Price+table.Open+table.Max+table.Min)/4
            go = go.iloc[::-1].reset_index()[0]
            for i in range(len(go)-1):
                go[i] = go[i+1] - go[i]
            go = (go[:-1].mean()*100)/(((table.Price+table.Open+table.Max+table.Min)/4).mean())

            table_ = data.iloc[:-2,:]
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
                if stock not in cons.UPDATED.keys() or cons.UPDATED[stock] != 'fw':
                    updt.message.reply_text(f"Buy {stock.upper()} under {fq}\nAs it's {stock.upper()}\'s first weekly quarter\nAnd you'll have a chance to get profit of {round((tq/fq-1)*100,2)}%")
                    cons.UPDATED[stock] = 'fw'
            elif (table.Price[0] <= sq and round(tq/fq-1,2) >= 0.8) and not ((go < -0.5)):
                if stock not in cons.UPDATED.keys() or cons.UPDATED[stock] != 'sw':
                    updt.message.reply_text(f"Buy {stock.upper()} under {sq}\nAs it's {stock.upper()}\'s second weekly quarter\nAnd you'll have a chance to get profit of {round(((tq/fq-1)*100)/2,2)}%")
                    cons.UPDATED[stock] = 'sw'
            elif (table.Price[0] <= fq_ and round(tq_/fq_-1,2) >= 0.06) and not ((go_ < -0.25)):
                if stock not in cons.UPDATED.keys() or cons.UPDATED[stock] != 'fm':
                    updt.message.reply_text(f"Buy {stock.upper()} under {fq_}\nAs it's {stock.upper()}\'s first monthly quarter\nAnd you'll have a chance to get profit of {round((tq_/fq_-1)*100,2)}%")
                    cons.UPDATED[stock] = 'fm'
            elif ( (table.Price[0] <= sq_ and round(tq_/fq_-1,2) >= 0.12)) and not ((go_ < -0.25)):
                if stock not in cons.UPDATED.keys() or cons.UPDATED[stock] != 'sm':
                    updt.message.reply_text(f"Buy {stock.upper()} under {sq_}\nAs it's {stock.upper()}\'s second monthly quarter\nAnd you'll have a chance to get profit of {round(((tq_/fq_-1)*100)/2,2)}%")
                    cons.UPDATED[stock] = 'sm'
            elif (table.Price[0] >= tq_) and (not ((go > 0.5))):
                if stock not in cons.UPDATED or cons.UPDATED[stock] != 'slm':
                    updt.message.reply_text(f"sell {stock.upper()} above {round(tq_,3)}\nAs it's {stock.upper()}\'s third monthly quarter.")
                    cons.UPDATED[stock] = 'slm'
            elif (table.Price[0] >= tq) and (not ((go > 0.5))):
                if stock not in cons.UPDATED or cons.UPDATED[stock] != 'slw':
                    updt.message.reply_text(f"sell {stock.upper()} above {round(tq,3)}\nAs it's {stock.upper()}\'s third weekly quarter.")
                    cons.UPDATED[stock] = 'slw'
            else:
                if stock in cons.UPDATED:
                    cons.UPDATED.pop(stock)
        except:
            pass


def resps(updt,inpt,updtr):
    user_msg = str(inpt).lower()
    if user_msg in ('shutdown'):
        updt.message.reply_animation(random.choice(cons.BYE))
        os.system("shutdown /s /t 1")
        return
    if user_msg in ('done'):
        updt.message.reply_animation(random.choice(cons.BYE))
        os._exit(0)
    for input_stock in user_msg.split(' '):
        if input_stock in cons.STOCKS.keys():
            updt.message.reply_text(info(input_stock,cons.STOCKS[input_stock]))
        else:
            updt.message.reply_text(f'{input_stock.upper()} is not recognized as an avilable stock')
    
    