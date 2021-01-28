from tkinter import *
import os.path, math

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.triangle = PhotoImage(file = os.path.dirname(__file__) + "\\data\\triangle.png")
        self.create_widgets()

    def create_widgets(self):
        self.r_tri = Label(root, image = self.triangle)
        self.r_tri.pack(side="top")

        self.a_label = Label(root, text= "a = ")
        self.a_text = Text(root, width=10, height=1)
        self.a_label.pack(side="left")
        self.a_text.pack(side="left")

        self.b_label = Label(root, text= "b = ")
        self.b_text = Text(root, width=10, height=1)
        self.b_label.pack(side="left")
        self.b_text.pack(side="left")

        self.c_label = Label(root, text= "c = ")
        self.c_text = Text(root, width=10, height=1)
        self.c_label.pack(side="left")
        self.c_text.pack(side="left")

        self.angle_label = Label(root, text= "A (degrees)= ")
        self.angle_text = Text(root, width=10, height=1)
        self.angle_text.pack(side="right")
        self.angle_label.pack(side="right")
        
        self.solve = Button(root, text="Solve", command= self.solve_question)
        self.solve.pack(side = "bottom", fill="none")
        self.clear = Button(root, text="Clear", command= self.clear_all)
        self.clear.pack(side = "bottom", fill="none")
   
    def solve_question(self):
        a = self.a_text.get("1.0", "end-1c").replace(",","").replace("\t","").replace(" ", "")
        b = self.b_text.get("1.0", "end-1c").replace(",","").replace("\t","").replace(" ", "")
        c = self.c_text.get("1.0", "end-1c").replace(",","").replace("\t","").replace(" ", "")
        angle = self.angle_text.get("1.0", "end-1c").replace(",","").replace("\t","").replace(" ", "")
        
        new_a, new_b, new_c, new_angle = self.round_up(a,b,c,angle)
        #checks if user puts angle
        if new_angle.isdigit():
            angle_rad = math.radians(float(angle))
            #given a, solve b and c
            if new_a.isdigit() and not new_b.isdigit() and not new_c.isdigit():
                #answer b - ADJACENT - a/b = opposite/adjacent --> TOA
                answer_b = float(a) / math.tan(angle_rad)
                #answer c - HYPOTENUSE - a/c = opposite/hypotensue --> SOH
                answer_c = float(a) / math.sin(angle_rad)
                self.b_text.insert("1.0",str(answer_b))
                self.c_text.insert("1.0",str(answer_c))
            #given b, solve a and c
            elif new_b.isdigit() and not new_a.isdigit() and not new_c.isdigit():
                #answer a - OPPOSITE - a/b = opposite/adjacent --> TOA
                answer_a = float(b) * math.tan(angle_rad)
                #answer c - HYPOTENUSE - b/c = adjacent/hypotenuse --> CAH
                answer_c = float(b) / math.cos(angle_rad)
                self.a_text.insert("1.0",str(answer_a))
                self.c_text.insert("1.0",str(answer_c))
            #given c, solve a and b
            elif new_c.isdigit() and not new_a.isdigit() and not new_b.isdigit():
                #answer a - OPPOSITE - opposite/hypotenuse --> SOH
                answer_a = float(c) * math.sin(angle_rad)
                #answer b - ADJACENT - adjacent/hypotenuse --> CAH
                answer_b = float(c) * math.cos(angle_rad)
                self.a_text.insert("1.0",str(answer_a))
                self.b_text.insert("1.0",str(answer_b))
            else:
                print("You either entered no values, entered the wrong values, or entered too many values")
        #if not, then we are solving FOR the angle
        elif angle == "":
            if new_a.isdigit() and new_b.isdigit() and not new_c.isdigit(): #given a and b
                #angle measure - given opposite/adjacent --> TOA, a/b 
                answer_angle = math.atan(float(a)/float(b))
                #answer c - hypotenuse - opposite/hypotenuse --> SOH
                answer_c = float(a) / math.sin(answer_angle)
                answer_angle = math.degrees(answer_angle)
                self.c_text.insert("1.0",str(answer_c))
                self.angle_text.insert("1.0",str(answer_angle))
                
            elif new_a.isdigit() and not new_b.isdigit() and new_c.isdigit(): #given a and c
                #angle measure - given opposite/hypotenuse --> SOH, a/c 
                answer_angle = math.asin(float(a)/float(c))
                #answer b - adjacent - opposite/adjacent --> TOA
                answer_b = float(a) / math.tan(answer_angle)
                answer_angle = math.degrees(answer_angle)
                self.b_text.insert("1.0",str(answer_b))
                self.angle_text.insert("1.0",str(answer_angle))
               
            elif not new_a.isdigit() and new_b.isdigit() and new_c.isdigit(): #given b and c
                #angle measure - given adjacent/hypotenuse --> CAH, b/c 
                answer_angle = math.acos(float(b)/float(c))
                #answer a - opposite - opposite/adjacent --> TOA
                answer_a = float(b) / math.tan(answer_angle)
                answer_angle = math.degrees(answer_angle)
                self.a_text.insert("1.0",str(answer_a))
                self.angle_text.insert("1.0",str(answer_angle))
            else:
                print("You either entered no values, entered the wrong values, or entered too many values")
        else:
            print("You either entered no values, entered the wrong values, or entered too many values")

    def clear_all(self):
        self.a_text.delete('1.0', END)
        self.b_text.delete('1.0', END)
        self.c_text.delete('1.0', END)
        self.angle_text.delete('1.0', END)

    def round_up(self,a,b,c,angle): #this function is used to change a, b, c into a "rounded" up version because .isdigit does not work on floats
        new_a, new_b, new_c, new_angle = a, b, c, angle
        if a.find(".") != -1:
            new_a = a[0:a.find(".")]
        if b.find(".") != -1:
            new_b = b[0:b.find(".")]
        if c.find(".") != -1:
            new_c = c[0:c.find(".")]
        if angle.find(".") != -1:
            new_angle = angle[0:angle.find(".")]
        return new_a, new_b, new_c, new_angle

root = Tk()
root.title("Right Triangle Trig")
root.geometry("500x500")
logo = PhotoImage(file = os.path.dirname(__file__) + "\\data\\logo.png")
root.iconphoto(False, logo)

app = Application(master=root)
app.mainloop()