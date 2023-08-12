import requests # module use for api requests
from tkinter import PhotoImage, Button, Frame, Label, Tk # GUI library

class NewsApp:
    
    def __init__(self) -> None:
        
        # Fetch the data from api and convert into json format
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=7156ae05f8fd4b39b1facf8a03616704').json()
        
        # Intialize the GUI and load
        self.loading_page()
        
        # Load the first news item from api
        self.load_news_item(5)
    
    def loading_page(self):
        self.root = Tk()
        self.root.geometry('450x600')
        self.root.title('Inshort News Application')
        self.root.resizable(0,0)
        self.root.configure(bg='white')
    
    # clear method used for clear the existing page content
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
    def load_news_item(self, index):
        
        # clear the page
        self.clear()
        
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='white', fg='black', wraplength=350, justify='center')
        heading.pack(pady=(10,20))
        heading.configure(font=('tahoma', 18 , 'bold'))
        
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='white', fg='black', wraplength=450, justify='center')
        details.pack(pady=(5,20))
        details.configure(font=('tahoma', 12, 'bold'))
        
        frame = Frame(self.root, bg='white')
        frame.pack(expand=True, fill='both')
        
        prev_img = PhotoImage(file ='./Resources/left.png') 
        prev = Button(frame, image=prev_img, bd=0, bg='#ffffff',activebackground='#ffffff')
        prev.grid(row=1,column=1,padx=10,pady=10, ipadx=35)
        
        read_img = PhotoImage(file ='./Resources/ReadMore.png') 
        read = Button(frame, image=read_img, bd=0, bg='#ffffff',activebackground='#ffffff')
        read.grid(row=1,column=2,padx=5,pady=5)       
        
        next_img = PhotoImage(file ='./Resources/right.png') 
        next = Button(frame, image=next_img, bd=0, bg='#ffffff',activebackground='#ffffff')
        next.grid(row=1,column=3,padx=10,pady=10, ipadx=30)
        
        self.root.mainloop()
        
news = NewsApp()