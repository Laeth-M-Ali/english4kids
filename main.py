import kivy 
import datetime
import os 
from functools import partial
from kivy.app import App 
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button,Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
class ScrollTest(ScrollView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
        Window.bind(on_maximize=self.testing)
        self.size_hint = (1,None)
        self.pos_hint = {'center_x':0.5,'top': 1}
        self.size = (Window.width,Window.height)

        self.inside = GridLayout()
        self.inside.cols = 1
        self.inside.size_hint_y= None
        self.inside.spacing = 0
        self.inside.background_color='red'
        self.inside.bind(minimum_height=self.inside.setter('height'))#checks when window maximized     
        self.add_widget(self.inside)     
        self.submit2 = Button(text='',background_normal="image/logo.jpeg",size_hint_y=None, height=400)
        self.inside.add_widget(self.submit2)             
    def testing(self,instance):
        self.size= (Window.width,Window.height)

#main gui
class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.main_page = ScrollTest()
        with self.main_page.inside.canvas.before:
            Color(0, 1, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),
            pos=self.main_page.inside.pos)
        screen = Screen(name= 'Login')
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)
        self.submit3 = Button(text='Alphabet',size_hint_y=None, height=150,color='white',font_size=70,background_color='pink')
        self.submit3.bind(on_press=self.onclick)
        self.main_page.inside.add_widget(self.submit3)
        self.submit4 = Button(text='foods',size_hint_y=None, height=150,color='yellow',font_size=70,background_color='pink')
        self.submit4.bind(on_press=self.onclick2)
        self.main_page.inside.add_widget(self.submit4)
        self.submit5 = Button(text='drinks',size_hint_y=None, height=150,color='green',font_size=70,background_color='pink')
        self.submit5.bind(on_press=self.onclick3)
        self.main_page.inside.add_widget(self.submit5)
        self.submit6= Button(text='feelings',size_hint_y=None, height=150,color='red',font_size=70,background_color='pink')
        self.submit6.bind(on_press=self.onclick6)
        self.main_page.inside.add_widget(self.submit6)
        self.submit7 = Button(text='numbers',size_hint_y=None, height=150,color='orange',font_size=70,background_color='pink')
        self.submit7.bind(on_press=self.onclick5)
        self.main_page.inside.add_widget(self.submit7)
        self.submit12 = Button(text='clothis',size_hint_y=None, height=150,color='white',font_size=70,background_color='pink')
        self.submit12.bind(on_press=self.onclick12)
        self.main_page.inside.add_widget(self.submit12)
        self.submit13= Button(text='shapes',size_hint_y=None, height=150,color='yellow',font_size=70,background_color='pink')
        self.submit13.bind(on_press=self.onclick13)
        self.main_page.inside.add_widget(self.submit13)
        self.submit14= Button(text='budy',size_hint_y=None, height=150,color='green',font_size=70,background_color='pink')
        self.submit14.bind(on_press=self.onclick14)
        self.main_page.inside.add_widget(self.submit14)
        self.submit8= Button(text='family',size_hint_y=None, height=150,color='pink',font_size=70,background_color='pink')
        self.submit8.bind(on_press=self.onclick9)
        self.main_page.inside.add_widget(self.submit8)
        self.submit12= Button(text='flowers',size_hint_y=None, height=150,color='red',font_size=70,background_color='pink')
        self.submit12.bind(on_press=self.onclick15)
        self.main_page.inside.add_widget(self.submit12)
        self.submit9= Button(text='add',size_hint_y=None, height=150,color='gray',font_size=70,background_color='pink')
        self.submit9.bind(on_press=self.onclick10)
        self.main_page.inside.add_widget(self.submit9)
        self.submit16= Button(text='test',size_hint_y=None, height=150,color='white',font_size=70,background_color='pink')
        self.submit16.bind(on_press=self.onclick16)
        self.main_page.inside.add_widget(self.submit16)   
        self.submit11= Button(text='exit',size_hint_y=None, height=150,color='red',font_size=70,background_color='pink')
        self.submit11.bind(on_press=self.onclick8)
        self.main_page.inside.add_widget(self.submit11)
        return self.screen_manager
    def onclick(self,instance):
        Grid_LayoutApp().run()
    def onclick2(self,event):
        root=foodList()
        root.run()
    def onclick3(self,event):
        root=drink()
        root.run()
    def onclick6(self,event):
       # self.stop()
        root=feeling()
        root.run()
    
    def onclick5(self,event):
     #   self.stop()
        root=numbers()
        root.run()
    
    def onclick8(self,event):
        self.stop()
    def onclick9(self,event):
     #   self.stop()
        root=family()
        root.run()
    def onclick10(self,event):
      # self.stop()
        root=add()
        root.run() 
    def onclick12(self,event):
      #  self.stop()
        root=clothis()
        root.run()
    def onclick13(self,event):
     #   self.stop()
        root=shapes()
        root.run()
    def onclick14(self,event):
  #      self.stop()
        root=budy()
        root.run()
    def onclick15(self,event):
     #   self.stop()
        root=flowers()
        root.run()
    def onclick16(self,event):
    #    self.stop()
        root=test()
        root.run()

