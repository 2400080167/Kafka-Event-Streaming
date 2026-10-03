# AWS-Based Real-Time Event Streaming Using Apache Kafka

## 📌 Project Overview

This project implements a real-time event streaming system using **Apache Kafka deployed on AWS EC2**.

The system demonstrates how order events can be generated, published to a Kafka topic, and consumed in real time.

A Flask-based web dashboard provides a simple interface for submitting order events.

---

## 🎯 Objectives

- Implement real-time event streaming using Apache Kafka.
- Deploy Apache Kafka on AWS EC2.
- Create and use an `orders` Kafka topic.
- Implement a Kafka producer and consumer.
- Develop a web dashboard for sending order events.
- Demonstrate the complete event-streaming workflow.

---

## 🏗️ System Architecture

```text
                    AWS EC2
┌─────────────────────────────────────────────┐
│                                             │
│            Flask Web Dashboard              │
│                     │                       │
│                     ▼                       │
│              Kafka Producer                 │
│                     │                       │
│                     ▼                       │
│           Apache Kafka Broker               │
│                     │                       │
│                     ▼                       │
│                orders Topic                 │
│                     │                       │
│                     ▼                       │
│              Kafka Consumer                 │
│                     │                       │
│                     ▼                       │
│             Order Processing                │
│                                             │
└─────────────────────────────────────────────┘
🔄 Event Flow

The complete event flow of the project is:

User
  │
  │ Enter Order Details
  ▼
Flask Web Dashboard
  │
  │ Send Order Event
  ▼
Kafka Producer
  │
  │ Publish Event
  ▼
Apache Kafka Broker
  │
  │ Store / Stream Event
  ▼
orders Topic
  │
  │ Consume Event
  ▼
Kafka Consumer
  │
  │ Process Order Event
  ▼
Order Event Successfully Received
Event Flow Explanation
The user enters the order ID, product name, and amount in the Flask dashboard.
The Flask application creates the order event.
The Kafka producer sends the event to Apache Kafka.
Apache Kafka publishes the event to the orders topic.
The Kafka consumer subscribes to the orders topic.
The consumer receives the order event.
The received event can then be processed by the application.
🛠️ Technologies Used
Technology	Purpose
AWS EC2	Cloud deployment
Apache Kafka 4.3.1	Event streaming
Python	Application development
Flask	Web dashboard
kafka-python-ng	Kafka integration
Linux	Server environment
AWS Security Groups	Network access
☁️ AWS Deployment

The project is deployed on an AWS EC2 instance in the Mumbai region.

The EC2 instance hosts:

Apache Kafka
Kafka producer
Kafka consumer
Flask dashboard

The Flask dashboard is exposed through port 8080.

📂 Project Structure
Kafka-Event-Streaming/
│
├── app.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── dashboard.png
│   ├── EC2.png
│   ├── Kafka-topic.png
│   └── Producer-Consumer.png
│
└── docs/
    └── project-documentation.md
📡 Kafka Topic

The project uses a Kafka topic named:

orders

The orders topic is used to transport order events between the producer and consumer.

Sample Events
1001,Laptop,50000
1002,Phone,30000
1003,Keyboard,2500
📤 Kafka Producer

The Kafka producer is responsible for publishing order events to the orders topic.

Example event:

1005,Headphones,2500

The producer can receive events from the Flask dashboard or through Kafka console tools.

📥 Kafka Consumer

The Kafka consumer subscribes to the orders topic and receives the events published by the producer.

Example received events:

1001,Laptop,50000
1002,Phone,30000
1003,Keyboard,2500

The successful reception of these events demonstrates the Kafka producer-to-consumer streaming flow.

🌐 Web Dashboard

A Flask-based web dashboard was developed to provide a user-friendly interface for submitting order events.

Dashboard Features
Order ID input
Product input
Amount input
Send Event button
Total orders display
Total order value display
Recent order events
Live stream status
🧪 Demonstration

The system was tested using multiple order events.

Order ID	Product	Amount
1001	Laptop	₹50,000
1002	Phone	₹30,000
1003	Keyboard	₹2,500
1004	Mouse	₹1,500

A dashboard-generated order was successfully published to Kafka and received by the Kafka consumer.

📸 Project Evidence
EC2 Deployment

Kafka Topic

Producer and Consumer

Web Dashboard

📖 Documentation

Detailed project documentation and use-case mapping are available here:

Project Documentation

🎯 Use Case
Real-Time Order Event Streaming

Actor:

Order/Application User

Input:

Order ID
Product
Amount

Process:

User submits an order through the dashboard.
The Flask application creates the order event.
The event is sent to the Kafka producer.
The Kafka producer publishes the event to the orders topic.
The Kafka broker handles the event stream.
The Kafka consumer receives the event.
The order event can then be processed.

Output:

Successfully received order event.

📊 Results

The implementation successfully demonstrated:

Apache Kafka running on AWS EC2.
Successful creation of the orders topic.
Successful production of order events.
Successful consumption of order events.
Real-time order event streaming.
Flask dashboard deployment.
Dashboard-to-Kafka event transmission.
Producer-to-consumer event delivery.
⚠️ Limitations
The demonstration uses a single EC2 instance.
The implementation is intended as an academic/project demonstration rather than a production-scale deployment.
High availability and multi-broker Kafka configuration are not implemented.
Persistent database storage is not implemented.
🚀 Future Scope

Possible future extensions include:

Multiple Kafka brokers
Multiple consumer groups
Database integration
Cloud monitoring and alerting
Containerized deployment
Scalable production architecture
