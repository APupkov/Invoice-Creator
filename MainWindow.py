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
        self.window.geometry('600x400')
        # Добавление фрейма выбора общего файла с квитанциями
        gen_pdf_frame = self.create_frame_choose_general_pdf()
        gen_pdf_frame.pack(side=TOP, fill=X, pady=5)
        # Добавление фрейма выбора места сохранения
        savedir_frame = self.create_frame_choose_savedir()
        savedir_frame.pack(side=TOP, fill=X, pady=5)
        # Добавление фрейма выбора месяца и года
        date_frame = self.create_frame_date()
        date_frame.pack(anchor=NW, pady=5)

        self.window.mainloop()

    def create_frame_choose_general_pdf(self):
        '''Создание фрейма выбора общего файла с квитанциями'''

        frame = self.create_frame('Файл с квитанциями')
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

    def create_frame_choose_savedir(self):
        '''Создание фрейма выбора места сохранения индивидуальных квитанций'''

        frame = self.create_frame('Место сохранения')
        # добавляем на фрейм текстовое поле
        self.label_savedir = ttk.Label(frame, padding=[2, 2])
        self.label_savedir.pack(anchor=NW)
        # добавляем на фрейм кнопку
        btn = ttk.Button(frame, text='Сохранить в', command=self.btn_command_savedir)
        btn.pack(anchor=NE)
        # возвращаем фрейм из функции
        return frame

    def btn_command_savedir(self) -> None:
        self.pdf.select_savedir()
        self.label_savedir['text'] = self.pdf.savedir

    def create_frame(self, title: str) -> ttk.Frame:
        '''Create base frame with title'''

        frame = ttk.Frame(borderwidth=4, relief=SOLID, padding=[8, 10])
        # добавляем на фрейм метку
        label = ttk.Label(frame, text=title)
        label.pack(anchor=N)

        return frame

    def create_frame_date(self) -> ttk.Frame:
        '''create frame choose mouth and year'''

        frame = self.create_frame('Выбор месяца и года')

        # Комбо-бокс для выбора месяца
        months = list(range(1, 13))
        label_month = Label(frame, text="Месяц:", font=("Arial", 12))
        label_month.pack(anchor=NW)
        combo_month = ttk.Combobox(frame, values=months, state="readonly")
        combo_month.current(0)  # Устанавливаем первый элемент по умолчанию
        combo_month.pack(anchor=NW)

        # Комбо-бокс для выбора года
        years = list(range(2023, 2030))
        label_year = Label(frame, text="Год:", font=("Arial", 12))
        label_year.pack(anchor=NW)
        combo_year = ttk.Combobox(frame, values=years, state="readonly")
        combo_year.current(3)  # По центру списка выбираем средний год
        combo_year.pack(anchor=NW)

        return frame
