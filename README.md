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
- Christian Manuel

# Description

The programming language that we will be building consists of a combination of variable assignments and declarative language such as `SQL`.

The language will allow to perform basic server connection an sned recieve basic data.

***NOTE: Only basic operations will be made such as, local server to server connection and client connections performing some REST requests.***

# Language Structure

## Tokens
- Integers
  - regex: `\d+`
- Strings
  - regex: `duh... a string`
- Vars
  - regex: `[a-zA-Z_][a-zA-Z_0-9]*`

- Keywords

## Grammar

## Operations
- **Create**
    - `create server myserver "ip_addr" port_nbr`
    - `create client myclient server`
    - `myclient connect myserver`

- **Delete**
    - `delete server myserver1 myserver2 myserver_n`
    - `delete client myclient1 myclient2 myclient_n`

- **External Connections**
    - `myclient connect "addr_external_server"`
        - Example: `myclient connect "www.google.com" at port port`

- Variables
    - `var1 = "some_str"`
    - my_nbr = 1234
