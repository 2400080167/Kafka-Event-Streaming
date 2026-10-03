from flask import Flask, jsonify, request, render_template_string
from kafka import KafkaProducer
import json
from datetime import datetime

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

orders = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Kafka Event Streaming Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: #07111f;
            color: #eaf6ff;
            min-height: 100vh;
        }

        .header {
            padding: 25px 40px;
            background: #0b1728;
            border-bottom: 1px solid #18344d;
        }

        .header h1 {
            font-size: 28px;
            color: #38d9ff;
        }

        .header p {
            margin-top: 8px;
            color: #91a9bd;
        }

        .container {
            max-width: 1200px;
            margin: auto;
            padding: 30px;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 25px;
            color: #66ffb3;
        }

        .dot {
            width: 11px;
            height: 11px;
            background: #35e88b;
            border-radius: 50%;
            box-shadow: 0 0 12px #35e88b;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            background: #0d1c2e;
            border: 1px solid #183c55;
            border-radius: 15px;
            padding: 25px;
        }

        .card h3 {
            color: #8fa8bc;
            font-size: 14px;
            margin-bottom: 12px;
        }

        .value {
            font-size: 30px;
            font-weight: bold;
            color: #38d9ff;
        }

        .panel {
            background: #0d1c2e;
            border: 1px solid #183c55;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
        }

        .panel h2 {
            margin-bottom: 20px;
            color: #ffffff;
        }

        form {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr auto;
            gap: 12px;
        }

        input {
            padding: 13px;
            border-radius: 8px;
            border: 1px solid #284961;
            background: #07111f;
            color: white;
            outline: none;
        }

        input:focus {
            border-color: #38d9ff;
        }

        button {
            padding: 13px 20px;
            border: none;
            border-radius: 8px;
            background: #12bfe3;
            color: #031018;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #38d9ff;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            text-align: left;
            padding: 14px;
            border-bottom: 1px solid #1b3448;
        }

        th {
            color: #38d9ff;
            font-size: 13px;
        }

        td {
            color: #d4e4ef;
        }

        .badge {
            background: #123b35;
            color: #61f0b1;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
        }

        @media(max-width: 800px) {
            .cards {
                grid-template-columns: 1fr;
            }

            form {
                grid-template-columns: 1fr;
            }

            .container {
                padding: 20px;
            }
        }
    </style>
</head>

<body>

<div class="header">
    <h1>⚡ Kafka Event Streaming Dashboard</h1>
    <p>Real-Time Order Event Processing using Apache Kafka</p>
</div>

<div class="container">

    <div class="status">
        <span class="dot"></span>
        Kafka Broker Connected • Topic: <b>orders</b>
    </div>

    <div class="cards">

        <div class="card">
            <h3>TOTAL ORDERS</h3>
            <div class="value" id="totalOrders">0</div>
        </div>

        <div class="card">
            <h3>TOTAL ORDER VALUE</h3>
            <div class="value" id="totalValue">₹0</div>
        </div>

        <div class="card">
            <h3>STREAM STATUS</h3>
            <div class="value">LIVE</div>
        </div>

    </div>

    <div class="panel">
        <h2>Send New Order</h2>

        <form id="orderForm">

            <input id="orderId"
                   placeholder="Order ID"
                   required>

            <input id="product"
                   placeholder="Product"
                   required>

            <input id="amount"
                   type="number"
                   placeholder="Amount"
                   required>

            <button type="submit">
                Send Event
            </button>

        </form>
    </div>

    <div class="panel">

        <h2>Recent Order Events</h2>

        <table>

            <thead>
                <tr>
                    <th>Order ID</th>
                    <th>Product</th>
                    <th>Amount</th>
                    <th>Status</th>
                    <th>Time</th>
                </tr>
            </thead>

            <tbody id="ordersTable">
            </tbody>

        </table>

    </div>

</div>

<script>

async function loadOrders() {

    const response = await fetch('/orders');
    const data = await response.json();

    document.getElementById("totalOrders").innerText =
        data.length;

    let total = 0;

    const table = document.getElementById("ordersTable");

    table.innerHTML = "";

    data.slice().reverse().forEach(order => {

        total += Number(order.amount);

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${order.order_id}</td>
            <td>${order.product}</td>
            <td>₹${Number(order.amount).toLocaleString('en-IN')}</td>
            <td><span class="badge">Processed</span></td>
            <td>${order.time}</td>
        `;

        table.appendChild(row);
    });

    document.getElementById("totalValue").innerText =
        "₹" + total.toLocaleString('en-IN');
}

document.getElementById("orderForm").addEventListener("submit", async function(e) {

    e.preventDefault();

    const order = {
        order_id: document.getElementById("orderId").value,
        product: document.getElementById("product").value,
        amount: document.getElementById("amount").value
    };

    await fetch('/send-order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(order)
    });

    document.getElementById("orderForm").reset();

    setTimeout(loadOrders, 500);
});

loadOrders();

setInterval(loadOrders, 2000);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/orders")
def get_orders():
    return jsonify(orders)


@app.route("/send-order", methods=["POST"])
def send_order():

    data = request.json

    order = {
        "order_id": data["order_id"],
        "product": data["product"],
        "amount": float(data["amount"]),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    producer.send("orders", value=order)
    producer.flush()

    orders.append(order)

    return jsonify({
        "status": "success",
        "message": "Order sent to Kafka"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
