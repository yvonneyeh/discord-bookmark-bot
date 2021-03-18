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
node discord.js
```


## Usage

Create a #bookmarks channel in your server first, then you can bookmark and unbookmark any messages by emoji actions.

Create a **#bookmarks** channel first, then you can bookmark and unbookmark any messages with emoji actions:
* React any message with :bookmark: to save it in the #bookmarks channel!
* React to a saved post in the #bookmarks channel with :x: to delete it.