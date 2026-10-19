# Web Development

University course tasks written in Python: two socket programs and three web applications that run as CGI scripts.

| Folder | Description | Type |
|---|---|---|
| [`server_ring_topology`](server_ring_topology) | Servers connected in a ring that pass messages to each other | Console |
| [`web_crawler`](web_crawler) | Crawler that follows links starting from one web page | Console |
| [`continuation_forms`](continuation_forms) | Multi-step form for continuing studies | CGI |
| [`college_year_enrollment`](college_year_enrollment) | Subject enrollment by year with sessions stored in a database | CGI + MySQL |
| [`upload_files`](upload_files) | Image upload with registration, login and user management | CGI + MySQL |

## Requirements

- Python 3.8 or newer. The `cgi` module was removed in Python 3.13, so on 3.13+ install it with `pip install legacy-cgi`.
- For the CGI applications: a web server that runs CGI scripts (e.g. Apache from [XAMPP](https://www.apachefriends.org)).
- For `college_year_enrollment` and `upload_files`: MySQL or MariaDB and the connector:

  ```
  pip install mysql-connector-python
  ```

## Console programs

### server_ring_topology

```
python server_ring_topology/server_ring_topology.py
```

Enter the number of servers. They start on `127.0.0.1`, ports `40101`, `40201`, `40301`... and each one connects to the next, the last one to the first. Then enter a message for each server in turn; the message travels around the ring until it reaches the server that sent it.

### web_crawler

```
python web_crawler/web_crawler.py
```

Starts at `http://www.scratchpads.eu/explore/sites-list`, collects links from every page it visits (plain HTTP on port 80) and prints the list of visited links after about 50 pages.

## CGI applications

1. Copy the application folder into your web server's `cgi-bin` folder.
2. Change the first line (shebang) of the scripts to the path of your Python, e.g. `#!C:\Python312\python.exe` or `#!/usr/bin/env python3`. The scripts currently point to the author's Python installation.
3. The database connection settings are in `db_conf` in `database.py` (and `create_database.py`). By default they use user `root` with no password on `localhost`.
4. Open the start page in the browser, e.g. `http://localhost/cgi-bin/continuation_forms/login.py`.

### continuation_forms

Start page: `login.py`. No database is needed.

Login (name and repeated password) → student info (status, e-mail, specialisation, master's thesis) → remark → summary of the entered data.

### college_year_enrollment

Start page: `index.py`.

Create the database and the session table once:

```sql
CREATE DATABASE sessiondb;
```

```
python college_year_enrollment/create_database.py
```

For every subject you can choose Not selected, Enrolled or Passed, and the Certificate page lists all subjects with the total ECTS. Third year subjects can be enrolled or passed only if the whole first year is passed and passed second year subjects are worth at least 10 ECTS. The session id is kept in a cookie.

### upload_files

Start page: `login_page.py`.

Create the database:

```sql
CREATE DATABASE authentication;
USE authentication;

CREATE TABLE roles (
    role_id INT PRIMARY KEY,
    role VARCHAR(20)
);
INSERT INTO roles VALUES (0, 'admin'), (1, 'user');

-- Keep the column order, the code reads columns by position
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100) UNIQUE,
    question VARCHAR(255),
    answer VARCHAR(255),
    sex CHAR(1),
    role_id INT DEFAULT 1
);

CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(255)
);
```

New users are registered as regular users. To make someone an admin:

```sql
UPDATE users SET role_id = 0 WHERE username = 'your_username';
```

- Users register with a secret question, which they can use to reset a forgotten password.
- Passwords and answers are stored as salted PBKDF2 hashes.
- Logged-in users can upload images and see all uploaded images.
- Admins can also edit (username, sex, role) and delete users.
- Uploaded images are saved to `htdocs/images`, four folders above the script folder (`img_dir_path` in `upload_page.py`), so change that path if your server is set up differently.
