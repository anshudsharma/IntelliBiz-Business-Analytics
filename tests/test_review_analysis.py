from analytics.review_analysis import ReviewAnalysis

review = ReviewAnalysis()

print("\n===== AVERAGE REVIEW SCORE =====")
print(review.get_average_review_score())

print("\n===== REVIEW DISTRIBUTION =====")
print(review.get_review_distribution())

print("\n===== BEST RATED CATEGORIES =====")
print(review.get_best_rated_categories())


print("\n===== WORST RATED CATEGORIES =====")
print(review.get_worst_rated_categories())