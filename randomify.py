"""
USING THIS PROGRAM
1> First one need to create an API key for Etherscan.io API calls which can be created at "https://etherscan.io/myapikey" and paster the api_key in the api_key variable
2> Run this program and enter the number of participants to select a random person out of them.
3> Enter a unique id of each like username, id number or anything associated with them
4> Enter the date and time for which the program will start running the randomization. P.S.: Enter date and time in UTC in the format yyyy mm dd hh MM ss 
  where yyyy refers to year , mm for months , dd for day, hh for hours in 24 hour clock, MM for minutes and ss for seconds.
  For example, if the program is set to randomize from 1st January 2020 at 13:30:00, then enter the input as : 2020 1 1 13 30 0
5> Then confirm the date by 1 as input
6> After confirmation, sit back and relax. The program will randomly select one participant as winner.
P.S. i> The date and time should be of future like 30 minutes from the initial run of Program.
     ii> Note the input like number of particiapants , list of participants in the same sequence in which it is entered and date-time of start of randomization.
         You can share this detail with the public before the final confirmation and the public can verify the result.
"""
import time
import math
import requests
import datetime as dt

PARTICIPANTS = []

api_key = ""  # Enter API-key for the ETHERSCAN API


def nonce_val(block):
    current_block = latest_block()
    while current_block < block+1:
        time.sleep(5)
        current_block = latest_block()
    nonc = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag=" + hex(
        block) + "&boolean=true&apikey=" + api_key)
    return int(nonc.json()["result"]["nonce"], 16)


def latest_block():
    req = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=" + api_key)
    return int(req.json()["result"], 16)


def get_start_block(timestamp):
    req = requests.get(
        "https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp="+str(timestamp)+"&closest=before&apikey=" + api_key)
    return (int(req.json()['result'])+1)


def add_nos(i, n):
    return i + n


def sub_nos(i, n):
    return abs(i - n)


def sum_sq(i, n):
    return int(math.sqrt(i * i + n * n))


def cube_rt(i, n):
    return int(math.pow((i * i * i + n * n * n), 1 / 3))


def mul_nos(i, n):
    return i * n


def am_nos(i, n):
    return (i + n) // 2


def gm_nos(i, n):
    return int(math.sqrt(i * n))


def hm_nos(i, n):
    return i * n // (i + n)


if __name__ == "__main__":
    conf = 0
    arr = [add_nos, sub_nos, sum_sq, cube_rt, mul_nos, am_nos, gm_nos, hm_nos]
    try:
        nop=int(input('Enter the number of Participants:'))
    except ValueError:
        nop = int(input('Enter the number of Participants:'))
    for i in range(nop):
        participant = input('Enter name of Participant: ')
        PARTICIPANTS.append(participant)
    while conf == 0:
        try:
            a = [int(x) for x in input('Enter Start Time in UTC Format: YYYY MM DD hh mm ss:').split()]
            start_dt = dt.datetime(a[0], a[1], a[2], a[3], a[4], a[5])
        except ValueError:
            a = [int(x) for x in input('Please Enter Start Time in following Format: YYYY MM DD hh mm ss:').split()]
            start_dt = dt.datetime(a[0], a[1], a[2], a[3], a[4], a[5])
        except IndexError:
            a = [int(x) for x in input('Please Enter Start Time in UTC Format: YYYY MM DD hh mm ss:').split()]
            start_dt = dt.datetime(a[0], a[1], a[2], a[3], a[4], a[5])
        print("Your Start date for Randomization: ", start_dt.strftime("%H:%M:%S , %d %B %Y"))
        try:
            conf = int(input("Do you confirm? 1 for Yes / 0 for No: "))
        except ValueError:
            print("Error! Enter a number")
            conf = int(input("Do you confirm? 1 for Yes / 0 for No: "))
    while dt.datetime.utcnow() < start_dt:
        print(".", end='')
        time.sleep(1)
    start_dt=dt.datetime(start_dt.year,start_dt.month,start_dt.day,start_dt.hour,start_dt.minute,start_dt.second,tzinfo=dt.timezone.utc)
    print()
    print("Wating for one more min...")
    time.sleep(60)
    start_block=get_start_block(int(start_dt.timestamp()))
    end_block = start_block+100
    k = 8
    l = i = len(PARTICIPANTS)
    while end_block > start_block:
        n = nonce_val(start_block)
        cop = arr[(i % k)]
        i = int(cop(i, n) % l)
        print(i, n, start_block, i % l)
        start_block += 1
    print("Winner is: ",PARTICIPANTS[i % l])
