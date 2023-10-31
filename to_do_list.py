import tkinter as tk


root= tk.Tk()

root.title("To do Check list")
root.geometry('500x500')
# root.maxsize(300,400)
root.minsize(100,200)


def add_checklist():
    global text
    text= tk.Entry(root,bd=3, width=30)
    text.place(x=250,y=60)  

    display_info=tk.Label(root,text=' ENTER TO ADD TODO',font= 'timesnewroman', borderwidth=1,anchor='w',width=20,pady=1)
    display_info.place(x=0,y=60)

    save = tk.Button(root, text="Enter", command=save_text,bd=1,)
    save.place(x=450,y=60)
    
    

def save_text():
    global i
    global x
    global listbox
    save_text=text.get()
    # dictionary[i]=save_text
    # listbox.insert(tk.END,save_text)
    # check_box= tk.Checkbutton(root)
    listbox.insert(tk.END,save_text)
    text.delete(0,tk.END)

     
    
# for i in dictionary:
        
        
    """checklist=tk.Label(root,text=dictionary[i],bd=3,border=3,font= 'Arial', borderwidth=6)
        if len(dictionary[i])==0:
            pass
        else:
            checklist.grid(row=x)
            button1 = tk.Checkbutton(root,   
                      variable = dictionary[i], 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 6, 
                      width = 10) 
            button1.grid(row=x,column=2)

            delete_button=tk.Button(root,text='Delete',command=delete_checklist(),justify='right')
            delete_button.grid(row=x,column=3)
    x+=1"""
   

#    text_file = open("test.txt", "w")
#    text_file.write(text.get(1.0, END))
#    text_file.close()


def delete_checklist():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass






l1= tk.Label(root,text='TO ADD TODO LIST',bd=3,font= 'Arial', borderwidth=6,anchor='w',width=20,pady=0)
l1.place(x=0,y=6)

add_button= tk.Button(root,text='ADD',command=add_checklist,width=5,height=1)
add_button.place(x=250,y=10)

delete_button= tk.Button(root,text='DELETE',command=delete_checklist,width=8,height=1)
delete_button.place(x=300,y=10)



listbox = tk.Listbox(root, width=45,height=19,font='timesnewroman',foreground='black', )
listbox.place(x=0,y=100)



root.mainloop()