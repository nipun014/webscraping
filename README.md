# Web Scraping Script

This Python script allows you to scrape data from a given URL and search for specific keywords within the text content. It returns the count of how many times each keyword appears in the text.

## Features

- **Web scraping**: Fetches the HTML content from the specified URL
- **Keyword search**: Searches for the given keywords in the text content of the webpage
- **Case-insensitive search**: Keywords are matched without considering case

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/nipun014/webscraping.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```

3. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. Run the Python script:
   ```bash
   python test.py
   ```

2. Enter the following details when prompted:
   - The URL you want to scrape
   - The number of keywords you want to search
   - The keywords themselves

3. The script will output the number of times each keyword appears in the text content of the webpage.

## Example

```plaintext
Enter URL: https://example.com
Enter number of keywords: 2
Enter keyword 1: Python
Enter keyword 2: Web scraping

Keyword search results:
'Python': 5 occurrences
'Web scraping': 3 occurrences
```

## Requirements

- Python 3.x
- requests library
- beautifulsoup4 library

