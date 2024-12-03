import statistics

def get_grade(s1,s2,s3):
    mean_grade= statistics.mean(s1,s2,s3)
    if 90 <= mean_grade <= 100:
        return 'A'
    else:
        return 'works' 