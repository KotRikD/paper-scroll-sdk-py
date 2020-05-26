# PaperScroll SDK для Python3.6+
**PaperScroll SDK для Python3.6+** простая реализация методов API PaperScroll

[![python version](https://img.shields.io/pypi/pyversions/paperscrollsdk)](https://pypi.org/project/paperscrollsdk/)
[![package version](https://img.shields.io/pypi/v/paperscrollsdk)](https://pypi.org/project/paperscrollsdk/)
[![pypi downloads](https://img.shields.io/pypi/dm/paperscrollsdk)](https://pypi.org/project/paperscrollsdk/)
![license: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

[Документация PaperScroll API](https://paperscroll.docs.apiary.io)

### Установка

```js
$ pip install paperscrollsdk
```

### Пример использования

```python
from paperscrollsdk import PaperScroll

paperClient = PaperScroll(merchant_id, "access_token")
paperApi = paperClient.getApi()

someMerchants = paperApi.getMerchants()
print(someMerchants)
```

### Методы SDK

|       API Метод           |       Метод в коде       |
|---------------------------|--------------------------|
| merchants.get             | getMerchants             |
| merchants.edit            | editMerchant             |
| users.get                 | getUsers                 |
| users.getBalances         | getUsersBalances         |
| transfers.create          | createTransfer           |
| transfers.get             | getTransfers             |
| transfers.getHistory      | getHistoryTransfers      |
| storage.getDisinfectants  | getDisinfectantsStorage  |
| storage.getItems          | getItemsStorage          |
| webhooks.get              | getWebhook               |
| webhooks.create           | createWebhook            |
| webhooks.delete           | deleteWebhook            |
| webhooks.getLogs          | getLogsWebhook           |
| *                         | callMethod               |

### Баги и PR
Репозиторий открыт для изменений! Если вы заметили какую-то ошибку связанную с кодом, откройте ***Issue*** и если знаете, как эту ошибку решить, открывайте ***Pull Request***