class test(App):
    txt = ''
    
    def build(self):
        layout = GridLayout(cols = 1)
        
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=50)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=50)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal="image/potato.jpg",height=450) 
        layout.add_widget(btn)
  #      btn.bind(on_press =self.onclick)  
        textinput = TextInput(text='')
        
        layout.add_widget(textinput)
        	
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press = self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        return layout
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='potato':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      	#  self.stop()
      	  root=test2()
      	  root.run()
  
    def onclick4(self,event):
      	  root=MyApp()
      	  root.run()
      	    
class test2(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/cato.jpeg') 
        layout.add_widget(btn)
        textinput = TextInput(text='')

 #       btn.bind(on_press =self.onclick)  
        
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout  
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='cake':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      #	  self.stop()
      	  root=test3()
      	  root.run()
    def onclick4(self,event):
      #	  self.stop()
      	  root=MyApp()
      	  root.run()   	  
class test3(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/one.png') 
        layout.add_widget(btn)
        textinput = TextInput(text='')
 #       btn.bind(on_press =self.onclick)  
        
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='one':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      #	  self.stop()
      	  root=test4()
      	  root.run()
    def onclick4(self,event):
      	#  self.stop()
      	  root=MyApp()
      	  root.run()

class test4(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/Hat.jpeg') 
        layout.add_widget(btn)
        textinput = TextInput(text='')
 #       btn.bind(on_press =self.onclick)  
        
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='hat':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      #	  self.stop()
      	  root=test5()
      	  root.run()
    def onclick4(self,event):
      	#  self.stop()
      	  root=MyApp()
      	  root.run()

class test5(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/apple.jpg') 
        layout.add_widget(btn)
        textinput = TextInput(text='')
 #       btn.bind(on_press =self.onclick)  
        
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='apple':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      	#  self.stop()
      	  root=test6()
      	  root.run()
    def onclick4(self,event):
      	 # self.stop()
      	  root=MyApp()
      	  root.run()


class test6(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/star.jpeg') 
        layout.add_widget(btn)
        textinput = TextInput(text='')
 #       btn.bind(on_press =self.onclick)  
        
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='star':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      #	  self.stop()
      	  root=test7()
      	  root.run()
    def onclick4(self,event):
      	 # self.stop()
      	  root=MyApp()
      	  root.run()

class test7(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/eye.jpeg') 
        layout.add_widget(btn)
        textinput = TextInput(text='')
 #       btn.bind(on_press =self.onclick)  
        
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn3=Button(text ='Next',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout
    def onclick2(self,event):
        txt=textp.text
        if txt=='eye':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    def onclick3(self,event):
      #	  self.stop()
      	  root=test8()
      	  root.run()
    def onclick4(self,event):
      	#  self.stop()
      	  root=MyApp()
      	  root.run()

class test8(App):
    txt = ''
    def build(self):
        layout = GridLayout(cols = 1)
        with layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),pos=layout.pos)
        lb=Label(text=' English 4 kids',color='pink',font_size=70)
        layout.add_widget(lb)
        lb2=Label(text='write what you see',color='blue',font_size=70)
        layout.add_widget(lb2)
        btn=Button(text ='',background_normal='image/tea.jpg') 
        layout.add_widget(btn)
        textinput = TextInput(text='')
 #       btn.bind(on_press =self.onclick)  
        layout.add_widget(textinput)
        btn2=Button(text ='check',color='yellow',font_size=70,background_color='pink') 
        layout.add_widget(btn2)
        btn2.fbind('on_press', self.onclick2,textp=textinput)
        btn4=Button(text ='Home',color='green',font_size=70,background_color='pink') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)     
        return layout
    def onclick2(self,event,textp):
        txt=textp.text
        if txt=='tea':
        	sound=SoundLoader.load('audio/true.wav')
        	sound.play()
        else:
      	  sound=SoundLoader.load('audio/false.wav')
        sound.play()
    
    def onclick4(self,event):
      #	  self.stop()
      	  root=MyApp()
      	  root.run()
#food list

class foodList(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        '''Creation of login screen'''
        self.main_page = ScrollTest()
        with self.main_page.inside.canvas.before:
            Color(0, 1, 0, 1) 
            self.rect = Rectangle(size=(10000,10000),
            pos=self.main_page.inside.pos)
        screen = Screen(name= 'Login')
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)
        self.submit3 = Button(text='Fruits',size_hint_y=None, height=250,color='white',font_size=70,background_color='pink')
        self.submit3.bind(on_press=self.onclick)
        self.main_page.inside.add_widget(self.submit3)
        self.submit4 = Button(text='Vegetables',size_hint_y=None, height=250,color='yellow',font_size=70,background_color='pink')
        self.submit4.bind(on_press=self.onclick2)
        self.main_page.inside.add_widget(self.submit4)
        self.submit5 = Button(text='Desserts',size_hint_y=None, height=250,color='green',font_size=70,background_color='pink')
        self.submit5.bind(on_press=self.onclick3)
        self.main_page.inside.add_widget(self.submit5)
        self.submit6= Button(text='Pastries',size_hint_y=None, height=250,color='red',font_size=70,background_color='pink')
        self.main_page.inside.add_widget(self.submit6)
        self.submit6.bind(on_press=self.onclick6)
        self.submit8= Button(text='back',size_hint_y=None, height=250,color='pink',font_size=70,background_color='pink')
        self.submit8.bind(on_press=self.onclick5)
        self.main_page.inside.add_widget(self.submit8)
        
        return self.screen_manager
    def onclick5(self,event):
     #   self.stop()
        root=MyApp()
        root.run()
    def onclick(self,event):
      #  self.stop()
        root=fruits()
        root.run()
    def onclick2(self,event):
     #   self.stop()
        root=veget()
        root.run()
    def onclick3(self,event):
      #  self.stop()
        root=desserts()
        root.run()
    def onclick6(self,event):
       # self.stop()
        root=Pastries()
        root.run()   
class add(App):
    def build(self):
        layout=GridLayout(cols = 5)
        btn=Button(text='',background_normal='image/1.jpeg')
        layout.add_widget(btn)
        btn.fbind('on_press',self.onclick,txt='one.wav')
        
        btn2=Button(text='',background_normal='image/pl.png')
        layout.add_widget(btn2)
        btn2.fbind('on_press',self.onclick,txt='plus.wav')
        
        btn3=Button(text='',background_normal='image/1.jpeg')
        layout.add_widget(btn3)
        btn3.fbind('on_press',self.onclick,txt='one.wav')
        
        btn4=Button(text='',background_normal='image/eq.png')
        layout.add_widget(btn4)
        btn4.fbind('on_press',self.onclick,txt='equal.wav')  
        
        btn5=Button(text='',background_normal='image/2.png')
        layout.add_widget(btn5)
        btn5.fbind('on_press',self.onclick,txt='two.wav')
        
        btn6=Button(text='',background_normal='image/1.jpeg')
        layout.add_widget(btn6)
        btn6.fbind('on_press',self.onclick,txt='one.wav')
        
        btn7=Button(text='',background_normal='image/pl.png')
        layout.add_widget(btn7)
        btn7.fbind('on_press',self.onclick,txt='plus.wav')
        
        btn8=Button(text='',background_normal='image/2.png')
        layout.add_widget(btn8)
        btn8.fbind('on_press',self.onclick,txt='two.wav')
        
        btn9=Button(text='',background_normal='image/eq.png')
        layout.add_widget(btn9)
        btn9.fbind('on_press',self.onclick,txt='equal.wav')
        btn10=Button(text='',background_normal='image/3.png')
        layout.add_widget(btn10)
        btn10.fbind('on_press',self.onclick,txt='three.wav')  
        btn11=Button(text='',background_normal='image/1.jpeg')
        layout.add_widget(btn11)
        btn11.fbind('on_press',self.onclick,txt='one.wav')
        btn12=Button(text='',background_normal='image/pl.png')
        layout.add_widget(btn12)
        btn12.fbind('on_press',self.onclick,txt='plus.wav')
        btn13=Button(text='',background_normal='image/3.png')
        layout.add_widget(btn13)
        btn13.fbind('on_press',self.onclick,txt='three.wav')
        
        btn14=Button(text='',background_normal='image/eq.png')
        layout.add_widget(btn14)
        btn14.fbind('on_press',self.onclick,txt='equal.wav')
        
        btn15=Button(text='',background_normal='image/4.jpeg')
        layout.add_widget(btn15)
        btn15.fbind('on_press',self.onclick,txt='four.wav')
        
        btn17=Button(text='',background_normal='image/a.jpeg')
        layout.add_widget(btn17)
        
        btn18=Button(text='',background_normal='image/d.jpeg')
        layout.add_widget(btn18)
        
        btn19=Button(text='',background_normal='image/d.jpeg')
        layout.add_widget(btn19)
        
        btn20=Button(text='',background_normal='image/s.png')
        layout.add_widget(btn20)
        
        btn16=Button(text='',background_normal='image/bc.jpg')
        layout.add_widget(btn16)
        btn16.bind(on_press=self.onclick8)    
        return layout
    def onclick(self,event,txt):
        sound=SoundLoader.load('audio/'+txt)
        sound.play()                  
    def onclick8(self,event):
   #     self.stop()
        root=MyApp()
        root.run()    	      

class family(App):
    def build(self):
        layout=GridLayout(cols = 2)
        btn=Button(text='',background_normal='image/mother.jpg')
        layout.add_widget(btn)
        btn.fbind('on_press',self.onclick,txt='mother.wav')
              	        	
        btn2=Button(text='',background_normal='image/father.jpeg')
        layout.add_widget(btn2)
        btn2.fbind('on_press',self.onclick,txt='Ff.wav')
        
        btn3=Button(text='',background_normal='image/sister.jpeg')
        layout.add_widget(btn3)
        btn3.fbind('on_press',self.onclick,txt='sister.wav')
        
        btn4=Button(text='',background_normal='image/brother.jpeg')
        layout.add_widget(btn4)
        btn4.fbind('on_press',self.onclick,txt='brother.wav')
        
        
        btn5=Button(text='',background_normal='image/grand.jpg')
        layout.add_widget(btn5)
        btn5.fbind('on_press',self.onclick,txt='grandparents.wav')
        
        btn6=Button(text='',background_normal='image/bc.jpg')
        layout.add_widget(btn6)
        btn6.bind(on_press=self.onclick6)
        
        return layout      
          	
    def onclick(self,event,txt):    
        sound=SoundLoader.load('audio/'+txt)
        sound.play()        
    def onclick6(self,event):
   #     self.stop()
        root=MyApp()
        root.run()
#fruits gui            	        	                         	      
class fruits(App):
    def build(self):
        layout=GridLayout(cols = 2)
        btn=Button(text='',background_normal='image/apple.jpg')
        layout.add_widget(btn)
        btn.fbind('on_press',self.onclick,txt='apple.wav')
              	        	
        btn2=Button(text='',background_normal='image/banana.jpg')
        layout.add_widget(btn2)
        btn2.fbind('on_press',self.onclick,txt='banana.wav')
        
        btn3=Button(text='',background_normal='image/orange.jpg')
        layout.add_widget(btn3)
        btn3.fbind('on_press',self.onclick,txt='orange.wav')
        
        btn4=Button(text='',background_normal='image/mango.jpg')
        layout.add_widget(btn4)
        btn4.fbind('on_press',self.onclick,txt='Mango.wav')
        
        
        btn5=Button(text='',background_normal='image/wmelon.jpg')
        layout.add_widget(btn5)
        btn5.fbind('on_press',self.onclick,txt='watermelon.wav')
        btn7=Button(text='',background_normal='image/enab.jpg')
        layout.add_widget(btn7)
        btn7.fbind('on_press',self.onclick,txt='Grape.wav')
        btn8=Button(text='',background_normal='image/teen.jpg')
        layout.add_widget(btn8)
        btn8.fbind('on_press',self.onclick,txt='Figs.wav')
        btn9=Button(text='',background_normal='image/straw.jpg')
        layout.add_widget(btn9)
        btn9.fbind('on_press',self.onclick,txt='Strawberry.wav')
        btn10=Button(text='',background_normal='image/chers.jpg')
        layout.add_widget(btn10)
        btn10.fbind('on_press',self.onclick,txt='Cherry.wav')
        btn6=Button(text='',background_normal='image/bc.jpg')
        layout.add_widget(btn6)
        btn6.bind(on_press=self.onclick6)
        
        
        return layout                 
	
    def onclick(self,event,txt):    
        sound=SoundLoader.load('audio/'+txt)
        sound.play()                                 
    def onclick6(self,event):
        #self.stop()
        root=foodList()
        root.run()        
#vegetabels gui
class veget(App):
    def build(self):
        layout=GridLayout(cols = 2)
        btn=Button(text='',background_normal='image/tomato.jpg')
        layout.add_widget(btn)
        btn.fbind('on_press',self.onclick,txt='tomat.wav')
              	        	
        btn2=Button(text='',background_normal='image/potato.jpg')
        layout.add_widget(btn2)
        btn2.fbind('on_press',self.onclick,txt='potat.wav')
        
        btn3=Button(text='',background_normal='image/fool.jpg')
        layout.add_widget(btn3)
        btn3.fbind('on_press',self.onclick,txt='Bean.wav')
        
        btn4=Button(text='',background_normal='image/flef.jpg')
        layout.add_widget(btn4)
        btn4.fbind('on_press',self.onclick,txt='pepper.wav')
        
        btn5=Button(text='',background_normal='image/Khiar.jpg')
        layout.add_widget(btn5)
        btn5.fbind('on_press',self.onclick,txt='cucumber.wav')
        btn7=Button(text='',background_normal='image/bazl.jpg')
        layout.add_widget(btn7)
        btn7.fbind(on_press=self.onclick,txt='peas.wav')
        btn8=Button(text='',background_normal='image/batn.jpg')
        layout.add_widget(btn8)
        btn8.fbind('on_press',self.onclick,txt='Eggplant.wav')
        btn9=Button(text='',background_normal='image/kosa.jpg')
        layout.add_widget(btn9)
        btn9.fbind('on_press',self.onclick,txt='Zucchini.wav')
        btn10=Button(text='',background_normal='image/khs.jpg')
        layout.add_widget(btn10)
        btn10.fbind('on_press',self.onclick,txt='lettuce.wav')
        btn6=Button(text='',background_normal='image/bc.jpg')
        layout.add_widget(btn6)
        btn6.bind(on_press=self.onclick6)
        
        
        return layout                	 

    def onclick(self,event,txt):    
        sound=SoundLoader.load('audio/'+txt)
        sound.play()                                   
    def onclick6(self,event):
   #     self.stop()
        root=foodList()
        root.run()            	        	                     

#desserts gui

class desserts(App):
    def build(self):
        layout=GridLayout(cols = 2)
        btn=Button(text='',background_normal='image/baclava.jpeg')
        layout.add_widget(btn)
        btn.fbind('on_press',self.onclick,txt='baklava.wav')
              	        	
        btn2=Button(text='',background_normal='image/Betty Four.jpeg')
        layout.add_widget(btn2)
        btn2.fbind('on_press',self.onclick,txt='Betty Four.wav')
        
        btn3=Button(text='',background_normal='image/candies.jpeg')
        layout.add_widget(btn3)
        btn3.fbind('on_press',self.onclick,txt='candies.wav')
        
        btn4=Button(text='',background_normal='image/cato.jpeg')
        layout.add_widget(btn4)
        btn4.fbind('on_press',self.onclick,txt='cake.wav')
        
        
        btn5=Button(text='',background_normal='image/cheescake.jpeg')
        layout.add_widget(btn5)
        btn5.fbind('on_press',self.onclick,txt='cheese cake.wav')
        btn7=Button(text='',background_normal='image/ice_cream.jpg')
        layout.add_widget(btn7)
        btn7.fbind('on_press',self.onclick,txt='ice.wav')
        btn8=Button(text='',background_normal='image/jeleh.jpeg')
        layout.add_widget(btn8)
        btn8.fbind('on_press',self.onclick,txt='jelly.wav')
        btn6=Button(text='',background_normal='image/bc.jpg')
        layout.add_widget(btn6)
        btn6.bind(on_press=self.onclick6)
        return layout                	 
    def onclick(self,event,txt):    
        sound=SoundLoader.load('audio/'+txt)
        sound.play()        
    def onclick6(self,event):
    #    self.stop()
        root=foodList()
        root.run()
#معجنات
class Pastries(App):
    def build(self):
        layout=GridLayout(cols = 2)
        btn=Button(text='',background_normal='image/bread.jpeg')
        layout.add_widget(btn)
        btn.bind(on_press=self.onclick)
              	        	
        btn2=Button(text='',background_normal='image/crowasan.jpeg')
        layout.add_widget(btn2)
        btn2.bind(on_press=self.onclick2)
        
        btn3=Button(text='',background_normal='image/fater.jpeg')
        layout.add_widget(btn3)
        btn3.bind(on_press=self.onclick3)
        
        btn4=Button(text='',background_normal='image/fatermk.jpeg')
        layout.add_widget(btn4)
        btn4.bind(on_press=self.onclick4)
        btn5=Button(text='',background_normal='image/pizza.jpg')
        layout.add_widget(btn5)
        btn5.bind(on_press=self.onclick5)
        btn7=Button(text='',background_normal='image/sammon.jpeg')
        layout.add_widget(btn7)
        btn7.bind(on_press=self.onclick7)
        btn8=Button(text='',background_normal='image/towst.jpeg')
        layout.add_widget(btn8)
        btn8.bind(on_press=self.onclick8)
        btn6=Button(text='',background_normal='image/bc.jpg')
        layout.add_widget(btn6)
        btn6.bind(on_press=self.onclick6)
        return layout               
    def onclick(self,event):    
        sound=SoundLoader.load('audio/Bread.wav')
        sound.play()        
    def onclick2(self,event):    
        sound=SoundLoader.load('audio/croissants.wav')
        sound.play()
    def onclick3(self,event):
        sound=SoundLoader.load('audio/pastry.wav')
        sound.play()
    def onclick4(self,event):
        sound=SoundLoader.load('audio/fried dumplings.wav')
        sound.play()
    def onclick5(self,event):
        sound=SoundLoader.load('audio/pizza.wav')
        sound.play()  
    def onclick7(self,event):
        sound=SoundLoader.load('audio/Samoon.wav')
        sound.play()  
    def onclick8(self,event):
        sound=SoundLoader.load('audio/toast.wav')
        sound.play()    
    def onclick6(self,event):
      #  self.stop()
        root=foodList()
        root.run()


class feeling(App):
    
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/shy.jpg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal='image/happy.jpg') 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal='image/sad.jpg') 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal='image/angry.jpg') 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick5)
        
        
        btn5=Button(text ='',background_normal='image/fel.jpg') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick6)
        
        btn6=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick7)
       
        return layout 

    def onclick(self,event):
        sound = SoundLoader.load('audio/shy.wav')
        sound.play()
     
        
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/happy.wav')
        sound.play()
        
    def onclick3(self,event):
        sound = SoundLoader.load('audio/sad.wav')
        sound.play()
        
    
    def onclick5(self,event):
        sound = SoundLoader.load('audio/angry.wav')
        sound.play()
        
    def onclick6(self,event):
        sound = SoundLoader.load('audio/fraid.wav')
        sound.play()
    def onclick7(self,event):
     #     self.stop()
          root=MyApp()
          root.run()
          
          	
