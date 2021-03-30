levochki
========
Вебсайт, содержащий общедоступные ресурсы и публикации ридинг-группы левочки.

Селф-хост
---------
1. Установите и настройте nginx и fcgiwrap
2. Клонируйте этот репозиторий:  
   `git clone --recursive git://sysrq.in:/levochki /var/www/levochki`
3. С помощью директивы `include` или иным способом включите
   [levochki.nginx.conf][1] в файл конфигурации nginx, внеся необходимые
   изменения

Лицензия
--------
Права на переводы принадлежат автор\_кам исходных статей и опубликованы с их
согласия.

Всё остальное распространяется на условиях [CC BY-SA 4.0][cc], если не указано
иное.

[cc]: http://creativecommons.org/licenses/by-sa/4.0/

Участие в разработке
--------------------
Присылайте патчи и пулл-реквесты с помощью [git-send-email(1)][git1] или
[git-request-pull(1)][git2] на адрес <cyber@sysrq.in>.

[git1]: https://git-send-email.io/
[git2]: https://git-scm.com/docs/git-request-pull

[1]: ./levochki.nginx.conf
