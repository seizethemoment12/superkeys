# Title: superkeys
# Author: Brandon Allen
# Date: Feb 2015
# Purpose: Keyboard launcher for linux/gnome

# imported for ui elements
from tkinter import *

# imported to allow us to run other processes
import subprocess

# imported for string manipulation
import re

# only being imported because I might need it later. Will probably take this out
import os


	#####################################################
	# 						TODO LIST					#
	#####################################################
#TODO: Change from using subprocess so we can do stuff after we open an application
#TODO: Handle enter press when text field is selected
#TODO: Handle visability using a key combination
#TODO: Make a display window instead of using the console to output to
#TODO: More functionality

class Application(Frame):

	######################################################
	# Function that grabs the users entry
	# and decides what to do with it
	######################################################
	def grab_entry(self):
		#variable definitions
		key_words = ['ls', 'web']
		browser = 'epiphany'
		
		# grab the user's entry
		query_to_pass = self.search_field.get()
        
        # check if the word entered is a keyword
		phrase_split = re.split(' ', query_to_pass)
		word = phrase_split[0]
		if word in key_words:
			self.use_keyword(query_to_pass, key_words)
        
        # if it wasn't a keyword then move on
		else:
			# try to launch the program
			try:
				self.launch_program(query_to_pass)
			except:
				# if not on system check the web
				self.do_web_search(browser, query_to_pass)
	
	
	######################################################
	# Function that performs an action based on a keyword
	######################################################
	def use_keyword(self, passed_argument, key_words):
		
		# grab first part of the passed query
		phrase_split = re.split(' ', passed_argument)
		word = phrase_split[0]
		if len(phrase_split) > 1:
			argument = phrase_split[1]
					
		# a key word exists in our list so lets see if we can work with it	
		try:
			if word == 'ls':
					directory = ' ' + argument
					subprocess.call(['ls', directory])
					print('ls' + directory)
			if word == 'web':
					print('need to find chrome command')
		except:
			print('keyword usage failed')

		
	######################################################
	# Function that launches a program 
	######################################################
	def launch_program(self, passed_program):
		subprocess.call([passed_program])
	
	######################################################
	# Function that performs a web search
	# based on the users input
	######################################################	
	def do_web_search(self, browser, passed_query):
		search_agent = 'https://www.google.com/#q='
		query = search_agent+passed_query
		subprocess.call([browser, query])
		
	######################################################
	# Function for debugging
	######################################################
	def test(self):
		print("Enter Pressed")

	######################################################
	# Function that creates the UI elements
	######################################################
	def createWidgets(self):
		# create the exit button
		self.quit_button = Button(self)
		self.quit_button["text"] = "QUIT"
		self.quit_button["fg"] = "red"
		self.quit_button["command"] = self.quit
		self.quit_button.pack({"side": "left"})
		
		# create the text entry field
		self.search_field = Entry(self)
		self.search_field.pack({"side": "left"})
		
		# how can I catch "Enter" being pressed???
		#self.search_field.bind('<Return>', self.test())
        
		# create the search button
		self.search_button = Button(self)
		self.search_button["text"] = "Magic",
		self.search_button["command"] = self.grab_entry
		self.search_button.pack({"side": "left"})
		
	######################################################
	# Main Function
	######################################################
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
    
# create the app and screen
root = Tk()

app = Application(master=root)

# tell the window where to go on the screen
root.geometry("300x50+800+500")


# adjust the size
app.master.title("SuperKeys")

# start the program
app.mainloop()

# kill the program
root.destroy()
