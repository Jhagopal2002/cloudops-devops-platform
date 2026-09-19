# ============================================================
# 1. IMPORTS
# ============================================================

# Flask application banane aur web routes create karne ke liye
from flask import Flask, jsonify, render_template

# System ki information collect karne ke liye
import platform

# Python version ki information lene ke liye
import sys

# Disk ki total, used aur free space check karne ke liye
import shutil

# CPU aur RAM usage monitor karne ke liye
import psutil

# Application ke events aur errors ko log file me store karne ke liye
import logging

# Health-check response me current date/time dene ke liye
from datetime import datetime


# ============================================================
# 2. FLASK APPLICATION
# ============================================================

# Flask application ka object create kar rahe hain
app = Flask(__name__)


# ============================================================
# 3. LOGGING CONFIGURATION
# ============================================================

# Application ke logs "cloudops.log" file me save honge
logging.basicConfig(
    filename="cloudops.log",

    # INFO level aur usse upar ke logs record honge
    level=logging.INFO,

    # Log ka format:
    # Date/Time - Log Level - Message
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Logger object create kar rahe hain
logger = logging.getLogger(__name__)


# ============================================================
# 4. SYSTEM INFORMATION FUNCTION
# ============================================================

def get_system_info():
    """
    Basic system information collect karta hai.
    """

    # Disk ki total, used aur free space bytes me milti hai
    total, used, free = shutil.disk_usage("/")

    # System ki RAM/memory information collect kar rahe hain
    memory = psutil.virtual_memory()

    # Collected information ko dictionary ke form me return kar rahe hain
    return {
        "operating_system": platform.system(),
        "platform": platform.platform(),
        "python_version": sys.version.split()[0],
        "hostname": platform.node(),

        # CPU usage percentage
        "cpu_usage": psutil.cpu_percent(interval=1),

        # RAM usage percentage
        "memory_usage": memory.percent,

        # Disk usage percentage
        "disk_usage": round((used / total) * 100, 2),

        # Free disk space GB me
        "disk_free_gb": round(free / (1024 ** 3), 2),

        # Total disk space GB me
        "disk_total_gb": round(total / (1024 ** 3), 2)
    }


# ============================================================
# 5. HOME / DASHBOARD ROUTE
# ============================================================

# "/" URL ko home page se connect kar rahe hain
@app.route("/")
def home():

    # System information collect kar rahe hain
    system_info = get_system_info()

    # index.html template ko system information bhej rahe hain
    return render_template(
        "index.html",
        system_info=system_info
    )


# ============================================================
# 6. HEALTH CHECK API
# ============================================================

# "/health" URL application ki health check karega
@app.route("/health")
def health_check():

    # Current CPU usage check kar rahe hain
    cpu_usage = psutil.cpu_percent(interval=1)

    # Current RAM usage check kar rahe hain
    memory_usage = psutil.virtual_memory().percent

    # Agar CPU aur RAM dono 90% se kam hain,
    # to application/system ko healthy maan rahe hain
    if cpu_usage < 90 and memory_usage < 90:
        status = "healthy"

    # Agar CPU ya RAM 90% ya usse zyada hai,
    # to warning status return hoga
    else:
        status = "warning"

    # Data ko JSON response ke form me return kar rahe hain
    return jsonify({
        "status": status,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "timestamp": datetime.now().isoformat()
    })


# ============================================================
# 7. SYSTEM INFORMATION API
# ============================================================

# "/api/system" URL system information JSON me return karega
@app.route("/api/system")
def system_information():

    try:
        # System information collect kar rahe hain
        system_info = get_system_info()

        # Successful request ka log create kar rahe hain
        logger.info("System information collected successfully")

        # System information JSON format me return kar rahe hain
        return jsonify(system_info)

    except Exception as error:

        # Agar koi error aata hai to usko log file me save karenge
        logger.error("Failed to collect system information: %s", error)

        # User ko error ka JSON response denge
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


# ============================================================
# 8. APPLICATION START
# ============================================================

# Ye code tabhi execute hoga jab hum directly
# "python app.py" run karenge
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)