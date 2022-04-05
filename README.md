# Coalesce

![CI/CD](https://github.com/EmilRex/coalesce/actions/workflows/test.yml/badge.svg)

Coalesce is an API that gathers insurance coverage from many upstream APIs and coalesces it into a single response. The architectural choices made are meant to reflect best practices.

## Getting Started

Make sure you have `docker` and `docker-compose` installed, then simply run:

```shell
docker-compose up --build --detach
```

Now the API should be available at http://0.0.0.0:8080/.

You must provide the `member_id` as a query parameter and you can optionally provide a `strategy` (default is `average`). For example, http://0.0.0.0:8080/?member_id=1&strategy=minimum will return the minimum of each coverage element for member 1.
