from ai.advisory import AIAdvisor


def test_ai_advisor():

    advisor = AIAdvisor()

    report = (
        advisor.generate_recommendations(
            1
        )
    )


    print(
        "\n===== AI ADVISOR REPORT =====\n"
    )

    print(report)


if __name__ == "__main__":
    test_ai_advisor()