class flowers(App):
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/images (13).jpeg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal="image/images (14).jpeg") 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal="image/download (15).jpeg") 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal="image/Qr.jpeg") 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        
        btn5=Button(text ='',background_normal='image/download (17).jpeg') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick5)
        
        btn6=Button(text ='',background_normal='image/download (18).jpeg') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick6)
        btn7=Button(text ='',background_normal='image/download (19).jpeg') 
        layout.add_widget(btn7)
        btn7.bind(on_press =self.onclick7)
        btn9=Button(text ='',background_normal='image/download (20).jpeg') 
        layout.add_widget(btn9)
        btn9.bind(on_press =self.onclick9)
        btn10=Button(text ='',background_normal='image/download (21).jpeg') 
        layout.add_widget(btn10)
        btn10.bind(on_press =self.onclick10) 
        btn8=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn8)
        btn8.bind(on_press =self.onclick8)    
        
        
             

        return layout 

    def onclick(self,event):
        sound = SoundLoader.load('audio/rose.wav')
        sound.play()
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/Iris flower.wav')
        sound.play()
    def onclick3(self,event):
        sound = SoundLoader.load('audio/jasmin.wav')
        sound.play()
    def onclick4(self,event):
        sound = SoundLoader.load('audio/carnation flower.wav')
        sound.play()
    def onclick5(self,event):
        sound = SoundLoader.load('audio/tulip flower.wav')
        sound.play()
    def onclick6(self,event):
        sound = SoundLoader.load('audio/chrysanthemum flower.wav')
        sound.play()
    def onclick7(self,event):
        sound = SoundLoader.load('audio/Narcissus flower.wav')
        sound.play()
    def onclick9(self,event):
        sound = SoundLoader.load('audio/Lily Flower.wav')
        sound.play()
    def onclick10(self,event):
        sound = SoundLoader.load('audio/The gardenia flower.wav')
        sound.play()
    def onclick8(self,event):
   #     self.stop()
        root=MyApp()
        root.run()

