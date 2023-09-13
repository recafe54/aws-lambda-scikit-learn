docker build --platform linux/amd64 -t docker-image:test .

export AWS_PROFILE=qa_devops1


aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com


aws ecr create-repository --repository-name aws-lambda-scikit-learn --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE


docker tag docker-image:test 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest


docker build --platform linux/amd64 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest -f Dockerfile .


docker push 785385202614.dkr.ecr.ap-southeast-1.amazonaws.com/aws-lambda-scikit-learn:latest
