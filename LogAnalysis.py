#!/usr/bin/python3
import psycopg2


def output_top_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "select articles.title, count(*) as hits from log, articles " \
            "where log.path like concat('%',articles.slug)" \
            " group by articles.title " \
            "order by hits desc limit 3"
    c.execute(query)
    top_articles = c.fetchall()
    db.close()
    for article in top_articles:
        print(article[0] + " - " + str(article[1]) + " views")
    return


def output_top_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "select authors.name, count(log.path) as hits " \
            "from authors, log, articles " \
            "where log.path like concat('%',articles.slug) " \
            "and authors.id = articles.author " \
            "group by authors.name order by hits desc"
    c.execute(query)
    top_authors = c.fetchall()
    db.close()
    for author in top_authors:
        print(author[0] + " - " + str(author[1]) + " hits")
    return


def output_high_error_days():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "select date, errorPercentage from dailyErrors " \
            "where errorPercentage > 1.0"
    c.execute(query)
    bad_days = c.fetchall()
    db.close()
    for day in bad_days:
        print(str(day[0]) + " - " + str(day[1]) + "% errors")
    return
