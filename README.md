Генератор текста на основе цепей Маркова
===
Программа запускается из командной строки, вводятся три аргумента: "*название файла с текстом-образцом*", "*количество связанных слов*", "*требуемый размер текста*".

Количество связанных слов отвечает за связанность сгенерированного текста: чем больше это число, тем красивее текст, но тем больше он похож на оригинал. Лучше использвовать числа 1 или 2

Пример: python markov-generator.py corpus.txt 1 50

Вывод:
===
Текст А.П.Чехова не причинить вред другим. Таким образом, оба мнения приведу аргумент из текста. Рассказчик убеждён, что возможно. В этом тексте В.А. Солоухин.Автор повествует о том, что медицинский пункт необходим, ведь его долг интеллектуала, помогая друг другу, показывают, что сидеть сложа руки», нужно служить ближним.Автор считает,что главная цель жизни, чего стоит отметить, что болезни, смерть, дети не думал о нелегкой судьбе женщин того тяжёлую жизнь людей.
