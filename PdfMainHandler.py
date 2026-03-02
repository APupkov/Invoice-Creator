from pypdf import PdfWriter
from tkinter import filedialog as fd, ttk, Tk, Label, Button


from Owner import Owner

'''D:/Работа/Мелникова 25/квитанции/26/02/Квитанции за февраль 26г. по Северному дворику.pdf'''

class PdfMainHandler:
    '''объект пдф листа и логика работы с ним'''

    def __init__(self):
        pass



    def select_date(self):
        def show_selection():
            chosen_month = combo_month.get()
            chosen_year = combo_year.get()
            result_label.config(text=f"Выбраны: месяц - {chosen_month}, год - {chosen_year}")

        # Список месяцев
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

        # Диапазон годов (пример: от текущего года минус 10 лет до плюс 10 лет)
        current_year = 2023  # Пример текущего года
        years = list(range(current_year - 10, current_year + 11))

        # Создание окна
        window = Tk()
        window.title("Выбор месяца и года")

        # Комбо-бокс для выбора месяца
        label_month = Label(window, text="Месяц:", font=("Arial", 12))
        label_month.grid(column=0, row=0, padx=10, pady=10)
        combo_month = ttk.Combobox(window, values=months, state="readonly")
        combo_month.current(0)  # Устанавливаем первый элемент по умолчанию
        combo_month.grid(column=1, row=0, padx=10, pady=10)

        # Комбо-бокс для выбора года
        label_year = Label(window, text="Год:", font=("Arial", 12))
        label_year.grid(column=0, row=1, padx=10, pady=10)
        combo_year = ttk.Combobox(window, values=years, state="readonly")
        combo_year.current(len(years) // 2)  # По центру списка выбираем средний год
        combo_year.grid(column=1, row=1, padx=10, pady=10)

        # Кнопка подтверждения выбора
        button_confirm = Button(window, text="Подтвердить", command=show_selection)
        button_confirm.grid(column=0, row=2, columnspan=2, pady=10)

        # Метка результата
        result_label = Label(window, text="", font=("Arial", 12))
        result_label.grid(column=0, row=3, columnspan=2, pady=10)

        # Запуск главного цикла
        window.mainloop()

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

    def creat_invoice(self, owner: Owner):
        pass


test = PdfMainHandler()