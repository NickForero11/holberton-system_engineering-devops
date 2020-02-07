# 0x16. API advanced

## Description

Learning objectives from this project:

* How to read API documentation to find the endpoints you’re looking for.
* How to use an API with pagination.
* How to parse JSON results from an API.
* How to make a recursive API call.
* How to sort a dictionary by value.

---

### [0. How many subs?](./0-subs.py)

* Python function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the Python function should return 0.

### [1. Top Ten](./1-top_ten.py)

* Python function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

### [2. Recurse it!](./2-recurse.py)

* Python function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the Python function should return None.

### [3. Count it!](./100-count.py)

* Python function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces: Javascript should count as javascript, but java should not).

  * Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically. Words with no matches should be skipped and not printed.
  * Results are based on the number of times a keyword appears, not titles it appears in. ‘java java java’ counts as 3 separate occurrences of java.
  * To make life easier, ‘java.’ or ‘java!’ or ‘java_’ should not count as ‘java’

---

## Author

* **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)
