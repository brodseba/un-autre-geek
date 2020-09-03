# un-autre-geek


```bash
docker build -t gcr.io/un-autre-geek-dev/app-v2 .
docker push gcr.io/un-autre-geek-dev/app-v2
gcloud run deploy app-v2 --image=gcr.io/un-autre-geek-dev/app-v2 --region=northamerica-northeast1 --platform=managed --max-instances=1 --cpu=1 --memory=128Mi --allow-unauthenticated
```

```yaml
steps:
    # Build the container image
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '-t', 'gcr.io/un-autre-geek-dev/app-v2', '.']
    # Push the container image to Container Registry
    - name: 'gcr.io/cloud-builders/docker'
      args: ['push', 'gcr.io/un-autre-geek-dev/app-v2']
    # Deploy container image to Cloud Run
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      entrypoint: gcloud
      args: ['run', 'deploy', 'app-v2', '--image', 'gcr.io/un-autre-geek-dev/app-v2', '--region', 'northamerica-northeast1', '--platform', 'managed', '--max-instances', '1', '--cpu', '1', '--memory', '128Mi', '--allow-unauthenticated']
timeout: 1200s
images:
    - gcr.io/un-autre-geek-dev/app-v2
```