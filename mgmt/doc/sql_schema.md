## SQL Schema Example

```
Host
    --------------------------------------------------------------------
   | index    | host               | type           | state   | health  |
   | <serial> | <text>             | <text>         | <text>  | <text>  |   
   |          | PRIMARY            |                |         |         |   
    --------------------------------------------------------------------
   | 0        | 10.10.127.100:5000 | Crawler        | waiting | healthy |
   | 1        | 10.10.127.101:5000 | Index Builider | offline | failure |
   | 2        | 10.10.127.102:5000 | Index Server   | online  | healthy |
    --------------------------------------------------------------------

Crawler
    -------------------------------------------------------
   | index    | chunk_id | C_host             | C_task     |
   | <serial> | <int>    | <text>             | <text>     |
   |          | PRIMARY  | REF                |            | 
    -------------------------------------------------------
   | 0        | 100      | 10.10.127.100:5000 | crawling   |
   | 1        | 101      | 10.10.127.100:5000 | crawled    | 
   | 2        | 102      | 10.10.127.100:5000 | propagated | 
    -------------------------------------------------------

Index Builder
    -------------------------------------------------------
   | index    | chunk_id | IB_host            | IB_task    | 
   | <serial> | <int>    | <text>             | <text>     | 
   |          | REF      | REF                |            |
    -------------------------------------------------------
   | 0        | 100      | 10.10.127.101:5000 | building   |
   | 1        | 101      | 10.10.127.101:5000 | built      |
   | 2        | 102      | 10.10.127.101:5000 | propagated |
    ----------------------------------------------------

Index Server
    --------------------------------------------------
   | index    | row   | chunk_id | IS's host          | 
   | <serial> | <int> | <int>    | <text>             | 
   | PRIMARY  |       | REF      | REF                |
    --------------------------------------------------
   | 0        | 1     | 100      | 10.10.127.102:5000 |
   | 1        | 1     | 101      | 10.10.127.102:5000 |
   | 2        | 1     | 102      | 10.10.127.102:5000 |
    --------------------------------------------------
```