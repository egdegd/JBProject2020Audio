# JBProject2020Audio
Тестовое задание для проекта "Автоматический поиск аномалий на аудиозаписях": 
консольное-приложение на Python3 для примитивной обработки аудио.

Для запуска:
```
git clone https://github.com/egdegd/JBProject2020Audio.git
cd JBProject2020Audio
./build.sh
python3 ./src/MusicClient.py
```
Также возможно запустить приложение через docker образ.
##### Функционал приложения:
```
help - выводит список всех команд

join <output file> <list of input file> - склеивает произвольное количество аудиофайлов в один

split_all_file <input file> <list of points in ms> - разрезает аудиофайл на части

cut_interval <input file> <output file> <start of interval in ms> <finish of interval in ms> - вырезает интервал из аудиофайла

everse <input file> <output file> - инвертирует входной аудиофайл

exit - выходит из приложения
```