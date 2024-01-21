from testing_framework.controls.element import Element


class Table(Element):
    """
    Table web element
    """

    def __init__(self, locator, eng_name):
        super().__init__(locator, eng_name)

    def __str__(self):
        return f'"{self.eng_name}" table'

    def row(self, row_id):
        """Return row of table
        :param row_id - id of desired row
        """

        return self.subelement(f'[id={row_id}]', f"'{row_id}' table row")

    def cell(self, row_id, cell_id):
        """Return cell of some row"""

        table_row = self.subelement(f'[id={row_id}]', f"'{row_id}' table row")
        return table_row.subelement(f'[id={cell_id}]', f"Cell '{cell_id}' of table row '{row_id}'")

