import statistics

def get_grade(s1,s2,s3):
    d = {
        'F': [0,59],
        'D': [60,69],
        'C': [70,79],
        'B':[80,89],
        'A':[90,100]
    }
    mean_grade= (s1+s2+s3)/3
    for key, value in d.items():
        if value[0] <= int(mean_grade) <= value[1]:
            return key 