# pywise
## A wrapper client for simplifying interactions with the ConnectWise Manage API in Python

Currently undergoing full rewrite. Hold onto your butts.

- - - - 
Coverage:
=========

| Endpoint | Done? | Todo |
|----------|-------|------|
| Company | :o: | PATCH, PUT, DELETE |

- - - - 
How-to:
======
- [Initialize API client](#initialize-api-client)
- [Working with Endpoints](#working-with-endpoints)
  - [Get](#get)
  - [Child Endpoints](#child-endpoints)
- [Pagination](#pagination)

- - - - 
# Initialize API client
```python
from pywise.client import ConnectWiseAPIClient

# init client
api = ConnectWiseAPIClient(
  # company name,
  # company url,
  # client id,
  # public key,
  # private key
)
```

- - - - 
# Working with Endpoints
Endpoints follow the standard CRUD pattern in accordance to what's available with ConnectWise Manage - [ConnectWise Manage REST API Docs (requires ConnectWise Developer account)](https://developer.connectwise.com/Products/ConnectWise_PSA/REST)

# Get

Get many
```python
# sends get request to /company/companies endpoint
companies = api.company.get()
```

Get one
```python
# sends get request to /company/companies/{id} endpoint
companies = api.company.get_with_id(250)
```

Get with params
```python
# sends get request to /company/companies with a condition query string
conditional_get = api.company.get(params={
  'conditions': 'company/id=250'
})
```

# Child Endpoints
The ConnectWise API has many instances of nested endpoints - for example, /company/companies/{company_id}/sites

This is replicated in the library. All Endpoints provide an ```id``` method for setting the ID and traversing down the chain.

Example using the above (/company/companies/{company_id}/sites)
```python
sites = api.company.id(250).sites.get()
```

If you attempt to retrieve a child endpoint without first using the ```id``` method, an exception will be thrown.

- - - - 
# Pagination
The ConnectWise API paginates data for performance reasons through the ```page``` and ```pageSize``` query parameters. ```pageSize``` is limited to a maximum of 1000.

To make working with paginated data dead simple, Endpoints supply a ```paginated()``` method. Under the hood this wraps a Get request, but does a lot of neat stuff to make working with pages easier.

Working with pagination
```python
# initialize a PaginatedResponse instance for the companies endpoint, starting on page 1 with a pageSize of 100
paginated_companies = api.company.paginated(1,100)

# access the data from the current page using the .data field
page_one_data = paginated_companies.data

# if there's a next page, retrieve the next page worth of data
paginated_companies.get_next_page()

# if there's a previous page, retrieve the previous page worth of data
paginated_companies.get_previous_page()

# iterate over all companies on the current page
for company in paginated_companies:
  # ... do things ...
  
# iterate over all companies in all pages
# this works by yielding every item on the page, then fetching the next page and continuing until there's no data left
for company in paginated_companies.all():
  # ... do things ...
```
