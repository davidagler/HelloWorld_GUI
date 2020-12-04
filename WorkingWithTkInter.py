from tkinter import*
root = Tk() #root is blank window

topFrame = Frame(root)#root is blank window
topFrame.pack()
botFrame = Frame(root)#root is blank window
botFrame.pack(side=BOTTOM)

#Buttons - Creation
button1 = Button(topFrame, text="Button 1 - Hello World", fg="white", bg="black")
button2 = Button(topFrame, text="Button 2 - Hello World", fg="yellow", bg="blue")
button3 = Button(topFrame, text="Button 3 - Hello World", fg="red", bg="yellow")
button4 = Button(botFrame, text="Button 4 - Hello World", fg="green", bg="orange")

#Buttons - Display
button1.pack(side=LEFT) #pack button in on left
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop() #display it it in an infinite loop
