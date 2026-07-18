from ml.sales_forecasting import SalesForecasting


def test_sales_forecasting():

    forecast = SalesForecasting()

    company_id = 1

    monthly_revenue = (
        forecast.get_monthly_revenue(
            company_id
        )
    )

    training_data = (
        forecast.prepare_training_data(
            company_id
        )
    )

    trained_model = (
        forecast.train_model(
            company_id
        )
    )

    print("\n===== MONTHLY REVENUE =====")
    print(monthly_revenue)

    print("\n===== TRAINING DATA =====")
    print(training_data)

    print("\nTotal Training Months:")
    print(len(training_data))

    print("\n===== MODEL RESULTS =====")
    print(
        f"Accuracy: "
        f"{trained_model['accuracy']}%"
    )

    forecast_result = (
        forecast.forecast_next_month(
            company_id
        )
    )

    print(
        "\n===== NEXT MONTH FORECAST ====="
    )

    print(
        f"Predicted Revenue: "
        f"${forecast_result['predicted_revenue']:,.2f}"
    )

    print(
        f"Model Accuracy: "
        f"{forecast_result['accuracy']}%"
    )




    saved_forecast = (
        forecast.save_prediction(
            company_id
        )
    )

    print("\n===== SAVED FORECAST =====")
    print(saved_forecast)

    
if __name__ == "__main__":
    test_sales_forecasting()