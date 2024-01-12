
#x = input('Press 1 to download VIDEO or \nPress 2 to download AUDIO: ')

#if x == '1':
#  print("VIDEO selected")

#elif x == '2':
#  print("AUDIO selected")

#else:
#  print("Please try again. Select[1(for video) or 2(for audio)]")

from pytube import YouTube
import os 



while True:
    # your code

    x = input('Press 1 to download VIDEO  \nPress 2 to download AUDIO or \nPress 3 to QUIT: ')

    if x == '1':
      print("VIDEO selected")

    elif x == '2':
      print("AUDIO selected")

    elif x == '3':
      print("Program Ended. Thank You for using Me")
      break

    else:
      print("Please try again. Select[1(for video) 2(for audio) or 3(to quit)]")

    
    cont = input("Do you want to download again? yes/no > ")

    while cont.lower() not in ("yes", "no"):
        cont = input("Do you want to download again? yes/no > ")

    if cont == "no":
        print("Program Ended. Thank You for using Me")
        break
   


