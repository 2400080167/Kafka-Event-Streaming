# Project Documentation

## 1. Project Title

AWS-Based Real-Time Event Streaming Using Apache Kafka

## 2. Project Overview

This project implements a real-time event streaming system using Apache Kafka deployed on an AWS EC2 instance.

The system demonstrates how order events can be generated, published to a Kafka topic, and received by a consumer in real time.

A Flask-based web dashboard is provided for submitting order events.

---

## 3. Problem Statement

Modern applications generate continuous streams of events such as customer orders and transactions.

A system is required to transmit these events efficiently and allow consumers to process them independently.

This project demonstrates an event-streaming architecture using Apache Kafka.

---

## 4. Objectives

- Implement real-time event streaming using Apache Kafka.
- Deploy Apache Kafka on AWS EC2.
- Create and use a Kafka topic named `orders`.
- Implement a Kafka producer.
- Implement a Kafka consumer.
- Develop a web dashboard for submitting order events.
- Demonstrate the complete producer-to-consumer event flow.

---

## 5. Architecture

```text
              Web Dashboard
                    |
                    v
             Kafka Producer
                    |
                    v
          Apache Kafka Broker
                    |
                    v
              orders Topic
                    |
                    v
             Kafka Consumer
                    |
                    v
             Order Processing

6. Technologies Used
Technology	Purpose
AWS EC2	Cloud compute environment
Apache Kafka 4.3.1	Event streaming platform
Python	Application development
Flask	Web dashboard
kafka-python-ng	Python Kafka integration
Linux	Server environment
AWS Security Groups	Network access control
7. AWS Deployment

The project was deployed on an AWS EC2 instance in the Mumbai region.

The EC2 instance hosts:

Apache Kafka
Kafka producer/consumer tools
Flask dashboard

The Flask dashboard is exposed through port 8080.

8. Kafka Topic

A Kafka topic named orders was created.

The topic is used to transport order events between producers and consumers.

Example:

1001,Laptop,50000
1002,Phone,30000
1003,Keyboard,2500
9. Producer

The producer sends order events to the Kafka orders topic.

The producer can be operated using Kafka console tools or through the Flask dashboard.

Example event:

1005,Headphones,2500
10. Consumer

The Kafka consumer subscribes to the orders topic and receives the events published by the producer.

Example received events:

1001,Laptop,50000
1002,Phone,30000
1003,Keyboard,2500

This demonstrates successful event streaming through Kafka.

11. Web Dashboard

A Flask-based web dashboard was developed to provide a simple interface for submitting order events.

The dashboard provides:

Order ID input
Product input
Amount input
Send Event button
Total orders display
Total order value display
Recent order event display
12. Event Flow

The complete event flow is:

User
 |
 v
Flask Dashboard
 |
 v
Kafka Producer
 |
 v
Apache Kafka Broker
 |
 v
orders Topic
 |
 v
Kafka Consumer
 |
 v
Order Event Processing
13. Sample Demonstration

The system was tested using sample order events.

Order ID	Product	Amount
1001	Laptop	₹50,000
1002	Phone	₹30,000
1003	Keyboard	₹2,500
1004	Mouse	₹1,500

The order event generated through the dashboard was successfully received by the Kafka consumer.

14. Use-Case Mapping
Use Case: Real-Time Order Event Streaming

Actor:

Order/Application User

Input:

Order ID
Product
Amount

Process:

User submits an order through the dashboard.
Flask application creates the order event.
The event is sent to the Kafka producer.
Kafka producer publishes the event to the orders topic.
Kafka broker stores/transmits the event.
Kafka consumer receives the event.
The order event can then be processed by the consumer.

Output:

Successfully received order event.
15. Results

The implemented system successfully demonstrated:

Apache Kafka running on AWS EC2.
Successful creation of the orders topic.
Successful production of order events.
Successful consumption of order events.
Flask dashboard deployment.
Dashboard-to-Kafka event transmission.
Producer-to-consumer event streaming.
16. Limitations
The demonstration uses a single EC2 instance.
The implementation is intended as a project demonstration rather than a production-scale Kafka deployment.
High availability and multi-broker Kafka configuration are not implemented.
Persistent database storage is not implemented.
17. Future Scope

Possible future extensions include:

Multiple Kafka brokers.
Multiple consumer groups.
Database integration.
Cloud monitoring and alerting.
Containerized deployment.
Scalable production architecture.
18. Deployment Note

This implementation uses Apache Kafka directly on AWS EC2.

Amazon MSK is not used in this implementation.

The project demonstrates the underlying Kafka event-streaming architecture using an AWS EC2 deployment.


---

