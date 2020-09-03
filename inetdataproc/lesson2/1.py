"""
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы)
 с сайтов Superjob и HH.
 Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
 Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (отдельно минимальную и максимальную).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия.
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
Структура должна быть одинаковая для вакансий с обоих сайтов.
Общий результат можно вывести с помощью dataFrame через pandas.
"""

# https://krasnogorsk.hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&search_field=name&text=%D1%81%D0%B0%D0%BD%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA&page=38

import requests
from bs4 import BeautifulSoup


# url_hh = 'https://krasnogorsk.hh.ru/search/vacancy'
# params_hh = {
#     'L_is_autosearch': 'false',
#     'clusters': 'true',
#     'enable_snippets': 'true',
#     'search_field': 'name',
#     'text': None
# }


class MyRequests:
    headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    proxies = {
        'http': 'http://shchelakov.den:ntggjojcm@msk-tmg-04.infotecs-nt:3128',
        'https': 'https://shchelakov.den:ntggjojcm@msk-tmg-04.infotecs-nt:3128'
    }

    @staticmethod
    def get(url, params):
        return requests.get(url, params=params, headers=MyRequests.headers, proxies=MyRequests.proxies)


class Superjob:
    url = 'https://www.superjob.ru'

    def __init__(self, vacancy):
        self.vacancy = vacancy

    def get(self):
        params = {
            'keywords': self.vacancy,
            'page': 1
        }

        while True:
            response = MyRequests.get(Superjob.url + '/vacancy/search/', params)
            print(f'request: {response.url}\nresponse status: {response.status_code}')
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                vacancy_list = soup.find_all('div', {'class': 'f-test-vacancy-item'})
                if len(vacancy_list):
                    for vacancy in vacancy_list:
                        self._parse_vacancy_block(vacancy)

                    params['page'] += 1
                    # continue

            break

    @staticmethod
    def _parse_vacancy_block(block):
        print(Superjob._parse_vacancy_name(block))
        print(Superjob._parse_vacancy_salary(block))
        print(Superjob._parse_vacancy_link(block))

    @staticmethod
    def _parse_vacancy_name(block):
        for link in block.find_all('a'):
            if link.get('href').startswith('/vakansii/'):
                return link.getText()

        return 'unknown'

    @staticmethod
    def _parse_vacancy_salary(block):
        min_salary = None
        max_salary = None
        for salary in block.find_all('span', {'class': 'f-test-text-company-item-salary'}):
            print(salary.getText())

        return min_salary, max_salary

    @staticmethod
    def _parse_vacancy_link(block):
        for link in block.find_all('a'):
            href = link.get('href')
            if href.startswith('/vakansii/'):
                return Superjob.url + href

        return 'unknown'


Superjob('преподаватель математики').get()


# <span class="_1OuF_ _1qw9T f-test-text-company-item-salary"><span><span class="_3mfro _2Wp8I PlM3e _2JVkc _2VHxz">72&nbsp;280<span>&nbsp;<!-- -->—<!-- -->&nbsp;</span>90&nbsp;350<!-- -->&nbsp;<!-- -->руб.</span></span><span>/<span class="_3mfro PlM3e _2JVkc _2VHxz">месяц</span></span></span>
# <a class="icMQ_ _6AfZ9 f-test-link-Uchitel_matematiki _2JivQ _1UJAN" target="_blank" href="/vakansii/uchitel-matematiki-32168401.html?search_id=9b4f9966-edbd-11ea-bdcd-fe87291dd3d0&amp;vacancyShouldHighlight=true"><span class="_1rS-s">Учитель</span> <span class="_1rS-s">математики</span></a>
# <a class="icMQ_ _6AfZ9 f-test-link-Prepodavatel_prikladnoj_i_vysshej_matematiki _2JivQ _1UJAN" target="_blank" href="/vakansii/prepodavatel-prikladnoj-i-vysshej-matematiki-34374968.html?search_id=9b4f9966-edbd-11ea-bdcd-fe87291dd3d0&amp;vacancyShouldHighlight=true"><span class="_1rS-s">Преподаватель</span> прикладной и высшей <span class="_1rS-s">математики</span></a>
# while True:
#     vacancy = input('Enter vacancy name or "quit" to exit: ')
#     if vacancy == 'quit':
#         break
#
#     Superjob('vacancy').get()


