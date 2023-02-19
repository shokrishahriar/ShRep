from tkinter import *
from tkinter import messagebox
import pyperclip


global id
id=0
#functions

def add_user():
    c=list_box.size()
    n=list_box.get(c-1)
    number=n.split('.')

    user_str=str(int(number[0])+1)+'.'+name_entry.get()+'_'+family_entry.get()+','+password_entry.get()+': '+phone_entry.get()+';'+str(id)
    list_box.insert(END,user_str)



    name_entry.delete(0,END)
    family_entry.delete(0,END)
    phone_entry.delete(0,END)
########################



def delete_user():
    list_box.delete(ANCHOR)
    name_entry.delete(0,END)
    family_entry.delete(0,END)
    pass_entry.delete(0,END)
    phone_entry.delete(0,END)


def exit():
    choice=messagebox.askquestion('Exit Appliction','Are You Sure You Want To Close The Application?')
    if choice=='yes':
        root.destroy()
    else:
        return

def copy_number():
    selected_contact=list_box.get(ANCHOR)
    number=selected_contact.split(':')
    pyperclip.copy(number[1].replace('\n',""))


def save_list_users():
    with open('D:\ContactPrj\\users.txt','w') as f1:
        list_tuple=list_box.get(0,END)
        for item in list_tuple:
                f1.write(item+'\n')


def open_list_users():
    list_box.delete()
    with open ('D:\ContactPrj\\users.txt','r') as f1:
        for line in f1:
            list_box.insert(END,line)
    f1.close()


def save_list():
    with open('D:\ContactPrj\\users.txt','w') as f:
        list_tuple=list_box.get(0,END)
        for item in list_tuple:
                f.write(item+'\n')


def open_list():
    list_box.delete()
    with open ('D:\ContactPrj\contacts.txt','r') as f:
        for line in f:
            list_box.insert(END,line)
    f.close()
#________________________________________Contact____________________________________________
def add_contact():
    c=list_box_c.size()
    n=list_box_c.get(c-1)
    number=n.split('.')

    user_str=str(int(number[0])+1)+'.'+name_entry_c.get()+'_'+family_entry_c.get()+': '+phone_entry_c.get()+';'+str(id)
    list_box_c.insert(END,user_str)



    name_entry_c.delete(0,END)
    family_entry_c.delete(0,END)
    phone_entry_c.delete(0,END)

def delete_contact():
    list_box_c.delete(ANCHOR)
    name_entry_c.delete(0,END)
    family_entry_c.delete(0,END)
    phone_entry_c.delete(0,END)

def save_list_contacts():
    with open('D:\ContactPrj\contacts.txt','w') as f:
        list_tuple=list_box_c.get(0,END)
        for item in list_tuple:
                f.write(item+'\n')

#_________________
# 
# ____________________________________________________________________
def exit_all():
    Screen.destroy         

