********
Requests
********

There are more pages on the web than people on Earth. And while I have not
checked, I am sure each on is full of original, high quality content that would
make our ancestors proud.

Most people access web pages through a browser, but as programmers we have other
methods... Today, we will learn how to use Python to send GET requests to web
servers, and then parse the response. This way, you can write software to read
websites for you, giving you more time to [...] browse the internet.

.. topic:: URL

    In a browser, you access a web page by typing the *URL* in the address bar.
    URL stands for **Uniform Resource Locator** and this string can hold a lot
    of information, for example:
    ``https://en.wikipedia.org/wiki/Pythonidae?filter=none&select=42#Relationship_with_humans``
    contains the following components:

    - Protocol: ``https``
    - Hostname: ``en.wikipedia.org``
    - Path: ``wiki/Pythonidae``
    - Querystring: ``?filter=none&select=42``
    - Fragment: ``#Relationship_with_humans``


The ``requests`` library is the de facto standard for making HTTP requests in
Python. It hides the complexities of making requests behind a beautiful and
simple API, so you can focus on interacting with services and consuming data in
your application.

.. seealso::

    Though I’ve tried to include as much information as you need to understand
    the features and examples included in this lesson, I do assume a very `basic
    general knowledge of HTTP requests
    <https://www.w3schools.com/tags/ref_httpmethods.asp>`_.


Getting started
###############

Let's begin by installing the ``requests`` module. To do so, run the following
command:

.. code-block:: console

    macbook$ pip install requests

Once installed, please check the installation by trying to import the module in
your python console:

    >>> import requests
    >>>

If Python does not report any error it means you're all set, and it is time to
begin your journey through web.


The GET request
###############

`HTTP methods<https://www.w3schools.com/tags/ref_httpmethods.asp>`_ such as GET
and POST, determine what kind of action you want the web server to perform. One
of the most common methods is **GET**. This indicates that you want to retrieve
data from a specified location (or resource). To make such a request in your
application all you need is calling ``requests.get()`` and specifying a URL (or
an address).

To test this out, let's make a request to GitHub's root API:

    >>> requests.get('https://api.github.com')
    <Response [200]>
    >>>

This is it. You've made your first request. Notice that we got a ``<Response [200]>`` message
which is the representation of a response object with code *200* (the http
numeric code for success).


The Response
############

A *Response* is a powerful object for inspecting the results of the request.
Let’s make that same request again, but this time store the return value in a
variable so that you can get a closer look at its attributes and behaviors:

    >>> response = requests.get('https://api.github.com')
    >>>

Status Code
***********

The first bit of information that you can gather from **Response** is the
**status code**. A status code informs you of the status of the request.

For example, a **200** status means that your request was successful, whereas a
**404** status means that the resource you were looking for was *not found*.
There are many other `possible status codes
<https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`_ as well to give you
specific insights into what happened with your request.

Sometimes, you might want to use this information to make decisions in your code:

.. code-block:: python

    if response.status_code == 200:
        print("Request completed successfully.")
    elif response.status_code == 404:
        print("Resource not found.")
    elif response.status_code == 500:
        print("The server reported an internal error. Please try again later.")


The **requests** module goes one step further in simplifying this process for
you. If you use a **Response** object in a conditional expression, it will
evaluate to *True* if the status code was between 200 and 400, and *False*
otherwise. Therefore you can simplify the last example to:

.. code-block:: python

    if response:
        print("Request completed successfully.")
    else:
        print(f"Request has failed, with code {response.status_code}.")

Keep in mind that this method is not verifying that the status code is equal to
**200**. The reason for this is that other status codes within the 200 to 400
range, such as **204 NO CONTENT** and **304 NOT MODIFIED**, are also considered
successful in the sense that they provide some workable response. For example,
the 204 tells you that the response was successful, but there’s no content to
return in the message body.

So, make sure you use this convenient shorthand only if you want to know if the
request was generally successful and then, if necessary, handle the response
appropriately based on the status code.


Content
*******

Now, you know a lot about how to deal with the status code of the response you
got back from the server. However, when you make a GET request, you rarely only
care about the status code of the response. Usually, you want to see more.

The response of a GET request often has some valuable information, known as a
payload, in the message body. Using the attributes and methods of Response, you
can view the payload in a variety of different formats.

To see the response’s content in bytes, you use ``.content`` attribute:

    >>> response = requests.get('https://api.github.com')
    >>> response.content
    b'{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","notifications_url":"https://api.github.com/notifications","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_url":"https://api.github.com/orgs/{org}","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'
    >>>

While ``.content`` gives you access to the raw bytes of the response payload,
you will often want to convert them into a string using a character encoding
such as **UTF-8**. ``response`` will do that for you when you access ``.text``:

    >>> response.text
    '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'
    >>>

Because the decoding of *bytes* to a *string* requires an encoding scheme,
requests will try to guess the encoding based on the response’s headers if you
do not specify one. You can provide an explicit encoding by setting ``.encoding``
before accessing ``.text`` attribute:

    >>> response.encoding = 'utf-8' # Optional: requests infers this internally
    >>> response.text
    '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'
    >>>

