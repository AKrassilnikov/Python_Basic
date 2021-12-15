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
def find_id(code_id,site,dept):
    if code_id in site:
        return site[code_id]
    if dept > 1:
        for sub_site_code in site.values():
            if isinstance(sub_site_code,dict):
                sub_result = find_id(code_id,sub_site_code,dept - 1)  #рекурсия на поиск
                if sub_result:
                    break
        else:
            sub_result = None
        return sub_result

code_id = input('Какой ключ ищем? ')
dept = int(input('Введите глубину поиска: '))
result = find_id(code_id,site,dept)
if result:
    print(result)
else:
    print('Такого ключа в структуре сайта нет.')
