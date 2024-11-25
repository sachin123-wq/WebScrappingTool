# WebScrappingTool
Developed a scraping tool using Python FastAPI framework to automate the information scraping process from the target website.


## The main objective of this project is to:

Automate the process of gathering product data for monitoring prices or inventory.
Provide an easily extensible framework for scraping data from websites.
Save time and effort by avoiding manual data collection.


## Functionality
### Data Scraping

Scrapes product titles, prices, and image paths from e-commerce web pages.
Handles dynamic data loading on websites (if applicable with libraries like selenium or similar).
Data Management

### Updates scraped data intelligently:

If the product exists and its price has changed, the price is updated.
If the product does not exist, it is added as a new entry.
Stores scraped data in a structured JSON file (scraped_data.json).

### Error Handling

Handles JSON decoding errors and empty file scenarios gracefully.
Provides warnings when files are missing or empty.

## Libraries and Technologies Used

**Python** 3.9+: Core programming language.
**FastAPI**: For building a RESTful API to handle scraping tasks.
**Uvicorn**: ASGI server to run the FastAPI app.
**JSON**: For storing and managing scraped data.
**os and Pathlib**: For file and path management.
**Pydantic**: To define and validate data models.
**Requests/BeautifulSoup:** For HTTP requests and HTML parsing (optional for scraping dynamic pages).

## Setup Instructions

### Clone the Repository

git clone https://github.com/sachin123-wq/WebScrappingTool.git
cd WebScrappingTool

## Install Dependencies

## Run the API Server(uvicorn)

app.router.routes:app --reload (Run inside the **WebScrappingTool** directory).
Also start redis server(**http://locahhost(127.0.0.1):6379**)

## Access the API

Open your browser or use tools like Postman to access the API at **http://127.0.0.1:8000/scrape**.

**HTTP POST request Example:- **

curl -X POST -H "Authorization: Bearer secure_token_123" \
     -H "Content-Type: application/json" \
     -d '{"max_pages": 1}' \
     http://127.0.0.1:8000/scrape
 
