from django.shortcuts import render
import random
import datetime

# Simulated IoT data
def generate_energy_data():
    data = []
    now = datetime.datetime.now()
    for i in range(10):  # last 10 hours
        timestamp = (now - datetime.timedelta(hours=i)).strftime("%H:%M")
        energy = random.randint(200, 600)  # kWh
        temperature = random.randint(20, 35)  # °C
        data.append({"time": timestamp, "energy": energy, "temperature": temperature})
    return list(reversed(data))

def dashboard_view(request):
    data = generate_energy_data()
    labels = [d["time"] for d in data]
    energy = [d["energy"] for d in data]
    temp = [d["temperature"] for d in data]
    return render(request, "dashboard.html", {
        "labels": labels,
        "energy": energy,
        "temp": temp,
    })

def reports_view(request):
    # Sustainability report (simulated)
    total_energy = random.randint(5000, 10000)
    co2_saved = round(total_energy * 0.0007, 2)  # fake calculation
    efficiency = random.randint(70, 95)

    report = {
        "total_energy": total_energy,
        "co2_saved": co2_saved,
        "efficiency": efficiency,
    }
    return render(request, "reports.html", {"report": report})
