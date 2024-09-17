## Database Overview

L'objectif dial had database hia tastocki ga3 les information 3la User, 
Education dialo, technologies li kay mitrizi

## Database Schema
The database consists of the following tables:
- **Users**: Stores user information.
  - `id`: Integer, primary key
  - `username`: String, unique
  - `email`: String, unique
  - `password`: String
  - `job_title`: String -> ```Domain dialo ex: Frontend, backend, Data Analysis ...```
  - `country`: String
  - `city`: String 
  - `bio`: String -> ```Bio paragraph lighatkon 3ndo f webpage dialo```
  - `Exp`: String -> ```Che7al mn chehar dial experience 3ndo l user maghaydkhlahch nichan but ghat7sab```
  - `profile_pic`: String -> ```photo dial lprofile```
  - `facebook_url`: String 
  - `linkedln`: String
  - `stackoverflow`: String
  - `medium_url`: String
  - `pro_mail`: String
#####
- **Education**: Stores user education or training certificate.
  - `id`: Integer, primary key
  - `school_id`: Integer
  - `start_date`: Datetime
  - `end_date`: Datetime
  - `user_id`: String, Foreign key
######
- **School**: Stores Schools name and information.
  - `id`: String, primary key
  - `school_id`: String, Foreign key
  - `start_date`: Datetime
  - `end_date`: Datetime
  - `user_id`: String, Foreign key
#####
- **technology**: Stores Programing language and framework likay mitrizi l User.
  - `id`: String, primary key
  - `name`: String, Foreign key
  - `picture`: Datetime
  - `parent_id`: String -> ```l case dial framework ghaykon 3ndo parent id lihowa language bach m9ad dak lframework```

## How to read from Database

### 1. kifach t connecta b database b3da:
```python
from models import storage
```
Awal hajda dirha hia t importi storage mn models package fin kayn ga3 functions lghat7taj o lighanchera7 mora hadchi
### 2. Functions:
#### I-list dial all users
```python
users = storage.all(User).values()
for user in users:
    print(user.id, user.username, user.job_title)
```
#### II-get user b ID dialo
```python
user = storage.get_user_by_id(id="123e4567-e89b-12d3-a456-426614174001")
for user in users:
    print(user.username, user.email, user.job_title)
```
#### III-get user b job_title dialo
```python
users = storage.get_users_by_job_title("Data")
for user in users:
    print(user.username, user.email, user.job_title)
```
#### VI-create a new user
```python
username="zouhir"
email = "zouhir@gmail.com"
job_title = "Fullstack engineer"
country = "Morocco"
city="Casa"
password = "12345678"
exp=3
other... `(ana dayrhom optional walakin t9dar t3mrhom)`
storage.create_user_profile(username=username, email=email, password=password, country=country, city=city, exp=exp, ...)
```


