 self.btn_browse1 = tk.Button(self.master,width=17,height=2,text='Browse...')
    self.btn_browse1.grid(row=7,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.btn_browse2 = tk.Button(self.master,width=17,height=2,text='Browse...')
    self.btn_browse2.grid(row=8,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.btn_chkFiles = tk.Button(self.master,width=17,height=3,text='Check for files...')
    self.btn_chkFiles.grid(row=9,column=0,rowspan=2,padx=(20,0),pady=(10,0),sticky=N+W)
    self.btn_close = tk.Button(self.master,width=3,height=3,text='Close Program')
    self.btn_close.grid(row=9,column=14,padx=(0,0),pady=(0,0),sticky=S+E)
    self.btn_chkFiles.grid(row=3,column=0,rowspan=2,padx=(20,0),pady=(10,0),sticky=N+W)
    self.btn_close = tk.Button(self.master,width=17,height=3,text='Close Program')
    self.btn_close.grid(row=3,column=10,padx=(0,0),pady=(10,0),sticky=S+E)



    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=4,column=4,columnspan=20,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=5,column=4,columnspan=10,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_browse1 = tk.Entry(self.master,width=28,text='')
    self.txt_browse1.grid(row=0,column=4,padx=(30,20),pady=(25,0),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,width=28,text='')
    self.txt_browse2.grid(row=1,column=4,padx=(30,20),pady=(25,0),sticky=N+E+W)





if __name__ == "__main__":
    pass
