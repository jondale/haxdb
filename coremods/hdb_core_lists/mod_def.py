mod_def = {}

mod_def["LISTS"] = {
    "NAME": "LISTS",
    "ROW_NAME": "LISTS_NAME",
    "NEW": 1,
    "UDF": 0,
    "ORDER": ["LISTS_NAME"],
    "INDEX": [],
    "UNIQUE": [["LISTS_NAME"]],
    "CLIENT": {
        "MAJOR": 0,
        "MINOR": 1,
        "PARENT": None,
        "ICON": "list"
    },
    "AUTH": {
        "READ": 0,
        "WRITE": 100,
        "INSERT": 100,
        "DELETE": 100,
    },
    "COLS": [
        {
            "CATEGORY": "LIST",
            "NAME": "LISTS_NAME",
            "HEADER": "NAME",
            "TYPE": "STR",
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "NEW": 1,
            "DEFAULT": None,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
    ],
    "CALLS": ["list", "view", "save", "new", "delete"]
}

mod_def["LIST_ITEMS"] = {
    "NAME": "LIST_ITEMS",
    "ROW_NAME": "LIST_ITEMS_NAME",
    "NEW": 1,
    "UDF": 5,
    "ORDER": ["LIST_ITEMS_LISTS_ID", "LIST_ITEMS_ORDER"],
    "INDEX": [],
    "UNIQUE": [["LIST_ITEMS_LISTS_ID", "LIST_ITEMS_NAME"]],
    "CLIENT": {
        "MAJOR": 0,
        "MINOR": 0,
        "PARENT": "LISTS",
        "ICON": "key"
    },
    "AUTH": {
        "READ": 0,
        "WRITE": 100,
        "INSERT": 100,
        "DELETE": 100,
    },
    "COLS": [
        {
            "CATEGORY": "LIST ITEM",
            "NAME": "LIST_ITEMS_LISTS_ID",
            "HEADER": "LIST",
            "TYPE": "ID",
            "API_ID": "LISTS",
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "NEW": 0,
            "DEFAULT": None,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "LIST ITEM",
            "NAME": "LIST_ITEMS_NAME",
            "HEADER": "NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "NEW": 1,
            "DEFAULT": None,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "LIST ITEM",
            "NAME": "LIST_ITEMS_VALUE",
            "HEADER": "VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "NEW": 1,
            "DEFAULT": None,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "LIST ITEM",
            "NAME": "LIST_ITEMS_ENABLED",
            "HEADER": "ENABLED",
            "TYPE": "BOOL",
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "NEW": 1,
            "DEFAULT": None,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "LIST ITEM",
            "NAME": "LIST_ITEMS_ORDER",
            "HEADER": "ORDER",
            "TYPE": "FLOAT",
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 1,
            "NEW": 0,
            "DEFAULT": 999.9,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
    ],
    "CALLS": ["list", "view", "save", "new", "delete"]
}