#ملابس 
class clothis (App):
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/bant.jpeg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal="image/blouse.jpeg") 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal="image/dress.jpeg") 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal="image/glass.jpeg") 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        
        btn5=Button(text ='',background_normal='image/Hat.jpeg') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick5)
        
        btn6=Button(text ='',background_normal='image/qmes.jpeg') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick6)
        btn7=Button(text ='',background_normal='image/Scarf.jpeg') 
        layout.add_widget(btn7)
        btn7.bind(on_press =self.onclick7)
        btn9=Button(text ='',background_normal='image/shoes.jpeg') 
        layout.add_widget(btn9)
        btn9.bind(on_press =self.onclick9)
        btn10=Button(text ='',background_normal='image/short.jpeg') 
        layout.add_widget(btn10)
        btn10.bind(on_press =self.onclick10) 
        btn8=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn8)
        btn8.bind(on_press =self.onclick8)    
        
        
             

        return layout 

    def onclick(self,event):
        sound = SoundLoader.load('audio/pants.wav')
        sound.play()
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/blouse.wav')
        sound.play()
    def onclick3(self,event):
        sound = SoundLoader.load('audio/dress.wav')
        sound.play()
    def onclick4(self,event):
        sound = SoundLoader.load('audio/Eyeglasses.wav')
        sound.play()
    def onclick5(self,event):
        sound = SoundLoader.load('audio/hat.wav')
        sound.play()
    def onclick6(self,event):
        sound = SoundLoader.load('audio/shirt.wav')
        sound.play()
    def onclick7(self,event):
        sound = SoundLoader.load('audio/scarf.wav')
        sound.play()
    def onclick9(self,event):
        sound = SoundLoader.load('audio/shoes.wav')
        sound.play()
    def onclick10(self,event):
        sound = SoundLoader.load('audio/short.wav')
        sound.play()
    def onclick8(self,event):
  #      self.stop()
        root=MyApp()
        root.run()
