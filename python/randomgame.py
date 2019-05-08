#!/usr/bin/python3

import requests

MYAPI = "https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():
    result = requests.get(MYAPI)
    if "1" in result.text:
        print("You Won!")
    else:
        print("Looooossserrrrrr")

main()

