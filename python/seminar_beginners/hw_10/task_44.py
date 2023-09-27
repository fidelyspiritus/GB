import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Создание объекта OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Преобразование столбца в one hot представление
one_hot_data = encoder.fit_transform(data[['whoAmI']])

# Создание DataFrame из one hot представления
one_hot_df = pd.DataFrame(one_hot_data, columns=encoder.categories_[0])

one_hot_df.head()
