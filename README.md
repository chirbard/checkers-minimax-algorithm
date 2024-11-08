# checkers-minimax-algorithm

Checkers Minimax algorithm written in Python.

It can beat https://www.online-checkers.com/ easy bot.

## Usage
Input your current checkers state as the initial_board, making sure `number ones are on top`.

Algorithm will output new board with best move.
### Example
```powershell
❯ docker run checkers-image
initial board:
| |x| |x| |x| |x|
|x| |x| |x| |x| |
| |x| |x| |x| |x|
| | | | | | | | |
| | | | | | | | |
|o| |o| |o| |o| |
| |o| |o| |o| |o|
|o| |o| |o| |o| |

best move:
| |x| |x| |x| |x|
|x| |x| |x| |x| |
| | | |x| |x| |x|
|x| | | | | | | |
| | | | | | | | |
|o| |o| |o| |o| |
| |o| |o| |o| |o|
|o| |o| |o| |o| |
```

## Running
### Build using docker
```sh
docker build -t checkers-image .
```
### Run using docker
```sh
docker run checkers-image 
```
### Run and build with one command
bash:
```sh
docker build -t checkers-image . && docker run checkers-image
```

powershell:
```powershell
docker build -t checkers-image . ; if ($?) { docker run checkers-image }
```