import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from typing import Dict, List, Union, Optional
import json
from dataclasses import dataclass
from urllib.parse import urljoin

@dataclass
class CurrencyConfig:
    path: str
    flag: str

class CurrencyScraper:
    """A class to scrape currency exchange rates from tejaratnews.com."""
    
    BASE_URL = "https://tejaratnews.com/"
    CURRENCIES = {
        "دلار": CurrencyConfig(path="قیمت-دلار", flag="🇺🇸"),
        "یورو": CurrencyConfig(path="قیمت-یورو", flag="🇪🇺"),
        "پوند": CurrencyConfig(path="قیمت-پوند", flag="🇬🇧"),
        "درهم امارات": CurrencyConfig(path="قیمت-درهم-امارات", flag="🇦🇪"),
        "لیر ترکیه": CurrencyConfig(path="قیمت-لیر-ترکیه", flag="🇹🇷"),
        "یوان چین": CurrencyConfig(path="قیمت-یوان-چین", flag="🇨🇳"),
        "روبل روسیه": CurrencyConfig(path="قیمت-روبل-روسیه", flag="🇷🇺"),
        "دینار عراق": CurrencyConfig(path="قیمت-دینار-عراق", flag="🇮🇶"),
        "دلار کانادا": CurrencyConfig(path="قیمت-دلار-کانادا", flag="🇨🇦"),
        "افغانی افغانستان": CurrencyConfig(path="قیمت-افغانی-افغانستان", flag="🇦🇫"),
        "ریال قطر": CurrencyConfig(path="قیمت-ریال-قطر", flag="🇶🇦"),
        "ریال عمان": CurrencyConfig(path="قیمت-ریال-عمان", flag="🇴🇲"),
        "دلار استرالیا": CurrencyConfig(path="قیمت-دلار-استرالیا", flag="🇦🇺"),
        "کرون سوئد": CurrencyConfig(path="قیمت-کرون-سوئد", flag="🇸🇪"),
        "درام ارمنستان": CurrencyConfig(path="قیمت-درام-ارمنستان", flag="🇦🇲"),
        "منات آذربایجان": CurrencyConfig(path="قیمت-منات-اذربایجان", flag="🇦🇿"),
        "فرانک سوئیس": CurrencyConfig(path="قیمت-فرانک-سوئیس", flag="🇨🇭"),
        "کرون دانمارک": CurrencyConfig(path="قیمت-کرون-دانمارک", flag="🇩🇰"),
        "روپیه هند": CurrencyConfig(path="قیمت-روپیه-هند", flag="🇮🇳"),
        "رینگیت مالزی": CurrencyConfig(path="قیمت-رینگیت-مالزی", flag="🇲🇾"),
        "کرون نروژ": CurrencyConfig(path="قیمت-کرون-نروژ", flag="🇳🇴"),
        "ریال عربستان": CurrencyConfig(path="قیمت-ریال-عربستان", flag="🇸🇦"),
        "دلار سنگاپور": CurrencyConfig(path="قیمت-دلار-سنگاپور", flag="🇸🇬"),
    }
    
    def __init__(self):
        """Initialize the scraper with a requests session."""
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def fetch_html(self, url: str) -> str:
        """
        Fetch HTML content from the specified URL.
        
        Args:
            url (str): The URL to fetch HTML from.
            
        Returns:
            str: The HTML content.
            
        Raises:
            RuntimeError: If the HTTP request fails or returns invalid content.
        """
        try:
            response = self.session.get(
                url,
                timeout=30,
                allow_redirects=True,
                verify=False  # Equivalent to CURLOPT_SSL_VERIFYPEER = false
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch HTML from {url}: {str(e)}")

    def parse_price(self, html: str, currency_name: str) -> Dict[str, Union[str, List, Optional[str]]]:
        """
        Parse price data from HTML content for a specific currency.
        
        Args:
            html (str): The HTML content to parse.
            currency_name (str): The name of the currency to extract data for.
            
        Returns:
            Dict[str, Union[str, List, Optional[str]]]: Parsed data including unit, date, and currency details.
        """
        soup = BeautifulSoup(html, "html.parser")
        data = []
        unit = "تومان"
        date = None

        # Extract date from tfoot
        tfoot_tds = soup.select("tfoot tr td")
        if tfoot_tds:
            date_match = re.search(r"تاریخ بروزرسانی:\s*([\d\/]+)", tfoot_tds[0].get_text(strip=True))
            if date_match:
                date = date_match.group(1)

        # Parse table rows
        for row in soup.select("table tbody tr"):
            cols = row.find_all("td")
            if len(cols) < 4:
                continue
                
            name = cols[0].get_text(strip=True)
            if name != currency_name:
                continue
                
            try:
                price = int(cols[1].get_text(strip=True).replace(",", ""))
            except ValueError:
                price = 0
                
            data.append({
                "name": name,
                "price": price,
                "change": cols[2].get_text(strip=True),
                "time": cols[3].get_text(strip=True),
            })

        return {"unit": unit, "date": date, "data": data}

    def scrape(self) -> Dict[str, Union[bool, str, Dict]]:
        """
        Scrape currency data for all configured currencies.
        
        Returns:
            Dict[str, Union[bool, str, Dict]]: Scraped data with status and timestamps.
        """
        result = {}
        for name, config in self.CURRENCIES.items():
            try:
                url = urljoin(self.BASE_URL, config.path)
                html = self.fetch_html(url)
                result[name] = {
                    **self.parse_price(html, name),
                    "flag": config.flag
                }
            except RuntimeError as e:
                result[name] = {
                    "error": f"خطا در دریافت داده‌ها: {str(e)}",
                    "flag": config.flag
                }

        return {
            "ok": True,
            "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "currencies": result
        }

def main():
    """Main function to run the scraper and output JSON."""
    try:
        scraper = CurrencyScraper()
        result = scraper.scrape()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({
            "ok": False,
            "error": "سرور با خطا مواجه شد"
        }, ensure_ascii=False))

if __name__ == "__main__":
    main()