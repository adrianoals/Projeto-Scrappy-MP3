# Project-Scrappy-MP3

## Description
This project is a web scraper that scans a music hosting website, allowing users to play the songs and select which instruments will be played. The code scans the website and downloads all music files.

## Technologies Used
- Python
- MongoDB
- Selenium
- Requests
- And other Python libraries

## How to Use
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the project dependencies with the command `pip install -r requirements.txt`.
4. You need to have an account on the website that was the target of the scraper to run this project.
5. Run the main script with the command `python src/main.py`. This script will scan the website and store the music links as documents in MongoDB.
6. To save all the music links that were stored in MongoDB, run the `saving_files.py` file with the command `python src/saving_files.py`.

## Contributing
Contributions to this project are welcome. Please open an issue to discuss proposed changes before submitting a pull request. If you have any questions, feel free to contact us.
