import locale

locale.setlocale(locale.LC_ALL, 'uz_UZ.UTF-8')

pul = 1234567.89
print(locale.format_string('%.2f', pul, grouping=True))
```

Kodni ishlatish uchun quyidagilar kerak:

1. `locale` moduli yuklab olish uchun `pip install python-locales` komandasi yoki `sudo apt-get install locales` komandasi (Ubuntu uchun) yoki `brew install python-locales` komandasi (MacOS uchun) ni bajarish.
2. `locale.setlocale(locale.LC_ALL, 'uz_UZ.UTF-8')` satrida `uz_UZ.UTF-8` ni o'zining operatsion sistemasida mavjud bo'lgan locale kodiga o'zgartirish.
3. `pul` deyariyadagi qiymatni o'zgartirish.
