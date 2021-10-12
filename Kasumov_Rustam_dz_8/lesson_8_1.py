import re


def email_parse(email):
    dict_parser = {'username': None, 'domain': None }
    PAR_EMAIL = re.compile(r"([^@]+)@([\w_-]*\.[\w_-]{2,})$")
    pars_list = (PAR_EMAIL.findall(email))
    if not pars_list:
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    dict_parser['username'] = pars_list[0][0]
    dict_parser['domain'] = pars_list[0][1]
    return dict_parser


email_adr = input('Inter your email : ')
print(email_parse(email_adr))
