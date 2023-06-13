# Windscribe-Ephemeral-Port-Script

#### Original Credit: https://github.com/Mibo5354, https://gist.github.com/Mibo5354/cf265bc2108edb839e3607d9c9359dfa

This script has been modified from Mibo5454's original to refresh the Windscribe Ephermeral port and set qBittorrents
listening port automatically.

Disclaimer: Reports of using the script often can lead to account being temporarily disabled. Reduce usage to the minimum required timeframe

## Requirements

* Python (Tested on 3.10.7)
* selenium Package (Tested on 4.5.0)
* qbittorrent-api Package (Tested on 2022.8.38)

## Setup

Windscribe and qBittorrnet credentials are required in the following sections, as outlined in the script

Replace username and password with Windscribe credentials in the lines below
* user.send_keys('username') - Line 30
* passw.send_keys('password') - Line 35


Replace https://qbittorrent.example.com with qbittorrents URL (either reverse proxy or localhost url)

Replace 'username' and 'password' with qbittorrents WEBUI credentials
* client = qbittorrentapi.Client(host='https://qbittorrent.example.com', port=443, username='username', password='password') - Line 71
