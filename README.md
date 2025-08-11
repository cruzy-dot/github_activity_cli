GitHub Activity CLI
A simple Python command-line tool to fetch and display the recent public activity of any GitHub user using the GitHub API.
This project is great for practicing working with APIs, handling JSON data, and building CLI applications.

Features
Fetches recent public activity for any GitHub username.

Allows specifying the number of events to display.

Displays event type and timestamp.

Simple and lightweight — no authentication required.

Installation
1. Clone the repository
bash
git clone https://github.com/cruzy-dot/github_activity_cli.git
cd github_activity_cli

3. Install dependencies
Make sure you have Python installed. Then install required packages:

bash
pip install requests
Usage
Run the script with:

bash
python main.py <username> [-n NUMBER]
Arguments
Argument	Description	Example
username	GitHub username (required)	cruzy-dot
-n / --number	Number of events to show (optional, default: 5)	-n 10


Future Improvements
Pretty-print event details (repo name, commit messages).

Handle API rate limits.

Option to save output to a file.

Color-coded terminal output.


