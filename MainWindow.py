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
        self.window.geometry('600x450')
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

    @staticmethod
    def create_frame(title: str) -> ttk.Frame:
        '''Create base frame with title'''

        frame = ttk.Frame(borderwidth=4, relief=SOLID, padding=[8, 10])
        # добавляем на фрейм метку
        label = ttk.Label(frame, text=title)
        label.pack(anchor=N)

        return frame

    def create_frame_date(self) -> ttk.Frame:
        '''create frame choose month and year'''

        def combo_month_selected(event):
            self.pdf.month = combo_month.get()

        def combo_year_selected(event):
            self.pdf.year = combo_year.get()

        frame = self.create_frame('Выбор месяца и года')
        frame = ttk.Frame(borderwidth=4, relief=SOLID, padding=[8, 10])
        # добавляем на фрейм метку
        label = ttk.Label(frame, text='Выбор месяца и года')
        label.grid(row=0, column=0)

        # Комбо-бокс для выбора месяца
        months = list(range(0, 13))
        label_month = Label(frame, text="Месяц:")
        label_month.grid(row=1, column=0)
        combo_month = ttk.Combobox(frame, values=months, state="readonly")
        combo_month.bind("<<ComboboxSelected>>", combo_month_selected)
        combo_month.current(0)  # Устанавливаем первый элемент по умолчанию
        combo_month.grid(row=2, column=0)

        # Комбо-бокс для выбора года
        years = list(range(23, 30))
        label_year = Label(frame, text="Год:")
        label_year.grid(row=1, column=1)
        combo_year = ttk.Combobox(frame, values=years, state="readonly")
        combo_year.bind("<<ComboboxSelected>>", combo_year_selected)
        combo_year.current(0)  # По центру списка выбираем средний год
        combo_year.grid(row=2, column=1, padx=(50, 90))

        btn_create_invoice = ttk.Button(frame, text='Сформировать квитанции', command=self.pdf.create_invoices)
        btn_create_invoice.grid(row=3, column=3)

        return frame
