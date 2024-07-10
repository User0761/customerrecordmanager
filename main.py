from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
window=Tk()
window.title('Customer Record')
window.geometry("780x450")
window.configure(bg="#DAF7A6")
#labelframe
labelFrame=LabelFrame(window,text="Personal Details",font=("Courier",12, "bold"),fg="#055B6B",bg="#DAF7A6")
labelFrame.grid(row=2,column=3)

#Create an empty dictionary
customerRecord={}
#function to clear text of the entry
def clear_all():
	contact.delete(0,END)
	name.delete(0,END)
	address.delete(0,END)
	email.delete(0,END)
#update the listbox
def update():
	key=contact.get()
	if key=="":
		messagebox.showinfo("Error", "Contact cannot be empty")
	else:
		if key not in customerRecord.keys():
			customer_list.insert(END,key)
		customerRecord[key]=(name.get(),address.get(),email.get())
		clear_all()
#edit the selected item
def edit():
	#clear the textboxes if any
	clear_all()
	# get selected line index
	index = customer_list.curselection()
	if index:
		#add contact to entry
		contact.insert(0,customer_list.get(index))
		#get details corresponding to contact from dictionary
		details=customerRecord[contact.get()]
		#add details to text boxes
		name.insert(0,details[0])
		address.insert(0,details[1])
		email.insert(0,details[2])
	else:
		messagebox.showinfo("Error", "Select a record.")
#delete selected item
def delete():
  # get selected line index
  index = customer_list.curselection()
  if index:
    #delete from dictionary
    del customerRecord[customer_list.get(index)]
	#delete from listbox
    customer_list.delete(index)
    #clear the textboxes if any
    clear_all()
  else:
    messagebox.showinfo("Error", "Select a record.")
def reset():
  clear_all()
  #deletes the listbox
  customer_list.delete(0,END)
  #Removes all existing entries
  customerRecord.clear()
def save():
	#get file using dialog
	fileSave=asksaveasfile()
	#if filename selected 
	if fileSave:
		print(customerRecord,file=fileSave)
		reset()
	else:
		messagebox.showinfo("Warning", "Customer Record not saved")
def openFile():
	reset()
	#opens file using dialog
	fileOpen=askopenfile()
	#if filename selected
	if fileOpen:
    #read file 
		customerRecord=eval(fileOpen.read())
		#populate listbox
		for key in customerRecord.keys():
			customer_list.insert(END,key)
			#display filename on screen
	else:
		messagebox.showinfo("Warning", "No Customer Record opened.")
#Design window/Layout
informationLabel  = Label(window, text='Enter Customer Details',width=60,bg="#055B6B",fg="white", font=("Courier",16))
informationLabel.grid(row = 0, column = 0,pady = 10,columnspan=5)
# Contact list
customer_list =Listbox(window,height=15,width=40)
customer_list.grid(row = 2, column = 0,columnspan=3, rowspan = 5)
#Text/Entry fields to display contact information
#Contact Label
contact_label =Label(labelFrame, text = 'Contact:',fg="#055B6B",bg="#DAF7A6", font=("Courier",12, "bold"))
contact_label.grid(row=0,column=0,pady=20)
#Contact Entry
contact =Entry(labelFrame)
contact.grid(row=0,column=1,pady=20,padx=10)
#Name Label
name_label =Label(labelFrame, text = 'Name:',fg="#055B6B",bg="#DAF7A6", font=("Courier",12, "bold"))
name_label.grid(row=1,column=0,pady=20)
#Name Entry
name =Entry(labelFrame)
name.grid(row=1,column=1,pady=20)
#Address Label
address_label =Label(labelFrame, text = 'Address :',fg="#055B6B",bg="#DAF7A6", font=("Courier",12, "bold"))
address_label.grid(row=2,column=0,pady=20)
#Address Entry
address =Entry(labelFrame)
address.grid(row=2,column=1,pady=20)
#Email Label
email_label = Label(labelFrame, text = 'Email:',fg="#055B6B",bg="#DAF7A6", font=("Courier",12, "bold"))
email_label.grid(row=3,column=0,pady=20)
email =Entry(labelFrame)
email.grid(row=3,column=1,pady=20)
#buttons
#Edit button
edit_button = Button(window, text = 'Edit',width=10,fg="white",bg="#055B6B", font=("Courier" "bold"),command=edit)
edit_button.grid(row = 7, column = 1,pady=12)
#Delete button
delete_button =Button(window, text = 'Delete',width=10,fg="white",bg="#055B6B", font=("Courier" "bold"),command=delete)
delete_button.grid(row = 7, column = 2,pady=12)
#Update/Add button
update_button =Button(window, text = 'Update/Add',width=20,bg="#055B6B",fg="white", font=("Courier" "bold"),command=update)
update_button.grid(row = 7, column = 3,pady=12, padx=5)
#Open button
open_button = Button(window, text='Open',width=10,bg="#055B6B",fg="white", font=("Courier" "bold"),command=openFile)
open_button.grid(row = 8, column = 2,pady = 10)
#Save button
save_button = Button(window, text='Save',width=10,bg="#055B6B",fg="white", font=("Courier" "bold"),command=save)
save_button.grid(row = 8, column = 2,pady = 10,columnspan=3)
window.mainloop()