---V1---
Метод простых итераций не сходится к корню 1,935575... 
Все эквивалентные функции перепробовал никак


---V2---
Поправил, все теперь сходится. Оказывается есть функция фи, которая с минус корнем, и все заработало
Также добавил графики производный этих функций для проверки, что их производная ограничена единицей
Но как объяснить что приходится использовать две функции не знаю.


---V3---
Поправил проверку в методе Ньютона, написал метод хорд и Чебышева и функцию check() для проверки правильности корней
Если корень меньше Эпсилон то все ок. Однако после такой проверки видно, что еще метод Дихотомии и метод хорд все еще сбоит (нехватает точности).
Завтра поправлю
Наверное...


---V4---
Нашел опечатку в методе хорд, и сделал правильное условие остановы для дихотомии
Теперь все корни считаются правильно и это конечная версия программы ☺
