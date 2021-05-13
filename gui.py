import Tkinter as tk 

from literadar import LibRadarLite
import json
import pandas as pd
from termcolor import colored


Height=800
Width=800

df=pd.read_csv("flashlightpermission.csv")
fb=pd.read_csv("camerapermissions.csv")
cf=pd.read_csv("filemanagerpermissions.csv") 






def getscore(list,name,f):
	total=0
	flag=0
	for i in list:
		if CheckVar1.get()==1:                                 # for which csv file to be compared. 
			j= cf.loc[cf['NAME'] == i]
		if CheckVar2.get()==1:                                 #if it is checkvar2=flashlight, so take NAME of df file, if it is other then take fb file and so forth
			j= df.loc[df['NAME'] == i]
		if CheckVar3.get()==1:
			j= fb.loc[fb['NAME'] == i]



		
		score=int(j.SCORE.values.tolist()[0])  # to convert panda series to list. to select first element - [0]
		f.write("Permission:{}  &&  SCORE :{} \n".format(i,score))

		print(" Permission:{}  &&  SCORE :{} ".format(i,score))
		total+=score
	print ("\nTOTAL SCORE for library {}:  {}   (Vulnerability score) ".format(name,total))
	f.write("TOTAL SCORE for library {}:  {}   (Vulnerability score) \n".format(name,total))
	#if total>34:
		#flag
		
	if total>34:

		flag=1
	if total>40:
		flag=2
	if total>50:
		flag=3


	return flag

			



def import_button_press(entry):

    lrd = LibRadarLite(entry)                                    #literadar default. app name in entry
    res = lrd.compare()                                    # function of literadar, does'nt concern us
    pop=0
    with open("file.txt", "w+") as f:                      #for returning/writing terminal output in file.txt
	    for i in range(len(res)):                      # Picking up and comparing library by library

	    	if res[i]['Library']=="Unknown":                #done to make tool compatible with esfileapp.  #If lib is unknown do this.
	    		print("\n{}".format("-"*5))
	    		f.write("\n{}Unknown Library \n ")             #to write to file.txt
	    		print colored("\nUnknown Library{} \n ")          #to display in terminal
	    		
	    		


			    


	    	if res[i]['Library']!="Unknown":                #If lib is not unknown do this #done to make tool compatible with esfileapp



			    j=res[i]['Permission']
			    name=res[i]['Library']
			    print("\n{}".format("-"*5))
			    f.write("\nLibrary used :{} \n ".format(name))
			    print colored("\nLibrary used :{} \n ".format(name),"green")
			    


			    l= getscore(j,name,f)
			    pop+=l

		    
			    

    if pop==0:                     # this condition for differentiating btw safe and risky 
    	print colored("\n\t\t\tThis app is SAFE","green")
    	label = tk.Label(frame1, text= "This app is SAFE",bg="GREEN",font=25)
    	label.pack()




    if  pop!=0:                    # this condition for differentiating btw safe and risky 
                                   # this means that app is risky. Risky to hai hi but level of risk we'll divide further


    	print colored("\n\t\t\tThis app causes system to be at RISK","red")  

    	label = tk.Label(frame1, text= "This app causes system to be at RISK",bg="white",font=25)
    	
    	label.pack()
    	
    	



		
    	
    	

    	if pop==1:                                         #for level of risk 
    		print colored("\n\t\t\tRISK:LOW \n","red")  
    		label = tk.Label(frame1, text= "RISK:LOW ",bg="red",font=25)
    		label.pack()

    	if pop==2:
    		print colored("\n\t\t\tRISK:MEDIUM \n","red")  
    		label = tk.Label(frame1, text= "RISK:MEDIUM ",bg="red",font=25)
    		label.pack()
		if pop==3:
			print colored("\n\t\t\tRISK:HIGH \n","red")  
			label = tk.Label(frame1, text= "RISK:HIGH ",bg="red",font=25)
			label.pack()
    	

    	button = tk.Button(frame1, text="HELP", command=Help_button_result)	        #help button, it calls result(). 
    	button.pack()
    		

		
    		







    	
def Help_button_result():              # function for HELP button. Basically to read the file.txt 

	
	with open("file.txt", "r") as f:
		tk.Label(frame1, text=f.read()).pack()

   

     

 	







    
   

	
	

root = tk.Tk()                #Tk to create a main window with a title bar and name of that window is root.
root.title('NON_playstore-app_RISK_EVALUATOR')

canvas=tk.Canvas(root,height=Height, width=Width)
canvas.pack()                             # pack()- Put a widget inside a frame (or any other container widget), and have it fill the entire frame

background_image=tk.PhotoImage(file='landscape.png')
background_label=tk.Label(root, image=background_image)                  #LABEL- you can add text or image in label  #here root is parent window. can be master
background_label.place(relwidth=1,relheight=1)


frame=tk.Frame(root,bg='#80c1ff',bd=5)                #First Frame
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.08,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)



frame1=tk.Frame(root,bg='#80c1ff',bd=5)              # THIRD FRAME
frame1.place(relx=0.5,rely=0.35,relwidth=0.8,relheight=0.6,anchor='n')



frame2=tk.Frame(root,bg='#80c1ff',bd=5)            #SECOND FRAME
frame2.place(relx=0.5,rely=0.25,relwidth=0.8,relheight=0.06,anchor='n')

CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(frame2, text = "Filemanager", variable = CheckVar1,  onvalue = 1, offvalue = 0, height=5,width = 20)
C1.place(relx=0.7,relheight=1,relwidth=0.2)
                 
CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(frame2, text = "Flashlight", variable = CheckVar2,  onvalue = 1, offvalue = 0, height=5,width = 20)
C2.place(relx=0.4,relheight=1,relwidth=0.2)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(frame2, text = "Camera", variable = CheckVar3,  onvalue = 1, offvalue = 0, height=5,width = 20)
C3.place(relx=0.1,relheight=1,relwidth=0.2)







button=tk.Button(frame,text="Import APK ",font=40,command=lambda: import_button_press(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)



root.mainloop()    #mainloop() is an infinite loop used to run the application, process the event as long as the window is not closed.

 