If you take a look at the response, you’ll see that it is actually serialized
JSON content. To get a dictionary, you could take the string you retrieved from
``.text`` and deserialize it using ``json.loads()``. However, a simpler way to
accomplish this task is to use ``.json()``:

    >>> response.json()
    {'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}', 'notifications_url': 'https://api.github.com/notifications', 'organization_url': 'https://api.github.com/orgs/{org}', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_teams_url': 'https://api.github.com/orgs/{org}/teams', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}
    >>> response.json()["current_user_url"]
    'https://api.github.com/user'
    >>> response.json()["events_url"]
    'https://api.github.com/events'
    >>>

The type of the return value of ``.json()`` is a *dictionary*, so you can access
values in the object by key.


Headers
*******

You can do a lot with status codes and message bodies. But, if you need more
information, like metadata about the response itself, you’ll need to look at the
response’s headers. They contain a lot of useful information, such as the
*content type* of the response payload and a time limit on how long to cache the
response. To view these headers, access the ``.headers`` attribute:

    >>> response.headers
    {'Server': 'GitHub.com', 'Date': 'Fri, 04 Jun 2021 07:42:54 GMT', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With', 'ETag': '"27278c3efffccc4a7be1bf315653b901b14f2989b2c2600d7cc2e90a97ffbf60"', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Type': 'application/json; charset=utf-8', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Content-Encoding': 'gzip', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '59', 'X-RateLimit-Reset': '1622796180', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Used': '1', 'Accept-Ranges': 'bytes', 'Content-Length': '496', 'X-GitHub-Request-Id': 'C416:12E42:3B33FEF:3C4A8B7:60B9D984'}
    >>>

``.headers`` returns a dictionary-like object, allowing you to access header
values by key. For example, to see the content type of the response payload, you
can access ``Content-Type`` key:

    >>> response.headers["Content-Type"]
    'application/json; charset=utf-8'
    >>>

There is something special about this dictionary-like headers object, though.
The HTTP specifications defines headers to be case-insensitive, which means we
are able to access these headers without worrying about their capitalization:

    >>> response.headers["content-type"]
    'application/json; charset=utf-8'
    >>>

Whether you use the key **content-type** or **Content-Type** key, you will get
the same value.

Now, you’ve learned the basics about Response. You’ve seen its most useful
attributes and methods in action. Let’s take a step back and see how your
responses change when you customize your GET requests.


QueryString parameters
######################

One common way to customize a GET request is to pass values through query string
parameters in the URL. To do this using ``get()``, you pass data through params
argument. For example, you can use GitHub’s Search API to look for the requests
library:

.. literalinclude:: ../examples/web_requests.py
    :language: python
    :emphasize-lines: 6

.. code-block:: console

    macbook$ python3 web_requests.py
    Repository name: grequests
    Repository description: Requests + Gevent = <3
    macbook$ _

By passing the dictionary ``{"q": "requests+language:python"}`` to the **params**
argument of ``.get()``, you are able to modify the results that come back from
the Search API.

You can pass params to **get()** in the form of a dictionary, as you have just
done, or as a list of tuples:


Other HTTP Methods
##################

Aside from GET, other popular HTTP methods include POST, PUT, DELETE, HEAD,
PATCH, and OPTIONS. **requests** provides a method, with a similar signature to
**get()**, for each of these HTTP methods:

    >>> requests.post('https://httpbin.org/post', data={'key':'value'})
    >>> requests.put('https://httpbin.org/put', data={'key':'value'})
    >>> requests.delete('https://httpbin.org/delete')
    >>> requests.head('https://httpbin.org/get')
    >>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
    >>> requests.options('https://httpbin.org/get')

Each function call makes a request to the *httpbin service* using the
corresponding HTTP method. For each method, you can inspect their responses in
the same way you did before:

    >>> response = requests.head('https://httpbin.org/get')
    >>> response.headers['Content-Type']
    'application/json'

    >>> response = requests.delete('https://httpbin.org/delete')
    >>> json_response = response.json()
    >>> json_response['args']
    {}

Headers, response bodies, status codes, and more are returned in the Response
for each method.

.. sidebar:: httpbin.org

    **httpbin.org** is a great resource created by the author of requests,
    `Kenneth Reitz<https://kenreitz.org/>`_. It’s a service that accepts test
    requests and responds with data about the requests


The Message Body
****************

According to the HTTP specification, POST, PUT, and the less common PATCH
requests pass their data through the message body rather than through parameters
in the query string. Using requests, you’ll pass the payload to the
corresponding function’s data parameter.

The ``data`` argument takes a *dictionary*, a *list of tuples*, *bytes*, or a
*file-like object*. You’ll want to adapt the data you send in the body of your
request to the specific needs of the service you’re interacting with.

For example, if your request’s content type is
``application/x-www-form-urlencoded``, you can send the form data as a
dictionary, but also as a list of tuples:

    >>> requests.post('https://httpbin.org/post', data={'key':'value'})
    <Response [200]>
    >>> requests.post('https://httpbin.org/post', data=[('key', 'value')])
    <Response [200]>
    >>>

If, however, you need to send JSON data, you can use the ``json`` parameter.
When you pass JSON data via ``json``, requests will serialize your data and add
the correct **Content-Type** header for you.

    >>> response = requests.post('https://httpbin.org/post', json={'key':'value'})
    >>> json_response = response.json()
    >>> json_response['data']
    '{"key": "value"}'
    >>> json_response['headers']['Content-Type']
    'application/json'
    >>
