import tkinter
import time
import random
import math
import questions
from PIL import ImageTk, Image




questionss = ''
answerss = ''   

def new_question(subject):
  if subject == 'life':
    global questionss
    global answerss
    questionss, answerss = random.choice(list(questions.LifeSQ1.items()))
    









entry_window = tkinter.Tk()
welcome_image = ImageTk.PhotoImage(Image.open("welcome_image.jpg"))

def destroy():
  entry_window.destroy()

image_label = tkinter.Label(image=welcome_image)
destroy_button = tkinter.Button(entry_window,text='Go',command=destroy)

image_label.grid(row=0,column=0)
destroy_button.grid(row=5,column=0)

entry_window.mainloop()








main_window = tkinter.Tk()
""""
def high_school_window():
    main_window.destroy()
    high_schoolwindow = tkinter.Tk()
    high_schoolwindow.title('Science Bowl High School Practice Questions')

    biology_q = tkinter.Button(high_schoolwindow,text='Biology',width=15,padx=0)
    physics_q = tkinter.Button(high_schoolwindow,text='Physics',width=15,padx=0)
    earth_q = tkinter.Button(high_schoolwindow,text='Earth Science',width=15,padx=0)
    space_q = tkinter.Button(high_schoolwindow,text='Astrology',width=15,padx=0)
    math_q = tkinter.Button(high_schoolwindow,text='Math',width=15,padx=0)
    energy_q = tkinter.Button(high_schoolwindow,text='Energy',width=15,padx=0)
    chemistry_q = tkinter.Button(high_schoolwindow,text='Chemistry',width=15,padx=0,pady=0)
    answer_entry = tkinter.Entry(high_schoolwindow,text='Answer',width=30,bd=5)

    biology_q.grid(row=3,column=0)
    physics_q.grid(row=3,column=1)
    space_q.grid(row=3,column=2)
    earth_q.grid(row=3,column=3)
    math_q.grid(row=3,column=4)
    energy_q.grid(row=3,column=5)
    chemistry_q.grid(row=3,column=6)
    answer_entry.grid(row=2,column=0,columnspan=3,padx=0)

    high_schoolwindow.mainloop()
""" 

  
      

    

def middle_school_window():
  total = 0
  main_window.destroy()
  middle_schoolwindow = tkinter.Tk()
  middle_schoolwindow.title('Science Bowl Middle School Practice Questions')
  middle_schoolwindow.configure(bg='deep sky blue')
  def new_question(subject):
    global questionss
    global answerss
    if subject == 'life':

      questionss, answerss = random.choice(list(questions.LifeSQ1.items()))
    if subject == 'math':

      questionss, answerss = random.choice(list(questions.MathQ1.items()))
    if subject == 'General':

      questionss, answerss = random.choice(list(questions.GeneralSQ1.items()))
    if subject == 'earth':

      questionss, answerss = random.choice(list(questions.EarthSQ1.items()))
    if subject == 'physical':

      questionss, answerss = random.choice(list(questions.PhysicalSQ1.items()))
    question_entry.delete(0,tkinter.END)
    question_entry.insert(0,questionss)
    question_entry.config({"background":"antique white"})
    answer_entry.config({"background":"antique white"})
    answer_entry.delete(0,tkinter.END)
  def enter():
    answer = answer_entry.get()
    if answer.lower() == answerss.lower():
      answer_entry.delete(0,tkinter.END)
      answer_entry.insert(0,'CORRECT!')
      answer_entry.config({"background":"Light Green"})
    else:
      answer_entry.delete(0,tkinter.END)
      answer_entry.insert(0,'WRONG')
      answer_entry.delete(0,tkinter.END)
      correct_answer = 'The correct answer is: ' + str(answerss).lower()
      answer_entry.insert(0,correct_answer)
      answer_entry.config({"background":"Red"})
    
    

  life_q = tkinter.Button(middle_schoolwindow,text='Life Science',width=15,padx=0,bg="gold",command = lambda:new_question('life'))
  physical_q = tkinter.Button(middle_schoolwindow,text='Physical Science',width=15,padx=0,bg="gold",command = lambda:new_question('physical'))
  earth_q = tkinter.Button(middle_schoolwindow,text='Earth Science',width=15,padx=0,bg="gold",command = lambda:new_question('earth'))
  General_q = tkinter.Button(middle_schoolwindow,text='General Science',width=15,padx=0,bg="gold",command = lambda:new_question('General'))
  math_q = tkinter.Button(middle_schoolwindow,text='Math',width=15,padx=0,bg="gold",command = lambda:new_question('math'))
  answer_entry = tkinter.Entry(middle_schoolwindow,text='Answer',width=150,bd=5)
  question_entry = tkinter.Entry(middle_schoolwindow,width=150,bd=5)
  enter_button = tkinter.Button(middle_schoolwindow,width=15,padx=0,text='Enter',bg="light green",command=enter)
  left_text = tkinter.Text(middle_schoolwindow)
  left_text.insert(tkinter.INSERT,'Science Bowl')
  right_text = tkinter.Text(middle_schoolwindow)
  right_text.insert(tkinter.INSERT,'Middle School')
  question_entry.delete(0,tkinter.END)
  question_entry.insert(0,questionss)
  question_entry.config({"background":"antique white"})
  answer_entry.config({"background":"antique white"})



  life_q.grid(row=3,column=0)
  physical_q.grid(row=3,column=1)
  General_q.grid(row=3,column=2)
  earth_q.grid(row=3,column=3)
  math_q.grid(row=3,column=4)
  answer_entry.grid(row=4,columnspan=5,padx=0)
  question_entry.grid(row=2,columnspan=5,padx=0)
  enter_button.grid(row=5,column=2)
  left_text.grid(row=5,column=0)
  left_text.grid(row=5,column=4)

  middle_schoolwindow.mainloop()
  

   

    
 

  


  

   
  

middle_school = tkinter.Button(main_window,text='Middle School Questions',command=middle_school_window)
#high_school = tkinter.Button(main_window,text='High School Questions',command=high_school_window)


#high_school.grid(row=2,column=1)
middle_school.grid(row=2,column=2)
