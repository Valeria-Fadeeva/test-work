----
-- phpLiteAdmin дамп базы данных (https://www.phpliteadmin.org/)
-- phpLiteAdmin версия: 1.9.9-dev
-- Экспортировано: 8:51am on August 24, 2021 (MSK)
-- файл базы данных: ./db/valeria.sqlite
----
BEGIN TRANSACTION;

----
-- Удалить table для post_type
----
DROP TABLE IF EXISTS "post_type";

----
-- Table структура для post_type
----
CREATE TABLE 'post_type' ('id' INTEGER PRIMARY KEY NOT NULL, 'type' TEXT);

----
-- Дамп данных для post_type, суммарно 4 строк
----
INSERT INTO "post_type" ("id","type") VALUES ('0','Текст');
INSERT INTO "post_type" ("id","type") VALUES ('1','Учёба');
INSERT INTO "post_type" ("id","type") VALUES ('2','Практика');
INSERT INTO "post_type" ("id","type") VALUES ('3','Отдых');

----
-- Удалить table для post
----
DROP TABLE IF EXISTS "post";

----
-- Table структура для post
----
CREATE TABLE 'post' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'type' INTEGER, 'header' TEXT, 'content' TEXT, 'table_of_contents' TEXT, 'date' DATETIME NOT NULL DEFAULT CURRENT_DATE, 'column' INTEGER,'hidden' BOOLEAN);

