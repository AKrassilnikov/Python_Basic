site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def new_sites(site,site_number,product_name):

    for sub_site_code in site.values():
        if isinstance(sub_site_code,dict):
            sub_site_code[0]['title'] = 'Куплю/продам {} недорого'.format(product_name)
            sub_site_code[1]['h2'] = 'У нас самая низкая цена на {}'.format(product_name)
    return site




site_number = int(input("Сколько сайтов: "))
product_name = ['Tesla']
output = new_sites(site,site_number,product_name)
print(output)
