from Tkinter import *
def login():
                x1=e1.get()
                x2=e2.get()
                t1=len(x1)
                t2=len(x2)
                if x1=="111" and x2=="222":
                                c['text']="登陆成功"
                else :
                                c['text']="用户名或密码错误"
                                e1.delete(0,t1)
                                e2.delete(0,t2)
root=Tk()
s1=Label(root,text="用户名:")
s1.grid(row=0,column=0,sticky=W)

s2=Label(root,text="密码:")
s2.grid(row=1,column=0,sticky=W)

e1=Entry(root)
e1.grid(row=0,column=1,sticky=E)

e2=Entry(root)
e2['show']='*'
e2.grid(row=1,column=1,sticky=E)

n=Button(root,text="登陆",command=login)
n.grid(row=2,column=1,sticky=E)

c=Label(root,text="")
c.grid(row=3)
root.mainloop()
