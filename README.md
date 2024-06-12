For setup:
    Run the setup.py file and follow the instructions.
    After this you should find some file named /whitelist/pterodactyl.txt there you need to insert the server id(s) of the server(s) you want to sync the whitelist with and the path for the whitelist (should be 'whitelist.json' for Minecraft). The server's id is the first part of its UUID / Docker Container ID or just https://[your-panel-url]/server/[this part]

Pterodactyl API-key:
    You have to go to https://[your-panel-url]/admin/api and create a new key. Read and Write acces for Servers should be enough but I recommend just checking it for every category. You also need to specify a description. You then want to go to https://[your-panel-url]/account/api and create another key, there you have to insert the same description as before. This is the key you need to copy and then use for your setup.