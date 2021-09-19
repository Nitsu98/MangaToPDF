from PIL import Image as img
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from os import listdir
import shutil

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 400, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Manga to PDF', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))

canvas1.create_window(150, 60, window=label1)

# Create a Tkinter variable
colorFormat = tk.StringVar(root)

# Dictionary with options
colorFormatChoices = { 'L','RGB'}
colorFormat.set('L') # set the default option

colorFormatLabel = tk.Label(root, text="L = Grey scale, RGB = Color", bg = 'lightsteelblue2')
colorFormatLabel.config(font=('helvetica', 12))
canvas1.create_window(150, 100, window=colorFormatLabel)

colorFormatMenu = tk.OptionMenu(root, colorFormat, *colorFormatChoices)
canvas1.create_window(150, 130, window=colorFormatMenu)
#colorFormatMenu.pack()

# Create a Tkinter variable
widthSize = tk.StringVar(root)

# Dictionary with options
widthSizeChoices = {'658', '494', '329'}
widthSize.set('494') # set the default option

widthSizeLabel1 = tk.Label(root, text="Choose base width", bg = 'lightsteelblue2')
widthSizeLabel1.config(font=('helvetica', 12))
canvas1.create_window(150, 170, window=widthSizeLabel1)

widthSizeLabel2 = tk.Label(root, text="Heigth will be proportional", bg = 'lightsteelblue2')
widthSizeLabel2.config(font=('helvetica', 12))
canvas1.create_window(150, 190, window=widthSizeLabel2)

widthSizeMenu = tk.OptionMenu(root, widthSize, *widthSizeChoices)
canvas1.create_window(150, 220, window=widthSizeMenu)
#widthSizeMenu.pack()


pageList = []
def getFile ():
    global pageList
    
    #import_file_path = filedialog.askopenfilename()
    import_file_path = filedialog.askdirectory(mustexist = True)
    chapterList = listdir(import_file_path)
    chapterList.sort()

    for chapter in chapterList:
        if Path(import_file_path+'/'+chapter).is_dir():

            imageList = listdir(import_file_path + '/' + chapter)
            imageList.sort()
            for image in imageList:

                image1 = img.open(import_file_path+'/'+ chapter + '/'+image)
                im1 = image1.convert(colorFormat.get())

                basewidth = int(widthSize.get())
                wpercent = (basewidth/float(im1.size[0]))
                hsize = int((float(im1.size[1])*float(wpercent)))
                im1= im1.resize((basewidth,hsize), img.LANCZOS)

                pageList.append(im1)





browseButton = tk.Button(root, text='Select Folder with Chapters', command=getFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 270, window=browseButton)

def convertToPdf ():
    global pageList
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    pageList[0].save(export_file_path, save_all=True, append_images=pageList[1:])

saveAsButton = tk.Button(root, text='Convert to a single PDF', command=convertToPdf, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 310, window=saveAsButton)
     
exitButton = tk.Button (root, text='Exit Application',command=root.destroy, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 350, window=exitButton)

root.mainloop()
