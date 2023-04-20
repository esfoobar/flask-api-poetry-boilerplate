"""
Utilities for the API
"""


def paginate_metadata_object(data_query):
    """
    Generate the paginate metadata for the response
    """

    # get the total number of pages
    total_pages = data_query.pages

    # get the next page number
    next_page = data_query.next_num if data_query.has_next else None

    # get the previous page number
    prev_page = data_query.prev_num if data_query.has_prev else None

    metadata = {"total_pages": total_pages}

    if next_page:
        metadata["next_page"] = next_page

    if prev_page:
        metadata["prev_page"] = prev_page

    return metadata