# преподаватель математики
# https://www.superjob.ru/vacancy/search/?keywords=%D0%BF%D1%80%D0%B5%D0%BF%D0%BE%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8&geo%5Bt%5D%5B0%5D=4

# <div class="iJCa5 f-test-vacancy-item _1fma_ undefined _2nteL"><div class="Fo44F QiY08 LvoDO" spacing="3"><div class="_2g1F-"></div><div class="_2g1F-"><div><div class="jNMYr GPKTZ _1tH7S"><div class="_3mfro PlM3e _2JVkc _3LJqf"><a class="icMQ_ _6AfZ9 f-test-link-Prepodavatel_matematiki _2JivQ _1UJAN" target="_blank" href="/vakansii/prepodavatel-matematiki-34389304.html"><span class="_1rS-s">Преподаватель</span> <span class="_1rS-s">математики</span></a></div><span class="_1OuF_ _1qw9T f-test-text-company-item-salary"><span><span class="_3mfro _2Wp8I PlM3e _2JVkc _2VHxz">от<!-- -->&nbsp;<!-- -->80&nbsp;000&nbsp;руб.</span></span><span>/<span class="_3mfro PlM3e _2JVkc _2VHxz">месяц</span></span></span></div><div class="_3_eyK _3P0J7 _9_FPy" spacing="2"><div class="_2g1F-"><span class="_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd _2JVkc _2VHxz _15msI"><a class="icMQ_ _205Zx f-test-link-Moskovskij_kolledzh_elektromehaniki_i_informacionnyh_tehnologij _25-u7" target="_self" href="/clients/moskovskij-kolledzh-elektromehaniki-i-informacionnyh-tehnologij-2051981.html">Московский колледж электромеханики и информационных технологий</a></span></div><div class="_2g1F-"><span class="_3mfro f-test-text-company-item-location _9fXTd _2JVkc _2VHxz"><span class="_3mfro _9fXTd _2JVkc _2VHxz">Вчера</span><span class="clLH5"> • </span><span>Москва, улица Академика Миллионщикова, 20</span></span></div></div><div class="HSTPm _3C76h _10Aay _2_FIo _1tH7S"><span class="_3mfro _38T7m _9fXTd _2JVkc _2VHxz _15msI">Проводит обучение в соответствии с требованиями ФГОС. Выполняет обязанности, предусмотренные Единым квалификационным справочником…<br>Наличие профессионального образования. Наличие справки об отсутствии судимости. Наличие результата независимой диагностики МЦКО</span></div></div></div><div class="_2g1F-"><div class="_3Qutk _3fT-Z _2W8_a"><div class="_1Ttd8"><div class="_3P0J7 _9_FPy _1iZ5S" spacing="2"><div class="_2g1F-"><button class="_1_Cht f-test-vacancy-response-button f-test-button-Otkliknutsya" tabindex="0" type="button"><span class="qTHqo _3evr6 _3YDqW _1QeOa _24vIk" tabindex="-1"><span class="_23m0W"><span class="_3IDf-">Откликнуться</span></span></span></button></div><div class="_2g1F-"><div class="_3wu2D f-test-tooltip- _3TToE _2oiD- NpUCm AVPNH"><div class="_3yxRZ"><div class="f-test-tooltip-interact-area"><button class="_1_Cht f-test-button-Pokazat_kontakty" tabindex="0" type="button"><span class="qTHqo _9aT_7 _3YDqW DYJ1Y _2FQ5q" tabindex="-1"><span class="_23m0W"><span class="_3IDf-">Показать контакты</span></span></span></button></div><div class="_3AyK7 _36uTa" style="transition:opacity 100ms linear, transform 100ms linear;display:none;opacity:0"><div class="_2ODE0 _3zCNK _3_wME"><div class="_3zucV u-J7P OnzVW vSsGW _1A2w_ _3SGgo"><div class="_3wZVt OuDXD"><div class="_2g1F-"><div class="_1o0Xp GPKTZ _1tH7S"><span class="_3mfro _1enBN _2JVkc _2VHxz">контакты</span><button class="_1_Cht f-test-button-close" tabindex="0" type="button"><span class="qTHqo _3SHdK _2h9me _2HO6x _1rPPk _1Uw6n _2H-A7" tabindex="-1"><span class="_23m0W"><span class="_3f5Nw"><svg viewBox="0 0 24 24" class="_2pknO _3ZJ4b"><use xlink:href="#close"></use></svg></span></span></span></button></div></div><div class="_2g1F-"><div class="_3mfro _1hP6a _2JVkc _2VHxz _3LJqf"><span class="_3mfro _1hP6a _2JVkc _2VHxz _3bJal">Чтобы связаться с этим <!-- -->работодателем<!-- -->,&nbsp;<a class="icMQ_ f-test-link-sozdajte_rezyume" target="_self" href="/resume/create/?returnUrl=%2Fvacancy%2Fsearch%2F%3Fkeywords%3D%25D0%25BF%25D1%2580%25D0%25B5%25D0%25BF%25D0%25BE%25D0%25B4%25D0%25B0%25D0%25B2%25D0%25B0%25D1%2582%25D0%25B5%25D0%25BB%25D1%258C%2520%25D0%25BC%25D0%25B0%25D1%2582%25D0%25B5%25D0%25BC%25D0%25B0%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B8"><span class="_3mfro _30TaS _2JVkc _2VHxz _3Zhrb">создайте резюме</span></a>&nbsp;и откликнитесь на вакансию.</span></div></div></div></div></div></div></div></div></div></div></div><div class="_1Ttd8"><div class="_3P0J7 _9_FPy _1iZ5S" spacing="2"><div class="_2g1F-"><div class="dPsvk"><button type="button" class="_1xLyt f-test-clickable-"><span role="button" tabindex="0" class="_1xLyt _1V1Nk f-test-star_border-star _1Mrhs HO2FB f-test-clickable-"><div class="_2q4uC"><svg viewBox="0 0 24 24" class="_2pknO _3ZJ4b _3MNT6"><use xlink:href="#star_border"></use></svg></div><div class="_1Acan"><svg viewBox="0 0 24 24" class="_2pknO _3ZJ4b _3luW8"><use xlink:href="#star"></use></svg></div></span></button></div><div role="tooltip" class="_19fjG _3rSv1" style="position: absolute; left: 0px; top: 0px; margin: 0px; right: auto; bottom: auto; transform: translate(-53px, 32px);" data-popper-placement="bottom" data-popper-reference-hidden="" data-popper-escaped=""><div class="IeOui _31NcS">Добавить в избранное</div></div></div><div class="_2g1F-"><div class="_2BDyW"><div class="_9hBiK"><button class="_1_Cht f-test-button-more_vert" tabindex="0" type="button"><span class="qTHqo _9aT_7 _3YDqW DYJ1Y _2FQ5q _31YLM _2H-A7" tabindex="-1"><span class="_23m0W"><span class="_3f5Nw"><svg viewBox="0 0 24 24" class="_2pknO _3ZJ4b"><use xlink:href="#more_vert"></use></svg></span></span></span></button></div></div></div></div></div></div></div><div class="_2g1F-"></div></div></div>



# from bs4 import BeautifulSoup as bs
# import requests
# from pprint import pprint
#
#
# main_link = 'https://www.kinopoisk.ru'
# headers = {'User_Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
#                          '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
#
# response = requests.get(main_link + '/popular/films/?quick_filters=serials&tab=all',headers=headers)
# soup = bs(response.text,'html.parser')
#
# # serials_block = soup.find('div',{'class':'selection-list'})
# # serials_list = serials_block.findChildren(recursive=False)
# serials_list = soup.find_all('div',{'class':'desktop-rating-selection-film-item'})
#
# serials = []
# for serial in serials_list:
#     serial_data={}
#     serial_link = main_link + serial.find('a', class_='selection-film-item-meta__link').get('href')
#     serial_name = serial.find('p').getText()
#     serial_genre = serial.find('span',
#                                class_='selection-film-item-meta__meta-additional-item').find_next_sibling().getText()
#     try:
#         serial_rating = serial.find('span',class_='rating__value').getText()
#     except:
#         serial_rating = 0
#
#     serial_data['name'] = serial_name
#     serial_data['link'] = serial_link
#     serial_data['genre'] = serial_genre
#     serial_data['rating'] = serial_rating
#
#     serials.append(serial_data)
#
# pprint(serials)