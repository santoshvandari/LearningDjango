# Usign Supabase sql.

** You Need to Install psycopg2-binary to use supabase postgress database using database information**
```bash
pip install psycopg2-binary
```

** You Need to Install dj-database-url to use supabase postgress database using connection String**
```bash
pip install django dj-database-url
import dj_database_url
```

config of connection string
```python
DATABASES = {
    'default': dj_database_url.config(default='postgres://postgres:[YOUR-PASSWORD]@db.wcvelnmhgborfrktbfoy.supabase.co:5432/postgres')
}
```

