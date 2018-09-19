def build(args):
    query = " where 1 = 1"
    for key in args.keys():
        query +=" and " + key + " = '" + str(args[key]) + "'"
    return query