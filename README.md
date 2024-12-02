# WebScrappingTool
Developed a scraping tool using Python FastAPI framework to automate the information scraping process from the target website.


## The main objective of this project is to:

- Automate the process of gathering product data for monitoring prices or inventory.
- Provide an easily extensible framework for scraping data from websites.
- Save time and effort by avoiding manual data collection.


## Functionality
### Data Scraping

- Scrapes product titles, prices, and image paths from e-commerce web pages.
- Handles dynamic data loading on websites (if applicable with libraries like selenium or similar).
- Data Management

### Updates scraped data intelligently:

- If the product exists and its price has changed, the price is updated.
- If the product does not exist, it is added as a new entry.
- Stores scraped data in a structured JSON file (scraped_data.json).

### Error Handling

- Handles JSON decoding errors and empty file scenarios gracefully.
- Provides warnings when files are missing or empty.

## Technology Stack

- **Libraries Used**:
  - `FastAPI`: For building the web server and API endpoints.
  - `Requests`: For making HTTP requests to fetch webpage content.
  - `BeautifulSoup`: For parsing HTML and extracting required data.
  - `json`: For storing and manipulating data.
  - `os` and `pathlib`: For file and path handling.

## Setup Instructions

### Clone the Repository

```
git clone https://github.com/sachin123-wq/WebScrappingTool.git
cd WebScrappingTool
```

## Run the API Server(uvicorn)

```
uvicorn app.main:app --reload (Run inside the WebScrappingTool directory).
Also start redis server(http://locahhost(127.0.0.1):6379)
```

## Access the API

```
Open your browser or use tools like Postman to access the API at http://127.0.0.1:8000/scrape.
```

HTTP POST request Example:- 

```

curl -X POST -H "Authorization: Bearer secure_token_123" \
     -H "Content-Type: application/json" \
     -d '{"max_pages": 1}' \
     http://127.0.0.1:8000/scrape
```
 
