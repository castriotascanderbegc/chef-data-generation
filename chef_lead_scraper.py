import os
import csv
import requests
from dotenv import load_dotenv

class ChefLeadScraper:
    def __init__(self):
        """ Initialize the scraper with API keys, search queries, locations, and CSV file details """
        # Load the API keys and endpoints from the .env file
        load_dotenv()
        # Define the API keys and endpoints
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.google_new_api_key = os.getenv("GOOGLE_NEW_API_KEY")
        self.yelp_api_key = os.getenv("YELP_API_KEY")
        self.google_places_endpoint = os.getenv("GOOGLE_PLACES_ENDPOINT")
        self.yelp_api_url = os.getenv('YELP_API_ENDPOINT')
        
        # Define the search queries and locations
        self.search_queries = ["private chef", "catering services", "personal chef"]
        self.locations = ["New York, USA", 
                          "Los Angeles, USA", 
                          "Chicago, USA", 
                          "San Francisco, USA", 
                          "Miami, USA", 
                          "Houston, USA", 
                          "Boston, USA",
                          "Washington, USA",
                          "Philadelphia, USA",
                          "Atlanta, USA"]
        
        # Define the CSV file to save the leads
        self.csv_file = "chef_leads.csv"
        # Define the CSV headers
        self.headers = ["Name", "Location", "Address", "Contact", "Website", "Rating", "Reviews", "Source"]

    def fetch_google_places(self, query, location):
        """ Fetch data from Google Places API """
        # Define the query parameters
        params = {
            "query": f"{query} in {location}",
            "key": self.google_api_key,
        }
        try:
            # Fetch the data from the Google Places API
            response = requests.get(self.google_places_endpoint, params=params)
            response.raise_for_status()
            return response.json().get("results", [])
        except requests.RequestException as e:
            print(f"Error fetching Google Places data: {e}")
            return []

    def fetch_yelp_places(self, query, location):
        """ Fetch data from Yelp API """
        # Define the headers and query parameters
        headers = {"Authorization": f"Bearer {self.yelp_api_key}"}
        params = {"term": query, "location": location, "limit": 50}
        try:
            # Fetch the data from the Yelp API
            response = requests.get(self.yelp_api_url, headers=headers, params=params)
            response.raise_for_status()
            return response.json().get("businesses", [])
        except requests.RequestException as e:
            print(f"Error fetching Yelp data: {e}")
            return []

    def collect_leads(self):
        """ Collect leads from Google Places and Yelp APIs """
        leads = []
        # Iterate over the search queries and locations
        for query in self.search_queries:
            for location in self.locations:
                # Fetch from Google Places API
                google_results = self.fetch_google_places(query, location)
                for place in google_results:
                    # Append the place details to the leads list
                    leads.append([
                        place.get("name"),
                        location,
                        place.get("formatted_address", "N/A"),
                        place.get("formatted_phone_number", "N/A"),
                        place.get("website", "N/A"),
                        place.get("rating", "N/A"),
                        place.get("user_ratings_total", "N/A"),
                        "Google Places"
                    ])

                # Fetch from Yelp API
                yelp_results = self.fetch_yelp_places(query, location)
                for business in yelp_results:
                    # Append the business details to the leads list
                    leads.append([
                        business.get("name"),
                        location,
                        business.get("location").get("display_address"),
                        business.get("phone", "N/A"),
                        business.get("url", "N/A"),
                        business.get("rating", "N/A"),
                        business.get("review_count", "N/A"),
                        "Yelp"
                    ])
        return leads

    def save_to_csv(self, leads):
        """ Save the leads to a CSV file """
        with open(self.csv_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
            writer.writerows(leads)
        print(f"Scraped {len(leads)} chef leads and saved to {self.csv_file}")

    def run(self):
        """ Run the scraper """
        leads = self.collect_leads()
        self.save_to_csv(leads)

if __name__ == "__main__":
    scraper = ChefLeadScraper()
    scraper.run()
