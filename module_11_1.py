import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# requests - запросить данные с сайта и вывести их в консоль.
# image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png') не работает
image = requests.get('https://otvet.imgsmail.ru/download/u_6027dee40c2c2e6ac26e5c9d4adb067b_800.png')

with open('1new_image.png', 'wb') as f:
    f.write(image.content)

# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
df = pd.read_csv('data_info.txt')
print(df)

# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
phi = np.linspace(1, 2.*np.pi, 100)
plt.plot(phi, np.sin(phi))
plt.plot(phi, np.cos(phi))
plt.plot(phi, np.log(phi))

plt.show()