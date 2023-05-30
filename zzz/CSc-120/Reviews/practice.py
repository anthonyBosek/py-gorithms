my_catalog = {
    "MIS": {"mis 101": 4, "mis 102": 3, "mis 202": 2},
    "CSC": {"csc 110": 4, "csc 120": 4, "csc 352": 3},
    "ECE": {"ece111": 3, "ece 222": 3, "ece 333": 4},
}


def find_courses(catalog, units):
    courses = []
    for dep in catalog:
        for course in catalog[dep]:
            if catalog[dep][course] == units:
                courses.append(course)
    return sorted(courses)


print(find_courses(my_catalog, 2))
print(find_courses(my_catalog, 3))
print(find_courses(my_catalog, 4))
