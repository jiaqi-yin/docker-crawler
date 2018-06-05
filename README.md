# Web Crawler

The project simply builds a web crawler to check and find broken webpages across the whole website.

## User Story

    As a developer

    I want a tool to automatically check all the webpages in the website

    So that I can quickly identify if the new features or the bug fixing changes introduced to the website break any existing pages.

## Acceptance Criteria

- All the customer-facing webpages in the website can be easily located and tested.
- Any error pages should be logged for further follow-ups.

# Getting Started

## Install and Run

> This project is tested in MacOS ONLY.

1. [Install Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
1. Clone this project to your local environment.
1. Run `docker-compose up` from the top level directory for your project.

This `docker-compose up` command will start a `crawler` service and run the crawler for the specified website.

# Common Practices

[Avoiding getting banned for scraping](https://doc.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned)
