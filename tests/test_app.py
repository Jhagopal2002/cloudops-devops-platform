# ============================================================
# TEST FILE
# ============================================================

# Flask application ko app.py se import kar rahe hain
from app import app


# ============================================================
# FLASK TEST CLIENT
# ============================================================

# Flask ka test client create kar rahe hain.
# Isse browser/server manually start kiye bina
# application ke routes test kar sakte hain.
client = app.test_client()


# ============================================================
# TEST 1 - HOME PAGE
# ============================================================

def test_home_page():

    # Home route ko request bhej rahe hain
    response = client.get("/")

    # Check kar rahe hain ki request successful hai
    assert response.status_code == 200


# ============================================================
# TEST 2 - HEALTH CHECK
# ============================================================

def test_health_check():

    # Health endpoint ko request bhej rahe hain
    response = client.get("/health")

    # HTTP status 200 hona chahiye
    assert response.status_code == 200

    # JSON response ko Python dictionary me convert kar rahe hain
    data = response.get_json()

    # Response me status key honi chahiye
    assert "status" in data


# ============================================================
# TEST 3 - SYSTEM INFORMATION API
# ============================================================

def test_system_information():

    # System information API ko request bhej rahe hain
    response = client.get("/api/system")

    # Request successful honi chahiye
    assert response.status_code == 200

    # JSON response obtain kar rahe hain
    data = response.get_json()

    # Important system information available honi chahiye
    assert "operating_system" in data
    assert "python_version" in data
    assert "cpu_usage" in data
    assert "memory_usage" in data