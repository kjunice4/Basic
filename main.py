#Free Calculator App

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '15sp'
            background_color: 0, 0 , 0 , 1
            height: 100
            size_hint_y: None
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"        

        Button:
            font_size: '15sp'
            background_color: 0, 0 , 0 , 1
            height: 100
            size_hint_y: None
            text: "KSquared-Mathematics : Basic Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "Basic Calculator"   
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Basic"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                text: "Visit KSquared-Mathematics"
                background_color: 0, 1, 1, 1
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
                    
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            acing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Free Basic Calculator v0.1"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

#Basic
Builder.load_string("""
<Basic>
    id:Basic
    name:"Basic"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Basic Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                acing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Base_entry.text = ""
                        list_of_steps.clear_widgets()       
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: Base_entry
                    text: Base_entry.text
                    hint_text: "Entry:"
                    multiline: False
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    promo.clear_widgets()
                    list_of_steps.clear_widgets() 
                    Basic.steps(Base_entry.text)    
            
            GridLayout:
                id: promo
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   
            
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                text: "Visit KSquared-Mathematics"
                background_color: 0, 1, 1, 1
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')        
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Basic(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Basic, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            self.ids.promo.add_widget(Label(text= "Click on the link below to" ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.promo.add_widget(Label(text= "subscribe to more KSquared-Math apps!" ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + entry, font_size = '15sp', size_hint_y= None, height=100))
            
            Answer = str(eval(str(entry).replace("^","**")))
            Answer = "{:,}".format(float(Answer.replace(",","")))
            print("Answer",Answer)
            
            self.ids.list_of_steps.add_widget(Label(text="Answer: " + '[color=33CAFF]' + Answer + '[/color]', markup=True, font_size = '15sp', size_hint_y= None, height=100))
        
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Basic Calculator cannot compute" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(Basic(name="Basic"))     
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   

class Basic(App):
    def __init__(self, **kwargs):
        super(Basic, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Basic().run()
    

