indexMapping = {
    "properties": {
        "ProductID": {"type": "long"},
        "ProductName": {"type": "text"},
        "ProductBrand": {"type": "text"},
        "Product": {"type": "long"},
        "Gender": {"type": "text"},
        "Price (INR)": {"type": "long"},
        "NumImages": {"type": "long"},
        "Description": {"type": "text"},
        "PrimaryColor": {"type": "text"},
        "DescriptionVector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "l2_norm",
        },
    }
}
