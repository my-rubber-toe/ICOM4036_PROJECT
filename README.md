# ICOM4036 Project: Device Communications

Design a new programming language to simplify the communication between
devices: The new language must be declarative and functional and provide
simple functionality to create local servers and allow communication with
external servers. You must clearly define the syntax of the new language.

-  Use Python libraries (e.g. PLY) to develop the scanner, parser and
intermediate code.
- Develop a short video (up to 4 minutes) to demonstrate the features of your
language.
- Provide a public GitHub repo with your code and documentation. Be sure all
members of the team are equally contributing to the project.

# Team Members

- Roberto Guzmán
- Cristian Ruiz

# Description

The programming language that we will be building consists of a combination of variable assignments and declarative language such as `SQL`.

The language will allow to perform basic creation of local servers and allow communication with external servers.

***
#####NOTES

1. Only basic operations will be made such as, local server to server connections and client connections. External connections will be performing some GET requests.

2. Some operating systems may take longer to close ports. So, if testing is done fast enough error will be thrown.
***

# Language Structure

## Tokens
- Data
  - regex: `\".*\"`
- Integers
  - regex: `\d+`
- Equal
  - regex: `=`
- String
  - regex: `[a-zA-Z_.-][a-zA-Z0-9_.-]*`
- Reserverd Keywords
   ```Javascript
    {
        'create' : 'CREATE', 
        'server' : 'SERVER', 
        'client' : 'CLIENT', 
        'delete' : 'DELETE', 
        'connect' : 'CONNECT', 
        'send' : 'SEND', 
        'info' : 'INFO' 
    }
  ```
## Grammar
```
statement : CREATE CLIENT STRING | DELETE CLIENT STRING | DELETE SERVER STRING
statement : CREATE SERVER STRING DATA INT | CREATE SERVER STRING STRING INT | CREATE SERVER STRING
statement : INFO STRING
statement : STRING EQUALS DATA | STRING EQUALS INT
statement : STRING SEND STRING DATA | STRING SEND STRING STRING
statement : STRING CONNECT STRING | STRING CONNECT DATA
```
This grammar could be also represented in a more convenient way using the following sequence:
```
statement : CREATE CLIENT STRING | DELETE CLIENT STRING | DELETE SERVER STRING | CREATE SERVER STRING DATA INT | CREATE SERVER STRING STRING INT | CREATE SERVER STRING | INFO STRING | STRING EQUALS DATA | STRING EQUALS INT | STRING SEND STRING DATA | STRING SEND STRING STRING | STRING CONNECT STRING | STRING CONNECT DATA
```
## Operations
- **Create**
    - `create server myserver "ip_addr" port_nbr`
    - `create client myclient`
- **Delete**
    - `delete server myserver`
    - `delete client myclient`
- **Local Connection**
    - `myclient connect myserver`
- **External Connection**
    - `myclient connect "addr_external_server"`
        - Example: `myclient connect "https://www.google.com"`
        *NOTE: "https://www.google.com" === "172.217.8.132"*
- **Data Processing**
    - `myclient send myserver "data or message"`
    - `myserver1 send myserver2 "data or message"`
- **Info**
    - `info myserver`
    - `info myclient`
- **Variables**
    - `var1 = "some string"`
