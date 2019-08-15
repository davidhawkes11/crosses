from tkinter import *
from classes import *

global is_second_player
is_second_player = False
global main_screen
global sc_width
global sc_height
global WINDOW_SIZE
global buttons
global handle
def pop_up(msg,isWarn=False):
   global main_screen
   popup = Toplevel()
   bgcolor="red"
   fgcolor="white"
   if not isWarn:
      bgcolor="green"
      popup.title("Message")
   else: popup.title("Warning")
   popup.wm_attributes('-type', 'splash')
   Label(popup, text=msg,bg=bgcolor,fg=fgcolor,height="3", width="50").pack()
   popup.after(1500, lambda: popup.destroy())     # time in ms
   main_screen.after(1500, lambda: main_screen.destroy()) 
   popup.mainloop()

def main_screen():
	global main_screen
	global WINDOW_SIZE
	global sc_width
	global sc_height
	main_screen = Tk() 
	sc_width = int(main_screen.winfo_screenwidth()/3)
	sc_height = int(main_screen.winfo_screenheight()/3)
	WINDOW_SIZE='%sx%s' % (int(sc_width), int(sc_height))
	main_screen.geometry(WINDOW_SIZE) 
	main_screen.title("Crosses")
def analyze():
	global buttons
	txts = []
	for i in range(9):
		txts.append(str(buttons[i]['text']))
	if (txts[0] != '[   ]' and txts[0] == txts[1] and txts[0] ==txts[2]) or (txts[3] != '[   ]' and  txts[3] == txts[4] and txts[3] ==txts[5]) or (txts[6] != '[   ]' and txts[6] == txts[7] and txts[6] ==txts[8]):
		return True
	elif (txts[0] != '[   ]' and txts[0] == txts[3] and txts[0] ==txts[6]) or (txts[1] != '[   ]' and txts[1] == txts[4] and txts[1] ==txts[7]) or (txts[2] != '[   ]' and txts[2] == txts[5] and txts[2] ==txts[8]):
		return True
	elif (txts[0] != '[   ]' and txts[0] == txts[4] and txts[0] ==txts[8]) or (txts[2] != '[   ]' and txts[2] == txts[4] and txts[2] ==txts[6]):
		return True
	return False
def box_action(b_index):
	global buttons
	global main_screen
	global is_second_player
	b = handle.boxs[b_index]
	val = None
	btext = '[T]'
	if not is_second_player:	btext = '[T]'
	else:	btext = '[F]'
	b.set( not is_second_player)
	buttons[b_index].configure(bg=b.bgcolor,fg=b.fgcolor,text=btext)
	is_second_player = not is_second_player 
	
	buttons[b_index]['state'] = 'disabled'
	if analyze():
		pop_up(btext+" wins!")
		

def create_gui():
	global main_screen
	global buttons
	global handle
	global sc_width
	global sc_height
	main_screen()
	handle = Handler()
	buttons = []
	color='black'
	text='[   ]'
	wd = int(sc_width/29)
	ht = 4
	b0 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(0))
	b1 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(1))
	b2 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(2))
	b3 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(3))
	b4 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(4))
	b5 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(5))
	b6 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(6))
	b7 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(7))
	b8 = Button(main_screen,text=text,bg="white",width=wd,height=ht, fg=color, command=lambda:   box_action(8))

	b0.grid(row=0,column=0)
	b1.grid(row=0,column=1)
	b2.grid(row=0,column=2)
	b3.grid(row=1,column=0)
	b4.grid(row=1,column=1)
	b5.grid(row=1,column=2)
	b6.grid(row=2,column=0)
	b7.grid(row=2,column=1)
	b8.grid(row=2,column=2)
	buttons.append(b0)
	buttons.append(b1)
	buttons.append(b2)
	buttons.append(b3)
	buttons.append(b4)
	buttons.append(b5)
	buttons.append(b6)
	buttons.append(b7)
	buttons.append(b8)
 	

create_gui()
main_screen.mainloop()