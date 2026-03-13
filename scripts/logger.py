import csv
import os
import time

LOG_FILE = "logs/routing_performance.csv"

def initialize_logs():
    """Ensures the log file exists with headers."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "query", "route_decision", "agent_used", "latency", "status"])

def log_routing_event(query, route, agent, latency, status="success"):
    """Appends a new routing event to the performance log."""
    initialize_logs()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, query, route, agent, latency, status])

if __name__ == "__main__":
    # Test Logging
    log_routing_event("Test Query", "rag_pipeline", "RAG Specialist", 0.45)
    print(f"Logged test event to {LOG_FILE}")
