## Importing all the neccesary modules.
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import os
from PIL import ImageTk, Image
from pygame import mixer
from tkinter import ttk

from mutagen.mp3 import MP3

import threading
import time
import random
import _thread


#    INITIAL VARIABAL  DECLARATION
mixer.init()

playing = False
paused = False
mute = False
cur_playing = ''
con_style = 'rep_one'
to_break = False
current_time = 0


# Main Class DECLARATION (This class contain all the function required for a Advanced Music Player.)


class Main_class():

    songs = []
    play_thread = None
    # This "About" Function Used to provide short info related to Music Player
    def about(self):
        mb.showinfo('About',"This Music Software is created by Team Technotuners. Its just a Prototype of an online Advanced Music Player in the form of Offline Player." )





    # This "Lyricslist" function helps to provide the lyrics of the required song of your choice which is presented in the Database of the lyrics folder.
    def lyricslist(self):


        root=Tk()

        root.geometry('520x520')
        root.resizable(0, 0)
        root.title('Chords')
        root.wm_attributes('-alpha', 0.95)

        # setting the windows size
        root.geometry("600x400")

        def return_entry(en):
            active.delete("0", END)
            """Gets and prints the content of the entry"""
            content = entry.get()
            try:
                with open("C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/lyrics/{}.txt".format(content.title()),"r") as a:
                    b=a.readlines()
                    for i in b:
                        active.insert(END,"                                                "+i+"")
            except FileNotFoundError :
                active.delete("0", END)
                active.insert(END,"No Result Found or check the spelling")
                active.insert(END, "")
                music_ex = ['txt']
                c="C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/lyrics"
                os.chdir(c)
                dir_files = os.listdir(c)
                list=[]
                for file in dir_files:
                    exten = file.split('.')[-1]

                    if exten ==music_ex[0] :
                        list.append(file)
                active.insert(END,"Total No of Lyrics File in Our Database"+" {}".format(len(list)))
                active.insert(END,"\n")
                for file in dir_files:
                    exten = file.split('.')
                    for ex in music_ex:
                        if exten[-1] == ex:
                            active.insert(END, exten[0])






        Label(root, text="Search Lyrics: ").grid(row=0, sticky=W)

        entry = Entry(root)
        entry.grid(row=0, column=1)
        global active
        active = Listbox(root, height=21, width="400", bg="black", fg="white")
        active.place(x=0, y=50)
        # Connect the entry with the return button
        entry.bind('<Return>', return_entry)


        root.mainloop()
        # This "Start_count" function to count the time of the music side by side of the playing music.
        # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing).
        # Continue - Ignores all of the statements below it. We check if music is paused or not.
    def start_count(self,t):

        global current_time
        while current_time <= t and mixer.music.get_busy():
            global paused
            global dur_start
            global progress_bar
            global total_length
            global con_style
            global to_break

            if paused:
                continue
            elif to_break:
                break
            else:                
                mins, secs = divmod(current_time, 60)
                mins = round(mins)
                secs = round(secs)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                dur_start['text'] = timeformat
                time.sleep(1)
                current_time += 1
                progress_bar['value'] = current_time
                progress_bar.update()
        if to_break:
            to_break = False
            current_time=0
            return None
        else:         
            try:
                self.con_func(con_style)            
            except:
                pass
                
                


    #It provide all the information related to the song which is going to be  played
    def show_details(self,play_song):
        global dur_end
        global progress_bar
        global total_length
        # global th
        file_data = os.path.splitext(play_song)

        if file_data[1] == '.mp3':
            audio = MP3(play_song)
            total_length = audio.info.length


            # with open('temp.jpg', 'wb') as img:
            #     a = ID3(play_song)
            #     img.write(a.getall('APIC')[0].data)
            #     image = self.makeAlbumArtImage('temp.jpg')
            #     self.album_art_label.configure(image=image)
            #     self.album_art_label.image = image


        else:
            a = mixer.Sound(play_song)
            total_length = a.get_length()

        progress_bar['maximum'] = total_length
        # div - total_length/60, mod - total_length % 60
        mins, secs = divmod(total_length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        dur_end['text'] = timeformat


        self.play_thread = _thread.start_new_thread(self.start_count,(total_length,))

        #t1 = threading.Thread(target=self.start_count, args=(total_length,))
        #t1.start()
    # this "Item"function is one of the genre of the hindi songs which load the the "Item song" in the list box
    def Item(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']
        play_list.delete("0", END)

        os.chdir('C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Item')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir('C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Item')
        status_bar['text'] = 'Playlist Updated.'

        self.songs = []

        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # this "Classic"function is one of the genre of the hindi songs which load the the "Classic song" in the list box
    def Classic(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']
        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Item')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Classic')
        status_bar['text'] = 'Playlist Updated.'
        self.songs = []
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # this "Regional"function is one of the genre of the hindi songs which load the the "Regional song" in the list box
    def Regional(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']

        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Item')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Item')
        status_bar['text'] = 'Playlist Updated.'
        self.songs = []
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # this "Bhajan"function is one of the genre of the hindi songs which load the the "Bhajan song" in the list box
    def Bhajan(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']

        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Bhajan')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/Hindi/Bhajan')
        status_bar['text'] = 'Playlist Updated.'
        self.songs = []
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # this "Country" function is one of the genre of the English songs which load the the "Country song" in the list box
    def Country(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']

        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Country')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir('C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Country')
        status_bar['text'] = 'Playlist Updated.'
        self.songs = []
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # # this " Rock "function is one of the genre of the English songs which load the the "Rock song" in the list box

    def Rock(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']

        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Rock')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Rock')
        status_bar['text'] = 'Playlist Updated.'
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # this "Pop"function is one of the genre of the English songs which load the the "Pop song" in the list box
    def Pop(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']
        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Pop')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Pop')
        status_bar['text'] = 'Playlist Updated.'
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)

    # this "Metal"function is one of the genre of the English songs which load the the "Metal song" in the list box
    def Metal(self):
        global songs
        music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']
        os.chdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Metal')
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(
            'C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/Genre/English/Metal')
        status_bar['text'] = 'Playlist Updated.'
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END, file)
                    self.songs.append(file)



    ## Add songs folder  to the playlist list box.
    def set_playlist(self):
        global songs
        music_ex = ['mp3','wav','mpeg','m4a','wma','ogg']

        dir_ =  filedialog.askdirectory(initialdir='D:\\',title='Select Directory')
        os.chdir(dir_)
        status_bar['text'] = 'Playlist Updated.'
        dir_files = os.listdir(dir_)
        self.songs = []
        play_list.delete("0", END)
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END,file)
                    self.songs.append(file)
    # provide suggestions from the given Playlist list box
    def suggestions(self):
        global songs
        sample=[]
        suggest.delete("0",END)
        sample= random.sample(self.songs,2)
        for file in sample:
            suggest.insert(END,file)



    # This "Con_func" is a convinent way for the user to choice to 1) play random song or 2) repeat all the song or 3) play next song.
    def con_func(self,con):
        global cur_playing
        global current_time
        current_time=0
        if con == 'rand':
            try:
                in_ = random.randint(0,len(self.songs))
                next_play = self.songs[in_]
                self.play_next(next_play)
            except:
                self.play_music()
        elif con == 'rep_all':
            try:
                in_ = self.songs.index(cur_playing)
                next_play = self.songs[in_+1]
                self.play_next(next_play)
            except:
                self.play_music()
        else:
            self.play_next(cur_playing)
                    

    # After the user Select the choice in the con_func then this function Help to to play next song
    def play_next(self,song):
        global playing
        global cur_playing
        global file
        file = song
        cur_playing = file
        mixer.music.load(file)
        mixer.music.play()
        status_bar['text'] = 'Playing - '+file
        play_button['image'] = pause_img
        playing = True
        self.show_details(file)

    # this helps to play the song which is select in the list box by double click
    def playSongInitial(self, *args):
        self.stop()
        self.play_music()

    def playsongs(self, *args):
        self.stop()
        self.play_music()
                
    # This is the main function which will load the music file and play the song by using pygame.mixer module
    def play_music(self):
        global playing
        global cur_playing
        try:
            if playing == False:
                global file
                file = play_list.get(ACTIVE)
                cur_playing = file
                mixer.music.load(file)
                mixer.music.play()
                status_bar['text'] = 'Playing - '+file
                play_button['image'] = pause_img
                playing = True
                self.show_details(file)
            else:
                global paused
                if paused == True:
                    mixer.music.unpause()
                    paused = False
                    status_bar['text'] = 'Playing - '+file
                    play_button['image'] = pause_img
                else:
                    mixer.music.pause()
                    paused = True
                    play_button['image'] = play_img
                    status_bar['text'] = 'Music Paused'
        except:
                mb.showerror('error','No file found to play.')
                


    # this "stop" function will stop the music completely and turn the progress bar to null and Time duration  start and  stop
    def stop(self):
        mixer.music.stop()
        global playing
        global paused
        global dur_start
        global progress_bar
        global cur_playing
        global current_time
        global to_break
        to_break = True
        current_time=0
        cur_playing = ''
        playing = False
        paused = False
        dur_start['text'] = '--:--'
        dur_end['text'] = '--:--'
        progress_bar['value'] = 0.0
        progress_bar.update()



        
        play_button['image'] = play_img
        status_bar['text'] = 'Music Stopped'
        to_break = False

        return None
        
        


    # this "next_prev" function helps to play next song or previous song in the listbox
    def next_prev(self,num):
        global file
        global playing
        global to_break
        global dur_start
        to_break = True
        dur_start['text'] = '00:00'
        try:
            if num == 1:
                index = self.songs.index(file) - 1
                file = self.songs[index]
                mixer.music.load(file)
                mixer.music.play()
                status_bar['text'] = 'Playing - '+file
                play_button['image'] = pause_img
                playing = True
                self.show_details(file)
            else:
                index = self.songs.index(file) + 1
                file = self.songs[index]
                mixer.music.load(file)
                mixer.music.play()
                status_bar['text'] = 'Playing - '+file
                play_button['image'] = pause_img
                playing = True
                self.show_details(file)
        except IndexError:
            self.play_music()
        except ValueError:
            global paused
            playing = False
            paused = False
            self.play_music()




    def open_file(self):
        dir_ = filedialog.askopenfilename(initialdir='D:/',title='Select File')
        cng_dir = dir_.split('/')[0:-1]
        cng_dir = ''.join(cng_dir)
        os.chdir(cng_dir)
        self.songs.append(dir_)
        filename = os.path.basename(dir_)
        play_list.insert(END,filename)
        global playing
        playing = False

    # function  to select
    def set_con(self,num):
        global con_style
        if num == 1:
            con_style = 'rand'
        elif num == 2:
            con_style = 'rep_all'
        else:
            con_style = 'rep_one'


    # this function helps to mute the song or unmute the song
    def speaker_func(self):
        global mute
        global status_bar
        if mute == False:
            speaker['image'] = mute_img
            mixer.music.set_volume(0.0)
            mute = True            
        else:
            speaker['image'] = speaker_img
            num = scale.get()
            mixer.music.set_volume(float(num) /100)
            mute = False

    # this function help to increase or decrease the volume the song
    def set_vol(self,num):
        global mute
        global status_bar
        if num == float(0):
            speaker['image'] = mute_img
            mixer.music.set_volume(0.0)
            mute = True
        elif mute == True:
            speaker['image'] = speaker_img
            num = scale.get()
            mixer.music.set_volume(float(num) /100)
            mute = False
        else:
            volume = float(num) / 100
            mixer.music.set_volume(volume)



    # this function helps to close the program
    def exit(self):
        self.stop()
        win.destroy()
        sys.exit()

    #This function helps to Feature You Clicked Will Be Coming Soon.\n Please Wait For An Update. Stay Tuned
    def coming_soon(self):
        mb.showinfo('Coming Soon','The Feature You Clicked Will Be Coming Soon.\n Please Wait For An Update. Stay Tuned')





    


    ## Constructer Method -  Main method For GUI.
    def __init__(self):
        
        # this whole part is the Tkinter part where we connect all the all the above function to the buttion ,label ,menus ext
        ## Making Tkinter Window.
        global win
        win = Tk()
        win.config(bg="black")
        win.geometry('1000x520')
        win.resizable(0,0)
        win.title('Chords')
        win.wm_attributes('-alpha',0.95)
        win.iconbitmap("C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/icon.ico")


        ## Menu bar - all the menu_cascades and menu_commands.
        main_menu = Menu(win,tearoff=0)

        win.configure(menu=main_menu)

        
        file = Menu(main_menu,tearoff=0)
        main_menu.add_cascade(label='Media', menu=file)

        
        file.add_command(label='Open',command=self.open_file)
        file.add_command(label='Open Folder',command=self.set_playlist)
        file.add_command(label='Save Playlist',command=self.coming_soon)
        file.add_command(label='Open Muliple Files',command=self.coming_soon)
        file.add_command(label='Open Disk',command=self.coming_soon)
        file.add_command(label='Open Network Stream',command=self.coming_soon)
        file.add_separator()
        file.add_command(label='Open Recent Media',command=self.coming_soon)
        file.add_command(label='Add Inteface',command=self.coming_soon)
        file.add_command(label='Fullscreen',command=self.coming_soon)
        file.add_separator()
        file.add_command(label='Exit',command=self.exit)

        about = Menu(main_menu,tearoff=0)
        main_menu.add_cascade(label='About',menu=about)

        about.add_command(label='About Us',command=self.about)
        lyrics = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label='Lyrics', menu=lyrics)
        lyrics.add_command(label="lyrics",command=self.lyricslist)




        fileMenu = Menu(main_menu,tearoff=0)




        submenu = Menu(fileMenu,tearoff=0)
        submenu.add_command(label="Item",command=self.Item)
        submenu.add_command(label="Classic",command=self.Classic)
        submenu.add_command(label="Regional",command=self.Regional)
        submenu.add_command(label="Bhajan",command=self.Bhajan)
        fileMenu.add_cascade(label='Hindi Songs', menu=submenu, underline=0)



        submenu1 = Menu(fileMenu, tearoff=0)
        submenu1.add_command(label="Country",command=self.Country)
        submenu1.add_command(label="Rock",command=self.Rock)
        submenu1.add_command(label="Pop",command=self.Pop)
        submenu1.add_command(label="Metal",command=self.Metal)
        fileMenu.add_cascade(label='English Songs', menu=submenu1, underline=0)
        main_menu.add_separator()


        main_menu.add_cascade(label="Genre", underline=0, menu=fileMenu)



        image1 = Image.open("C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/icon.png")
        image1 = image1.resize((450, 350), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)

        label1 =Label(image=test,bg="black")
        label1.image = test

        # Position image
        label1.place(x= 40, y =20)



        #Playlist Frame
        Label(win,text='', bg='#030F26',height=19,width=35,relief_='ridge').place(x=543,y=0)

        Button(win, text='Add a Folder.',bd=2,font=('white',13),width=25,command=self.set_playlist).place(x=552,y=10)

        global play_list
        play_list = Listbox(win,height=21,width=41,bg="#0C1D40",fg="white")
        play_list.place(x=544,y=50)
        play_list.bind('<Double-Button>', self.playSongInitial)




        Label(win, text='', bg='#030F26', height=19, width=35, relief_='ridge').place(x=800, y=0)

        button1 =Button(win, text='Suggestions Songs.', bd=2, font=('white', 13), width=25, command=self.suggestions).place(
            x=810, y=11,height="33",width="185")

        global suggest
        suggest = Listbox(win, height=21, width=32, bg="#0C1D40", fg="white")
        suggest.place(x=800, y=50)



        ## Bottom Control Center
        Label(win, text='',height=5,relief_='groove',bg="black",width=200).place(x=0,y=395)




        global play_img 
        play_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/play.png')

        def on_enter_play(event):
            play_des.place(x=25,y=460)

        def on_leave_play(event):
            play_des.place(x=1000,y=1000)

        global play_button
        play_button = Button(win, image=play_img,bg="black",bd=0,command=self.play_music)
        play_button.place(x=10,y=440)        
        play_button.bind('<Enter>',on_enter_play)
        play_button.bind('<Leave>',on_leave_play)


        def on_enter_prev(event):
            prev_des.place(x=45,y=460)

        def on_leave_prev(event):
            prev_des.place(x=1000,y=1000)
        

        prev_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/rep_one.png')
        prev_button = Button(win, image=prev_img,bd=0,bg="black",command=lambda:self.next_prev(1))
        prev_button.place(x=50,y=433)
        prev_button.bind('<Enter>',on_enter_prev)
        prev_button.bind('<Leave>',on_leave_prev)



        def on_enter_stop(event):
            stop_des.place(x=70,y=460)

        def on_leave_stop(event):
            stop_des.place(x=1000,y=1000)

        stop_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/stop.png')
        stop_button = Button(win,image=stop_img,bd=0,bg="black",command=self.stop)
        stop_button.place(x=85,y=438)
        stop_button.bind('<Enter>',on_enter_stop)
        stop_button.bind('<Leave>',on_leave_stop)


        def on_enter_next(event):
            next_des.place(x=100,y=460)

        def on_leave_next(event):
            next_des.place(x=1000,y=1000)

        next_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/next.png')
        next_button = Button(win, image=next_img,bd=0,bg="black",command=lambda:self.next_prev(2))
        next_button.place(x=113,y=433)
        next_button.bind('<Enter>',on_enter_next)
        next_button.bind('<Leave>',on_leave_next)

        global pause_img
        pause_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/pause.png')


        global speaker_img
        speaker_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/vol.png')

        global mute_img
        mute_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/mute.png')


        def on_enter_vol(event):
            vol_des.place(x=560,y=450)

        def on_leave_vol(event):
            vol_des.place(x=1000,y=1000)

        global speaker
        speaker = Button(win,image=speaker_img,bd=0,bg="black",command=self.speaker_func)
        speaker.place(x=815,y=439)
        speaker.bind('<Enter>',on_enter_vol)
        speaker.bind('<Leave>',on_leave_vol)


        def on_enter_shuffle(event):
            shuffle_des.place(x=180,y=460)

        def on_leave_shuffle(event):
            shuffle_des.place(x=1000,y=1000)

        shuffle_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/shuffle.png')
        shuffle_button = Button(win, image=shuffle_img,bd=0,bg="black",command=lambda:self.set_con(1))
        shuffle_button.place(x=170,y=440)
        shuffle_button.bind('<Enter>',on_enter_shuffle)
        shuffle_button.bind('<Leave>',on_leave_shuffle)

        def on_enter_rep_all(event):
            rep_all_des.place(x=220,y=460)

        def on_leave_rep_all(event):
            rep_all_des.place(x=1000,y=1000)


        repeat_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/repeat.png')
        repeat_button = Button(win, image=repeat_img,bd=0,bg="black",command=lambda:self.set_con(2))
        repeat_button.place(x=200,y=440)
        repeat_button.bind('<Enter>',on_enter_rep_all)
        repeat_button.bind('<Leave>',on_leave_rep_all)


        def on_enter_rep_one(event):
            rep_one_des.place(x=250,y=460)

        def on_leave_rep_one(event):
            rep_one_des.place(x=1000,y=1000)

        rep_one_img = PhotoImage(file='C:/Users/Manish Agarwal/Desktop/pythonProject/Chords Music Player By Team Techntuners/Chords Music Player By Team Techntuners/resources/rep_one.png')
        rep_one_button = Button(win, image=rep_one_img,bd=0,bg="black",command=lambda:self.set_con(3))
        rep_one_button.place(x=230,y=437)
        rep_one_button.bind('<Enter>',on_enter_rep_one)
        rep_one_button.bind('<Leave>',on_leave_rep_one)


        play_des = Label(win, text='Play/Pause',relief='groove')
        prev_des = Label(win, text='Previous Track',relief='groove')
        stop_des = Label(win, text='Stop Music',relief='groove')
        next_des = Label(win, text='Next Track',relief='groove')
        shuffle_des = Label(win, text='Shuffle All',relief='groove')
        rep_all_des = Label(win, text='Repeat All',relief='groove')
        rep_one_des = Label(win, text='Repeat One',relief='groove')
        vol_des = Label(win, text='Adjust Volume',relief='groove')


        ## Volume Scale - adjust volume
        global scale

        scale = ttk.Scale(win, from_=0, to=100,length="112", orient=HORIZONTAL,command=self.set_vol)
        scale.set(70)  # implement the default value of scale when music player starts
        mixer.music.set_volume(0.7)
        scale.place(x=850,y=440)

        ## Time Durations
        global dur_start, dur_end
        dur_start = Label(win, text='--:--',font=('Calibri',10,'bold',),bg="black",fg="white")
        dur_start.place(x=5,y=400)
        dur_end = Label(win, text='--:--',font=('Calibri',10,'bold'),bg="black",fg="white")
        dur_end.place(x=962,y=400)


        ## Progress Bar - The progress bar which indicates the running music
        global progress_bar
        style = ttk.Style()
        style.theme_use('default')
        style.configure("grey.Horizontal.TProgressbar", background='navy blue')
        progress_bar = ttk.Progressbar(win, orient='horizontal',length=920,style='grey.Horizontal.TProgressbar')
        progress_bar.place(x=42,y=400)


        ## Status Bar - at the bottom of window
        global status_bar
        status_bar = Label(win,text='------------------------------------------------------Welcome to Chords------------------------------------ Created by Team Technotuners-----------------------------------------------------------------------',fg="white",bg="black",relief_='sunken',anchor=W)
        status_bar.pack(side=BOTTOM,fill=X)


        win.protocol("WM_DELETE_WINDOW", self.exit)
        win.mainloop()






music_player = Main_class()

