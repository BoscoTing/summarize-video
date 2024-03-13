import requests, os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_URL = 'https://api.notion.com/v1/pages'
NOTION_ACCESS_TOKEN = os.getenv('notion_integration_secret')
NOTION_DATABASE_ID = 'YOUR_NOTION_DATABASE_ID'

headers = {
    'Authorization': f'Bearer {NOTION_ACCESS_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

data = {
    'parent': {
        'database_id': NOTION_DATABASE_ID
    },
    'properties': {
        'title': {
            'type': 'title',
            'title': [
                {
                    'text': {
                        'content': 'Your Note Title'
                    }
                }
            ]
        },
        # Add other properties as needed
    },
    # Add other content blocks as needed
}

response = requests.post(NOTION_API_URL, headers=headers, json=data)
if response.status_code == 200:
    print('Note added successfully!')
else:
    print(f'Error: {response.status_code}')
