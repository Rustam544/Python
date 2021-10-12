import requests as req
import decimal as dec


def currency_rates(argv):
    program, *args = argv
    currency = args[0]
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    result = req.get(url)
    s = result.text
    str_pos = result.text.find('Date')
    cur_time = s[str_pos + 6: str_pos + 16]
    str_pos = s.find(currency.upper())
    if str_pos == -1:
        s = 'None'
        print(f'{args[0].upper()} =', s, cur_time)
    else:
        val_pos = s.find('<Value>', str_pos, len(s))
        val_end_pos = s.find('</Value>', val_pos, len(s))
        s = s[val_pos + 7: val_end_pos].replace(',', '.')
        s = dec.Decimal(s).quantize(dec.Decimal('1.00000'))
        print(f'Курс {args[0].upper()} =',s, cur_time)
    return 0


if __name__ == "__main__":
    import sys

    exit(currency_rates(sys.argv))
