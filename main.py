import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk


Nome_arquivo = "qr_code.png"

class MainCode:
    def __init__(self, *args, **kwargs):
        self.janela = tk.Tk()
        self.abrir_janela()
        
    def Gerar_Qr(self, *args, **kwargs):
        link_qr = self.entry_link.get()
        
        self.qr = qrcode.QRCode(
            version=1, 
            box_size=10, 
            border=4
        )
        
        self.qr.add_data(link_qr)
        self.qr.make(fit=True)
        
        imagem = self.qr.make_image(fill='black', back_color='white')
        imagem.save(Nome_arquivo)
        
        imagem_qr = Image.open(Nome_arquivo)
        self.imagem_qr = ImageTk.PhotoImage(imagem_qr)
        
        self.label_qr.config(image=self.imagem_qr)
        self.label_qr.image = self.imagem_qr
        
        
    def abrir_janela(self, *args, **kwargs):
        self.janela.geometry('500x700')
        self.janela.title('QRecode') 
        
        self.frame_principal = tk.Frame(self.janela, width=500, height=700, bg='white')
        self.frame_principal.place(x=0, y=0)
        
        self.label_link = tk.Label(self.frame_principal, text='Cole o link:', font='Temple 12 bold', bg='white', fg='black')
        self.label_link.place(x=10, y=20)
        
        self.entry_link = tk.Entry(self.frame_principal, width=35, font='Temple 12 bold', relief='solid')
        self.entry_link.place(x=100, y=20)
        
        self.label_qr = tk.Label(self.frame_principal)
        self.label_qr.place(x=10, y=150)
        
        self.btnGerar = tk.Button(self.frame_principal, text='gerar', width=8, height=1, font='Temple 12 bold', 
                                  relief='raised', bg='light blue', fg='black', command=self.Gerar_Qr)
        self.btnGerar.place(x=330, y=50)
        

        self.janela.mainloop()

# Run the application
if __name__ == "__main__":
    app = MainCode()

        
        
        
        
        
        
        
 ##     ##  ######    #########    ######   ########  #######                   #
    # #   # #  #    #   R       R  #      #  #      #  #                   ############
     #  # #  #  #    #   R     RR   #         #      #  #                   # #   #  #
      #   #   #  #    #   RRRRRR     #  #####  ########  #######             #      #
       #       #  #    #   R     R    #  #   #  #      #        #           # #    # #
        #       #  ######   R      R   #######   #      #  #######         ############
                                                                                 # 