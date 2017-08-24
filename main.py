#! /usr/bin/env python3
from modules import top_three_articles, authors, error_logs


def main():
    top_three_articles.print_top_three_articles()
    authors.print_authors()
    error_logs.print_error_logs()


if __name__ == '__main__':
    main()
