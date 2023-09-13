# Local Environment

## 1. Build Docker Image [Locally]

Build & Setup Local Server with port 8000:

```
docker build --platform linux/amd64 -t docker-image:test -f Dockerfile .
docker run -p 9000:8080 docker-image:test
```

## 2. Test Locally

Call API locally:

```
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

# Deploy Scikit-Learn model to Public API using AWS

## 1. Install AWS CLI & Docker

Reference:

+ Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  ```
  aws --version
  ```
+ Install Docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
  ```
  docker --version
  ```



## 2. Configure AWS Account [AWS]

Account Id:

```
785385202614
```

Configure new profile to use AWS CLI with above `Account Id`

```
aws configure --profile=demo_ctai_qa
```

Start using new profile

```
export AWS_PROFILE=demo_ctai_qa
```

## 3. Build ECR Docker Image 

Following format:

```
docker build --platform linux/amd64 -t <account_id>.dkr.ecr.<region-code>.amazonaws.com/aws-lambda-scikit-learn:latest -f Dockerfile .
```


Since `account_id` =  785385202614, our command:

```
docker build --platform linux/amd64 -t 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest -f Dockerfile .
```


## 4. Push Docker Image to ECR service (Docker Hub host by AWS)

Make sure using profile with granted permission:

```
export AWS_PROFILE=demo_ctai_qa

```


Login to Docker Hub with AWS credential:

```
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com
```


Push image to Docker Hub:

```
docker push 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest
```
