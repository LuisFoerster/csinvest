def flatten_dict(d: dict):
    r = d.copy()
    for (k, v) in d.items():
        if isinstance(v, dict):
            r.update(v)
            r.pop(k)
    return r