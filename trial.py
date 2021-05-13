import Tkinter as tk 
root = tk.Tk()                #Tk to create a main window with a title bar and name of that window is root.
root.title('NON_playstore-app_RISK_EVALUATOR')
canvas=tk.Canvas(root,height=400, width=400)
canvas.pack()

frame=tk.Frame(root,bg='#000000',bd=5)                #First Frame
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.08,anchor='n')
root.mainloop() 
