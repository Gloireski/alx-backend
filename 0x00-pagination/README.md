# 0x00-pagination

Learning Objectives:

* How to `paginate` a dataset with `simple page` and `page_size` parameters
* How to `paginate` a dataset with `hypermedia` metadata
* How to `paginate` in a `deletion-resilient` manner

## Files 

[0-simple_helper_function.py](./0-simple_helper_function.py)

Contains a function `index_range` that returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

[1-simple_pagination.py](./1-simple_pagination.py)

Containes an implemented method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.
