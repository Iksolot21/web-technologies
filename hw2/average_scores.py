def compute_average_scores(scores):
    num_students = len(scores[0])
    avg_scores = []
    for i in range(num_students):
        total = 0
        for subject_scores in scores:
            total += subject_scores[i]
        avg_scores.append(round(total / len(scores), 1))
    return tuple(avg_scores)

if __name__ == '__main__':
    N, X = map(int, input().split())
    scores = []
    for _ in range(X):
        scores.append(tuple(map(float, input().split())))

    avg_scores = compute_average_scores(scores)
    for score in avg_scores:
        print(score)