#اشكال هندسة

class shapes(App):
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/haram.jpeg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal="image/star.jpeg") 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal="image/ball.jpeg") 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal="image/square.png") 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        
        btn5=Button(text ='',background_normal='image/rect.png') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick5)
        
        btn6=Button(text ='',background_normal='image/circle.png') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick6)
        btn7=Button(text ='',background_normal='image/triangle.png') 
        layout.add_widget(btn7)
        btn7.bind(on_press =self.onclick7)
        btn9=Button(text ='',background_normal='image/cube.png') 
        layout.add_widget(btn9)
        btn9.bind(on_press =self.onclick9)
        btn10=Button(text ='',background_normal='image/line.png') 
        layout.add_widget(btn10)
        btn10.bind(on_press =self.onclick10) 
        btn8=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn8)
        btn8.bind(on_press =self.onclick8)    
        
        
             

        return layout 
 

    def onclick(self,event):
        sound = SoundLoader.load('audio/pyramid.wav')
        sound.play()
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/star.wav')
        sound.play()
    def onclick3(self,event):
        sound = SoundLoader.load('audio/ball.wav')
        sound.play()
    def onclick4(self,event):
        sound = SoundLoader.load('audio/sqaure.wav')
        sound.play()
    def onclick5(self,event):
        sound = SoundLoader.load('audio/rectangle.wav')
        sound.play()
    def onclick6(self,event):
        sound = SoundLoader.load('audio/circle.wav')
        sound.play()
    def onclick7(self,event):
        sound = SoundLoader.load('audio/Triangle.wav')
        sound.play()
    def onclick9(self,event):
        sound = SoundLoader.load('audio/cube.wav')
        sound.play()
    def onclick10(self,event):
        sound = SoundLoader.load('audio/line.wav')
        sound.play()
    def onclick8(self,event):
   #     self.stop()
        root=MyApp()
        root.run()
