from tkinter import *
import tkinter.ttk as ttk
 
root = Tk()
 
root.geometry('800x600')
root.title('TIC TAC TOE')
root.resizable(False,False)

#-------images---------
homepage_image=PhotoImage(file="images\homepage.png")
tictac_image=PhotoImage(file="images\grid.png")

home_page=Canvas(root,height=600,width=800)
home_page.create_image(0,0,image=homepage_image,anchor=NW)
home_page.place(x=0,y=0)

data={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}

def gamepage():

    global turn
    global counts

    turn=0
    count=0
    data={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}

    game_page=Canvas(root,height=600,width=800,bg="white")
    game_page.create_image(230,150,image=tictac_image,anchor=NW)
    game_page.place(x=0,y=0)
     
    game_page.create_rectangle(99,572,80,550,fill='red')

    Label(root,text="X starts first",font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=330,y=10)
    Label(root,text="PLAYER 1",font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=102,y=548)
    Label(root,text="PLAYER 2",font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=652,y=548)

    

    def chancex():
        game_page.create_rectangle(690,572,630,550,fill='white')
        game_page.create_rectangle(99,572,80,550,fill='red')
    
    def chanceo():
        game_page.create_rectangle(99,572,80,550,fill='white')
        game_page.create_rectangle(690,572,630,550,fill='blue')


    def newgame():
        gamepage() 

    def restart():
        global turn
        global count
        btn9 = Button(root,text='Restart',font=('Footlight MT light',20, 'bold'),foreground='Black',bd=0,highlightthickness = 0,activebackground='white',bg='White',command = newgame,width= 6).place(x=330,y=80)
        turn=0
        count=0
        data={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
    
    def win():
        Label(root,text='Its A Draw',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
        restart()
        



    def Mark1():
        global turn
        global count
        try:

            if turn%2==0:
                Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=250,y=353)
                data[7]='x'
                chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=250,y=353)
                data[7]='o'
                chancex()
            if count<8:
                
                turn+=1
                count+=1
                          
            else:
                win()

            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
      
        except:
            turn=0
            count=0
            Mark1()



    def Mark2():
        global turn
        global count
        try:

            if turn%2==0:
                    Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=250,y=253)
                    data[4]='x'
                    chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=250,y=253)
                data[4]='o'
                chancex()
            if count<8:
                
                turn+=1
                count+=1
                            
            else:
                win()

            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
 
        except:
            turn=0
            count=0
            Mark2()
    def Mark3():
        global turn
        global count
        try:


            if turn%2==0:
                    Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=250,y=152)
                    data[1]='x'
                    chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=250,y=152)
                data[1]='o'
                chancex()
            if count<8:
                turn+=1  
                count+=1
                        
                 
            else:
                win()

            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

        except:
            turn=0
            count=0
            Mark3()
    def Mark4():
        global turn
        global count
        try:
            if turn%2==0:
                    Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=354,y=355)
                    data[8]='x'
                    chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=354,y=355)
                data[8]='o'
                chancex()            
            if count<8:
                turn+=1
                count+=1
            else:
                win()
            
            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

        except:
            turn=0
            count=0
            Mark4()
    def Mark5():
        global turn
        global count
        try:
            if turn%2==0:
                    Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=354,y=253)
                    data[5]='x'
                    chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=353,y=253)
                data[5]='o'
                chancex()
            if count<8:
                
                turn+=1
                count+=1
                        
            else:
                win()

            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

        except:
            turn=0
            count=0
            Mark5()
    def Mark6():
        global turn
        global count
        try:

            if turn%2==0:
                    Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=354,y=152)
                    data[2]='x'
                    chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=354,y=152)
                data[2]='o'
                chancex()
            if count<8:
                
                turn+=1 
                count+=1
                 
            else:
                win()

            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
        except:
            turn=0
            count=0
            Mark6()
    def Mark7():
        global turn
        global count
        try:
            if turn%2==0:
                Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=450,y=355)
                data[9]='x'
                chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=450,y=355)
                data[9]='o'
                chancex()
            if count<8:
                
                turn+=1                
                count+=1
                 
            else:
                win()
            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

        except:
            turn=0
            count=0
            Mark7()
    def Mark8():
        global turn
        global count
        try:
            if turn%2==0:
                Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=450,y=253)
                data[6]='x'
                chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=450,y=253)
                data[6]='o'
                chancex()
            if count<8:
                
                turn+=1                
                count+=1
                 
            else:
                win()
            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

        except:
            turn=0
            count=0
            Mark8()
    def Mark9():
        global turn
        global count
        try:
            if turn%2==0:
                Label(root,text='X',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=450,y=152)
                data[3]='x'
                chanceo()
            else:
                Label(root,text='O',font=('Footlight MT light', 55, 'bold'),background='white',foreground='Black').place(x=450,y=152)
                data[3]='o'
                chancex()
            if count<8:
                
                turn+=1                
                count+=1
                 
            else:
                win()

            if data[1]==data[2] and data[2]==data[3] and data[3]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[2] and data[2]==data[3] and data[3]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[4]==data[5] and data[5]==data[6] and data[6]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[4]==data[5] and data[5]==data[6] and data[6]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[7]==data[8] and data[8]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[7]==data[8] and data[8]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[1]==data[4] and data[4]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[4] and data[4]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[2]==data[5] and data[5]==data[8] and data[8]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[2]==data[5] and data[5]==data[8] and data[8]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[6] and data[6]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[6] and data[6]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            
            if data[3]==data[5] and data[5]==data[7] and data[7]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[3]==data[5] and data[5]==data[7] and data[7]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

            if data[1]==data[5] and data[5]==data[9] and data[9]=='x':
                Label(root,text='PLayer 1 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()
            elif data[1]==data[5] and data[5]==data[9] and data[9]=='o':
                Label(root,text='PLayer 2 Wins',font=('Footlight MT light', 15, 'bold'),background='white',foreground='Black').place(x=300,y=500)
                restart()

        except:
            turn=0
            count=0
            Mark9()


    btn1 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark1,height= 6,width= 13).place(x=229,y=353)
    btn2 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark2,height= 6,width= 13).place(x=229,y=252)
    btn3 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark3,height= 6,width= 13).place(x=229,y=150)
    btn4 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark4,height= 6,width= 12).place(x=333,y=353)
    btn5 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark5,height= 6,width= 12).place(x=333,y=252)
    btn6 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark6,height= 6,width= 12).place(x=333,y=150)
    btn7 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark7,height= 6,width= 13).place(x=434,y=353)
    btn8 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark8,height= 6,width= 13).place(x=434,y=252)
    btn9 = Button(root,foreground='white',bd=0,highlightthickness = 0,activebackground='white',bg='white',command = Mark9,height= 6,width= 13).place(x=434,y=150)
    
    

 
btn = Button(root,text ="Start",command = gamepage,width=20)
btn.place(x=320,y=500)
 

mainloop()