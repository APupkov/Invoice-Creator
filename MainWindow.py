from tkinter import *
from tkinter import ttk
from PdfMainHandler import PdfMainHandler


class MainWindow:
    '''Создание главного окна программы'''

    def __init__(self):

        self.pdf = PdfMainHandler()
        # Создание окна
        self.window = Tk()
        self.window.title('Формирование индивидуальных квитанций')
        self.window.geometry('400x400')
        # Создание фрейма выбора общего файла с квитанциями
        gen_pdf_frame = self.create_frame_choose_general_pdf()
        gen_pdf_frame.pack(anchor=NW)

        self.window.mainloop()

    def create_frame_choose_general_pdf(self):
        '''Создание фрейма выбора общего файла с квитанциями'''

        frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
        # добавляем на фрейм метку
        label = ttk.Label(frame, text='Файл с квитанциями')
        label.pack(anchor=NW)
        # добавляем на фрейм текстовое поле
        self.label_gen_pdf = ttk.Label(frame, padding=[2, 2])
        self.label_gen_pdf.pack(anchor=NW)

        # добавляем на фрейм кнопку
        btn = ttk.Button(frame, text='Выбор файла', command=self.btn_command_gen_pdf)
        btn.pack(anchor=NE)
        # возвращаем фрейм из функции
        return frame

    def btn_command_gen_pdf(self) -> None:
        self.pdf.select_general_pdf()
        self.label_gen_pdf['text'] = self.pdf.general_pdf
