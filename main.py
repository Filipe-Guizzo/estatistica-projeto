import customtkinter as ctk
from generate_values import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

window = ctk.CTk()
window.title("Viagem Conforto")
window.geometry('500x300')

def change_theme():
    if (ctk.get_appearance_mode() == 'Dark'):
        ctk.set_appearance_mode('light')
    else:
        ctk.set_appearance_mode('dark')

def submit():
    month_selected =  get_month()
    city_selected =  get_city()
    if month_selected != 'Selecione um mês:' and city_selected != 'Selecione uma cidade:' :
        result = (find_values(month_selected, city_selected))
        dialog_result(result)

def get_month():
    return month.get()

def get_city():
    return city.get()

def dialog_result(result: dict):
    dialog = ctk.CTk()
    dialog.title("Modal")

    month_value = ctk.CTkLabel(dialog, text=f"Mês: {result['month']}")
    month_value.pack(pady=10)

    precipitation_value = ctk.CTkLabel(dialog, text=f"Precipitação: {result['precipitation']}")
    precipitation_value.pack(pady=10)

    temperature_value = ctk.CTkLabel(dialog, text=f"Temperatura: {result['temperature']}")
    temperature_value.pack(pady=10)

    humidity_value = ctk.CTkLabel(dialog, text=f"Umidade: {result['humidity']}")
    humidity_value.pack(pady=10)

    wind_value = ctk.CTkLabel(dialog, text=f"Vento: {result['wind']}")
    wind_value.pack(pady=10)

title = ctk.CTkLabel(window, text="Bem vindo ao Viagem Conforto")
title.pack(pady=10)

subtitle = ctk.CTkLabel(window, text="Selecione o local e mês da sua viagem:")
subtitle.pack(pady=10)

month_values = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
month = ctk.CTkOptionMenu(master=window, values=month_values)
month.pack(pady=10)
month.set("Selecione um mês:")

city_values = ["LAGES", "CHAPADINHA", "FLORIANOPOLIS"]
city = ctk.CTkOptionMenu(master=window, values=city_values)
city.pack(pady=10)
city.set("Selecione uma cidade:")

send = ctk.CTkButton(window, text = "ENVIAR", command=submit)
send.pack(pady=10)

send = ctk.CTkButton(window, text = "TEMA", command=change_theme)
send.pack(pady=10)

window.mainloop()