def calculate_feedback(ratings):
    if len(ratings) == 0:
        return 0
    positive_feedback = sum(1 for rating in ratings if rating >= 4)
    return (positive_feedback / len(ratings)) * 100

# input 
ratings = [5, 4, 3, 5, 2, 4, 1, 5]

# calculate positive feedback percentage
positive_feedback_percentage = calculate_feedback(ratings)
print(f"Positive Feedback: {positive_feedback_percentage}%")
