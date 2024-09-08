import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Fetch the Web Page
def fetch_page(url):
    """
    Fetches the content of the web page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# 2. Parse HTML Content
def parse_html(html_content):
    """
    Parses the HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# 3. Extract Data
def extract_data(soup):
    """
    Extracts data from the parsed HTML.
    This function should be customized based on the website's structure.
    """
    data = []
    
    # Example: Extracting titles and links from a blog page
    for article in soup.find_all('article'):
        title = article.find('h2').get_text(strip=True)
        link = article.find('a')['href']
        data.append({'title': title, 'link': link})
    
    return data

# 4. Save Data to CSV
def save_to_csv(data, filename):
    """
    Saves the extracted data to a CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main Pipeline Function
def scrape_website(url, output_file):
    """
    Runs the entire web scraping pipeline.
    """
    print(f"Fetching {url}...")
    html_content = fetch_page(url)
    if html_content:
        print("Parsing HTML...")
        soup = parse_html(html_content)
        print("Extracting data...")
        data = extract_data(soup)
        print("Saving data...")
        save_to_csv(data, output_file)

# Example usage
if __name__ == "__main__":
    url = 'https://example-blog.com'  # Replace with the URL you want to scrape
    output_file = 'scraped_data.csv'
    scrape_website(url, output_file)








'''
Explanation of Steps:
Fetch the Web Page:

Use the requests library to send an HTTP request to the URL and get the HTML content of the page.
Handle potential errors such as network issues or invalid URLs.
Parse HTML Content:

Use BeautifulSoup from the bs4 library to parse the HTML content.
This creates a BeautifulSoup object that allows you to navigate and search the HTML structure easily.
Extract Data:

Define the logic to extract relevant data from the parsed HTML. This step depends on the structure of the HTML you’re working with.
For example, if you are scraping blog titles and links, you would find and extract those elements from the BeautifulSoup object.
Save Data to CSV:

Convert the extracted data into a DataFrame using pandas.
Save the DataFrame to a CSV file for easy access and analysis.
Customization Tips:
Adjusting Data Extraction: Modify the extract_data function based on the specific HTML structure of the website you are scraping. Use BeautifulSoup’s methods like find, find_all, and select to navigate the HTML.
Handling Dynamic Content: If the website uses JavaScript to load content dynamically, you might need to use tools like Selenium or Scrapy to handle such cases.
'''
