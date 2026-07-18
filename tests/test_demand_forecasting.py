from ml.category_level_demand_forecasting import DemandForecasting


def test_demand_forecasting():

    demand = DemandForecasting()

    company_id = 1

    data = (
        demand.get_monthly_category_demand(
            company_id
        )
    )

    print(
        "\n===== MONTHLY CATEGORY DEMAND ====="
    )

    print(data.head())

    print(
        "\nTotal Records:"
    )

    print(len(data))

    training_data = (
        demand.prepare_training_data(
            company_id
        )
    )

    print(
        "\n===== TRAINING DATA ====="
    )

    print(
        training_data.head()
    )

    print(
        "\nTotal Training Records:"
    )

    print(
        len(training_data)
    )

    print(
        "\n===== DEMAND DISTRIBUTION ====="
    )

    print(
        training_data[
            "total_quantity"
        ].describe()
    )

    trained_model = (
        demand.train_model(
            company_id
        )
    )

    print(
        "\n===== MODEL RESULTS ====="
    )

    print(
        f"R² Score: "
        f"{trained_model['accuracy']}%"
    )


    print("\n===== DEMAND FORECAST SUMMARY =====")

    forecast = demand.forecast_demand(company_id)

    for key, value in forecast.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    test_demand_forecasting()