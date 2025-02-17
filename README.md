# Chef Data Generation

This repository contains an executable prototype for a Chef Lead Acquisition Data Generator. The purpose of this project is to scrape and generate data for potential chef leads leveraging Google Places and Yelp Fusion APIs.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/chef-data-generation.git
    ```
2. Navigate to the project directory:
    ```sh
    cd chef-data-generation
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary environment variables set up in a [.env](http://_vscodecontentref_/1) file.
2. Run the scraper script:
    ```sh
    python chef_lead_scraper.py
    ```
3. The generated data will be saved in [chef_leads.csv](http://_vscodecontentref_/2).

## Files

- [chef_lead_scraper.py](http://_vscodecontentref_/3): The main script to scrape and generate chef lead data.
- [chef_leads.csv](http://_vscodecontentref_/4): The output file containing the generated chef lead data.
- [.env](http://_vscodecontentref_/5): Environment variables required for the script.
- [.gitignore](http://_vscodecontentref_/6): Git ignore file.
- [README.md](http://_vscodecontentref_/7): This file.
