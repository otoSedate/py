from tkinter import *
from tkinter.filedialog import *
from tkinter.colorchooser import *
import os
import re

file1Name = ''
file2Name=''
appPath = os.getcwd()
currentFind = None
import string
#класс родительского окна'''
class main:
    def __init__(self, master):
      
        self.master = master
        
        self.master.title('WorkBench')
        self.master.iconname('editor')
        self.master.geometry('840x340+100+100')

        self.myBar = Frame(self.master, relief = RAISED, bd=2)

        
        self.myBar.pack(side = TOP, fill = X)

        self.text1=Frame(self.master)
        self.text1.config(width=1000,height=500)


        self.myScroll = Scrollbar(self.master)


    
        self.text1.pack(side=LEFT)
        self.text1.pack_propagate(False)
        self.text1.tx = Text(self.text1)
        
        self.myScroll.pack(side=LEFT, fill=Y)
        


        self.myScroll.configure(command = self.text1.tx.yview)
        
        self.text1.tx.pack()

 
     
        self.fileMenu()
        self.editMenu()
        self.MY()
        self.about()
        self.master.protocol('WM_DELETE_WINDOW', self.exitMethod)
        self.master.mainloop()

    def func(self):
        out = self.text1.tx.get(1.0,END)
        L1=out.split('\n')
        text=''
        for i in range(len(L1)) :
            for j in L1[i]:
                s=j
                if '0'<=s<='9':
                    s='_'
                elif 'a'<=s<='z':
                    s=s.upper()
                text+=s
        self.text1.tx.delete(1.0,END)
        self.text1.tx.insert(1.0,text)
                
#добавление меню file в панель меню'''
    def fileMenu(self):
        mButton = Menubutton(self.myBar, 
                         text = 'File  ', 
                         underline = 0)
        mButton.pack(side = LEFT)
        menu = Menu(mButton, tearoff = 0)
        menu.add_command(label = 'Open file',
                     underline = 0, 
                     command = self.fileOpen1)

        menu.add_separator({})
        menu.add_command(label = 'Save', 
                     underline = 0,command=self.save)
        menu.add_command(label = 'Save as...', 
                     underline = 5,command=self.saveas)
        menu.add_command(label = 'Exit', 
                     underline = 5,command=self.exitMethod)
        mButton.configure(menu = menu)
        return mButton
#добавление меню edit в панель меню'''
    def editMenu(self):
        mButton = Menubutton(self.myBar, text = 'Edit  ', underline = 0)
        mButton.pack(side = LEFT)
        menu = Menu(mButton, tearoff = 0)
        menu.add_command(label = 'Font style',
                         underline = 0, 
                         command = self.shrift)
        menu.add_command(label = 'Change background',
                         underline = 0, 
                         command = self.foncolor)       
        mButton.configure(menu = menu)
        return mButton
    def about(self):
        mButton = Menubutton(self.myBar, text = 'About', underline = 0)
        mButton.pack(side = LEFT)
        menu = Menu(mButton, tearoff = 0)
        menu.add_command(label = 'About ',
                         underline = 0, 
                         command = self.aboutus)
      
        mButton.configure(menu = menu)
        return mButton
    def aboutus(self):
        # Create components
        self.aboutlavel    = Toplevel()
        lab1=Label(self.aboutlavel,text='Программа заменяет цифры на знак подчеркивания,\n строчные латинские буквы на прописные')
        lab1.pack()
    def shrift(self):
        # Create components
        self.win    = Toplevel()
        self.fms = Frame(self.win, bd=2)
        self.fms.pack(side = TOP, fill = X)
        scrollbar = Scrollbar(self.fms)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.lb1=Listbox(self.fms,selectmode=SINGLE,yscrollcommand=scrollbar.set, width=20,height=5)
        list1=['arial','calibri']
        for i in list1:
            self.lb1.insert(END,i)
        self.lb1.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.lb1.yview)
        self.sfont_button=Button(self.win,

                               text = 'Set font',command=self.sfont)
        self.sk_button = Button(self.win,
                               text = 'Set color of font',command=self.shriftcolor)
        
        
        self.sfont_button.pack()
        self.sk_button.pack()

    def foncolor(self):
        b=askcolor()
        self.text1.tx.config(bg=b[1])

        
        
    def shriftcolor(self):
        b=askcolor()
        self.text1.tx.config(fg=b[1])

    def sfont(self):
        a=self.lb1.curselection()
        b=self.lb1.get(a)
        if b!='':
            self.text1.tx.config(font=b)

    def MY(self):
        mButton = Menubutton(self.myBar, text = 'My  ', underline = 0)
        mButton.pack(side = LEFT)
        menu = Menu(mButton, tearoff = 0)
        menu.add_command(label = 'Run program ', 
                     underline = 2, command=self.func)
        mButton.configure(menu = menu)
        return mButton

#выход из редактора'''
    def exitMethod(self):
        self.dialog = yesno(self.master)
        self.myMssg = 'Are you sure?'
        self.returnValue = self.dialog.go(message = self.myMssg)
        if self.returnValue:
            self.master.destroy()
    def save(self):
        global file1Name
        if file1Name!='':
            f=open(file1Name,'w')
            f.write(self.text1.tx.get(1.0,END))
            f.close
    def saveas(self):
        global file1Name
        if file1Name!='':
            sa = asksaveasfilename()
            letter = self.text1.tx.get(1.0,END)
            f = open(sa,"w")
            f.write(letter)
            f.close()
        
    def read(self,f):
        s=''
        for line in f:
            s+=line

        return s+'\n'
 
    def fileOpen1(self):
        global file1Name
        file1Name=askopenfilename()
        TEXT=self.read(open(file1Name))
        self.text1.tx.delete(1.0,END)
        self.text1.tx.insert(1.0,TEXT)



class yesno:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.frame = Frame(self.slave)
        self.frame.pack(side = BOTTOM)
        self.yes_button = Button(self.frame,
                               text = 'Yes',
                               command = self.yes)
        self.yes_button.pack(side = LEFT)
        self.no_button = Button(self.frame,
                              text = 'No',
                              command = self.no)
        self.no_button.pack(side = RIGHT)
        self.label = Label(self.slave)
        self.label.pack(side = TOP,
                      fill = BOTH,
                      expand = YES)
        self.slave.protocol('WM_DELETE_WINDOW', self.no)

    def go(self, title = 'Exit from menu',
               message = '[question goes here]',
               geometry = '300x100+300+265'):
        self.slave.title(title)
        self.slave.geometry(geometry)
        self.label.configure(text = message)
        self.booleanValue = TRUE
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        return self.booleanValue

    def yes(self):
        self.booleanValue = TRUE
        self.slave.destroy()

    def no(self):
        self.booleanValue = FALSE
        self.slave.destroy()
 


root = Tk()

# запуск окна
main(root)