----
-- Дамп данных для post, суммарно 24 строк
----
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('1','1','Марк Лутц - Изучаем Python (5-е изд). Том 1. 2019','143;818',NULL,'2021-11-20','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('2','1','Марк Лутц - Изучаем Python (5-е изд). Том 2. 2020','0;651',NULL,'2021-12-25','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('3','1','Дронов В. - Django 3.0 Практика создания веб-сайтов на Python. 2021','0;683',NULL,'2022-02-26','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('4','1','Дронов В. - Django 2.1 Практика создания веб-сайтов на Python. 2019','0;644',NULL,'2022-01-29','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('5','1','Бхаргава А. - Грокаем алгоритмы. 2017','0;273','Глава 1. Знакомство с алгоритмами|18
Глава 2. Сортировка выбором|40
Глава 3. Рекурсия|59
Глава 4. Быстрая сортировка|75
Глава 5. Хеш-таблицы|100
Глава 6. Поиск в ширину|127
Глава 7. Алгоритм Дейкстры|151
Глава 8. Жадные алгоритмы|182
Глава 9. Динамическое программирование|206
Глава 10. Алгоритм k ближайших соседей|236
Глава 11. Что дальше?|254','2021-11-06','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('7','2','Проект #1 PHP','0;1000',NULL,'2021-08-07','2',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('8','2','Проект #2 PHP','0;1000',NULL,'2021-10-09','2',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('9','2','Проект #3 Python','0;1000',NULL,'2021-11-20','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('10','2','Проект #4 Python','0;1000',NULL,'2021-12-25','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('11','2','Проект #5 Django 3','0;1000',NULL,'2022-01-29','2',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('12','2','Проект #6 C++ решение задач','0;1000',NULL,'2022-04-02','2',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('13','1','Чакон С., Страуб Б. - Pro Git v2.1.73. 2020','0;490','Введение|8
Основы Git|25
Ветвление в Git|64
Git на сервере|106
Распределенный Git|129
GitHub|171
Инструменты Git|225
Настройка Git|353
Git и другие системы контроля версий|388
Git изнутри|447
Appendix A: Git в других окружениях|491
Appendix B: Встраивание Git в ваши приложения|506
Appendix C: Команды Git|519','2021-10-23','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('15','1','Редмонд Э., Уилсон Д. - Семь баз данных. 2013','0;362','Вступление|17
Глава 1. Введение|21
Глава 2. PostgreSQL|30
Глава 3. Riak|78
Глава 4. HBase|125
Глава 5. MongoDB|169
Глава 6. CouchDB|214
Глава 7. Neo4J|259
Глава 8. Redis|305
Глава 9. Подводя итоги|356','2021-10-09','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('16','1','Моргунов Е. - Язык SQL. Базовый курс. 2017','0;254','Введение|5
Глава 1. Введение в базы данный и SQL|9
Глава 2. Создание рабочей среды|18
Глава 3. Основные операции с таблицами|22
Глава 4. Типы данных СУБД PostgreSQL|37
Глава 5. Основы языка определения данных|71
Глава 6. Запросы|110
Глава 7. Изменение данных|165
Глава 8. Индексы|188
Глава 9. Транзакции|199
Глава 10. Повышение производительности|228','2021-09-25','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('17','1','Прата С. - Язык программирования C. Лекции и упражнения (6-е изд). 2015','32;790',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('18','1','The Rust Programming Language','0;1000',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('19','1','Прата С. - Язык программирования C++. Лекции и упражнения (C++11) (6-е изд). 2012','0;1103',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('20','1','Страуструп Б. - Программирование. Принципы и практика с использованием C++ (C++11 C++14) (2е+изд). 2016','0;1157',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('21','1','Галовиц Я. - C++17 STL. Стандартная библиотека шаблонов. 2018','0;427',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('22','1','Страуструп Б. - Язык программирования C++. Краткий курс. 2019','0;308',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('23','1','Полухин А. - Разработка приложений на C++ с использованием Boost. 2020','0;343',NULL,'','2','1');
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('24','3','Отпуск','0;1000',NULL,'2022-07-10','0',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('25','1','Котеров Д. Симдянов И. PHP 7 в подлиннике. 2016','167;1063:421;447','Предисловие|29

Часть I. Основы Web-программирования|41
Глава 1. Принципы работы Интернета|43
Глава 2. Интерфейс CGI и протокол HTTP|60
Глава 3. CGI изнутри|72
Глава 4. Встроенный сервер PHP|104

Часть II. Основы языка PHP|113
Глава 5. Характеристика языка PHP|115
Глава 6. Переменные, константы, типы данных|127
Глава 7. Выражения и операции PHP|147
Глава 8. Работа с данными формы|168
Глава 9. Конструкции языка|180
Глава 10. Ассоциативные массивы|194
Глава 11. Функции и области видимости|209
Глава 12. Генераторы|237

Часть III. Стандартные функции PHP|249
Глава 13. Строковые функции|251
Глава 14. Работа с массивами|279
Глава 15. Математические функции|302
Глава 16. Работа с файлами и каталогами|313
Глава 17. Права доступа и атрибуты файлов|342
Глава 18. Запуск внешних программ|356
Глава 19. Работа с датой и временем|363
Глава 20. Основы регулярных выражений|377
Глава 21. Разные функции|413

Часть IV. Основы объектно-ориентированного программирования|421
Глава 22. Объекты и классы|423
Глава 23. Наследование|459
Глава 24. Интерфейсы и трейты|484
Глава 25. Пространство имён|492
Глава 26. Обработка ошибок и исключения|503

Часть V. Предопределенные классы PHP|539
Глава 27. Предопределенные классы PHP|541
Глава 28. Календарные классы PHP|550
Глава 29. Итераторы|556
Глава 30. Отображения|568

Часть VI. Работа с сетью в PHP|583
Глава 31. Работа с HTTP и WWW|585
Глава 32. Сетевые функции|596
Глава 33. Посылка писем через PHP|605
Глава 34. Управление сессиями|622

Часть VII. Расширения PHP|635
Глава 35. Расширения PHP|637
Глава 36. Фильтрация и проверка данных|646
Глава 37. Работа с СУБД MySQL|666
Глава 38. Работа с изображениями|716
Глава 39. Работа с сетью|740
Глава 40. Сервер memcached|749

Часть VIII. Библиотеки|765
Глава 41. Компоненты|767
Глава 42. Стандарты PSR|785
Глава 43. Документирование|809
Глава 44. Разработка собственного компонента|816
Глава 45. PHAR-архивы|843

Часть IX. Приёмы программирования на PHP|855
Глава 46. XML|857
Глава 47. Загрузка файлов на сервер|866
Глава 48. Использование перенаправлений|875
Глава 49. Перехват выходного потока|882
Глава 50. Код и шаблон страницы|895
Глава 51. AJAX|927

Часть X. Развёртывание|953
Глава 52. Протокол SSH|955
Глава 53. Виртуальные машины|976
Глава 54. Система контроля версий Git|996
Глава 55. Web-сервер Nginx|1023
Глава 56. PHP-FPM|1038
Глава 57. Администрирование MySQL|1045

Приложение. HTTP-коды|1063','2021-08-07','1',NULL);
INSERT INTO "post" ("id","type","header","content","table_of_contents","date","column","hidden") VALUES ('26','1','Лафоре Р.  - Объектно-ориентированное программирование в C++ (4-е изд.). 2004','0;795','','2022-04-02','1',NULL);
COMMIT;
