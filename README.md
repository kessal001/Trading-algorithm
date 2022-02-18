
# Trading Algorithm

A trading algorithm that helps the trader to predict and analyze past and future trends
## Features

- Moving Average Trading Strategy
- Live previews
- Useful plots

## Documentation

#### Load asset and analyze it

```python
  loadAsset(asset)
```

| Parameter | Type     | Description                |Where to find the tag?|
| :-------- | :------- | :------------------------- |:----|
| `asset` | `string` | **Required**. Your asset |[Yahoo Finance](https://finance.yahoo.com/)|




## Installation

Clone the repository on the local machine:

```bash
  $ git clone https://github.com/gracida001/Trading-algorithm.git
```
Go to the project directory

```bash
  cd my-project
```
Install all the packages:
```bash
  $ pip install -r requirements.txt
```
    

## Run Locally

Execute the program:

```bash
  python main.py asset
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Usage/Examples

```bash
  python main.py GLD
```

```python
def loadAsset(asset):
    loaded_asset = pdr.get_data_yahoo(asset)
    ...
    plt.show()

def main():
    loadAsset(sys.argv[1])

```
## Roadmap

- Add more trading algorithm

## Contributing and Support

Contributions are always welcome!

For support, email luca.pedersoli@mail.polimi.it

## 🔗 Links
[![github](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gracida001)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/luca-pedersoli-820009202)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/LucaPedersoli01)


## License
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


