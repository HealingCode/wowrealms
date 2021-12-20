from tkinter import *
from tkinter import ttk
import os

#GET DIRS

dir_path= os.path.dirname(os.path.realpath(__file__))
existConfig = os.path.exists(dir_path + "\Config.txt")
	
#FIN

#METODOS KEYDOWN

def popupInsertRealm():
	top=Toplevel(window)
	top.geometry("200x200")
	realmEntry= Entry(top, width=100)
	realmEntry.pack()
	b=Button(top, text="Submit", command=lambda:submit_realm(realmEntry))
	b.pack();


def popupChangeRealm():
	top=Toplevel(window)
	top.geometry("500x500")
	choices=getSetOfRealms()
	choices=list(choices)
	choicesvar= StringVar(value=choices)
	listaRealms = Listbox(top, listvariable=choicesvar)
	listaRealms.pack()
	extraer = ttk.Button(top, text="Establecer realm", default="active", command=lambda:select_item_Realm(listaRealms))
	extraer.pack()

def popupInsertWTF():
	top=Toplevel(window)
	top.geometry("350x200")
	advice = ttk.Label(top, text="You must enter both \n the WTF folder and the data folder addresses")
	WTFLbl = ttk.Label(top, text="Insert the address of your WTF config folder")
	wtfEntry= ttk.Entry(top)
	DATALbl = ttk.Label(top, text="Insert the address of your reallist data folder")
	wtfEntrydata= ttk.Entry(top)
	advice.pack()
	WTFLbl.pack()
	wtfEntry.pack()
	DATALbl.pack()
	wtfEntrydata.pack()
	b=Button(top, text="Submit", command=lambda:submit_WTF(wtfEntry,wtfEntrydata))
	b.pack();
	
def popupChangeWTF():
	top=Toplevel(window)
	top.geometry("500x500")
	choices=getSetOfWTF()
	choices=list(choices)
	choicesvar= StringVar(value=choices)
	listaWtfs = Listbox(top, listvariable=choicesvar)
	listaWtfs.pack()
	extraer = ttk.Button(top, text="Establecer WTF dir", default="active", command=lambda:select_item_WTF(listaWtfs))
	extraer.pack()

	
def del_realm():
	print("")


def submit_realm(realmEntry):
	realm=realmEntry.get()
	realm = realm + "\n"
	f = open("Realms.txt", "a")
	f.write(realm)
	f.close()

def submit_WTF(wtfEntry,dataEntry):
	realm=wtfEntry.get()
	realmtwo=dataEntry.get()
	realmtwo = realmtwo + "\n"
	realm= realm+"|"+realmtwo
	f = open("WTFdirs.txt", "a")
	f.write(realm)
	f.close()
	

def getListOfRealms():
	f=open("Realms.txt", "r")
	list=[]
	for x in f:
		list.append(x)
	f.close()


def refreshLbl(currentLbl):
	global existConfig
	if existConfig == False:
		f=open("Config.txt", "a")
		f.write("CURRENT_REALM=NULL")
		f.write("CURRENT_WTFDIR=NULL")
		currentLbl="NULL"
		f.close()
		existConfig=True
	else:
		f=open("Config.txt", "r")
		data = f.readlines()
		str=data[0].split("=")
		str1=data[1].split("=")
		currentLbl.config(text="Current realm is:"+str[1])
		currentLblWtf.config(text="Current WTF is:\n"+str1[1])
		f.close()

def stablishWTF():
	find = False
	wtf=getWTF()
	wtf = wtf[0:len(wtf)-1]
	splited = wtf.split('|')
	wtfDir = splited[0]
	parch =  splited[1]
	# WTF FOLDER PROCESS
	data_folder = wtfDir + "/Config.wtf"
	data_foldertmp = wtfDir + "/Configtmp.wtf"
	data_folder = data_folder.replace("\\", "/")
	print(data_folder)
	f=open(data_folder)
	data=f.readlines()
	str='realmList'
	c = 0
	for x in data:
		if str in x:
			find = True
			if find == True:
				break
		c = c+1
	newRealm=getRealm()
	data[c] = "SET realmList " + newRealm
	ftmp = open(data_foldertmp, "w")
	ftmp.writelines(data)
	#DATA FOLDER PROCESS
	data_folderdata = parch + "/realmlist.wtf"
	data_folderdatatmp = parch + "/realmlisttmp.wtf"
	data_folderdata = data_folderdata.replace("\\", "/")
	
	print(data_folderdata)
	g=open(data_folderdata)
	data=g.readlines()
	print(data)
	data[0] = "SET realmlist " + newRealm
	gtmp = open(data_folderdatatmp, "w")
	gtmp.writelines(data)
	f.close()
	ftmp.close()
	g.close()
	gtmp.close()
	os.remove(data_folder)
	os.rename(data_foldertmp,data_folder)
	os.remove(data_folderdata)
	os.rename(data_folderdatatmp,data_folderdata)

