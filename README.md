# PORNHUB_API_CLIENT
Simple lib to work with pornhub api

## Usage

### Installation

```
pip install pornhub-api-client
```

### Importing

```
import pornhub.client

phb_api = pornhub.client.PornhubApi()

phb_api.search(query="anal") # Search over pornhub
phb_api.stars() # Get all stars
phb_api.stars_detailed() # Get all start
phb_api.video_by_id(id=123) # Get all video by id
phb_api.is_video_active(id=123) # Check if video is active or not
phb_api.categories() # Returns all possible categories
phb_api.tags(tags = "a") # Search over tags
```

## Development

### Installation

Install to your environment as shown above:

```
git clone https://github.com/SpielmannMisha/pornhub_api_client
```

Install dependencies required for development:

```
pip install -r requirements-dev.txt
```

### Running the tests

Run following command in pornhub_api_client directory:
```
pytest
```
