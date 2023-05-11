# Cure
Cure is dedicated to providing information on diabetes and the latest technology for early diagnosis through retina scans. Our mission is to help individuals understand the importance of early detection and provide them with the tools and resources they need to take control of their health. In addition to our expertise in retina scans, we offer a range of features to support individuals with diabetes, including educational resources, personalized health tracking tools, and access to a community of experts. Whether you are looking to learn more about the disease, or manage your health, we are here to help. Thank you for visiting Cure, and we hope you find the information and features here useful.

# Technologies Used
Cure was built using the following technologies:

- HTML
- CSS
- JavaScript
- Django
- Docker
- Terraform
- Kubernetes
- AWS
- Python
- Machine Learning
- Deep Learning


# Installation
To install Cure, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using pip by running **pip install -r requirements.txt** in your command line.
3. Run the database migrations by running **python manage.py makemigrations** followed by **python manage.py migrate**.
4. Start the development server by running **python manage.py runserver 0.0.0.0:8000**.
5. You can also run the Docker container by running **docker build -t app .** followed by **docker run -d -p 8000:8000 app**.


# Usage
To use Cure, open a web browser and navigate to **http://localhost:8000/**. From there, you can access the various features, including educational resources, health tracking tools, and the retina scan feature.

# Deployment to Production
To deploy your application to production, you can use Terraform to create the necessary infrastructure resources on AWS.

1. Create an AWS account if you haven't already done so.
2. Clone the repository to your local machine.
3. Navigate to the **terraform** directory.
4. edit **image** with your docker image in ecs task.
5. Run **terraform init** to initialize the Terraform environment.
6. Run **terraform apply** to create the infrastructure resources on AWS. This will create a VPC, two subnets, two ECS Fargate tasks, and an Application Load Balancer.
It will also pull the latest image from your Docker Hub repository and deploy it to the Fargate tasks.
7. Once the infrastructure resources are created, you can view your application by going to the URL of the Application Load Balancer.
You can find this URL in the Terraform output.
The output should look something like this: load_balancer_url = "http://my-load-balancer-1234567890.us-west-2.elb.amazonaws.com"

Note: Don't forget to destroy the Terraform resources when you're done testing to avoid incurring unnecessary costs. You can do this by running **terraform destroy**.


![GRADUATION (1)](https://github.com/abdelrhmanawidaa/grad-proj/assets/108242922/5252fc8b-2670-455f-8317-9381e6a8e621)


# Contributing
We welcome contributions to Cure. If you would like to contribute, please feel free to fork the repository and submit a pull request. You can also contribute by reporting bugs or suggesting new features.


# Acknowledgements
We would like to thank the following team mates for their contributions to this project:

**Abdelrhman Adel** -
**Sohila Khaled** -
**Esraa Abdallah** -
**Shady Mohammed** -
**Salma Ashraf** -
**Abdelrhman Kamal** -
**Meran Ehab** -
**Seif Eleslam** 


# License

This project is licensed under the GNU General Public License (GPL) version 3.0. 

The GPL is a copyleft license that ensures the freedom to use, modify, and distribute the software and any derived works. It requires that if you distribute copies of the software or modify it, you must make the corresponding source code available under the GPL as well. This license promotes the principles of open source software and aims to protect the rights of users and developers.

For detailed information about the GPL license terms and conditions, please refer to the [LICENSE](./LICENSE) file.

By using this project, you agree to comply with the terms and conditions of the GPL license.

