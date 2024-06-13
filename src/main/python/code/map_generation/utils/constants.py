def get_crs(which='default'):
    crs = 'epsg:4326'
    if which == 'default':
        crs = 'EPSG:26916'
    print(f"crs is set to {crs}")
    return crs
    