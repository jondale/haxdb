import base64

haxdb = None


def has_perm(table, perm_type, perm_val):
    if haxdb.session("api_dba") == 1:
        return True

    nodes_id = haxdb.session("nodes_id")
    sql = """
    SELECT * FROM NODESPERM WHERE
    NODESPERM_NODES_ID=%s
    AND NODESPERM_TABLE=%s
    """
    row = haxdb.db.qaf(sql, (nodes_id, table))
    typecol = "NODESPERM_{}".format(perm_type)

    try:
        if int(perm_val) <= int(row[typeocl]):
            return True
    except Exception:
        return False
    return False


def init(app_haxdb):
    global haxdb
    haxdb = app_haxdb


def run():
    haxdb.func("PERM:HAS", has_perm)