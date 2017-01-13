mod_def = {}

mod_def["UDF"] = {
    "NAME": "UDF",
    "TABLE": "UDF",
    "ROWID": "UDF",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "UDF_CONTEXT",
         "HEADER": "CONTEXT",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "UDF_CONTEXT_ID",
         "HEADER": "CONTEXT_ID",
         "TYPE": "ID",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "UDF_CATEGORY",
         "HEADER": "CATEGORY",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "NAME": "UDF_NAME",
         "HEADER": "NAME",
         "TYPE": "CHAR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "NAME": "UDF_TYPE",
         "HEADER": "TYPE",
         "TYPE": "CHAR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "NAME": "UDF_LISTS_ID",
         "HEADER": "LIST",
         "TYPE": "ID",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "NAME": "UDF_ORDER",
         "HEADER": "ORDER",
         "TYPE": "FLOAT",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "NAME": "UDF_INTERNAL",
         "HEADER": "INTERNAL",
         "TYPE": "BOOL",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
    ],
    "ORDER": ["UDF_ORDER", "UDF_NAME"]
}
