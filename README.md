# Get Starting

![example workflow](https://github.com/HeywardLiu/st-final/actions/workflows/database_unittest.yml/badge.svg)

- Init a container

```shell
# build image
make build

# init dev-environment
make init

# delete container
make clean
```

- Use `$ ifconfig` to get container ip
- Modify ip, port when init a MongoDB object

```python
from MongoDB import MongoDB
db = MongoDB(ip="171.31.59.123", port=27017)
```
