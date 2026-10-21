class StringUtils:
    def capitalize(self, string: str) -> str:
        if not string:  # Если string равен None или пустой строке
            return ""
        return string[0].upper() + string[1:]

    def trim(self, string: str) -> str:
        if not string:  # Если None или пустая строка
            return ""
        return string.lstrip()  # lstrip() удаляет пробелы только слева, как в вашем тесте

    def contains(self, string: str, symbol: str) -> bool:
        if not string or not symbol:  # Если хотя бы один из аргументов None или пустой
            return False
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        if not string:  # Если строка None или пустая
            return ""
        return string.replace(symbol, "")  # replace заменяет symbol на пустоту, т.е. удаляет