#########################################################################
#main                                                                   #
#Created by: Antonio DiMicco                                            #
#Assignment #2                                                          #
#Takes 2 command line arguments:                                        #
#<Player 1 Type> <Player 2 Type>                                        #
#Run the program as such: python <player 1> <player 2>                  #
#Works and tested with Python 2.6.6                                     #
#########################################################################

from Tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
from random import randint
import sys
 
class main:
     
    def _board(self):
        self.canvas.create_rectangle(0,0,300,300, outline="black")
        self.canvas.create_rectangle(100,300,200,0, outline="black")
        self.canvas.create_rectangle(0,100,300,200, outline="black")
        
#    def randplayer(self):
        
   
    def start1(self):
        self.canvas.delete(ALL)
        self.label['text']=('Tic Tac Toe Game\n ' + self.player1 + ' vs ' + self.player2)
        self.canvas.bind("<ButtonPress-1>", self.play)  
        self._board()
        self.i=0
        self.j=False
        
    def play(self,event):
        for k in range(0,300,100):
            for j in range(0,300,100):
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    if self.canvas.find_enclosed(k,j,k+100,j+100)==():
                        if self.i%2==0:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="blue")
                            self.TTT[Y1][X1]=1
                            self.i+=1
                        else:                         
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="red")
                            self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="red")
                            self.TTT[Y1][X1]=9
                            self.i+=1
        self.check()
        print "Here"
        if self.player2 == "random":
            self.randplayer()
        
    def check(self):
        #horizontal check
        for i in range(0,3):
            if sum(self.TTT[i])==27:
                self.label['text']=('2nd player wins!')
                self.end()
            if sum(self.TTT[i])==3:
                self.label['text']=('1st player wins!')
                self.end()
                
        #vertical check
        #the matrix below transposes self.TTT so that it could use the sum fucntion again
        self.ttt=[[row[i] for row in self.TTT] for i in range(3)]
        for i in range(0,3):            
            if sum(self.ttt[i])==27:
                self.label['text']=('2nd player wins!')
                self.end()
            if sum(self.ttt[i])==3:
                self.label['text']=('1st player wins!')
                self.end()
                
        #check for diagonal wins
        if self.TTT[1][1]==9:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('2nd player wins!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('2nd player wins!')
                self.end()
        if self.TTT[1][1]==1:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('1st player wins!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('1st player wins!')
                self.end()
                
        #check for draws
        if self.j==False:
            a=0
            for i in range(0,3):
                a+= sum(self.TTT[i])
            if a==41:
                self.label['text']=("It's a draw!")
                self.end()
                
    def end(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.j=True
     
    def __init__(self, master, player1, player2):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.label=Label(self.frame, text='Tic Tac Toe Game', height=6, bg='black', fg='yellow')
        self.label.pack(fill="both", expand=True)
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        self.TTT=[[0,0,0],[0,0,0],[0,0,0]]
        self.player1 = player1
        self.player2 = player2
        
        if self.player1 == "human":
            self.start1()
        #self.Start1=Button(self.frameb, text='Click here to start\ndouble player', height=4, command=self.start1,bg='white', fg='purple')
        #self.Start1.pack(fill="both", expand=True, side=RIGHT)
        #self.Start2=Button(self.frameb, text='Click here to start\nsingle player', height=4, command=self.start2,bg='purple', fg='white')
        #self.Start2.pack(fill="both", expand=True, side=LEFT)  
 
root = Tk()
app = main(root, sys.argv[1], sys.argv[2])
root.mainloop()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])