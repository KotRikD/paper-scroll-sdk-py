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

### Баги и PR
Репозиторий открыт для изменений! Если вы заметили какую-то ошибку связанную с кодом, откройте ***Issue*** и если знаете, как эту ошибку решить, открывайте ***Pull Request***