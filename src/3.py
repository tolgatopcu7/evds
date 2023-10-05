# import requests
# import pandas as pd
import tkinter as tk
from tkinter import ttk
from evds import evdsAPI

# # TCMB EVDS API URL
# evds_api_url = "https://evds2.tcmb.gov.tr/service/evds/"

# TCMB API Anahtarınızı buraya ekleyin
evds = evdsAPI('ZGhjBH73U6')

# TCMB'den veri çekmek için bir işlev
# def fetch_evds_data(series_code, start_date, end_date):
#     params = {
#         "apikey": api_key,
#         "seriesid": series_code,
#         "startdate": start_date,
#         "enddate": end_date,
#     }
#     response = requests.get(evds_api_url, params=params)
#
#     if response.status_code == 200:
#         data = response.json()
#         return data.get("data", [])
#     else:
#         print(f"Veri çekme hatası: {response.status_code}")
#         return []

# Aylık ortalama dolar kuru verilerini çekme
def get_monthly_average_dollar(year, month):
    series_code = "TP.DK.USD.S.EF.YTL"
    start_date = f"01-{month}-{year}"
    end_date = f"31-{month}-{year}"

    dollar_data = evds.get_data(['TP.DK.USD.S.EF.YTL'], startdate=start_date, enddate=end_date)
    monthly_average_dollar = dollar_data['TP_DK_USD_S_EF_YTL'].mean()
    return monthly_average_dollar

# Kullanıcıdan ay ve yıl seçimini alacak olan işlev
def calculate_average_dollar():
    selected_month = month_combobox.get()
    selected_year = int(year_entry.get())

    result = get_monthly_average_dollar(selected_year, selected_month)

    # Sonucu ekranda gösterme
    result_label.config(text=f"Aylık Ortalama Dolar Kuru: {result:.4f}")

# Tkinter penceresini oluşturma
root = tk.Tk()
root.title("Aylık Ortalama Dolar Kuru Hesaplama")

# Etiketler ve giriş alanları
year_label = tk.Label(root, text="Yıl:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

month_label = tk.Label(root, text="Ay:")
month_label.pack()
month_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 13)])
month_combobox.pack()

calculate_button = tk.Button(root, text="Hesapla", command=calculate_average_dollar)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
