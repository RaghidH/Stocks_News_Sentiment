import requests
import webbrowser
from tabulate import tabulate

# Set your Alpha Vantage API key here
api_key = '9L1URKQBDIUVXDSF'
ticker = 'MARA'

url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={api_key}'
r = requests.get(url)
data = r.json()

# Extract relevant information from the API response
feed = data['feed']

# Prepare data for tabulation
table_data = []
for item in feed:
    title = item.get('title', '-')
    source = item.get('source', '-')
    sentiment_label = item.get('overall_sentiment_label', '-')
    sentiment_score = float(item.get('overall_sentiment_score', 0))
    table_data.append([title, source, sentiment_label, '{:.4f}'.format(sentiment_score)])

# Define table headers
headers = ['Title', 'Source', 'Sentiment', 'Sentiment Score']

# Generate the tabulated data
table = tabulate(table_data, headers=headers, tablefmt="html")

# Create the HTML content
html_content = f'''
<html>
<head>
<style>
table {{
  border-collapse: collapse;
  width: 100%;
}}

th, td {{
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}}

th {{
  background-color: #f2f2f2;
}}
</style>
</head>
<body>
{table}
</body>
</html>
'''

# Save the HTML content to a file
with open('output.html', 'w') as file:
    file.write(html_content)

# Open the HTML file in a new Chrome tab
webbrowser.open_new_tab('output.html')
