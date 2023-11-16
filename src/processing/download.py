import cbsodata


def download_data(
    table_id,
    dir=None,
    typed=False,
    select=None,
    filters=None,
    catalog_url=None,
    **kwargs,
):
    cbsodata.download_data(table_id, dir, typed, select, filters, catalog_url, **kwargs)


if __name__ == "__main__":
    download_data("83131NED", dir="data/consumenten-prijs-index", typed=True)