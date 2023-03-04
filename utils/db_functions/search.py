class TableSearch:
    @staticmethod
    def create_table_search(table_name: str, **kwargs):
        sql_expression = "\n\t(" + ") AND \n\t(".join(
            map(lambda x: f'"{x[0]}" LIKE "%{x[1]}%"', kwargs.items())
        ) + ")\n"

        sql_request = f'SELECT * FROM {table_name} WHERE ({sql_expression});' if kwargs else ";"

        return sql_request