#اعضاء الجسم
class budy(App):
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/fam.jpeg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal="image/eye.jpeg") 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal="image/ear.jpeg") 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal="image/face.jpeg") 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        
        btn5=Button(text ='',background_normal='image/foot.jpeg') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick5)
        
        btn6=Button(text ='',background_normal='image/yad.png') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick6)
        btn7=Button(text ='',background_normal='image/zira.png') 
        layout.add_widget(btn7)
        btn7.bind(on_press =self.onclick7)
        btn9=Button(text ='',background_normal='image/fingers.jpeg') 
        layout.add_widget(btn9)
        btn9.bind(on_press =self.onclick9)
        btn10=Button(text ='',background_normal='image/noise.jpeg') 
        layout.add_widget(btn10)
        btn10.bind(on_press =self.onclick10) 
        btn8=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn8)
        btn8.bind(on_press =self.onclick8)    
        
        
             

        return layout 

    def onclick(self,event):
        sound = SoundLoader.load('audio/Mouth.wav')
        sound.play()
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/eye.wav')
        sound.play()
    def onclick3(self,event):
        sound = SoundLoader.load('audio/ear.wav')
        sound.play()
    def onclick4(self,event):
        sound = SoundLoader.load('audio/face.wav')
        sound.play()
    def onclick5(self,event):
        sound = SoundLoader.load('audio/foot.wav')
        sound.play()
    def onclick6(self,event):
        sound = SoundLoader.load('audio/hand.wav')
        sound.play()
    def onclick7(self,event):
        sound = SoundLoader.load('audio/arm.wav')
        sound.play()
    def onclick9(self,event):
        sound = SoundLoader.load('audio/fingers.wav')
        sound.play()
    def onclick10(self,event):
        sound = SoundLoader.load('audio/noise.wav')
        sound.play()
    def onclick8(self,event):
        #self.stop()
        root=MyApp()
        root.run()

        
