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

The programming language that we will be building consists of a combination of variable assignments, native functions and object notation similar to `JSON`.

## Variables

The language will allow users to create simple variables from the following regex `[a-zA-Z_][a-zA-Z_0-9]*`.

## Objects

Objects will be used as a method of storing configuration data. They will flow the `JSON` format such as:

```JavaScript
{
    "ip_address": "my_ipaddress",
    "port": "my_port",
    "security": {
        "HTTPS": true,
        "PRIVATE_NET": true,
        ...
    },
    "type": "my_type"
    ...
}
```

## Native functions

The language will allow to perform `CRUD` operations such as:

1. create_connection()
2. create_client()
3. create_server()
4. update_client()
5. update_server()
6. etc...
=======
- Roberto Y. Guzmán Ortiz
- Christian M. Ruiz Cruz
