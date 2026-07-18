from ml.customer_segmentation import CustomerSegmentation


def test_customer_segmentation():

    segmentation = CustomerSegmentation()

    company_id = 1

    customer_data = (
        segmentation.get_customer_data(
            company_id
        )
    )

    print(
        "\n===== CUSTOMER DATA ====="
    )

    print(customer_data.head())

    print(
        "\nTotal Customers:"
    )

    print(len(customer_data))







    segmented_data = (
        segmentation.segment_customers(
            company_id
        )
    )

    print(
        "\n===== CUSTOMER SEGMENTS ====="
    )

    print(
        segmented_data.head()
    )

    print(
        "\nCluster Distribution:"
    )

    print(
        segmented_data[
            "cluster"
        ].value_counts()
    )




    cluster_analysis = (
        segmentation.analyze_clusters(
            company_id
        )
    )

    print(
        "\n===== CLUSTER ANALYSIS ====="
    )

    print(cluster_analysis)
if __name__ == "__main__":
    test_customer_segmentation()