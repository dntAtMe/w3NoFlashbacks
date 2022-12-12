# w3NoFlashbacks
## Description
When the game is loading, it plays a storybook scene as well, so players can catch up on the latest story bits. This, however, means that if your game is loaded **before** scene ends, you have to skip it manually.
Due to how game scripts work, if the scene ends first, game starts immediately when it's ready.
This mod aims to allow your game to start up as soon as it finishes loading.
## Details
The idea is to make storybooks scenes "empty" with duration set to 0. Thanks to that, no scene is played, but game recognizes that it started and ended (enabling auto-start when loading is finished). Storybooks are stored in `content/content0/movies.bundle`.
## Requirements
 - Python 3
 - [quickbms](http://aluigi.altervista.org/quickbms.htm) with witcher3.bms script (also provided as part of release)
## Installation
 - Download and unpack release anywhere
 - Run `python3 no_flashbacks.py --game [path to Witcher 3 root directory] --quickbms [path to quickbms]` <br>
 For example: `python3 no_flashbacks.py -g "G:\Games\The Witcher 3" -q "C:\Programs\quickbms"`
 
You can leave either argument (`game`, `quickbms`) not set, they're both optional. In such case, script assumes that needed prerequisite is in the same directory.
So, if you put `no_flashbacks.py` inside Witcher root directory, you only need to pass quickbms path argument.

## Result
[Imgur](https://i.imgur.com/sITTurc.gif)
