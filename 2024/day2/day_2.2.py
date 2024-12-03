import copy

reports = open('main.txt').read().splitlines()
safe_reports = 0


def requirement_1(report) -> bool:
    sorted_report = sorted(report)
    backwards_report = list(reversed(sorted_report))

    if sorted_report == report or backwards_report == report:
        return True
    else:
        return False


def requirement_2(report) -> bool:
    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) in [1,2,3]:
            pass
        else:
            return False
    else:
        return True


for report in reports:
    req1 = False
    req2 = False
    req1_problem = False

    report = [int(x) for x in report.split()]

    # // See if base report is safe without any changes
    if requirement_1(report) and requirement_2(report):
        safe_reports += 1
        continue

    # // Remove levels from the report
    for i in range(len(report)):
        new_report = copy.copy(report)
        new_report.pop(i)

        if requirement_1(new_report) and requirement_2(new_report):
            safe_reports += 1
            break

print(safe_reports)