class drink(App): 
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/tea.jpg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal="image/cofee.jpg") 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal="image/milk.jpg") 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal="image/water.jpg") 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        
        btn5=Button(text ='',background_normal='image/orangej.jpg') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick5)
        
        btn6=Button(text ='',background_normal='image/Soda.jpg') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick6)
        btn7=Button(text ='',background_normal='image/greentea.jpeg') 
        layout.add_widget(btn7)
        btn7.bind(on_press =self.onclick7)  
        btn8=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn8)
        btn8.bind(on_press =self.onclick8)    
        
        
             

        return layout 

    def onclick(self,event):
        sound = SoundLoader.load('audio/tea.wav')
        sound.play()
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/coffee.wav')
        sound.play()
    def onclick3(self,event):
        sound = SoundLoader.load('audio/milk.wav')
        sound.play()
    def onclick4(self,event):
        sound = SoundLoader.load('audio/water.wav')
        sound.play()
    def onclick5(self,event):
        sound = SoundLoader.load('audio/orange juice.wav')
        sound.play()
    def onclick6(self,event):
        sound = SoundLoader.load('audio/soda.wav')
        sound.play()
    def onclick7(self,event):
        sound = SoundLoader.load('audio/green tea.wav')
        sound.play()
    def onclick8(self,event):
   #     self.stop()
        root=MyApp()
        root.run()
class numbers(App):
    def build(self):
        layout = GridLayout(cols = 2)
        btn=Button(text ='',background_normal='image/zero.jpg') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)  
        btn2=Button(text ='',background_normal="image/one.png") 
        layout.add_widget(btn2)
        btn2.bind(on_press =self.onclick2)
        btn3=Button(text ='',background_normal="image/two.png") 
        layout.add_widget(btn3)
        btn3.bind(on_press =self.onclick3)   
        
        btn4=Button(text ='',background_normal="image/three.jpg") 
        layout.add_widget(btn4)
        btn4.bind(on_press =self.onclick4)  
        
        btn5=Button(text ='',background_normal='image/four.jpg') 
        layout.add_widget(btn5)
        btn5.bind(on_press =self.onclick5)
        
        btn6=Button(text ='',background_normal='image/five.jpg') 
        layout.add_widget(btn6)
        btn6.bind(on_press =self.onclick6)
        
        btn7=Button(text ='',background_normal='image/six.png') 
        layout.add_widget(btn7)
        btn7.bind(on_press =self.onclick7)  
        
        btn8=Button(text ='',background_normal='image/seven.png') 
        layout.add_widget(btn8)
        btn8.bind(on_press =self.onclick8)
        
        btn9=Button(text ='',background_normal='image/eight.jpg') 
        layout.add_widget(btn9)
        btn9.bind(on_press =self.onclick9)
        
        btn10=Button(text ='',background_normal='image/nine.jpg') 
        layout.add_widget(btn10)
        btn10.bind(on_press =self.onclick10)
        
        btn11=Button(text ='',background_normal='image/ten.jpg') 
        layout.add_widget(btn11)
        btn11.bind(on_press =self.onclick11)
        
        btn11=Button(text ='',background_normal='image/bc.jpg') 
        layout.add_widget(btn11)
        btn11.bind(on_press =self.onclick12)
        
        
             

        return layout 

    def onclick(self,event):
        sound = SoundLoader.load('audio/zero.wav')
        sound.play()
        
    def onclick2(self,event):
        sound = SoundLoader.load('audio/one.wav')
        sound.play()
    def onclick3(self,event):
        sound = SoundLoader.load('audio/two.wav')
        sound.play()
    def onclick4(self,event):
        sound = SoundLoader.load('audio/three.wav')
        sound.play()
    def onclick5(self,event):
        sound = SoundLoader.load('audio/four.wav')
        sound.play()
    def onclick6(self,event):
        sound = SoundLoader.load('audio/five.wav')
        sound.play()
    def onclick7(self,event):
        sound = SoundLoader.load('audio/six.wav')
        sound.play()
    def onclick8(self,event):
        sound = SoundLoader.load('audio/seven.wav')
        sound.play()
    def onclick9(self,event):
        sound = SoundLoader.load('audio/eight.wav')
        sound.play()
    def onclick10(self,event):
        sound = SoundLoader.load('audio/nine.wav')
        sound.play()
    def onclick11(self,event):
        sound = SoundLoader.load('audio/ten.wav')
        sound.play()
    def onclick12(self,event):
     #   self.stop()
        root=MyApp()
        root.run()