#METODOS NO KEYDOWN

def getSetOfRealms():
	f=open("Realms.txt", "r")
	list= set()
	for x in f:
		list.add(x)
	f.close()
	return list

def getSetOfWTF():
	f=open("WTFdirs.txt", "r")
	list=set()
	for x in f:
		list.add(x)
	f.close()
	return list

def getRealm():
	global existConfig
	if existConfig == False:
		f=open("Config.txt", "w")
		f.write("CURRENT_REALM=NULL\n")
		f.write("CURRENT_WTFDIR=NULL")
		existConfig=True;
		return "NULL"
	else:
		f=open("Config.txt","r")
		data = f.readlines()
		str = data[0].split("=")
		f.close()
	return str[1]
	
def getWTF():
	global existConfig
	if existConfig == False:
		f=open("Config.txt", "w")
		f.write("CURRENT_REALM=NULL")
		f.write("CURRENT_WTFDIR=NULL")
		existConfig=True;
		return "NULL"
	else:
		f=open("Config.txt","r")
		data = f.readlines()
		str = data[1].split("=")
		f.close()
	return str[1]
	
def setRealm(i):
	global existConfig
	if existConfig == False:
		f=open("Config.txt", "w")
		f.write("CURRENT_REALM="+i)
		f.write("CURRENT_WTFDIR=NULL")
		existConfig=True
		f.close()
	else:
		f=open("Config.txt", "r")
		data = f.readlines()
		data[0] = "CURRENT_REALM="+i
		ftmp=open("Configtmp.txt", "w")
		ftmp.writelines(data)
		f.close()
		ftmp.close()
		os.remove("Config.txt")
		os.rename("Configtmp.txt", "Config.txt")
		
def setWTF(i):
	global existConfig
	if existConfig == False:
		f=open("Config.txt", "w")
		f.write("CURRENT_REALM=NULL")
		f.write("CURRENT_WTFDIR="+i)
		existConfig=True
		f.close()
	else:
		f=open("Config.txt", "r")
		data = f.readlines()
		data[1] = "CURRENT_WTFDIR="+i
		ftmp=open("Configtmp.txt", "w")
		ftmp.writelines(data)
		f.close()
		ftmp.close()
		os.remove("Config.txt")
		os.rename("Configtmp.txt", "Config.txt")

def printListOfRealms(listaRealms):
	choices=getSetOfRealms()
	choices=list(choices)
	choicesvar= StringVar(value=choices)
	listaRealms = Listbox(frametwo, listvariable=choicesvar)
	listaRealms.grid(column=0, row=0)
	

def select_item_Realm(listbox):
	for i in listbox.curselection():
		setRealm(listbox.get(i))
	

def select_item_WTF(listbox):
	for i in listbox.curselection():
		setWTF(listbox.get(i))
	
#main: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

window = Tk()
#window.state('zoomed')
window.title("BETA 0.1 WOWREALMS ")

#frames ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

frameone = ttk.Frame(window)
frametwo = ttk.Frame(frameone, borderwidth=5, relief="ridge", width=200, height=100)
currentLbl = ttk.Label(frameone, text="Current realm is:" + getRealm())
currentLblWtf = ttk.Label(frameone, text="Current WTF dir is:" + getWTF())

#Menu

menubar = Menu(window, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  

#Opciones 

opciones = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')  
opciones.add_command(label="New realm",command=popupInsertRealm)
opciones.add_command(label="New WTF",command=popupInsertWTF)
opciones.add_command(label="Change current realm",command=popupChangeRealm) 
opciones.add_command(label="Change current WTF dir",command=popupChangeWTF) 
opciones.add_separator()
opciones.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="Opciones", menu=opciones)  

#Botones

refrescar = ttk.Button(frameone, text="Refresh", default="active", command=lambda:refreshLbl(currentLbl))
establecer = ttk.Button(frameone, text="Establish realm on WTF", default="active", command=lambda:stablishWTF())

#GRID

frameone.grid(column=0, row=0)
frametwo.grid(column=0, row=1, columnspan=3, rowspan=10)
currentLbl.grid(column=3, row=0, columnspan=2)
currentLblWtf.grid(column=3, row=1, columnspan=2)
refrescar.grid(column=1, row=0)
establecer.grid(column=2, row=0)

#run main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

window.config(menu=menubar)
window.mainloop()
