from tkinter import*

def click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def clearButton():
    global operator
    operator = ''
    text_input.set("")

def equalsInput():
    global operator
    result=str(eval(operator))
    text_input.set(result)
    operator = ''


calcul = Tk()
calcul.title('Calculator')
operator =""
text_input = StringVar()
display = Entry(calcul, font=('arial' , 20 , 'bold') , textvariable=text_input , bd=30 , insertwidth=4 , bg='powder blue', justify='right' ).grid(columnspan=4)


btn7 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') ,  text='7',command=lambda :click(7) ).grid(row=1 , column = 0)

btn8 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='8',command=lambda :click(8)).grid(row=1 , column = 1)

btn9 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='9',command=lambda :click(9)).grid(row=1 , column = 2)

addition = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='+',command=lambda :click('+')).grid(row=1 , column = 3)

#----------------------------------------------------------------------------------------------------------------------

btn4 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='4',command=lambda :click(4)).grid(row=2 , column = 0)

btn5 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='5',command=lambda :click(5)).grid(row=2 , column = 1)

btn6 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='6',command=lambda :click(6)).grid(row=2 , column = 2)

substraction = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='-',command=lambda :click('-')).grid(row=2 , column = 3)

#----------------------------------------------------------------------------------------------------------------------

btn1 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='1',command=lambda :click(1)).grid(row=3 , column = 0)

btn2 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='2',command=lambda :click(2)).grid(row=3 , column = 1)

btn3 = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='3',command=lambda :click(3)).grid(row=3 , column = 2)

multiply = Button(calcul , padx=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='*',command=lambda :click('*')).grid(row=3 , column = 3)

#----------------------------------------------------------------------------------------------------------------------

btn0 = Button(calcul , padx=16 , pady=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='0',command=lambda :click(0)).grid(row=4 , column = 0)

btnClear = Button(calcul , padx=16 , pady=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='C', command=clearButton ).grid(row=4 , column = 1)

camas = Button(calcul , padx=16  , pady=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text=',',command=lambda :click('.')).grid(row=4 , column=2)

Diviion = Button(calcul , padx=16 , pady=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='/',command=lambda :click('/')).grid(row=4 , column = 3)

btnEquals = Button(calcul , padx=16 , pady=16 , bd=8 , fg='black' , font=('arial' , 20 , 'bold') , text='=', command = equalsInput).grid(row=5, columnspan=4,sticky=W+E)


calcul.mainloop()