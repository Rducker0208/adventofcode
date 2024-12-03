reports = open('main.txt').read().splitlines()
safe_reports = 0

for report in reports:
    req1 = False
    req2 = True

    report = [int(x) for x in report.split()]
    sorted_report = sorted(report)
    backwards_report = list(reversed(sorted_report))

    if sorted_report == report or backwards_report == report:
        req1 = True

    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) in [1, 2, 3]:
            pass
        else:
            req2 = False
            break

    if req1 and req2:
        safe_reports += 1

print(safe_reports)
