# Web Scraper: Book Titles & Prices

## Author
Ali Hyder

## Description
This Python script scrapes all book titles and their prices from the homepage of [books.toscrape.com](http://books.toscrape.com/) and saves the data into a CSV file (`books.csv`).

## Features
- Scrapes book titles and prices from the website
- Handles encoding issues for special characters
- Saves results in a clean CSV format for easy use

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Installation
1. Clone the repository or download the files.
2. Install dependencies via pip:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage
1. Run the script:
   ```bash
   python your_script_name.py
   ```
2. After running, check the folder for `books.csv` which contains the scraped book titles and prices.

## Output
The output CSV file (`books.csv`) has two columns:
- `Title`: The title of the book
- `Price`: The price of the book

## Example
| Title                    | Price  |
|--------------------------|--------|
| A Light in the Attic     | £51.77 |
| Tipping the Velvet       | £53.74 |
| ...                      | ...    |

## Notes
- This scraper only collects data from the homepage.
- The website [books.toscrape.com](http://books.toscrape.com/) is used for learning and practice purposes.

## License
MIT License

---

*Happy scraping!* 🚀