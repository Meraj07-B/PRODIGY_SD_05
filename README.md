# Web Scraping Tool with Advanced GUI

This project is a **Python-based web scraping tool** that allows users to scrape product information (e.g., names, prices, ratings, and availability) from a structured e-commerce website and save the extracted data into a CSV file. The tool includes a **modern GUI built using Tkinter and ttk** for better user experience, with features like a progress bar and multithreading to ensure smooth operation.

## Features
- **Scrapes Product Information**: Extracts details like product names, prices, availability, and ratings.
- **Multi-page Scraping**: You can specify how many pages to scrape.
- **GUI for User Interaction**: Easy-to-use graphical interface built using `Tkinter` and `ttk`.
- **CSV Export**: Save the scraped data in a structured CSV format.
- **Progress Bar**: A visual indicator to track the scraping progress.
- **Multithreading**: Ensures the GUI remains responsive while scraping.



## Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` from `bs4` for HTML parsing
- `pandas` for data manipulation
- `tkinter` for the GUI
- `ttk` for enhanced GUI design

### Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/web-scraping-tool.git
cd web-scraping-tool
```

2. Install the required dependencies if you haven't already:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python scraper_gui.py
```

4. A window will appear. Enter the base URL (e.g., `http://books.toscrape.com`) and the number of pages you want to scrape.

5. Click on the "Scrape Data" button, and the scraping process will begin.

6. Once completed, you'll be prompted to save the scraped data as a CSV file.

## Example

To scrape data from the website "Books to Scrape" (http://books.toscrape.com) for 2 pages, you would:

- Enter the URL: `http://books.toscrape.com`
- Set the number of pages to `2`.
- Hit the **Scrape Data** button.
- Save the data when prompted.

## Project Structure

```plaintext
web-scraping-tool/
│
├── scraper_gui.py         # The main Python script with GUI and scraping functionality
├── README.md              # Project documentation
├── requirements.txt       # Required Python packages
└── preview_image.png      # GUI preview image for documentation (optional)
```

## Notes
- This tool was built for scraping structured websites like [Books to Scrape](http://books.toscrape.com). Ensure the website allows scraping by reviewing its `robots.txt` file.
- The GUI ensures a responsive experience even during long scraping processes by using threading.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

