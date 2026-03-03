from pypdf import PdfWriter
from tkinter import filedialog as fd, ttk, Tk, Label, Button


from Owner import Owner


class PdfMainHandler:
    '''объект пдф листа и логика работы с ним'''

    def __init__(self):
        self.month = None
        self.year = None

    def select_general_pdf(self):
        while True:
            self.general_pdf = fd.askopenfilename(
                title= 'Выберите файл с квитанциями',
                initialdir= 'D:/Работа/Мелникова 25/квитанции/',
                filetypes= [('PDF Files', '*.pdf')]
            )
            if self.general_pdf: break

    def select_savedir(self):
        while True:
            self.savedir = fd.askdirectory(
                title= 'Выберите место сохранения',
                initialdir= self.general_pdf,
            )
            if self.savedir: break

    def create_invoices(self):
        print('Поехали!')
