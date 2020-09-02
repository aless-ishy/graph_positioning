# Graph Positioning
Define nodes and edges positions of a cycle-less or undirected graph.
## Motivation
The main problem when drawing graphs is to position edges without trespassing nodes. To solve this problem and achieve an optimal solution was utilized A* algorithm and a JSON friendly api to allow easy drawing in front-end programs. 
## Requirements
The main project, _"structure"_ folder, has no requirement besides python 3.
## Examples  
### simple_example.py
Builds a small graph and find a edge path with _origin (1,0)_ and _target (3,4)_.
#### Run
```
~/Graph Positioning/python$ python examples/simple_example.py
```
### react_flask
React app using flask to handle communication between user interface and python program.

![example screenshot](screenshots/react_flask.png)
#### Requirements
* **_Flask_**
* _flask-cors (optional)_
* _Docker (optional)_
#### Run
You can run the server with docker or use flask development server.
#### 1 Docker
* Build image
```
~/Graph Positioning/python$ docker build --tag graphpositioning:1.0 .
```
* Run container
```
~/Graph Positioning/python$ docker container run -p 5000:5000 graphpositioning:1.0
```
You can access the app in http://localhost:5000/
#### 2 Flask Development Server
You will need to uncomment the first lines of **_server.py_** in **_~/python/examples/react_flask/_** .
* Before
```python
# # if not building with docker
# import os
# import sys
# # Add structure location to path.
# # Not needed if structure module is in the same location as this file or any file trying to import structure
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
```
* After
```python
# if not building with docker
import os
import sys
# Add structure location to path.
# Not needed if structure module is in the same location as this file or any file trying to import structure
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
```
* Run
```
~/Graph Positioning/python$ python examples/react_flask/server.py
```
You can access the app in http://localhost:5000/