class Grid_LayoutApp(App):
    def build(self):
        layout = GridLayout(cols = 3)
        btn=Button(text =''
        , background_normal = 'image/A.jpg') 
        layout.add_widget(btn)
        btn.fbind('on_press' ,self.onclick,txt='A.wav')  
        btn2=Button(text =''
        , background_normal = 'image/B.jpg') 
        layout.add_widget(btn2)
        btn2.fbind('on_press',self.onclick,txt='B.wav')
        btn3=Button(text =''
        , background_normal = 'image/C.jpg') 
        layout.add_widget(btn3)
        btn3.fbind('on_press',self.onclick,txt='C.wav')   
        
        btn4=Button(text =''
        , background_normal = 'image/D.jpg') 
        layout.add_widget(btn4)
        btn4.fbind('on_press',self.onclick,txt='D.wav')  
        
        btn5=Button(text =''
        , background_normal = 'image/E.jpg') 
        layout.add_widget(btn5)
        btn5.fbind('on_press',self.onclick,txt='E.wav')
        
        btn6=Button(text =''
        , background_normal = 'image/F.jpg') 
        layout.add_widget(btn6)
        btn6.fbind('on_press',self.onclick,txt='F.wav')  
        
        btn7=Button(text =''
        , background_normal = 'Image/G.jpg') 
        layout.add_widget(btn7)
        btn7.fbind('on_press',self.onclick,txt='G.wav')  
        
        btn8=Button(text =''
        , background_normal = 'image/H.jpg') 
        layout.add_widget(btn8)
        btn8.fbind('on_press',self.onclick,txt='H.wav')  
        
        btn9=Button(text =''
        , background_normal = 'image/I.jpg') 
        layout.add_widget(btn9)
        btn9.fbind('on_press',self.onclick,txt='I.wav')  
        
        btn10=Button(text =''
        , background_normal = 'image/J.jpg') 
        layout.add_widget(btn10)
        btn10.fbind('on_press',self.onclick,txt='J.wav') 
        
        btn11=Button(text =''
        , background_normal = 'image/K.jpg') 
        layout.add_widget(btn11)
        btn11.fbind('on_press',self.onclick,txt='K.wav')  
        
        btn12=Button(text =''
        , background_normal = 'image/L.png') 
        layout.add_widget(btn12)
        btn12.fbind('on_press',self.onclick,txt='L.wav')
        
        btn13=Button(text =''
        , background_normal = 'image/M.jpg') 
        layout.add_widget(btn13)
        btn13.fbind('on_press',self.onclick,txt='M.wav')   
        
        btn14=Button(text =''
        , background_normal = 'image/N.jpg') 
        layout.add_widget(btn14)
        btn14.fbind('on_press',self.onclick,txt='N.wav')
        
        btn16=Button(text =''
        , background_normal = 'image/O.jpg') 
        layout.add_widget(btn16)
        btn16.fbind('on_press',self.onclick,txt='O.wav')
        
        btn17=Button(text =''
        , background_normal = 'image/P.jpg') 
        layout.add_widget(btn17)
        btn17.fbind('on_press',self.onclick,txt='P.wav')
        
        btn18=Button(text =''
        , background_normal = 'image/Q.jpg') 
        layout.add_widget(btn18)
        btn18.fbind('on_press',self.onclick,txt='Q.wav')
        
        btn19=Button(text =''
        , background_normal = 'image/R.jpg') 
        layout.add_widget(btn19)
        btn19.fbind('on_press',self.onclick,txt='R.wav')
        
        btn20=Button(text =''
        , background_normal = 'image/S.jpg') 
        layout.add_widget(btn20)
        btn20.fbind('on_press',self.onclick,txt='S.wav')  
        
        btn21=Button(text =''
        , background_normal = 'image/T.jpg') 
        layout.add_widget(btn21)
        btn21.fbind('on_press',self.onclick,txt='T.wav') 
        
                 
        btn22=Button(text =''
        , background_normal = 'image/U.jpg') 
        layout.add_widget(btn22)
        btn22.fbind('on_press',self.onclick,txt='U.wav') 
        
        btn23=Button(text =''
        , background_normal = 'image/V.jpg') 
        layout.add_widget(btn23)
        btn23.fbind('on_press',self.onclick,txt='V.wav') 
        
        btn24=Button(text =''
        , background_normal = 'image/W.jpg') 
        layout.add_widget(btn24)
        btn24.fbind('on_press',self.onclick,txt='W.wav') 
        
        btn25=Button(text =''
        , background_normal = 'image/X.jpg') 
        layout.add_widget(btn25)
        btn25.fbind('on_press',self.onclick,txt='X.wav') 
        
        btn26=Button(text =''
        , background_normal = 'image/Y.jpg') 
        layout.add_widget(btn26)
        btn26.fbind('on_press',self.onclick,txt='Y.wav') 
        
        btn27=Button(text =''
        , background_normal = 'image/Z.jpg') 
        layout.add_widget(btn27)
        btn27.fbind('on_press',self.onclick,txt='Z.wav')
        btn28=Button(text =''
        , background_normal = 'image/bc.jpg') 
        layout.add_widget(btn28)
        btn28.bind(on_press =self.onclick28)
        return layout 
    def onclick(self,event,txt):
        sound = SoundLoader.load('audio/'+txt)
        sound.play()
    def onclick28(self,event):
    #    self.stop()
        root=MyApp()
        root.run()
class late(App):
    def build(self):
        layout = GridLayout(cols = 1)
        lb=Label(text='it is too late\nyou must go sleep now\ncomeback tomorrow\ngood night',font_size=60)
        layout.add_widget(lb)
        btn2=Button(text ='',background_normal='image/sleep.jpg') 
        layout.add_widget(btn2)
        btn=Button(text ='ok') 
        layout.add_widget(btn)
        btn.bind(on_press =self.onclick)
        return layout
    def onclick(self,event):
    	self.close()
if __name__ == "__main__":
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<6:
        root=late()
        root.run()
    else:
        root=MyApp()
        root.run()
