# Embedded Air Quality Measurement and Visualisation

A Python project combining remote environmental measurements with local Raspberry Pi temperature and humidity sensing. It reads ThingSpeak channel data, calculates summaries and air-quality indicators, and explores local display and cloud-update workflows.

The implementation uses two data sources: particulate measurements retrieved from a remote channel, and temperature/humidity readings acquired locally with a DHT11 sensor.

## Implementation

- Retrieve environmental records from a ThingSpeak JSON feed.
- Extract particulate measurements, calculate sample means and plot PM1.0, PM2.5 and PM10 series.
- Read DHT11 temperature and humidity through Raspberry Pi GPIO.
- Maintain a rolling measurement buffer.
- Calculate particulate AQI values and publish selected values to ThingSpeak.
- Present measurements through LED matrix and seven-segment display routines.

## Files

| File | Role |
|---|---|
| `Task1.py` | Remote feed retrieval, particulate summaries and plots |
| `Task2.py` | DHT11 acquisition and rolling temperature/humidity analysis |
| `Task3.py` | AQI calculations and ThingSpeak updates |
| `Task4.py` | GPIO and LED display integration |
| `Task4_2.py` | Supporting measurement/display calculations |
| `main.py` | Original task orchestration script |

## Hardware and dependencies

The hardware paths use a Raspberry Pi, DHT11 sensor, GPIO connections, a MAX7219-compatible LED matrix and an Adafruit-compatible seven-segment display. They are not generic desktop-only programs.

Imports include `RPi.GPIO`, `dht11`, `requests`, `thingspeak`, Matplotlib, `luma.led_matrix` and `Adafruit_LED_Backpack`. Configure GPIO, SPI and display interfaces for the connected hardware. Wiring and library versions must match the setup; no wiring diagram is included in this archive.

## Using the source

Read the task files in order to understand the data flow. Run the remote-data analysis separately when only feed inspection and plotting are needed. Sensor and publishing routines require the corresponding hardware and an authorised ThingSpeak channel.

The scripts share variables through imports, and acquisition routines contain continuous loops. They preserve the original hardware experiments rather than a scheduler-based application. `main.py` is not a documented one-command setup procedure.

Configure your own channel credentials privately before using the publishing routine. Do not reuse credentials found in public source; replace any previously published key through the service account.

## Measurement scope

Particulate values originate from the selected remote feed; this repository does not establish local particulate-sensor calibration. AQI interpretation depends on units, averaging periods and the applicable formula. The project is an environmental monitoring demonstration, not a certified health or regulatory measurement instrument.
