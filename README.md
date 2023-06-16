[![Health IT Logo](https://healthit.com.au/wp-content/uploads/2019/06/HIT-proper-logo.png)](https://healthit.com.au)

# PyWise - A wrapper client for simplifying interactions with the ConnectWise Manage API in Python

PyWise is a full featured, type-annotated API client written in Python for the ConnectWise API's. Currently, it only supports ConnectWise Manage, but more is planned.
- - - - 
Features:
=========
- 100% API Coverage. All endpoints and response schemas have had their code generated from the ConnectWise Manage OpenAPI Schema.
- Focus on type-annotation and DX. Models are parsed and validated using [Pydantic](https://github.com/pydantic/pydantic)

PyWise is currently in **pre-release**. This means that while it does work, you may come across issues and inconsistencies. 
As all Endpoint and Model code has been generated, not all of it has been tested. YMMV.
Please refer to the roadmap for more information.
- - - - 
Known Issues:
=============
- Currently only parses and validates **Response** models. No input models yet.
- As this project is still a WIP, documentation or code commentary may not always align. 
- Little to no error handling just yet

- - - - 
Planned and in progress:
=============
- Automate API Support
- Input model validation
- Robust error handling

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
from pywise import ConnectWiseManageAPIClient

# init client
api = ConnectWiseManageAPIClient(
  # company name,
  # company url,
  # client id,
  # public key,
  # private key
)
```

- - - - 
# Working with Endpoints
Endpoints are 1:1 to what's available with ConnectWise Manage as code is generated from their OpenAPI schema
For more information, check out the [ConnectWise Manage REST API Docs (requires ConnectWise Developer account)](https://developer.connectwise.com/Products/ConnectWise_PSA/REST)

# Get
```python
# sends get request to /company/companies endpoint
companies = api.company.companies.get()
```

# Get one
```python
# sends get request to /company/companies/{id} endpoint
companies = api.company.companies.id(250).get()
```

# Get with params
```python
# sends get request to /company/companies with a condition query string
conditional_get = api.company.companies.get(params={
  'conditions': 'company/id=250'
})
```

# Child Endpoints
The ConnectWise API has many instances of nested endpoints - for example, ```/company/companies/{company_id}/sites```

This is replicated in the library. Endpoints provide an ```id``` method for setting the ID and traversing down the path.

###### Example using ```/company/companies/{company_id}/sites```
```python
sites = api.company.companies.id(250).sites.get()
```

# Pagination
The ConnectWise API paginates data for performance reasons through the ```page``` and ```pageSize``` query parameters. ```pageSize``` is limited to a maximum of 1000.

To make working with paginated data easy, Endpoints that implement a GET response with an array also supply a ```paginated()``` method. Under the hood this wraps a GET request, but does a lot of neat stuff to make working with pages easier.

Working with pagination
```python
# initialize a PaginatedResponse instance for /company/companies, starting on page 1 with a pageSize of 100
paginated_companies = api.company.companies.paginated(1,100)

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
