from gtts import gTTS 

import os 

os.system("cd $HOME")

mytext = input("\n\n\tType Your message : ")


file = mytext.replace(" ", "_")



language = input("\tSelext language(en/ml) : ")

 

myobj = gTTS(text=mytext, lang=language, slow=False) 

  

myobj.save("%s.mp3" % os.path.join("~/storage/music/ttsVoice",file))


os.system("mpg123 %s.mp3" % os.path.join("~/storage/music/ttsVoice",file))


print ("\033[1m \033[91m hello ")

msg = "The file has been saved to \033[92m music/ttsVoice \033[91m in Your Directory"

len = len(msg)

print ( '+' + '-'*(len-8) + '+')
print ('| %-*.*s |' % (len,len,msg))
print ( '+' + '-'*(len-8) + '+')

print ("\033[0m")

os.system("cd ")