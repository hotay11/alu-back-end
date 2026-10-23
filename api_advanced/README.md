# Reddit API Advanced

Python functions that query the [Reddit API](https://www.reddit.com/dev/api/)
to get subreddit information. No authentication is needed for these features,
but every request sets a custom `User-Agent` so Reddit does not block it with
a "Too Many Requests" error.

## Learning Objectives

- How to read API documentation to find the endpoints you need
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements

- Ubuntu with python3
- The `requests` module: `pip3 install requests`
- Code follows the PEP 8 style (`pycodestyle`)
- All files are executable and start with `#!/usr/bin/python3`
- Every module has a docstring
- Dictionary values are accessed with `get`
- Redirects are never followed (`allow_redirects=False`), because an invalid
  subreddit can redirect to search results
- Allowed editors: `vi`, `vim`, `emacs`

## Files

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the total number of subscribers, or `0` if the subreddit is invalid |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or `None` if the subreddit is invalid |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` recursively returns a list of all hot post titles, or `None` if there are no results |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keywords in hot post titles and prints them sorted |

## Usage

The functions are meant to be imported by a main file. Example for task 0:

```python
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    print("{:d}".format(number_of_subscribers(sys.argv[1])))
```

```
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

### 0-subs.py

Returns the number of total subscribers (not active users). Returns `0` for
an invalid subreddit.

### 1-top_ten.py

```
$ python3 1-main.py programming
Title of hot post 1
Title of hot post 2
...
$ python3 1-main.py this_is_a_fake_subreddit
None
```

### 2-recurse.py

Uses pagination (the `after` value) and calls itself until every page has been
read.

```
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
```

### 3-count.py

Counts keywords (case-insensitive, whole words only) in all hot post titles.
Results are sorted by count (highest first), then alphabetically. Words with
no matches are not printed, and nothing is printed for an invalid subreddit.

```
$ python3 3-main.py programming 'react python java javascript scala'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
```

The numbers change over time because Reddit's hot posts change.

## Author

Your Name - [GitHub](https://github.com/YOUR_USERNAME)
