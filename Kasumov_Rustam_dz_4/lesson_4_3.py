import requests as req
import decimal as dec
from datetime import datetime


def currency_rates(currency):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    result = req.get(url)
    s = result.text
    str_pos = result.text.find('Date')
    cur_time = s[str_pos + 6: str_pos + 16]
    date_currency = datetime(year=int(cur_time[-4:]), month=int(cur_time[3:5]), day=int(cur_time[:2]))
    str_pos = s.find(currency.upper())
    if str_pos == -1:
        s = 'None'
    else:
        val_pos = s.find('<Value>', str_pos , len(s))
        val_end_pos = s.find('</Value>', val_pos, len(s))
        s = s [val_pos+7: val_end_pos].replace(',', '.')
        s = dec.Decimal(s).quantize(dec.Decimal('1.00000'))
    return s, date_currency


if __name__ == "__main__":
    print('Курс USD равен = ', currency_rates('usd'))
    print('Курс EURO равен = ', currency_rates('eur'))