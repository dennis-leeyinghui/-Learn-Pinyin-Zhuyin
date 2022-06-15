from tkinter import *
import tkinter
from pypinyin import pinyin, lazy_pinyin, Style
import re
from zhon import hanzi

def addPinyin(input):
    return pinyin(input, style=Style.TONE3)

def addZhuyin(input):
    return pinyin(input, style=Style.BOPOMOFO)

def main():
    root = Tk()
    root.geometry("600x500")
    root.resizable(False,True)
    root.iconbitmap(r'C:\Users\whatd\Downloads\pinyin-learn\logo.ico')
    root.title("簡易讀中文 - Learn Pinyin & Zhuyin")

    def generate():

        input = leftInput.get("1.0", "end")
        #regexp = (r"[\w]")
        
        formatted = re.findall('[{}]'.format(hanzi.characters), input)

        #rightOutput.configure(text=f"{formatted[count]}: {addPinyin(formatted[count])[0][0]} | {addZhuyin(formatted[count])[0][0]} \n")

        output = ""
        for f in formatted:
            print (f)

            if (formatted.index(f) == len(formatted) - 1):
                output += f"{f} > {addPinyin(f)[0][0].strip():<{6}} | {addZhuyin(f)[0][0].strip()}\n--------------------\n"
            else:
                output += f"{f} > {addPinyin(f)[0][0].strip():<{6}} | {addZhuyin(f)[0][0].strip()}\n--------------------\n"
        print(output)
        #rightOutput.config(text=output)
    
        rightOutput.insert("1.0", output)

        for f in (formatted):
            rightOutput.tag_add("start", f"{formatted.index(f) * 2 - 1}.0", f"{formatted.index(f) * 2 - 1}.1")
            rightOutput.tag_add("start", f"{formatted.index(formatted[-1]) * 2 + 1}.0", f"{formatted.index(formatted[-1]) * 2 + 1 }.1")
            rightOutput.tag_configure("start", background="OliveDrab1", foreground="black")

            print("formatted.index(formatted[-1])>>>>>", formatted.index(formatted[-1]))
            rightOutput.tag_add("line", f"{formatted.index(formatted[-1]) * 2 + 2}.0", f"{formatted.index(formatted[-1]) * 2 +2 }.20")
            rightOutput.tag_configure("line", background="red")

    leftInput = Text(root)
    leftInput.insert(INSERT,"請在此輸入中文句子。")
    leftButton = Button(root, text="找讀音", command=generate)
    rightOutput = Text(root, state="normal", relief='flat', font=("MingLiU 20 bold"))

    # scrolling
    scroll = tkinter.Scrollbar(root, orient='vertical', command=rightOutput.yview)
    rightOutput.configure(yscrollcommand=scroll.set)
    scroll.pack(side='right', fill='y')

    leftInput.place(relx= 0.1, rely= 0.05, relwidth= 0.25, relheight= 0.8)
    leftButton.place(relx= 0.1, rely= 0.85, relwidth= 0.25, relheight= 0.1)
    rightOutput.place(relx= 0.4, rely= 0.05, relwidth= 0.7, relheight= 1.0)

    #root.state('zoomed')
    root.mainloop()

if __name__ == '__main__':
    main()