import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "all_products"

try:
    es = Elasticsearch(
        hosts=["https://127.0.0.1:9200"],
        basic_auth=("elastic", "4151491"),
        ca_certs="C:\\Users\\LENOVO\\Downloads\\elasticsearch-8.11.3\\config\\certs\\http_ca.crt",
    )
except ConnectionAbortedError as e:
    print("connection Error:", e)

if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("oops! can not connect to ElasticSearch")


def search(input_keyword):
    model = SentenceTransformer("all-mpnet-base-v2")
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "DescriptionVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 500,
    }

    res = es.knn_search(
        index=indexName, knn=query, source=["ProductName", "Description"]
    )
    results = res["hits"]["hits"]
    return results


def main():
    st.title("Search Myntra Fashion Products")
    # input: User enters search query
    search_query = st.text_input("Enter your search query")
    
    # Button: User triggers the search
    if st.button("search"):
        if search_query:
            # perform the search and get results
            results = search(search_query)

            # display search results
            st.subheader("Search Results")

            for result in results:
                with st.container():
                    if "_source" in result:
                        print(result)
                        try:
                            st.header(f"{result['_source']['ProductName']}")
                        except Exception as e:
                            print(e)

                        try:
                            st.write(f"Description: {result['_source']['Description']}")
                        except Exception as e:
                            print(e)
                        st.divider()


if __name__ == "__main__":
    main()
