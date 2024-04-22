import gitlab

gitlab_client = gitlab.Gitlab.from_config("global", [".python-gitlab.cfg"])
project_ids = []
long_living_branches = []

if __name__ == "__main__":
    for project_id in project_ids:
        g_project = gitlab_client.projects.get(project_id)
        g_jobs = g_project.jobs.list(all=True)

        g_filtered_jobs = list(filter(
            lambda job: job.ref in long_living_branches and job.stage == "static-analysis" and job.status == "success",
            g_jobs))

        job_ids = ""
        for g_job in g_filtered_jobs:
            job_ids += (str(g_job.id) + ",")

            with open("data/" + str(project_id) + "/" + str(g_job.id) + ".log", "wb") as file:
                g_job.trace(streamed=True, action=file.write)

        with open("data/" + str(project_id) + "/job_ids.txt", "w") as file:
            file.write(job_ids[:-1])
