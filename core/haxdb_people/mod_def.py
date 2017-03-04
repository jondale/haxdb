mod_def = {}

mod_def["PEOPLE"] = {
    "NAME": "PEOPLE",
    "TABLE": "PEOPLE",
    "ROWID": "PEOPLE_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "CATEGORY": "ROW",
         "NAME": "PEOPLE_ID",
         "HEADER": "ID",
         "TYPE": "INT",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "NEW": 0,
        },
        {
         "CATEGORY": "ROW",
         "NAME": "PEOPLE_INSERTED",
         "HEADER": "CREATED",
         "TYPE": "STR",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "CATEGORY": "PERSON",
         "NAME": "PEOPLE_NAME_FIRST",
         "HEADER": "FIRST",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
         "NEW": 1,
         "DEFAULT": 1,
        },
        {
         "CATEGORY": "PERSON",
         "NAME": "PEOPLE_NAME_LAST",
         "HEADER": "LAST",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
         "NEW": 1,
         "DEFAULT": 1,
        },
        {
         "CATEGORY": "PERSON",
         "NAME": "PEOPLE_EMAIL",
         "HEADER": "EMAIL",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
         "NEW": 1,
         "DEFAULT": 1,
        },
        {
         "CATEGORY": "PERSON",
         "NAME": "PEOPLE_DBA",
         "HEADER": "DBA",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "NEW": 1,
         "DEFAULT_VALUE": 0,
        },
        {
         "CATEGORY": "PERSON",
         "NAME": "PEOPLE_MEMBERSHIP",
         "HEADER": "MEMBERSHIP",
         "TYPE": "LIST",
         "LIST_NAME": "MEMBERSHIPS",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "NEW": 1,
         "DEFAULT": 1,
        },
    ],
    "ORDER": ["PEOPLE_NAME_LAST", "PEOPLE_NAME_FIRST"]
}