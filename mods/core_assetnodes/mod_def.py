mod_def = {}

mod_def["ASSETNODE"] = {
    "NAME": "ASSETNODE",
    "TABLE": "ASSETNODE",
    "PARENT_TABLE": None,
    "ROWID": None,   #remove
    "ROW_NAME": "ASSETNODE_NAME",
    "DEFAULT_COLS": ["ASSETNODE_NAME",
                     "ASSETNODE_TIMEOUT",
                     "ASSETNODE_ASSETS_ID"],
    "UDF": {
        "CHAR": 10,
    },
    "ORDER": ["ASSETNODE_NAME"],
    "INDEX": [["ASSETNODE_ASSETS_ID"]],
    "UNIQUE": [["ASSETNODE_NODES_ID"]],
    "COLS": [
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_NAME",
            "HEADER": "NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "INTERNAL": 0,
            "DEFAULT": None,
            "NEW": 1,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_DESCRIPTION",
            "HEADER": "DESCRIPTION",
            "TYPE": "TEXT",
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_ASSETS_ID",
            "HEADER": "ASSET",
            "TYPE": "ID",
            "ID": "ASSETS",
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_NODES_ID",
            "HEADER": "NODE",
            "TYPE": "ID",
            "ID": "NODES",
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR0_NAME",
            "HEADER": "SENSOR0 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR0 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR0_VAL",
            "HEADER": "SENSOR0 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
            {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR1_NAME",
            "HEADER": "SENSOR1 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR1 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR1_VAL",
            "HEADER": "SENSOR1 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR2_NAME",
            "HEADER": "SENSOR2 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR2 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR2_VAL",
            "HEADER": "SENSOR2 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR3_NAME",
            "HEADER": "SENSOR3 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR3 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR3_VAL",
            "HEADER": "SENSOR3 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR4_NAME",
            "HEADER": "SENSOR4 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR4 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR4_VAL",
            "HEADER": "SENSOR4 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR5_NAME",
            "HEADER": "SENSOR5 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR5 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR5_VAL",
            "HEADER": "SENSOR5 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR6_NAME",
            "HEADER": "SENSOR6 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR6 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR6_VAL",
            "HEADER": "SENSOR6 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR7_NAME",
            "HEADER": "SENSOR7 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR7 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR7_VAL",
            "HEADER": "SENSOR7 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR8_NAME",
            "HEADER": "SENSOR8 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR8 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR8_VAL",
            "HEADER": "SENSOR8 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR9_NAME",
            "HEADER": "SENSOR9 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR9 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR9_VAL",
            "HEADER": "SENSOR9 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR1_NAME",
            "HEADER": "SENSOR1 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR1 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR1_VAL",
            "HEADER": "SENSOR1 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR2_NAME",
            "HEADER": "SENSOR2 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR2 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR2_VAL",
            "HEADER": "SENSOR2 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR3_NAME",
            "HEADER": "SENSOR3 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR3 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR3_VAL",
            "HEADER": "SENSOR3 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR4_NAME",
            "HEADER": "SENSOR4 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR4 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR4_VAL",
            "HEADER": "SENSOR4 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR5_NAME",
            "HEADER": "SENSOR5 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR5 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR5_VAL",
            "HEADER": "SENSOR5 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR6_NAME",
            "HEADER": "SENSOR6 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR6 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR6_VAL",
            "HEADER": "SENSOR6 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR7_NAME",
            "HEADER": "SENSOR7 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR7 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR7_VAL",
            "HEADER": "SENSOR7 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR8_NAME",
            "HEADER": "SENSOR8 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR8 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR8_VAL",
            "HEADER": "SENSOR8 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR9_NAME",
            "HEADER": "SENSOR9 NAME",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": "SENSOR9 NAME",
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
        {
            "CATEGORY": "NODE",
            "NAME": "ASSETNODE_SENSOR9_VAL",
            "HEADER": "SENSOR9 VALUE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 1,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 0,
            "INTERNAL": 0,
            "DEFAULT": 0.0,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 500,
            }
        },
    ]

}
