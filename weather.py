#!/usr/bin/env python3
"""terminal-weather — live ASCII weather in your terminal."""
import argparse, urllib.request, json, sys

def get_weather(city=""):
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=j1" if city else "https://wttr.in/?format=j1"
    try:
        import urllib.parse
        url = f"https://wttr.in/{urllib.parse.quote(city)}?format=j1"
        with urllib.request.urlopen(url, timeout=10) as r:
            return json.loads(r.read())
    except Exception as e:
        return None

ICONS = {"sunny":"☀️","cloudy":"☁️","rain":"🌧️","snow":"❄️","thunder":"⛈️","fog":"🌫️","partly":"⛅"}

def render(data, city):
    if not data:
        print("Could not fetch weather. Check your connection."); return
    cur = data["current_condition"][0]
    desc = cur["weatherDesc"][0]["value"].lower()
    icon = next((v for k,v in ICONS.items() if k in desc), "🌡️")
    temp_c = cur["temp_C"]; feels = cur["FeelsLikeC"]; humid = cur["humidity"]
    print(f"\n  {icon}  Weather for {city or 'your location'}")
    print(f"  ─────────────────────────")
    print(f"  🌡  {temp_c}°C  (feels like {feels}°C)")
    print(f"  💧 Humidity: {humid}%")
    print(f"  📋 {cur['weatherDesc'][0]['value']}\n")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--city", default="", help="City name")
    args = p.parse_args()
    data = get_weather(args.city)
    render(data, args.city)

if __name__ == "__main__":
    main()
