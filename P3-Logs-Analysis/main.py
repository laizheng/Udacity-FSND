import psycopg2


def main():
    q1 = "What are the most popular three articles of all time? "
    sql1 = "select title, count(*) as num from log " \
           "join articles on log.path = '/article/' || articles.slug " \
           "group by title order by num desc limit 3"

    q2 = "Who are the most popular article authors of all time?"
    sql2 = "select authors.name, count(*) as num from log " \
           "join articles on log.path = '/article/' || articles.slug " \
           "left join authors on authors.id = articles.author " \
           "group by authors.name order by num desc limit 5;"

    q3 = "On which days did more than 1% of requests lead to errors?"
    sql3 = ["create temp view failure as select date(time) as date, "
            "count(*) as num from log "
            "where status != '200 OK' group by date(time);",

            "create temp view success as select date(time) as date, "
            "count(*) as num from log "
            "where status = '200 OK' group by date(time);",

            "create temp view failure_rate as select failure.date, "
            "failure.num::decimal/success.num as percentage from failure "
            "join success on failure.date = success.date;",

            "select * from failure_rate where percentage > 0.01;"
            ]
    with psycopg2.connect("dbname=news") as conn:
        with conn.cursor() as curs:
            # Question 1:
            curs.execute(sql1)
            rows = curs.fetchall()
            print(q1)
            for row in rows:
                print(str(row[0]) + " -- " + str(row[1]))

            # Question 2:
            curs.execute(sql2)
            rows = curs.fetchall()
            print("\n" + q2)
            for row in rows:
                print(str(row[0]) + " -- " + str(row[1]))

            # Question 3:
            for sql in sql3:
                curs.execute(sql)
            rows = curs.fetchall()
            print("\n" + q3)
            for row in rows:
                print(str(row[0]) + " -- {:.2%}".format(row[1]) + " errors")


if __name__ == "__main__":
    main()
