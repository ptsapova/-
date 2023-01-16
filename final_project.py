import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# 0
'''Функция для перевода времени из часов и минут только в минуты. Принимает строку в форматах: "n hrs m mins ", "n hrs", "m mins"'''

def time_conversion(str_time):
  sep_hrs = str_time.find('hrs')
  sep_mins = str_time.find('mins')
  test_hr = str_time[sep_hrs]
  if test_hr == "h":
    hrs = str_time[:sep_hrs-1]
    mins = str_time[sep_hrs+4:sep_mins-1]
    if mins == '':
      total_mins =  int(hrs) * 60
    else:
      total_mins = 60 * int(hrs) + int(mins)
  elif test_hr == "s":
    total_mins =  int(str_time[:sep_mins-1])
  else:
    total_mins = 0
  return total_mins

# проверки
assert time_conversion('1 hrs 30 mins') == 90
assert time_conversion('25 mins') == 25
assert time_conversion('1 hrs 5 mins') == 65
assert time_conversion('7 mins') == 7
assert time_conversion('1 hrs') == 60
# 1
'''Функция, которая находит рецепт с курицей в csv файле, при условии, что в файле есть колонки: "recipe_name", "ingredients", а потом создает json'''
def recipes_with_chicken():
  file_name = str(input('Введите название файла:'))
  df = pd.read_csv(file_name)
  new_df = df[["recipe_name", "ingredients"]]
  chicken_recipes = new_df[new_df['ingredients'].str.contains(r'chicken')]
  return chicken_recipes.to_json ('recipes_with_chicken.json')

'''Функция, которая находит 3 самых долгих рецепта в csv файле, при условии, что в файле есть колонки: "recipe_name", "total_time", а потом создает json'''

def three_max_time_recipes():
  file_name = str(input('Введите название файла:'))  
  df2 = pd.read_csv(file_name)
  df2['total_time'] = df2['total_time'].fillna("10")
  df2['total_time'] = df2['total_time'].apply(time_conversion)
  df2 = df2.sort_values(by = "total_time", ascending = False)
  df2 = df2.loc[: 23, ['recipe_name', 'total_time']]
  return df2.to_json('3_max_time_recipes.json')

'''Функция, которая а каждое количество человек (servings) находит названия блюд, которые можно приготовить (recipe) '''
def serving():
  file_name = str(input('Введите название файла:'))  
  df3 = pd.read_csv(file_name)
  serving = df.groupby('servings')['recipe_name'].sum()
  return serving.to_json('распределение_по_количеству_человек.json')
#2
'''Функция для рисования гистограммы'''
def recipe_rating():
  file_name = str(input('Введите название файла:'))  
  df4 = pd.read_csv(file_name)
  plt.hist(df4.rating, label="All recipes",  
           color='green')
  plt.xlabel('Rating')
  plt.ylabel('Number of recipes')
  plt.grid(True)
  plt.savefig('recipe_rating.png')
