# TornadoSession
## Introduction
This is a simple session validation in Tornado, 
where the clients remote IP and user agent gets checked and compared with session information
stored in the PostgreSQL database.

This repository have two branches - **master** and **feature/stop_session_hijacking** - 
the first represents the issue where it's possible to hijack a session, 
and the other where the session validation has been implemented.

**Note**: This repository is not meant for production usage. 
Hence why it's missing multiple necessary features.

## Requirements
- PostgreSQL
- Tornado
- Asyncpg

## Getting started
### 1. Setting up the database
Create a table with the name **session_list** with the following columns:

| id        | user_name | created_at               | expires_at               | remote_ip | user_agent |
|-----------|-----------|--------------------------|--------------------------|-----------|------------|
| [PK] uuid | text      | timestamp with time zone | timestamp with time zone | text      | text       |

### 2. Change the PostgreSQL connection
Open the database directory and then database_manager.py.
Under the staticmethod **get_connection()**, change the value of **asyncpg.connect**
in accordance with your PostgreSQL database connection.

### 3. Start tornado
Run the **app.py** file located in the root directory.