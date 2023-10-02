
from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
root.iconbitmap('ai_lt.ico') #https://tkinter.com/ai_lt.ico

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Submit to ChatGPT
def speak():
	if chat_entry.get():
# Do Something
# Define our filename
		filename = "api_key"
		try:
			if os.path.isfile(filename):
			#Open the file
				input_file = open(filename, 'rb')

			#Load the data from the file into the variable 
				stuff = pickle.load(input_file)

				# Query ChatGPT
							

				# define our api key to chatgpt
				openai.api_key = stuff
	                
	            # create an instance
				openai.Model.list()
	            
	              # Define our Query / Response
				response = openai.Completion.create(
	               	model = "text-davinci-003",
	               	prompt = chat_entry.get(),
	               	temperature = 0,  
	               	max_tokens =60,
	               	top_p = 1.0,
	               	frequency_penalty=0.0,
	               	presence_penalty=0.0, 	
					)
				my_text.insert(END, (response["choices"][0]["text"]).strip())
				my_text.insert(END, "\n\n")

			else:
			# Create the file 
				input_file = open(filename, 'wb')
			# Close the file
				input_file.close()
			# Error Message - you need an api key
				my_text.insert(END, "\n\nYou Need an API Key to talk with CHATGPT. Get one here:\nhttps://beta.openai.com/account/api-keys")

		except Exception as e:
			my_text.insert(END, f"\n\n There was an error\n\n{e}")







		pass
	else:
		my_text.insert(END, "n\nHey You forgot to type anything")

#Clear the Screesn
def clear():
	#main text box
	my_text.delete(1.0, END)
	#clear the query entry box
	chat_entry.delete(0, END)

#Do API Stuff
def key():


# Define our filename
	filename = "api_key"
	try:
		if os.path.isfile(filename):
		#Open the file
			input_file = open(filename, 'rb')

		#Load the data from the file into the variable 
			stuff = pickle.load(input_file)

	#output stuff to our entry box
			api_entry.insert(END, stuff)

		else:
		# Create the file 
			input_file = open(filename, 'wb')
		# Close the file
			input_file.close()

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")


#resize app
	root.geometry('600x750')
	#reshow api frame
	api_frame.pack(pady=30)



#save the api key
def save_key():
	# Define our filename 
	filename = "api_key"
	try:
	#Open file
		output_file = open(filename, 'wb')

	# Actually add the data to the file
		pickle.dump(api_entry.get(), output_file)


	#Delete Entry Box
		api_entry.delete(0, END)

		#hide api frame
		api_frame.pack_forget()
		#resize app smaller 
		root.geometry('600x600')

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")

# Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

# Add Text Widget to get ChatGPT Responses
my_text = Text(text_frame,
	bg="#343638",
	width=65,
	bd=1, 
	fg="#d6d6d6",                                                                 
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")

my_text.grid(row=0, column=0) 
# Create Scrollbar

text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)

text_scroll.grid(row=0, column=1, sticky="ns")

# Add the Scrollbar to the textbox 

my_text.configure(yscrollcommand=text_scroll.set)

# Entry widget to type to stuff to chatgpt

chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type Something To ChatGPT...",
	width=535,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

# create buttons frame

button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)


# create buttons
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak To ChatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

clear_button = customtkinter.CTkButton(button_frame,
	text="Clear Response",
	command=clear)
clear_button.grid(row=0, column=1, padx=35)

Api_button = customtkinter.CTkButton(button_frame,
	text="Update API Key",
	command=key)
Api_button.grid(row=0, column=2, padx=25)


# Add API Key Frame

api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

#Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame, 
	placeholder_text="Enter Your API Key", 
	width=350, height=50, border_width=1)
api_entry.grid(row=0,column=0, padx=20, pady=20)

#Add API Button
api_save_button = customtkinter.CTkButton(api_frame, 
	text="Save Key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)





root.mainloop()

