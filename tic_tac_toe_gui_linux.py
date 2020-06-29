import tkinter as tk
from tkinter import messagebox

class board(tk.Canvas):
	def __init__(self,player1_name,player2_name):
		super().__init__(width="400",height="450",background="#b9d929",highlightthickness=0)
		self.create_board()
		self.player1_name=player1_name
		self.player2_name=player2_name
		self.turn=1
		self.no_of_turns=0
		self.moves_player1_row=[]
		self.moves_player1_column=[]
		self.moves_player2_row=[]
		self.moves_player2_column=[]
		self.set=1
		self.game_text=self.create_text(200,50,text="%s 's Turn"%self.player1_name,fill="#fff",font=("TkDefaultFont",20))
		self.bind("<Button-1>",self.callback)

	def create_board(self):
		self.create_line(150,100,150,400,width=5,fill="#270e4f")
		self.create_line(250,100,250,400,width=5,fill="#270e4f")
		self.create_line(50,200,350,200,width=5,fill="#270e4f")
		self.create_line(50,300,350,300,width=5,fill="#270e4f")
	def callback(self,event):
		self.click_position={}
		self.click_position["x"],self.click_position["y"]=event.x,event.y
		if (50<=self.click_position["x"] and self.click_position["x"]<=350
			and 100<=self.click_position["y"] and self.click_position["y"]<=400):
			self.perform_action()

	def perform_action(self):
		self.no_of_turns+=1

		if (50<=self.click_position["x"] and self.click_position["x"]<=150
			and 100<=self.click_position["y"] and self.click_position["y"]<=200):
			if ((0,0) in zip(self.moves_player1_row,self.moves_player1_column) or
				(0,0) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(0)
				self.moves_player1_column.append(0)				
				self.draw_cross(50,100,150,200)
			else:
				self.moves_player2_row.append(0)
				self.moves_player2_column.append(0)
				self.draw_circle(50,100,150,200)

		elif (150<=self.click_position["x"] and self.click_position["x"]<=250
			and 100<=self.click_position["y"] and self.click_position["y"]<=200):
			if ((0,1) in zip(self.moves_player1_row,self.moves_player1_column) or
				(0,1) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(0)
				self.moves_player1_column.append(1)					
				self.draw_cross(150,100,250,200)
			else:
				self.moves_player2_row.append(0)
				self.moves_player2_column.append(1)				
				self.draw_circle(150,100,250,200)

		elif (250<=self.click_position["x"] and self.click_position["x"]<=350
			and 100<=self.click_position["y"] and self.click_position["y"]<=200):
			if ((0,2) in zip(self.moves_player1_row,self.moves_player1_column) or
				(0,2) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(0)
				self.moves_player1_column.append(2)					
				self.draw_cross(250,100,350,200)
			else:
				self.moves_player2_row.append(0)
				self.moves_player2_column.append(2)					
				self.draw_circle(250,100,350,200)

		elif (50<=self.click_position["x"] and self.click_position["x"]<=150
			and 200<=self.click_position["y"] and self.click_position["y"]<=300):
			if ((1,0) in zip(self.moves_player1_row,self.moves_player1_column) or
				(1,0) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(1)
				self.moves_player1_column.append(0)					
				self.draw_cross(50,200,150,300)
			else:
				self.moves_player2_row.append(1)
				self.moves_player2_column.append(0)								
				self.draw_circle(50,200,150,300)

		elif (150<=self.click_position["x"] and self.click_position["x"]<=250
			and 200<=self.click_position["y"] and self.click_position["y"]<=300):
			if ((1,1) in zip(self.moves_player1_row,self.moves_player1_column) or
				(1,1) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(1)
				self.moves_player1_column.append(1)					
				self.draw_cross(150,200,250,300)
			else:
				self.moves_player2_row.append(1)
				self.moves_player2_column.append(1)								
				self.draw_circle(150,200,250,300)

		elif (250<=self.click_position["x"] and self.click_position["x"]<=350
			and 200<=self.click_position["y"] and self.click_position["y"]<=300):
			if ((1,2) in zip(self.moves_player1_row,self.moves_player1_column) or
				(1,2) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(1)
				self.moves_player1_column.append(2)								
				self.draw_cross(250,200,350,300)
			else:
				self.moves_player2_row.append(1)
				self.moves_player2_column.append(2)								
				self.draw_circle(250,200,350,300)

		elif (50<=self.click_position["x"] and self.click_position["x"]<=150
			and 300<=self.click_position["y"] and self.click_position["y"]<=400):
			if ((2,0) in zip(self.moves_player1_row,self.moves_player1_column) or
				(2,0) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(2)
				self.moves_player1_column.append(0)								
				self.draw_cross(50,300,150,400)
			else:
				self.moves_player2_row.append(2)
				self.moves_player2_column.append(0)								
				self.draw_circle(50,300,150,400)

		elif (150<=self.click_position["x"] and self.click_position["x"]<=250
			and 300<=self.click_position["y"] and self.click_position["y"]<=400):
			if ((2,1) in zip(self.moves_player1_row,self.moves_player1_column) or
				(2,1) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(2)
				self.moves_player1_column.append(1)				
				self.draw_cross(150,300,250,400)
			else:
				self.moves_player2_row.append(2)
				self.moves_player2_column.append(1)					
				self.draw_circle(150,300,250,400)

		elif (250<=self.click_position["x"] and self.click_position["x"]<=350
			and 300<=self.click_position["y"] and self.click_position["y"]<=400):
			if ((2,2) in zip(self.moves_player1_row,self.moves_player1_column) or 
				(2,2) in zip(self.moves_player2_row,self.moves_player2_column)):
				self.no_of_turns-=1
				return
			if self.turn==1:
				self.moves_player1_row.append(2)
				self.moves_player1_column.append(2)				
				self.draw_cross(250,300,350,400)
			else:
				self.moves_player2_row.append(2)
				self.moves_player2_column.append(2)				
				self.draw_circle(250,300,350,400)

		if self.no_of_turns>=9 and self.set==1:
			self.end_game_screen(2)

	def draw_cross(self,x1,y1,x2,y2):
		self.create_line(x1+20,y1+20,x2-20,y2-20,width=7,fill="#187058")
		self.create_line(x2-20,y1+20,x1+20,y2-20,width=7,fill="#187058")
		self.turn=0
		if len(self.moves_player1_row)>=3 and len(self.moves_player1_column)>=3:
			self.check(self.moves_player1_row,self.moves_player1_column,1)
		if self.set==1:
			self.itemconfig(self.game_text,text="%s 's Turn"%(self.player2_name))

	def draw_circle(self,x1,y1,x2,y2):
		self.create_oval(x1+20,y1+20,x2-20,y2-20,width=7,outline="#ab0205")
		self.turn=1
		if len(self.moves_player2_row)>=3 and len(self.moves_player2_column)>=3:
			self.check(self.moves_player2_row,self.moves_player2_column,0)
		if self.set==1:
			self.itemconfig(self.game_text,text="%s 's Turn"%(self.player1_name))
		

	def end_game_screen(self,winner,way=None,path=None):
		self.unbind("<Button-1>")
		self.set=0
		if winner == 2:
			self.itemconfig(self.game_text,text="Game Drawn!",fill="#9c067e",font=(30))
		else:
			if way == 0:
				if path == 0:
					self.create_line(50,150,350,150,width=7,fill="#bf6908")
				elif path == 1:
					self.create_line(50,250,350,250,width=7,fill="#bf6908")
				elif path == 2:
					self.create_line(50,350,350,350,width=7,fill="#bf6908")
			elif way == 1:
				if path == 0:
					self.create_line(100,100,100,400,width=7,fill="#bf6908")
				elif path == 1:
					self.create_line(200,100,200,400,width=7,fill="#bf6908")
				elif path == 2:
					self.create_line(300,100,300,400,width=7,fill="#bf6908")
			elif way==2:
				if path == 0:
					self.create_line(50,100,350,400,width=7,fill="#bf6908")
				elif path == 1:
					self.create_line(350,100,50,400,width=7,fill="#bf6908")
			if winner==1:
				self.itemconfig(self.game_text,text="%s Wins!"%self.player1_name,fill="#9c067e",font=(30))
			elif winner==0:
				self.itemconfig(self.game_text,text="%s Wins!"%self.player2_name,fill="#9c067e",font=(30))


		reply=messagebox.askquestion("Play Again!","Do you want to Play Again?")
		if reply=="yes":
			root.destroy()
			restart()

	
	def check(self,moves_row,moves_column,winner):
		for i in range(len(moves_row)):
			if moves_row.count(moves_row[i])==3:
				self.end_game_screen(winner,0,moves_row[i])

		for i in range(len(moves_column)):
			if moves_column.count(moves_column[i])==3:
				self.end_game_screen(winner,1,moves_column[i])
		match_equal=0
		match_opposite=0
		for i in range(len(moves_row)):
			if moves_row[i] == moves_column[i]:
				match_equal+=1
			if ( abs(moves_row[i]-moves_column[i])==2
			   or (moves_row[i] == 1 and moves_column[i] == 1) ):
				match_opposite+=1
			if match_equal==3:
				self.end_game_screen(winner,2,0)
			if match_opposite==3:
				self.end_game_screen(winner,2,1)
				



def root_buit():
	global root
	root=tk.Tk()
	root.title("TIC TAC TOE GAME")
	root.resizable(False,False)

class menu_screen():
	def __init__(self):
		self.set_menu=1
		self.opening()


	def opening(self):	
		root_buit()
		self.welcome_box()
		self.name_input()

	def welcome_box(self):
		root.geometry("500x300")
		root.config(bg="#FDCD30")
		self.welcome_text =tk.Label(root,text="WELCOME TO THE GAME OF TIC TAC TOE",font="60",bg="#FDCD30")
		self.welcome_text.pack(pady=30)

	def name_input(self):
		self.player1_text=tk.Label(root,text="Enter Name of Player 1:",font="20",bg="#FDCD30")
		self.player1_text.pack()
		self.entry_1=tk.Entry(root)
		self.entry_1.pack(pady=10)
		self.player2_text=tk.Label(root,text="Enter Name of Player 2:",font="20",bg="#FDCD30")
		self.player2_text.pack()
		self.entry_2=tk.Entry(root)
		self.entry_2.pack(pady=10)
		self.next_button=tk.Button(root,text="NEXT",command=self.name_assign)
		self.next_button.pack(pady=5)


	def radio_button_assign(self):
		self.check_box_msg=tk.Label(root,text="%s,Please Choose:"%self.name1,font="20",bg="#FDCD30")
		self.check_box_msg.pack()
		self.var=tk.IntVar()
		self.var.set(0)
		self.radio_button1=tk.Radiobutton(root,text="Cross",font="20",variable=self.var,value=0,bg="#FDCD30")
		self.radio_button1.pack(pady=10)
		self.radio_button2=tk.Radiobutton(root,text="Circle",font="20",variable=self.var,value=1,bg="#FDCD30")
		self.radio_button2.pack(pady=10)
		self.start_button=tk.Button(root,text="Start Game",command=self.role_assign)
		self.start_button.pack(pady=5)

	def role_assign(self):
		selection=self.var.get()
		if selection==0:
			self.player1_name=self.name1
			self.player2_name=self.name2
		else:
			self.player1_name=self.name2
			self.player2_name=self.name1
		self.welcome_text.pack_forget()
		self.check_box_msg.pack_forget()
		self.radio_button1.pack_forget()
		self.radio_button2.pack_forget()
		self.start_button.pack_forget()
		if self.set_menu==0:
			self.different_players_button.pack_forget()


		start_game(self.player1_name,self.player2_name)



	def name_assign(self):
		self.name1=self.entry_1.get()
		self.name2=self.entry_2.get()
		if self.name1!="" and self.name2!="":
			self.player1_text.pack_forget()
			self.entry_1.pack_forget()
			self.player2_text.pack_forget()
			self.entry_2.pack_forget()
			self.next_button.pack_forget()
			self.radio_button_assign()

menu=menu_screen()





def start_game(player1_name,player2_name):
	root.geometry("400x450")
	game=board(player1_name,player2_name)
	game.pack()

def restart_different():
	root.destroy()
	menu.set_menu=1
	menu.opening()



def restart():
	root_buit()
	menu.welcome_box()
	menu.radio_button_assign()
	menu.set_menu=0
	menu.different_players_button=tk.Button(root,text="Play with different player?",command=restart_different)
	menu.different_players_button.pack(pady=10)





root.mainloop()	