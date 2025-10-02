#예제1
from tkinter import*

root=Tk()
photo=PhotoImage(file="wl.gif")
w=Label(root,image=photo,justify="left").pack(side="right")
message="""삶이그대를속일지라도 
슬퍼하거나노하지말라! 
우울한날들을견디면:믿으라, 
기쁨의날이오리니. 
마음은미래에사는것 
현재는슬픈것: 
모든것은순간적인것,지나가는것이니 
그리고지나가는것은훗날소중하게되리니
"""
w2=Label(root,  padx=10,  text=message).pack(side="left")
root.mainloop()
