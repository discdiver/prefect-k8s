from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    image="discdiver/prefect:py3.10-baked",
    image_pull_policy="Always",
)

k8s_job.save("k8s-flow", overwrite=True)
