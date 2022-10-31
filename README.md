```python
Кулешов Иван
e-mail: satura@ngs.ru
telegram: @viranum
```

# [DS & ML проекты, Хакатоны](https://github.com/IvanKuleshov/Portfolio/tree/main/1.%20ML_DS_projects)
## [1. АвиаХакатон-2022 от IT-центра МАИ](https://github.com/IvanKuleshov/AviaHack-2022)
**Трек:** S7 "Реверс-инжиниринг систем Engine Condition Monitoring": Требовалось построить модели машинного обучения, способные рассчитывать показатели «здоровья» и производительности авиадвигателя и воздушного судна на основе обучающей выборки.

**Результат**: для каждого из 30 таргета построено семейство из обученных моделей регрессоров `sklearn` + `CatBoost` + `XGBoost` + нейросетей различной архитектуры на `Keras`, из которых выбрана лучшая.

**Итог**: команда AviaNet заняла 3-4 место.

![изображение](https://user-images.githubusercontent.com/78194312/198583865-5bcc460c-8c83-4609-905b-edc3d68b67bc.png)

## [2. Тестовое задание для Appscience](https://github.com/IvanKuleshov/Appscience)
Задание от Appscience: собрать ссылки на товары с сайта www.agilent.com

Результат: написан класс GetProductLinks - сбор всех ссылок на продукты; класс AgilentBrowser - навигацию по сайту, выбор страны-языка. Парсинг осуществляет сбор произвольного числа характеристик с произвольного числа страниц продукта, в несколько потоков запуская браузер Firefox.
Инструменты: `BeautifulSoup`, `Silenium`, `multiprocessing`.

---
# [Проекты и тестовые на Python](https://github.com/IvanKuleshov/Portfolio/tree/main/2.%20Python_projects)
## [Определение количества пассажиров в автобусе](https://github.com/IvanKuleshov/detect_humans_into_bus)
Тестовое задание-demo: определить количество пассажиров в салоне автобуса на всём протяжении рейса, с целью отслеживания неучтённых "зайцев".

Решение: видеопоток разделяется на фреймы, которые с заданной периодичностью отправляются на сегментацию людей.

Для сегментации используется библиотека [`pixellib`](https://pixellib.readthedocs.io/en/latest/), с загруженной моделью `mask_rcnn`, обученной на датасете `COCO`.

![bus](https://user-images.githubusercontent.com/78194312/198957168-303f0512-55a0-4ef8-ab54-29d75d857724.jpg)

Для работы с видеопотоком написан класс VideoCaptureGen, возвращающий исходный фрейм генератором и фрейм с отрисованными рамками, на протяжении видео ведётся статистика распознанных людей в кадре.—
![index](https://user-images.githubusercontent.com/78194312/198957148-66a41c21-84f8-4780-a906-c2c975e3f70c.jpg)

## [Загрузка информации о новых альбомах музыки в жанре метал](https://github.com/IvanKuleshov/Public/tree/main/Parcing%20sites)
Парсинг сайта, размещающего новые поступления в жанре металлической музыки. Программа определяет все новые размещённые альбомы, появившиеся с прошлой проверки, закачивает характеристики альбомов, уведомляет о любимых группах пользователя (favorite_bands.xlsx).

Инструменты: `BeautifulSoup`, `tkinter`.

![index](https://user-images.githubusercontent.com/78194312/198961769-bc092db9-a9c9-4253-9aff-ae37c9a50f9b.jpg)

## [Сервис для просмотра выписок из Росреестра](https://github.com/IvanKuleshov/Portfolio/tree/main/2.%20Python_projects/statements)
Для Регионального оператора по капитальному ремонту по Новосибирской области: у организации имеется большое количество архивных выписок из Росреестра с данными о помещениях, необходим сервис для их просмотра в историческом аспекте.

Инструменты: `Flask`, `SQLAlchemy` для БД выписок, а также `WTForms` для создания и валидации форм.

Описание: в поле вводится кадастровый номер помещения, в ответ выдаётся отсортированный по времени список запрошенных файлов, которые можно скачать из базы или просмотреть.

![index](https://user-images.githubusercontent.com/78194312/198975910-f88b08cf-103a-4dc1-bcac-a29ebbc3e0a6.jpg)

---
# [Портфолио учебных работ](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects)
[1. Компьютерное зрение - 3 работы](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/6%20CVML%20%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B5%20%D0%B7%D1%80%D0%B5%D0%BD%D0%B8%D0%B5)

[2. Обработка естественного языка - 2 работы](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/7%20NLP%20%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20%D0%B5%D1%81%D1%82%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0)

[3. Введение в нейронные сети - 2 работы](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/2%20DSNN)

[4. Рекомендательные системы - 2 работы](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/3%20RSML%20%D0%A0%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)

[5. Временные ряды - 3 работы](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/4%20TSML%20%D0%92%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%80%D1%8F%D0%B4%D1%8B)

[6. Менеджмент DS-проектов - 2 работы](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/5%20ZAK%20%D0%9C%D0%B5%D0%B4%D0%B5%D0%B6%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%B0%D1%82%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2)

[7. Классические методы машинного обучения - 11 работ](https://github.com/IvanKuleshov/Portfolio/tree/main/3.%20Study_projects/1%20ML)
