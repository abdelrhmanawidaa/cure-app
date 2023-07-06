
resource "aws_ecs_cluster" "my_cluster" {
  name = "app-cluster" 
}

resource "aws_ecs_task_definition" "app_task" {
  family                   = "app-first-task" 
  container_definitions    = <<DEFINITION
  [
    {
      "name": "app-first-task",
      "image": "abdelrhmanawidaa/graduation-app:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8000,
          "hostPort": 8000
        }
      ],
      "memory": 8192,
      "cpu": 4096
    }
  ]
  DEFINITION
  requires_compatibilities = ["FARGATE"] # use Fargate as the launch type
  network_mode             = "awsvpc"    # add the AWS VPN network mode as this is required for Fargate
  memory                   = 8192         # Specify the memory the container requires
  cpu                      = 4096         # Specify the CPU the container requires
  execution_role_arn       = "${aws_iam_role.ecsTaskExecutionRole.arn}"
}


resource "aws_iam_role" "ecsTaskExecutionRole" {
  name               = "ecsTaskExecutionRole"
  assume_role_policy = "${data.aws_iam_policy_document.assume_role_policy.json}"
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecsTaskExecutionRole_policy" {
  role       = "${aws_iam_role.ecsTaskExecutionRole.name}"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}


#monitoring

resource "aws_cloudwatch_log_group" "ecs_task_logs" {
  name = "/ecs/${aws_ecs_cluster.my_cluster.name}/${aws_ecs_task_definition.app_task.family}"
}

resource "aws_cloudwatch_log_stream" "ecs_task_logs" {
  name           = "ecs_task_logs"
  log_group_name = "${aws_cloudwatch_log_group.ecs_task_logs.name}"
}


resource "aws_cloudwatch_metric_alarm" "ecs_task_cpu_alarm" {
  alarm_name          = "ecs-task-cpu-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/ECS"
  period              = "60"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "This metric checks the CPU utilization of the ECS task"
  alarm_actions       = []  # Add the appropriate actions (e.g., SNS notification, Lambda function) here
  dimensions = {
    ClusterName = "${aws_ecs_cluster.my_cluster.name}"
    TaskFamily = "${aws_ecs_task_definition.app_task.family}"
  }
}
