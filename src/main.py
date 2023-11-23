import sys
sys.path.append('../borsa')
import schedule
import time
from data_scrapping.datas import connection_increasing, connection_decreasing
from data_scrapping.datas import  get_name_increasing, get_name_decreasing
from data_scrapping.datas import  ratio_increasing, ratio_decrasing
from data_scrapping.datas import  url1, url2
from twitter.twitter import connetion_to_account, tweeting_increasing, tweeting_decrasing
from errors import send_email

def main():
    tweets = connetion_to_account()
    conn1 = connection_increasing(url1)
    conn2 = connection_decreasing(url2)
    get_name_increasing(conn1)
    get_name_decreasing(conn2)
    ratio_increasing(conn1)
    ratio_decrasing(conn2)
    tweeting_decrasing(tweets)
    tweeting_increasing(tweets)

schedule.every().monday.at("16:30", "Europe/Paris").do(main)
schedule.every().tuesday.at("16:30", "Europe/Paris").do(main)
schedule.every().wednesday.at("16:30", "Europe/Paris").do(main)
schedule.every().thursday.at("16:30", "Europe/Paris").do(main)
schedule.every().friday.at("16:30", "Europe/Paris").do(main)


if __name__ == "__main__":
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        send_email(e)
        
    
        