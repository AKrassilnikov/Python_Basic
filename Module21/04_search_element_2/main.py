site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
def find_id(code_id,site):
    if code_id in site:
        return site[code_id]
    for sub_site_code in site.values():
        if isinstance(sub_site_code,dict):
            sub_result = find_id(code_id,sub_site_code)  #рекурсия на поиск
            if sub_result:
                break
    else:
        sub_result = None
    return sub_result

code_id = input("Input id: ")
result = find_id(code_id,site)
print(result)
