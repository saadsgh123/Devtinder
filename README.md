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
#### list dial all users
```python

```


