
# 0. Install AWS CLI & Docker

Reference:

+ Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
+ Install Docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04


# 1. Configure AWS Account [AWS]

aws configure --profile=demo_ctai_qa

export AWS_PROFILE=demo_ctai_qa


# 2. Build Docker Image [LOCAL]

docker build --platform linux/amd64 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest -f Dockerfile .



# 3. Test Locally

docker run -p 9000:8080 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest




# 4. Push Docker Image to ECR service [AWS]


aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com

aws ecr create-repository --repository-name aws-lambda-scikit-learn --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

docker push 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest
