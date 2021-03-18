# Discord Bookmark Bot

A Discord bot that bookmarks saved messages in a #bookmarks channel.

## Installation

Log in to Discord on your browser and visit the [Discord Developer Portal](https://discord.com/developers/applications) to request a Discord API token.

In your terminal, install the Discord.js module and its dependencies. Use npm in the command prompt to install the module:

Optional: Create and activate a virtual environment:
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

Install dependencies:
```shell
npm install discord.js
```

Create environmental variables to hold your API key:

_secrets.sh_
```shell
export DISCORD_TOKEN="{DISCORD_TOKEN}"
```

Run the code from the terminal:
```shell
source secrets.sh
node discord.js
```


## Usage

Create a **#bookmarks** channel first (if one does not already exist), then you can bookmark and unbookmark any messages with emoji actions:
* :bookmark: React to any message with the bookmark emoji to save it in the #bookmarks channel!
* :x: React to a saved post in the #bookmarks channel with the X emoji to delete it.