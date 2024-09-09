import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque
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
def extract_data(soup, base_url):
    """
    Extracts data from the parsed HTML and finds links to follow.
    """
    data = []
    links_to_follow = set()
    
    # Example: Extracting titles and links
    for article in soup.find_all('article'):
        title = article.find('h2').get_text(strip=True) if article.find('h2') else 'No Title'
        link = article.find('a')['href'] if article.find('a') else None
        if link:
            full_link = urljoin(base_url, link)
            links_to_follow.add(full_link)
        data.append({'title': title, 'link': link})
    
    return data, links_to_follow

# 4. Save Data to CSV
def save_to_csv(data, filename):
    """
    Saves the extracted data to a CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# 5. Crawler Function
def crawl_website(start_url, max_pages=50):
    """
    Runs the web crawler starting from the start_url.
    """
    visited = set()
    queue = deque([start_url])
    all_data = []
    
    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        
        print(f"Crawling {url}...")
        html_content = fetch_page(url)
        if html_content:
            soup = parse_html(html_content)
            data, links = extract_data(soup, start_url)
            all_data.extend(data)
            visited.add(url)
            
            # Add links to the queue if they haven't been visited
            for link in links:
                if link not in visited:
                    queue.append(link)
    
    save_to_csv(all_data, 'crawled_data.csv')

# Example usage
if __name__ == "__main__":
    start_url = 'https://example-blog.com'  # Replace with the URL you want to start crawling from
    crawl_website(start_url)





'''
Explanation of Steps:
Fetch the Web Page:

Similar to the web scraping pipeline, this function sends an HTTP request to the URL and returns the HTML content.
Parse HTML Content:

Uses BeautifulSoup to parse the HTML content for easy navigation and extraction.
Extract Data:

Extracts relevant data from the HTML (e.g., titles and links).
Finds new links to follow, ensuring that these links are absolute URLs within the same domain using urljoin.
Save Data to CSV:

Converts the collected data into a DataFrame and saves it to a CSV file.
Crawler Function:

Manages the crawling process:
Uses a queue to manage URLs to crawl and a set to keep track of visited URLs.
Limits the number of pages crawled using max_pages.
Adds newly discovered links to the queue if they haven't been visited yet.
Customization Tips:
Domain Restriction: To ensure the crawler only follows links within the same domain, you might want to include domain checks in the extract_data function.
Handling Different Page Structures: Adjust the extract_data function based on the specific HTML structure of the pages you are crawling.
Rate Limiting: Add delays between requests to avoid overwhelming the server and to adhere to the website's robots.txt file.
Example:
This basic crawler can be adapted to various crawling needs by modifying the extraction logic and managing the links queue. For more advanced features like handling JavaScript-loaded content or managing large-scale crawling tasks, you might explore libraries like Scrapy or Selenium.
'''
