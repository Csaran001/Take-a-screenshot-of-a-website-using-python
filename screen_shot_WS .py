import tkinter as tk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

root= tk.Tk()

root.title("SCREEN SHOT")

root.config(bg='#F2B33D')  


canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised',bg='#F2B33D')
canvas1.pack()

label2 = tk.Label(root, text='TYPE YOUR WEBSITE NAME',bg='#F2B33D')
label2.pack()
label2.config(font=("Courier", 12))
label2.config(fg="#0000FF")
label2.config(bg="yellow")
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1,height=30, width=300)

def browse ():
		c = entry1.get()
		print(c)
		options = webdriver.ChromeOptions()
		options.headless = True

		driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
		driver.implicitly_wait(5)
		url = str(c)
		url2='http://'+url+'/'

		driver.get(url2)

		S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
		driver.set_window_size(S("Width"), S('Height'))
		driver.find_element_by_tag_name('body').screenshot('screen_shot.png');


button1 = tk.Button(text='Take screenshot', command=browse, bg='brown', fg='white', font=('helvetica', 9, 'bold'), activebackground='#90ee90')
canvas1.create_window(200, 180, window=button1)

root.mainloop()