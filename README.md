
![Scanning](https://media.giphy.com/media/cMbZ3YwBMneMH4Ui9O/giphy.gif)

### Portscan With Python
 - Currently we are scanning a small list of ports `[21,22,23,25,53,80,110,111,135,139,143,332,443,445,993,995,1723,3306,3389,5900]`
 - You will be asked to provide a valid IP address or URL
 - The return will be either the OPEN port or a message saying that was not possible to get any open ports

 ## How to
- On the Terminal run
    - `sudo ./portscan`

## Error
 - If you receive a error saying that you don't have permission try to fix changing the permission of the file with this command
    - `chmod +x portscan`