def form():
    global root
    root=Tk()
    root.geometry('900x600')
    root.title('دفترچه ی تلفن')
    background='#808080'
    root.config(bg=background)
    bg2='White'
    id=0
 

 
    #______________Users View__________________________________

    #name_label
    name_label=Label(root,text='Name:',bg=bg2,fg='Black',anchor='w',justify=LEFT,padx=25)
    name_label.place(relx=0.15,rely=0.1,anchor='c')
    global name_entry
    name_entry=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    name_entry.place(relx=0.4,rely=0.1,anchor='c')

    #family_label
    family_label=Label(root,text='Family:',bg=bg2,fg='Black',anchor='w',justify=LEFT,padx=25)
    family_label.place(relx=0.15,rely=0.14,anchor='c')
    global family_entry
    family_entry=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    family_entry.place(relx=0.4,rely=0.14,anchor='c')

    #pass_label
    pass_label=Label(root,text='Password: ',bg=bg2,fg='Black',anchor='w',justify=LEFT,padx=25)
    pass_label.place(relx=0.15,rely=0.20,anchor='c')
    global password_entry
    password_entry=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    password_entry.place(relx=0.4,rely=0.20,anchor='c')

    #phone_label
    phone_label=Label(root,text='PhoneNumber:',bg=bg2,fg='Black',anchor='w',justify=LEFT)
    phone_label.place(relx=0.15,rely=0.24,anchor='c')
    global phone_entry
    phone_entry=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    phone_entry.place(relx=0.4,rely=0.24,anchor='c')

    #add_button
    add_button=Button(root,text='Add Contact',bg=bg2,fg='Black',padx=110,command=add_user)
    add_button.place(relx=0.32,rely=0.30,anchor='c')

    #save_button
    save_button=Button(root,text='Save List',bg=bg2,fg='Black',padx=120,command=save_list)
    save_button.place(relx=0.32,rely=0.36,anchor='c')

    #copy_phonenumber_button
    copy_button=Button(root,text='Copy PhoneNumber',bg=bg2,fg='Black',command=copy_number)
    copy_button.place(relx=0.2,rely=0.42,anchor='c')

    #open_file_button
    open_button=Button(root,text='Open Save File',bg=bg2,fg='Black',padx=17)
    open_button.place(relx=0.45,rely=0.42,anchor='c')

    #delete_button
    del_button=Button(root,text='Delete Contact',bg=bg2,fg='Black',padx=17,command=delete_user)
    del_button.place(relx=0.2,rely=0.47,anchor='c')

    #exit_app_button
    exit_button=Button(root,text='Exit',bg=bg2,fg='Black',padx=45,command=exit)
    exit_button.place(relx=0.45,rely=0.47,anchor='c')

    #list_box
    global list_box
    list_box=Listbox(root,width=40,height=15)
    list_box.place(relx=0.75,rely=0.30,anchor='c')


    #_____________End  User view___________________________________




    #______________Contact View__________________________________
    name_label_line=Label(root,text='************************************************************************************************************************************************************************************************************************************************',bg=bg2,fg='Black',anchor='w',justify=LEFT,padx=90)
    name_label_line.place(relx=0.15,rely=0.55,anchor='c')
    
    #name_label
    name_label_c=Label(root,text='Name:',bg=bg2,fg='Black',anchor='w',justify=LEFT,padx=25)
    name_label_c.place(relx=0.15,rely=0.60,anchor='c')
    global name_entry_c
    name_entry_c=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    name_entry_c.place(relx=0.4,rely=0.60,anchor='c')

    #family_label
    family_label_c=Label(root,text='Family:',bg=bg2,fg='Black',anchor='w',justify=LEFT,padx=25)
    family_label_c.place(relx=0.15,rely=0.64,anchor='c')
    global family_entry_c
    family_entry_c=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    family_entry_c.place(relx=0.4,rely=0.64,anchor='c')

    #phone_label
    phone_label_c=Label(root,text='PhoneNumber:',bg=bg2,fg='Black',anchor='w',justify=LEFT)
    phone_label_c.place(relx=0.15,rely=0.70,anchor='c')
    global phone_entry_c
    phone_entry_c=Entry(root,bg='White',fg='Black',width=30,borderwidth=2)
    phone_entry_c.place(relx=0.4,rely=0.70,anchor='c')

    #add_button
    add_button_c=Button(root,text='Add Contact',bg=bg2,fg='Black',padx=110,command=add_contact)
    add_button_c.place(relx=0.32,rely=0.75,anchor='c')

    #save_button
    save_button_c=Button(root,text='Save List',bg=bg2,fg='Black',padx=120,command=save_list_contacts)
    save_button_c.place(relx=0.32,rely=0.80,anchor='c')

    #delete_button
    del_button_c=Button(root,text='Delete Contact',bg=bg2,fg='Black',padx=17,command=delete_contact)
    del_button_c.place(relx=0.2,rely=0.85,anchor='c')

    #exit_app_button
    exit_button_c=Button(root,text='Exit',bg=bg2,fg='Black',padx=45,command=exit)
    exit_button_c.place(relx=0.45,rely=0.85,anchor='c')

    #list_box
    global list_box_c
    list_box_c=Listbox(root,width=40,height=15)
    list_box_c.place(relx=0.75,rely=0.80,anchor='c')


    #___________________End Contact View_________________________


    c=list_box.size()
    n=list_box.get(c-1)
    number=n.split('.')
    if(number[0]==''):
            user_str='0'+'.'+'admin'+'_'+'admin'+','+'admin'+': '+'admin'+';'+str(id)
            list_box.insert(END,user_str)
            with open('D:\ContactPrj\\users.txt','w') as f:
                list_tuple=list_box.get(0,END)
                for item in list_tuple:
                    f.write(item+'\n')

            contact_str='0'+'.'+'admin'+'_'+'admin'+': '+'admin'+';'+str(id)
            list_box_c.insert(END,contact_str)
            with open('D:\ContactPrj\contacts.txt','w') as f:
                list_tuple=list_box.get(0,END)
                for item in list_tuple:
                    f.write(item+'\n')           

    open_list()



def login_a_u():
    u=user_entry.get()

    #form()

    p=pass_entry.get()
    if u=='admin' and p=='admin':
      print('success')
      form()
    else:
      with open('D:\ContactPrj\\users.txt','r') as f1:
        for line in f1:
            num=line.split(',')
            num1=num[0].split('.')
            if u==num1[1]:
                id=num1[0]
                form()


def main():
    
    id=0
    global Screen
    Screen= Tk()
    Screen.title('login')
    Screen.geometry('500x300')
    bg2='#a1a1a1'
    Screen.config(bg=bg2)
    user_label=Label(Screen,text='username: ',bg=bg2,fg='White',anchor='w')
    user_label.place(relx=0.1,rely=0.1,anchor='c')
    pass_label=Label(Screen,text='password: ',bg=bg2,fg='White',anchor='w')
    pass_label.place(relx=0.1,rely=0.4,anchor='c')

    global user_entry
    user_entry=Entry(Screen,bg='White',fg=bg2,width=30)
    user_entry.place(relx=0.4,rely=0.1,anchor='c')

    global pass_entry
    pass_entry=Entry(Screen,bg='White',fg=bg2,width=30)
    pass_entry.place(relx=0.4,rely=0.4,anchor='c')

    global login_button
    login_button=Button(Screen,text='Log In',bg=bg2,fg='White',borderwidth=3,padx=50,command=login_a_u)
    login_button.place(relx=0.4,rely=0.5,anchor='c')


    global exit_button
    exit_button=Button(Screen,text='Exit',bg=bg2,fg='White',borderwidth=3,padx=50,command=exit_all)
    exit_button.place(relx=0.7,rely=0.5,anchor='c')






    Screen.mainloop()







main()