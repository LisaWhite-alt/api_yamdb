import csv
import sqlite3

csv_n_sql = {
    'category.csv': 'api_category',
    'comments.csv': 'api_comment',
    'genre_title.csv': 'api_title_genre',
    'genre.csv': 'api_genre',
    'review.csv': 'api_review',
    'titles.csv': 'api_title',
    'users.csv': 'api_user ',
}

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

for key, value in csv_n_sql.items():
    with open(f'data/{key}', 'r', encoding='utf-8') as payload:
        reader = csv.reader(payload)
        columns = next(reader)
        query = ("insert into " + value + "({0}) values ({1})")
        query = query.format(
            ','.join(columns), ','.join(
                '?' * len(columns)))
        cur = conn.cursor()
        for data in reader:
            cur.execute(query, data)
        conn.commit()

        '''
        Debug script information
        '''

        print(f'Begin add data from {key}.csv to table {value}')
        print(conn.execute(f'SELECT * FROM {value};').fetchall())
        print(f'End add data from {key}.csv to table {value}\n\n')


conn.close()
