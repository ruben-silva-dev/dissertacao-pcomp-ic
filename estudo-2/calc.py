import re

project_ids = ["55", "36", "78", "133", "41", "54", "56", "22", "26"]
issue_types = ["blocker", "critical", "major", "minor", "info"]


def calculate_reliability(log):
    reliability_matches = re.findall("Reliability Rating on New Code.+\\d+", log)

    if len(reliability_matches) > 0:
        reliability_text = reliability_matches[0]
        return re.findall("\\d+", reliability_text)[0]

    return 0


def calculate_security(log):
    security_matches = re.findall("Security Rating on New Code.+\\d+", log)

    if len(security_matches) > 0:
        security_text = security_matches[0]
        return re.findall("\\d+", security_text)[0]

    return 0


def calculate_maintainability(log):
    maintainability_matches = re.findall("Maintainability Rating on New Code.+\\d+", log)

    if len(maintainability_matches) > 0:
        maintainability_text = maintainability_matches[0]
        return re.findall("\\d+", maintainability_text)[0]

    return 0


def calculate_issues(log):
    issues_matches = re.findall("SonarQube reported QualityGate is.+", log)

    if len(issues_matches) > 0:
        issue_values = {}

        issues_text = issues_matches[0]
        issues = re.findall("\\d+ \\w+", issues_text)
        for issue in issues:
            issue_type = re.findall("[a-z]+", issue)[0]
            issue_value = re.findall("\\d+", issue)[0]
            if issue_type in issue_types:
                issue_values[issue_type] = issue_value

        return issue_values

    return {}


if __name__ == "__main__":
    projects = []

    for project_id in project_ids:
        project = {id: project_id}

        with open("data/" + project_id + "/job_ids.txt", "r") as file:
            job_ids = file.read().split(",")

        jobs = []
        for job_id in job_ids:
            job = {id: job_id}

            with open("data/" + project_id + "/" + job_id + ".log", "r") as file:
                log_file = file.read()

            job["reliability"] = calculate_reliability(log_file)

            if job["reliability"] == 0:
                continue

            job["security"] = calculate_security(log_file)
            job["maintainability"] = calculate_maintainability(log_file)
            job.update(calculate_issues(log_file))

            jobs.append(job)

        project["jobs"] = jobs
        projects.append(project)

    print("ksjbs")
