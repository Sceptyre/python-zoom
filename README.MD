# python-zoom
Designed for use with a server-to-server oauth zoom developer app

# Install
`pip install git+https://github.com/Sceptyre/python-zoom.git@main`  

Bleeding Edge:  
`pip install git+https://github.com/Sceptyre/python-zoom.git@devel`

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