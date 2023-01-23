# Install
`pip install git+https://github.com/Sceptyre/python-umbrella-client.git@main`  

Bleeding Edge:  
`pip install git+https://github.com/Sceptyre/python-umbrella-client.git@devel`

# Usage
```py
from zoomclient import ZoomClient

zoom = ZoomClient(
    '<API_KEY>',
    '<API_SECRET>'
)
```

```py
# List rooms
zoom.rooms.list_rooms()

# Get specific room
zoom.rooms.get_room('abc123')
```
