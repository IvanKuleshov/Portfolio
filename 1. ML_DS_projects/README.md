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
