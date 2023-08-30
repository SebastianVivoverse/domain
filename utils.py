def url_to_id(url):
    if url is not None:
        return int(url.split("/")[-2])
    return None
