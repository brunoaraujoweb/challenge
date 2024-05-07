## Challenge

The proposal follows this flow:

- 1: Performs the Python script daily through the Ansible Playbook
- 2: Python script counts the number of records in the media table successfully and unsuccessfully and saves in a new database (OPS)
- 3: We can render the information in a percentage of how many records are successful through the Grafana (and configure alerts based on this)

Flow is only necessary if by any requirement the Grafaba cannot directly access the database with the Media table, otherwise it would not be necessary a routine to capture the information by simply running the query to the original database.

![alt text](https://github.com/brunoaraujoweb/challenge/blob/main/assets/grafana-dashboard.png?raw=true)