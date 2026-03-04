import os

from pypdf import PdfWriter
from tkinter import filedialog as fd

from OwnerList import OwnerList
from Owner import Owner
from owners_tuple import owners_tuple
from number_page import rooms25, rooms29


class PdfMainHandler:
    """объект пдф листа и логика работы с ним"""

    def __init__(self):
        self.general_pdf = None
        self.savedir = None
        self.month = None
        self.year = None

    def select_general_pdf(self):
        while True:
            self.general_pdf = fd.askopenfilename(
                title='Выберите файл с квитанциями',
                initialdir='D:/Работа/Мелникова 25/квитанции/',
                filetypes=[('PDF Files', '*.pdf')]
            )
            if self.general_pdf:
                break

    def select_savedir(self):
        while True:
            self.savedir = fd.askdirectory(
                title='Выберите место сохранения',
                initialdir=self.general_pdf,
            )
            if self.savedir:
                break

    def create_invoices(self) -> str:
        """Метод создания индивидуальных квитанций"""

        def Check_ready_for_begin() -> str | None:
            """Проверка готовности к формированию квитанций"""
            if not self.general_pdf:
                return 'Выберите файл с квитанциями'
            if not self.savedir:
                return 'Выберите место сохранения'
            if not self.month or not self.year:
                return 'Укажите месяц и год формирования квитанций'

            return None

        def forming_date_for_name():
            date = f'{self.month}{self.year}'
            if len(date) == 3:
                date = '0' + date

            return date

        def create_invoice(ow: Owner) -> None:
            """Создание квитанции"""

            date = forming_date_for_name()
            name_invoice = f'{ow.room}-{ow.house} {date}.pdf'

            pages_dict = rooms25 if ow.house == 25 else rooms29
            if isinstance(ow.room, int | str):
                pages = [pages_dict[ow.room] - 1, ]
            else:
                pages = [pages_dict[i] - 1 for i in ow.room]

            invoice = PdfWriter()
            invoice.append(fileobj=self.general_pdf, pages=pages)

            invoice.write(f'{self.savedir}/{name_invoice}')

        result_checking = Check_ready_for_begin()
        if result_checking:
            return result_checking

        # Получение списка всех собственников для формирования квитанций
        owners = OwnerList(owners_tuple)

        # формирование квитанций
        for owner in owners:
            create_invoice(owner)

        # subprocess.run(["explorer", self.savedir])
        os.startfile(self.savedir)

        # Сообщение о успешном завершении операции
        return 'Квитанции успешно сформированы'
