import os
import amino
os.system('clear')
print ('''\033[0;31m _____   _____   _____   
/  ___/ |_   _| |  _  \  
| |___    | |   | |_| |  
\___  \   | |   |  _  /  
 ___| |   | |   | | \ \  
/_____/   |_|   |_|  \_\ ''')
input ('Enter to Use...')
os.system('clear')
print ('''\033[0;32m_       _____   _____   _   __   _  
| |     /  _  \ /  ___| | | |  \ | | 
| |     | | | | | |     | | |   \| | 
| |     | | | | | |  _  | | | |\   | 
| |___  | |_| | | |_| | | | | | \  | 
|_____| \_____/ \_____/ |_| |_|  \_| ''')
ema = input ('Enter the email:  ')
pas = input ('Enter the password:  ')
clint =amino.Client()
clint.login(email=ema,password=pas)
os.system('clear')
print ('''\033[1;33m _____   _____       ___  ___   _   _____  
/  ___| /  _  \     /   |/   | | | |  _  \ 
| |     | | | |    / /|   /| | | | | | | | 
| |     | | | |   / / |__/ | | | | | | | | 
| |___  | |_| |  / /       | | | | | |_| | 
\_____| \_____/ /_/        |_| |_| |_____/ ''')
com = input ('Enter comId:   ')
subclint =amino.SubClient(comId=com,profile=clint.profile)
os.system('clear')
print ('''\033[1;34m _____   _____   _       _____   _____   _____  
/  ___/ | ____| | |     | ____| /  ___| |_   _| 
| |___  | |__   | |     | |__   | |       | |   
\___  \ |  __|  | |     |  __|  | |       | |   
 ___| | | |___  | |___  | |___  | |___    | |   
/_____/ |_____| |_____| |_____| \_____|   |_|   ''')
print ('0)help')
print ('1)break')
print ('2)coupon')
print ('3)hide message')
print ('4)new chat spam')
print ('5)new blog spam')
spam = '''\033[4;36m _____   _____       ___       ___  ___  
/  ___/ |  _  \     /   |     /   |/   | 
| |___  | |_| |    / /| |    / /|   /| | 
\___  \ |  ___/   / / | |   / / |__/ | | 
 ___| | | |      / /  | |  / /       | | 
/_____/ |_|     /_/   |_| /_/        |_| '''
new = '''\033[4;36m __   _   _____   _          __ 
|  \ | | | ____| | |        / / 
|   \| | | |__   | |  __   / /  
| |\   | |  __|  | | /  | / /   
| | \  | | |___  | |/   |/ /    
|_|  \_| |_____| |___/|___/     '''
spy = '''\033[4;36m _____   _____  __    __ 
/  ___/ |  _  \ \ \  / / 
| |___  | |_| |  \ \/ /  
\___  \ |  ___/   \  /   
 ___| | | |       / /    
/_____/ |_|      /_/     '''
hide='''\033[4;36m _   _   _   _____   _____  
| | | | | | |  _  \ | ____| 
| |_| | | | | | | | | |__   
|  _  | | | | | | | |  __|  
| | | | | | | |_| | | |___  
|_| |_| |_| |_____/ |_____| '''
cup='''\033[4;36m _____   _____   _   _   _____   _____   __   _  
/  ___| /  _  \ | | | | |  _  \ /  _  \ |  \ | | 
| |     | | | | | | | | | |_| | | | | | |   \| | 
| |     | | | | | | | | |  ___/ | | | | | |\   | 
| |___  | |_| | | |_| | | |     | |_| | | | \  | 
\_____| \_____/ \_____/ |_|     \_____/ |_|  \_| '''
x = input ('select :    ')
if x =='1':
	os.system('exit1')
elif x=='2':
	print (cup)
	while True:
		clint.claim_new_user_coupon()
elif x =='3':
	print (hide)
	chid = input ('chatId')
	while True:
		me = input ('message:   ')
		subclint.send_message(chatId=chid,message=me,messageType='110')
elif x =='4':
	print (spam)
	name = input ('Enter title and content to chat:  ')
	us = input ('userId:   ')
	while True:
		subclint.start_chat(userId=us,message='اداة نفر',title=name,content=name)
		xxxx = 1
		print ('done',xxxx,'spam')
		xxxx+=1
elif x =='5':
	print (spam)
	namer = input ('Enter title and content to blog')
	while True:
		subclint.post_blog(title=namer,content=namer)
		print ('done','spam')
elif x =='0':
	print ('plese copy text and paste in other apk or read the english text')
	print ('''رقم واحد من اجل الخروج من الأداة 
رقم اثنين لسحب البطاقة واخذ العملات منها من المحتمل ان لا تنجح
رقم ثلاثه لاجل إرسال رسائل مخفيه داخل الدردشات العامه
رقم اربعه لاجل عمل سبام دردشات مع اي شخص بالمنتدى
رقم خمسه لاجل عمل سبام منشورات داخل اي منتدى
.
.
english
Number one for exit from the tool Number two for withdrawing the card and taking coins from it will likely not work Number three for sending messages hidden in public chats Number four in order to spam chats with anyone in the forum Number five in order to spam posts within any forum''')