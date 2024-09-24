import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time

# Function to scrape data from Books to Scrape
def scrape_data(url, pages):
    product_names, product_prices, product_availabilities, product_ratings = [], [], [], []

    for page in range(1, pages + 1):
        response = requests.get(f"{url}/catalogue/page-{page}.html")
        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all('article', class_='product_pod')

        for product in products:
            name = product.h3.a['title']
            price = product.find('p', class_='price_color').text
            availability = product.find('p', class_='instock availability').text.strip()
            rating = product.p['class'][1]  # class indicates rating (e.g., "One", "Two", etc.)

            product_names.append(name)
            product_prices.append(price)
            product_availabilities.append(availability)
            product_ratings.append(rating)

        time.sleep(1)  # Respectful scraping

    data = {
        'Name': product_names,
        'Price': product_prices,
        'Availability': product_availabilities,
        'Rating': product_ratings
    }
    return data

# Save Data to CSV
def save_to_csv(data):
    df = pd.DataFrame(data)
    file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file:
        df.to_csv(file, index=False)
        messagebox.showinfo("Success", f"Data saved to {file}")

# Background scraping process
def start_scraping(url, pages, progress_bar, start_button):
    start_button.config(state='disabled')
    progress_bar.start(10)

    def scrape_in_thread():
        data = scrape_data(url, pages)
        save_to_csv(data)
        progress_bar.stop()
        start_button.config(state='normal')
    
    threading.Thread(target=scrape_in_thread).start()

# GUI setup
def create_gui():
    window = tk.Tk()
    window.title("Advanced Web Scraping Tool")
    window.geometry('500x300')
    window.configure(bg='#f5f5f5')

    # Title Label
    title_label = ttk.Label(window, text="Web Scraping Tool", font=("Helvetica", 16))
    title_label.pack(pady=10)

    # URL Input
    url_frame = ttk.Frame(window)
    url_frame.pack(pady=10)

    ttk.Label(url_frame, text="Enter Base URL:").grid(row=0, column=0, padx=5)
    url_entry = ttk.Entry(url_frame, width=40)
    url_entry.insert(0, "http://books.toscrape.com")  # Default URL
    url_entry.grid(row=0, column=1)

    # Number of Pages Input
    pages_frame = ttk.Frame(window)
    pages_frame.pack(pady=10)

    ttk.Label(pages_frame, text="Number of Pages:").grid(row=0, column=0, padx=5)
    pages_entry = ttk.Entry(pages_frame, width=10)
    pages_entry.grid(row=0, column=1)

    # Progress Bar
    progress_bar = ttk.Progressbar(window, mode='indeterminate')
    progress_bar.pack(pady=20, padx=10, fill='x')

    # Scrape Button
    scrape_button = ttk.Button(window, text="Scrape Data", command=lambda: on_scrape(url_entry.get(), int(pages_entry.get()), progress_bar, scrape_button))
    scrape_button.pack(pady=10)

    # Help Label
    help_label = ttk.Label(window, text="Enter the number of pages you want to scrape.", font=("Helvetica", 10))
    help_label.pack(pady=5)

    # Start GUI Loop
    window.mainloop()

def on_scrape(url, pages, progress_bar, start_button):
    start_scraping(url, pages, progress_bar, start_button)

if __name__ == "__main__":
    create_gui()
