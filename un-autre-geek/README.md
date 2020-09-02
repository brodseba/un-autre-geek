# un-autre-geek

gcloud config set app/cloud_build_timeout 1200s
gcloud builds submit --tag gcr.io/un-autre-geek-dev/app-v2 --timeout=1200s
gcloud run deploy --image gcr.io/un-autre-geek-dev/app-v2 --platform managed --max-instances=1

gcloud builds submit