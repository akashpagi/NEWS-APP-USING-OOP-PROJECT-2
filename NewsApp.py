import io
import requests # module use for api requests
from tkinter import PhotoImage, Button, Frame, Label, Tk # GUI library
from PIL import Image, ImageTk 
from urllib.request import urlopen
import webbrowser


class NewsApp:
    
    def __init__(self) -> None:
        
        # Fetch the data from api and convert into json format
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=7156ae05f8fd4b39b1facf8a03616704').json()
        
        # Intialize the GUI and load
        self.loading_page()
        
        # Load the first news item from api
        self.load_news_item(0)
    
    def loading_page(self):
        self.root = Tk()
        self.root.iconbitmap('./Resources/favicon.ico')
        self.root.geometry('460x680')
        self.root.title('Inshort News Application')
        self.root.resizable(0,0)
        self.root.configure(bg='white')
    
    # clear method used for clear the existing page content
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
    # Loading the news on gui
    def load_news_item(self, index):
        
        # clear the page
        self.clear()
        
        try:
            # Placing image
            news_img_url = self.data['articles'][index]['urlToImage']
            response = urlopen(news_img_url).read()
            
            news_img = Image.open(io.BytesIO(response)).resize((350, 250))
            photo = ImageTk.PhotoImage(news_img)
            Label(self.root, image=photo).pack(pady=8)
        except:
            news_img_url = 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png'
            response = urlopen(news_img_url).read()
            news_img = Image.open(io.BytesIO(response)).resize((350, 250))
            photo = ImageTk.PhotoImage(news_img)
            Label(self.root, image=photo).pack(pady=8)
            
        
       # News heading
        heading = Label(self.root, text=self.data['articles'][index]['title'],bg='white', fg='#001a4d', wraplength=350, justify='center')
        heading.pack(pady=(10,20))
        heading.configure(font=('tahoma', 18 , 'bold'))
        
       # News details
        details = Label(self.root, text=self.data['articles'][index]['description'],bg='white', fg='black', wraplength=450, justify='center')
        details.pack(pady=(5,20))
        details.configure(font=('tahoma', 12, 'bold'))
        
       # Frames for buttons
        frame = Frame(self.root, bg='white')
        frame.pack(expand=True, fill='both')
        
        if index != 0:
            # prev button
            prev_img = PhotoImage(file ='./Resources/left.png') 
            prev = Button(frame, image=prev_img, bd=0, bg='#ffffff', activebackground='#ffffff', command=lambda :self.load_news_item(index - 1))
            prev.grid(row=1,column=1,padx=10,pady=10, ipadx=35)
        
        # Read more button
        read_img = PhotoImage(file='./Resources/ReadMore.png')
        read = Button(frame, image=read_img, bd=0, bg='#ffffff', activebackground='#ffffff', command=lambda: self.open_news_link(self.data['articles'][index]['url']))
        read.grid(row=1, column=2, padx=5, pady=5)
        
        if index != len(self.data['articles']) - 1:
            # Next button
            next_img = PhotoImage(file='./Resources/right.png')
            next_button = Button(frame, image=next_img, bd=0, bg='#ffffff', activebackground='#ffffff', command=lambda :self.load_news_item(index + 1))
            next_button.grid(row=1, column=3, padx=10, pady=10, ipadx=30)
        
        self.root.mainloop()
        
    # Show news after clink on buttons  
    def open_news_link(self, url):
        webbrowser.open(url)
   
news = NewsApp()