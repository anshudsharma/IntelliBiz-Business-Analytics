from ml.churn_prediction import ChurnPrediction


def test_churn_prediction():

    churn = ChurnPrediction()

    company_id = 1

    data = churn.prepare_churn_data(
        company_id
    )

    print(
        "\n===== CUSTOMER DATA ====="
    )

    print(data.head())

    print(
        "\nTotal Customers:"
    )

    print(len(data))



    print(
        "\n===== CHURN DATA ====="
    )

    print(
        data[
            [
                "customer_id",
                "days_since_last_purchase",
                "churn"
            ]
        ].head()
    )

    print(
        "\n===== CHURN DISTRIBUTION ====="
    )

    print(
        data["churn"].value_counts()
    )






    trained_model = (
        churn.train_model(
            company_id
        )
    )

    print(
        "\n===== MODEL RESULTS ====="
    )

    print(
        f"Accuracy: "
        f"{trained_model['accuracy']}%"
    )

    print(
        "\n===== CONFUSION MATRIX ====="
    )

    print(
        trained_model["confusion_matrix"]
    )
    
    print(
        "\n===== CHURN RISK SUMMARY ====="
    )

    risk_summary = (
        churn.predict_churn_risk(
            company_id
        )
    )

    for key, value in risk_summary.items():
        print(f"{key}: {value}")





if __name__ == "__main__":
    test_churn_prediction()