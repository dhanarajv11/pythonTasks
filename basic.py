import os
import time
import pyttsx3

#print("chat with your requiremtn")
#os.system("notepad")

con = True

while con:
#    os.system("cls")
    p = input("chat with your requirement : ")
    print(p)
    if ((("notepad" in p) or ("editor" in p) or ("notebook" in p) or ("paper" in p) or ("slips" in p) or ("block" in p) or ("jotter" in p) or ("quire" in p) or ("scratch" in p) or ("book" in p) ) and (("run" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("initiate" in p) or ("onset" in p) or ("commence" in p) or ("inaugurate" in p) or ("fire" in p) ) and (not (("dont" in p) or ("not" in p) or ("prevent" in p) or ("restrict" in p)))):
        os.system("notepad")
        time.sleep(2)
        os.system("cls")
    elif ((("chrome" in p) or ("browser" in p) or ("portal" in p) or ("gateway" in p) ) and ( ("run" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("initiate" in p) or ("onset" in p) or ("commence" in p) or ("inaugurate" in p) or ("fire" in p) ) and (not ( ("dont" in p) or ("not" in p) or ("prevent" in p) or ("restrict" in p)))):
        os.system("chrome")
        time.sleep(2)
        os.system("cls")
    elif ((("wmplayer" in p) or ("media" in p) or ("player" in p) or ("mediaplayer" in p) ) and ( ("run" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("initiate" in p) or ("onset" in p) or ("commence" in p) or ("inaugurate" in p) or ("fire" in p) ) and (not ( ("dont" in p) or ("not" in p) or ("prevent" in p) or ("restrict" in p)))):
        os.system("wmplayer")
        time.sleep(2)
        os.system("cls")
    elif ( ("quit" in p) or ("exit" in p) or ("close" in p)):
        os.system("cls")
        break
    else:
        print("dont support")
        time.sleep(3)
        os.system("cls")